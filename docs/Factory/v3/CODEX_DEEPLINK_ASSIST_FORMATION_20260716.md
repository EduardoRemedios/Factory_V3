# Codex Deep-Link Assist Formation - 2026-07-16

## Status

Research-only, non-enforcing, and non-executing mission-formation output for
candidate mission `V3-CODEX-DL-001`.

This artifact does not implement a helper, generate or open a live deep link,
create or message a Codex task, copy anything to the clipboard, modify Same
Second, install a dependency, inspect credentials, start a process, dispatch a
worker, or add runtime-control power.

## Mission Formation Result

### Route

`CANDIDATE_V3_ENVELOPE`

Completed discovery `V3-CODEX-DISC-001` established
`DEEPLINK_ASSIST_ONLY`: the documented desktop deep-link surface can carry an
absolute workspace and prefilled prompt into a new-task composer, but the human
must review and press Send. The smallest useful next candidate is therefore a
deterministic link builder, not a task adapter.

### Problem Statement

The sponsor currently creates the next Codex task, selects the workspace, and
copies an authored re-entry prompt manually. A deep-link helper can remove the
workspace-selection and prompt-copying steps while preserving the attended
human Send boundary.

The real problem is not worker orchestration. It is producing one reviewable,
reproducible handoff link from explicit authored inputs without claiming that
the link was opened or that its prompt was sent unchanged.

### Desired Outcome

Define a bounded stdlib-only implementation mission that can later produce:

1. one canonical `codex://new?path=...&prompt=...` URL;
2. the resolved absolute workspace included in that URL;
3. a full SHA-256 digest and byte count of the exact UTF-8 prompt input;
4. deterministic JSON suitable for a human-facing wrapper;
5. explicit flags that human Send is required and transport proof is absent.

### Non-Goals

- No link opening, task creation, prompt send, task ID, status, resume, archive,
  pin, handoff, or interrupt behavior.
- No worker execution, implementation command dispatch, verification dispatch,
  session orchestration, scheduler, automation, daemon, or background process.
- No clipboard integration, GUI control, browser control, AppleScript, shell
  opener, or operating-system URL handler call.
- No SDK, app-server, MCP, Codex CLI, plugin, package, dependency, credential,
  authentication, configuration, or network use.
- No prompt secret detection or claim that a prompt is safe to expose.
- No Same Second modification or product integration.
- No required gate, profile promotion, governance routing, or worker authority.

### Assumptions

- The helper is for short, non-sensitive authored re-entry prompts, not full
  mission packs or secret-bearing payloads.
- The caller supplies an existing prompt file rather than prompt text on the
  command line, avoiding shell-history duplication.
- The caller supplies an existing absolute local directory; the helper resolves
  it strictly before encoding.
- UTF-8 bytes are authoritative. The helper performs no newline, Unicode, or
  whitespace normalization.
- The digest proves only the helper input. It does not prove composer contents
  or the text ultimately sent by the human.
- A fixed v0.1 prompt-input ceiling of 8,192 bytes is a local safety bound, not
  a documented Codex product limit or compatibility guarantee.

### Unknowns

- Whether the installed desktop build accepts every correctly encoded link.
- Practical URL-size behavior below the local 8,192-byte prompt ceiling.
- Whether the desktop visibly resolves symlinks in the same form as the helper.
- Whether any desktop or OS component records the full URL.
- Whether a future live trial can compare the input digest with transport- or
  composer-observed content.
- Whether a later wrapper can present the link without adding logging or
  accidental-open risk.

## Options

| Option | Value | Risk / limitation | Formation verdict |
| --- | --- | --- | --- |
| A. Standalone stdlib Python CLI | Matches repository script patterns; deterministic; directly testable; no dependency | Emits a URL containing the prompt; does not prove desktop behavior | Recommended |
| B. Static Markdown/template instructions | No code | Leaves manual encoding, path mistakes, and copy/paste friction | Reject |
| C. Native task, CLI, SDK, app-server, or MCP adapter | Could automate Send/status later | Unavailable or outside current dependency/process/authority boundary | Defer to separate mission |

