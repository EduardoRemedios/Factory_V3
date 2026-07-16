from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import factory_v3_codex_deeplink as helper  # noqa: E402


FIXTURE_ROOT = REPO_ROOT / "tests/fixtures/factory_v3_codex_deeplink"
PROMPT_FIXTURE = FIXTURE_ROOT / "input/prompt.txt"
EXPECTED_FIXTURE = FIXTURE_ROOT / "expected/valid.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/cases.json"
SCRIPT_PATH = SCRIPTS_DIR / "factory_v3_codex_deeplink.py"
SYNTHETIC_WORKSPACE = "/synthetic/Factory V3/Same Second"


class CodexDeepLinkTests(unittest.TestCase):
    def run_cli(self, workspace: str, prompt_file: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--workspace",
                workspace,
                "--prompt-file",
                prompt_file,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_pure_encoder_matches_pinned_fixture(self) -> None:
        prompt_bytes = PROMPT_FIXTURE.read_bytes()
        payload = helper.build_payload(SYNTHETIC_WORKSPACE, prompt_bytes)
        self.assertEqual(payload, json.loads(EXPECTED_FIXTURE.read_text(encoding="utf-8")))

        parsed = urlparse(str(payload["url"]))
        query = parse_qs(parsed.query, keep_blank_values=True)
        self.assertEqual(parsed.scheme, "codex")
        self.assertEqual(parsed.netloc, "new")
        self.assertEqual(query["path"], [SYNTHETIC_WORKSPACE])
        self.assertEqual(query["prompt"], [prompt_bytes.decode("utf-8")])
        self.assertTrue(parsed.query.startswith("path="))
        self.assertIn("&prompt=", parsed.query)
        self.assertIn("%20", parsed.query)
        self.assertNotIn("+", parsed.query)

    def test_pure_encoder_is_deterministic(self) -> None:
        prompt_bytes = PROMPT_FIXTURE.read_bytes()
        first = helper.build_payload(SYNTHETIC_WORKSPACE, prompt_bytes)
        second = helper.build_payload(SYNTHETIC_WORKSPACE, prompt_bytes)
        self.assertEqual(first, second)
        self.assertEqual(first["prompt_sha256"], hashlib.sha256(prompt_bytes).hexdigest())
        self.assertIs(first["human_send_required"], True)
        self.assertIs(first["transport_proof"], False)

    def test_cli_success_resolves_workspace_and_preserves_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            workspace = root / "workspace with spaces"
            workspace.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_bytes(PROMPT_FIXTURE.read_bytes())
            before_prompt = prompt.read_bytes()
            before_workspace = sorted(item.name for item in workspace.iterdir())

            first = self.run_cli(str(workspace), str(prompt))
            second = self.run_cli(str(workspace), str(prompt))

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)
            payload = json.loads(first.stdout)
            self.assertEqual(payload["workspace"], str(workspace.resolve()))
            self.assertEqual(prompt.read_bytes(), before_prompt)
            self.assertEqual(sorted(item.name for item in workspace.iterdir()), before_workspace)

    def test_workspace_rejections_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prompt = root / "prompt.txt"
            prompt.write_text("Approved synthetic prompt.", encoding="utf-8")
            workspace_file = root / "not-a-directory"
            workspace_file.write_text("x", encoding="utf-8")

            cases = [
                ("relative/path", "workspace_not_absolute"),
                (str(root / "missing"), "workspace_not_found"),
                (str(workspace_file), "workspace_not_directory"),
            ]
            for workspace, expected_code in cases:
                with self.subTest(expected_code=expected_code):
                    result = self.run_cli(workspace, str(prompt))
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(json.loads(result.stdout)["error"]["code"], expected_code)

    def test_prompt_path_rejections_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            workspace = root / "workspace"
            workspace.mkdir()
            prompt_directory = root / "prompt-directory"
            prompt_directory.mkdir()

            cases = [
                (root / "missing.txt", "prompt_file_not_found"),
                (prompt_directory, "prompt_file_not_regular"),
            ]
            for prompt_path, expected_code in cases:
                with self.subTest(expected_code=expected_code):
                    result = self.run_cli(str(workspace), str(prompt_path))
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(json.loads(result.stdout)["error"]["code"], expected_code)

    def test_prompt_content_rejections_match_readable_fixture(self) -> None:
        cases = json.loads(INVALID_FIXTURE.read_text(encoding="utf-8"))
        payloads = {
            "prompt_empty": b"",
            "prompt_invalid_utf8": b"\xff",
            "prompt_contains_nul": b"before\x00after",
            "prompt_too_large": b"x" * (helper.MAX_PROMPT_BYTES + 1),
        }
        self.assertEqual([case["code"] for case in cases], list(payloads))

        for code, prompt_bytes in payloads.items():
            with self.subTest(code=code):
                with self.assertRaises(helper.InputError) as caught:
                    helper.build_payload(SYNTHETIC_WORKSPACE, prompt_bytes)
                self.assertEqual(caught.exception.code, code)

    def test_missing_cli_arguments_emit_json_and_exit_two(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "error")
        self.assertEqual(payload["error"]["code"], "invalid_arguments")

    def test_source_has_no_external_effect_path(self) -> None:
        source = SCRIPT_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import subprocess",
            "import webbrowser",
            "import socket",
            "urllib.request",
            "os.system",
            "Popen(",
            "pbcopy",
            "osascript",
            "startfile(",
            "codex app-server",
            "codex mcp-server",
        )
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
