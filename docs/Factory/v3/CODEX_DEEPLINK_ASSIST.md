# Codex Deep-Link Assist

## Version

v0.1

## Status

Research-only, advisory, and non-enforcing.

Implemented by approved mission `V3-CODEX-DL-001`. This helper generates text
only. It does not open a link, create or message a Codex task, run a worker,
copy to the clipboard, inspect credentials, use the Codex CLI/SDK/MCP, perform
network access, or grant execution authority.

## Purpose

Reduce attended re-entry friction by deterministically converting:

- one existing absolute local workspace directory; and
- one existing non-sensitive UTF-8 prompt file

into JSON containing a reviewable `codex://new` deep link and the SHA-256 of the
exact prompt input.

The human must still inspect the resolved workspace and digest, open the link,
review the composer, and press Send. Opening or testing a link requires a
separately approved live trial.

## Command

```bash
python3 scripts/factory_v3_codex_deeplink.py \
  --workspace /absolute/path/to/workspace \
  --prompt-file /path/to/non-sensitive-reentry-prompt.txt
```

The helper accepts no inline prompt argument and no stdin prompt mode. This
avoids duplicating prompt text in shell history.

## Success Output

Exit code: `0`.

Deterministic JSON fields:

- `schema_version`
- `status: "ok"`
- `workspace`: strictly resolved absolute directory
- `prompt_bytes`
- `prompt_sha256`: digest of exact input bytes only
- `url_bytes`
- `url`: `codex://new?path=<encoded-workspace>&prompt=<encoded-prompt>`
- `human_send_required: true`
- `transport_proof: false`

Output uses sorted keys, two-space indentation, and a final newline. Query
parameter order is exactly `path`, then `prompt`. Values use UTF-8 percent
encoding with `safe=""`; spaces are `%20`, not `+`.

## Input Policy

- Workspace must be absolute, exist, and be a directory.
- The encoded workspace is its strict resolved path.
- Prompt path must resolve to a regular file.
- Prompt must be non-empty valid UTF-8 without NUL.
- Prompt input must not exceed 8,192 bytes.
- The helper reads at most 8,193 bytes.
- Prompt text must be non-sensitive because the complete text appears in the
  generated URL and may later be visible in terminals, transcripts, or desktop
  URL handling.

The 8,192-byte ceiling is a local v0.1 safety policy, not a measured or
documented Codex product limit.

## Error Output

Invalid input exits `2` and emits deterministic JSON containing:

- `schema_version`
- `status: "error"`
- `error.code`
- `error.message`

Stable input error codes include:

- `invalid_arguments`
- `workspace_not_absolute`
- `workspace_not_found`
- `workspace_not_directory`
- `prompt_file_not_found`
- `prompt_file_not_regular`
- `prompt_file_unreadable`
- `prompt_empty`
- `prompt_invalid_utf8`
- `prompt_contains_nul`
- `prompt_too_large`

Invalid input never emits a success link.

## Evidence And Proof Limits

Focused deterministic coverage lives in:

- `tests/test_factory_v3_codex_deeplink.py`
- `tests/fixtures/factory_v3_codex_deeplink/`

The pinned fixture uses the fixed synthetic path
`/synthetic/Factory V3/Same Second` so it is portable across machines. Separate
temporary-directory tests prove real CLI path validation.

Tests prove local input validation, encoding, digesting, JSON shape, error
behavior, determinism, source preservation, and absence of named external-effect
paths. They do not prove:

- that the installed desktop accepts the URL;
- that the composer contains exactly the input text;
- that the user sends the same text;
- task identity, status, output, interrupt, sandbox, or resume behavior;
- prompt confidentiality after a link is opened;
- live worker or adapter behavior.

## Boundary

This helper is not a task adapter. It has no link-opening, clipboard, GUI,
browser, subprocess, socket, HTTP, SDK, MCP, Codex execution, scheduler,
background, product-write, deployment, or governance-routing path.

Manual task creation and copy/paste remain the safe fallback when input is
invalid, sensitive, too large, or unsuitable for a URL.