## Recommended Route

Implement Option A only after a separate sponsor Go. Keep the first version as
one direct Python script with focused tests and fixtures. Do not create a package,
registry, plugin seam, transport abstraction, or generic URI framework.

## Human Decisions Needed

1. Approve or reject the exact code-only candidate contract below.
2. Decide later, after implementation evidence, whether a separate attended
   live-link trial is worth authorizing.
3. Decide in a separate future mission whether human Send should ever be
   replaced by a programmatic surface.

## Pre-Resolved Decisions

- Mission ID: `V3-CODEX-DL-001`.
- Python standard library only.
- Prompt input is file-only; no `--prompt` argument and no stdin in v0.1.
- Workspace must be absolute, exist, and be a directory; strict resolution is
  used for the encoded value.
- Prompt file must exist and be a regular file. The CLI reads at most 8,193
  bytes so oversized input fails without an unbounded read.
- The script contains one small pure encoder that accepts an already validated
  canonical absolute workspace string plus exact prompt bytes. Filesystem
  validation remains in the CLI boundary.
- Query parameter order is exactly `path`, then `prompt`.
- Each value is UTF-8 percent-encoded with no safe characters; spaces become
  `%20`, not `+`.
- Prompt input over 8,192 bytes is rejected with exit code `2`. This is a local
  guardrail, not a product claim.
- Success and failure emit deterministic JSON with explicit exit codes.
- The helper never opens, copies, sends, or verifies a link.
- Session memory is not an accepted prompt, workspace, state, or authority
  source.

## Verification And Evidence Needs

- Unit coverage for ASCII, spaces, Unicode, `&`, `?`, `#`, percent signs,
  embedded and trailing newlines, and deterministic repeated output.
- Rejection coverage for relative workspace, missing workspace, non-directory
  workspace, missing prompt file, invalid UTF-8, empty prompt, NUL, and
  over-8,192-byte prompt.
- Pinned pure-encoder fixture output for one fixed synthetic absolute
  workspace/prompt pair, plus separate CLI path-validation tests. Pinned output
  must not contain the checkout's machine-specific resolved path.
- Direct assertion that parameter order is stable and spaces use `%20`.
- Direct assertion that the decoded URL values reproduce the resolved workspace
  and exact prompt string.
- Static/source inspection confirming no `subprocess`, `webbrowser`, clipboard,
  GUI, socket, HTTP, SDK, MCP, or Codex execution path.
- Full repository tests, advisory validators, compilation, JSON parsing, and
  `git diff --check`.
- Mission closeout must say explicitly that fixtures do not prove the desktop
  opened the URL or sent the prompt.

## Candidate Mission Contract

### Objective

Implement and document the smallest deterministic stdlib helper that converts
an existing absolute workspace plus a non-sensitive UTF-8 prompt file into a
reviewable Codex desktop deep link without opening or sending it.

### Success Criteria

1. `scripts/factory_v3_codex_deeplink.py` accepts only `--workspace` and
   `--prompt-file`.
2. It validates and strictly resolves the workspace, validates the prompt file,
   requires a regular file, reads at most 8,193 bytes, enforces the fixed
   8,192-byte ceiling, and preserves exact UTF-8 text.
3. It constructs exactly
   `codex://new?path=<encoded-workspace>&prompt=<encoded-prompt>`.
4. Success JSON contains:
   - `schema_version`
   - `status`
   - `workspace`
   - `prompt_bytes`
   - `prompt_sha256`
   - `url_bytes`
   - `url`
   - `human_send_required: true`
   - `transport_proof: false`
