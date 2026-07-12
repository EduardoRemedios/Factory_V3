from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from factory_v3_serial_mission_graph_lint import _lint_graph  # noqa: E402


VALID_FIXTURE = (
    REPO_ROOT / "tests/fixtures/factory_v3_serial_mission_graph/valid_serial_graph.json"
)


class SerialMissionGraphLintTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))

    def findings(self, graph: dict) -> list[dict[str, str]]:
        return _lint_graph(Path("fixture.json"), graph)

    def test_valid_serial_graph_passes(self) -> None:
        self.assertEqual(self.findings(self.graph), [])

    def test_cycle_is_rejected(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["children"][0]["dependencies"] = ["feature-c"]
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG072", ids)

    def test_multiple_active_children_are_rejected(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["children"][0]["status"] = "active"
        graph["children"][1]["status"] = "active"
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG073", ids)

    def test_child_scope_must_fit_parent_ceiling(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["children"][1]["authority"]["authorized_paths"] = ["secrets/production.env"]
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG085", ids)

    def test_parent_cannot_complete_before_required_children(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["parent_mission"]["status"] = "completed"
        graph["parent_closeout"]["parent_verification_result"] = "pass"
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG135", ids)

    def test_multiple_authorized_starts_are_rejected(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["children"][2]["dependencies"] = ["feature-a"]
        graph["children"][2]["status"] = "eligible"
        graph["children"][2]["continuation_gate"] = {
            "gate_result": "continue",
            "authorized_to_start": True,
            "authority_basis": "Invalid second start authorization.",
        }
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG077", ids)

    def test_verification_command_must_be_child_authorized(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["children"][1]["verification"]["required_commands"] = ["python3 scripts/verify_epic.py"]
        ids = {item["id"] for item in self.findings(graph)}
        self.assertIn("V3-SG094", ids)


if __name__ == "__main__":
    unittest.main()
