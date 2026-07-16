# Factory V3 Codex Deep-Link Fixtures

Research-only fixtures for `scripts/factory_v3_codex_deeplink.py`.

- `input/prompt.txt` contains spaces, Unicode, reserved URI characters, a
  percent sign, and a trailing newline.
- `expected/valid.json` pins the pure encoder against the fixed synthetic
  absolute workspace `/synthetic/Factory V3/Same Second`.
- `invalid/cases.json` names the bounded prompt-content rejection cases.

The pinned fixture does not use the checkout's real resolved path. Separate
temporary-directory tests cover CLI filesystem validation.

These fixtures prove deterministic local encoding only. They do not open a
link, create a Codex task, or prove desktop/composer behavior.