5. Output is `json.dumps(..., indent=2, sort_keys=True)` plus one final newline.
6. Invalid input emits deterministic JSON with `schema_version`, `status:
   "error"`, and an `error` object containing stable `code` and `message`
   strings, then exits `2`; success exits `0`.
7. Focused tests and fixtures pass without dependencies.
8. No code path opens the URL, invokes Codex, uses a clipboard, starts a
   process, performs network access, or modifies another repository.
9. A small pure encoder is pinned with a fixed synthetic absolute path; CLI
   tests separately prove strict real-workspace and prompt-file validation.

### Authorized Scope

- `scripts/factory_v3_codex_deeplink.py`
- `tests/test_factory_v3_codex_deeplink.py`
- `tests/fixtures/factory_v3_codex_deeplink/`
- `docs/Factory/v3/CODEX_DEEPLINK_ASSIST.md`
- one bounded closeout/evidence artifact under
  `docs/Factory/v3/deeplink_assist/V3-CODEX-DL-001/`
- active Factory V3 canon references required to record implementation status

### Forbidden Scope

- Same Second or any other product repository.
- Link opening, task creation, prompt send, worker run, desktop/GUI/browser
  control, clipboard access, or operating-system URL handler invocation.
- Codex CLI, app-server, SDK, MCP, Agents SDK, sub-agent, automation, scheduler,
  daemon, concurrency, background process, or external service.
- Dependency, package, plugin, credential, auth, config, network, deployment,
  push, merge, PR, required-gate, profile, or runtime-control changes.
- Prompt secret scanning, encryption, storage service, generic transport
  abstraction, framework, registry, or package.

### Allowed Tools And Commands

- Read-only repository inspection with `rg`, `sed`, `find`, `ls`, `wc`, and
  read-only Git commands.
- `apply_patch` for the exact authorized files.
- `python3 -m unittest discover -s tests`
- focused unit-test invocation for the new module
- `python3 -m py_compile scripts/factory_v3_codex_deeplink.py`
- `python3 -m json.tool` for fixture/evidence JSON
- canonical V3 advisory validators
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `git diff --check`

`open`, `pbcopy`, `osascript`, `webbrowser`, `codex`, network clients, package
managers, and process-start commands are forbidden.

### Dependency Policy

No new dependencies. Use only Python 3 standard-library modules such as
`argparse`, `hashlib`, `json`, `pathlib`, `sys`, and `urllib.parse`.

### Budget And Checkpoint Rules

- No duration, call, file, test, or output floor.
- Checkpoint after the pure encoding function, CLI validation/error contract,
  focused fixtures/tests, and full verification.
- Stop when the bounded helper and evidence are complete.
- Do not add abstractions for hypothetical future transports.

### Human Interrupt Rules

Stop and request separate approval before opening a generated link, creating or
messaging a task, adding an input mode, changing the 8,192-byte policy, adding
a dependency, accessing credentials/config, starting a process, modifying Same
Second, or expanding into a live trial or adapter.

### Halt And Fallback Rules

- Reject invalid, missing, empty, non-UTF-8, NUL-containing, or oversized prompt
  input without emitting a success link.
- Reject non-absolute, missing, or non-directory workspace input.
- Halt if deterministic decoding cannot reproduce the exact validated inputs.
- Halt on any need for Codex execution, OS integration, dependency, network,
  credential, or external write.
- Preserve manual task creation/copying as fallback; never weaken validation to
  force link generation.

### Re-Entry Instructions

Read this formation artifact, its challenge, `V3-CODEX-DISC-001` evidence,
current canons, and current repository state. Preserve all existing changes.
Confirm the sponsor approved this exact implementation contract. Do not accept
session memory as prompt content, workspace state, or authority. The one safe
first action is implementation inspection inside the authorized file set.

## Recommended Next Step

Run the challenge review and present the repaired code-only candidate for a
separate sponsor implementation Go. Do not implement from this artifact.

This is candidate mission-formation output only. It does not authorize execution
until the human explicitly approves the mission contract.
