#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Sequence
from urllib.parse import quote


SCHEMA_VERSION = "v0.1-codex-deeplink-assist"
MAX_PROMPT_BYTES = 8192


class InputError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise InputError("invalid_arguments", message)


def build_payload(workspace: str, prompt_bytes: bytes) -> dict[str, object]:
    if not Path(workspace).is_absolute():
        raise InputError("workspace_not_absolute", "workspace must be an absolute path")
    if not prompt_bytes:
        raise InputError("prompt_empty", "prompt file must not be empty")
    if len(prompt_bytes) > MAX_PROMPT_BYTES:
        raise InputError(
            "prompt_too_large",
            f"prompt file must not exceed {MAX_PROMPT_BYTES} bytes",
        )
    try:
        prompt = prompt_bytes.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise InputError("prompt_invalid_utf8", "prompt file must contain valid UTF-8") from exc
    if "\x00" in prompt:
        raise InputError("prompt_contains_nul", "prompt file must not contain NUL")

    encoded_workspace = quote(workspace, safe="", encoding="utf-8", errors="strict")
    encoded_prompt = quote(prompt, safe="", encoding="utf-8", errors="strict")
    url = f"codex://new?path={encoded_workspace}&prompt={encoded_prompt}"
    return {
        "human_send_required": True,
        "prompt_bytes": len(prompt_bytes),
        "prompt_sha256": hashlib.sha256(prompt_bytes).hexdigest(),
        "schema_version": SCHEMA_VERSION,
        "status": "ok",
        "transport_proof": False,
        "url": url,
        "url_bytes": len(url.encode("utf-8")),
        "workspace": workspace,
    }


def _resolve_workspace(value: str) -> str:
    workspace = Path(value)
    if not workspace.is_absolute():
        raise InputError("workspace_not_absolute", "workspace must be an absolute path")
    try:
        resolved = workspace.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise InputError("workspace_not_found", "workspace path does not exist") from exc
    if not resolved.is_dir():
        raise InputError("workspace_not_directory", "workspace path must be a directory")
    return str(resolved)


def _read_prompt(path_value: str) -> bytes:
    prompt_path = Path(path_value)
    try:
        resolved = prompt_path.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise InputError("prompt_file_not_found", "prompt file does not exist") from exc
    if not resolved.is_file():
        raise InputError("prompt_file_not_regular", "prompt file must be a regular file")
    try:
        with resolved.open("rb") as handle:
            return handle.read(MAX_PROMPT_BYTES + 1)
    except OSError as exc:
        raise InputError("prompt_file_unreadable", "prompt file could not be read") from exc


def _parser() -> JsonArgumentParser:
    parser = JsonArgumentParser(
        description="Build a deterministic, human-send Codex desktop deep link.",
    )
    parser.add_argument("--workspace", required=True, help="Existing absolute workspace directory.")
    parser.add_argument("--prompt-file", required=True, help="Existing non-sensitive UTF-8 prompt file.")
    return parser


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = _parser().parse_args(argv)
        workspace = _resolve_workspace(args.workspace)
        prompt_bytes = _read_prompt(args.prompt_file)
        payload = build_payload(workspace, prompt_bytes)
    except InputError as exc:
        _print_json(
            {
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                },
                "schema_version": SCHEMA_VERSION,
                "status": "error",
            }
        )
        return 2

    _print_json(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
