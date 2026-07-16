# Codex Deep-Link Assist Challenge - 2026-07-16

## Status

Research-only, non-enforcing, and non-executing challenge over
`CODEX_DEEPLINK_ASSIST_FORMATION_20260716.md`.

This challenge does not implement the helper, generate or open a live link,
create or message a task, modify Same Second, add a dependency or credential,
start a process, dispatch a worker, or add runtime-control power.

## Challenge Result

### Verdict

`PASS` for a separate sponsor implementation decision.

The candidate is sufficiently bounded for a stdlib-only code mission. Challenge
PASS is not execution authority and supplies no evidence that the desktop
accepts a generated link.

## Critical Findings

None after repair.

The initial concept would have been unsafe if it accepted prompt text directly
on the command line or implied that a digest proved what was sent. The repaired
contract requires a prompt file, non-sensitive input, and explicit
`transport_proof: false`.

## High Findings

1. The complete prompt is embedded in the URL.
   - Risk: terminals, transcripts, screenshots, launch services, or future
     wrappers may retain it.
   - Repair adopted: v0.1 is explicitly limited to non-sensitive prompts; it
     makes no secret-detection claim; prompt input is file-only; no clipboard or
     OS opener is allowed.

2. The digest is not transport proof.
   - Risk: a human may edit composer text, the app may transform it, or the wrong
     link may be opened while the helper output still looks internally valid.
   - Repair adopted: the digest is labeled as input evidence only; output must
     set `transport_proof: false` and `human_send_required: true`; any composer
     or sent-text comparison belongs to a separate live trial.

3. Workspace identity can drift through relative paths or symlinks.
   - Risk: a correct prompt may open against the wrong repository.
   - Repair adopted: reject relative and missing paths, require a directory,
     resolve strictly before encoding, and expose the resolved path in output.
     Do not support `originUrl` in v0.1.

4. Deep-link size compatibility is unproved.
   - Risk: a long but correctly encoded URL may be truncated or rejected by the
     desktop/OS while the helper declares success.
   - Repair adopted: enforce an 8,192-byte prompt-input ceiling as a conservative
     local v0.1 guardrail, label it as non-product evidence, report `url_bytes`,
     and retain manual copy/paste fallback. Compatibility still requires a
     separately approved trial.

5. A generic transport abstraction would create false readiness.
   - Risk: implementation could grow into native tasks, app-server, SDK, MCP,
     clipboard, or OS launch behavior under the label “helper.”
   - Repair adopted: one standalone script, one exact URL shape, no package,
   registry, strategy layer, plugin seam, or alternate transport.

6. Pinned output can accidentally become machine-specific.
   - Risk: a fixture built from `Path.resolve()` inside the current checkout
     embeds a user-specific absolute path and fails elsewhere.
   - Repair adopted: pin the pure encoder with a fixed synthetic absolute path;
     test strict filesystem resolution separately at the CLI boundary. This is
     one local function, not a transport abstraction.

## Medium/Low Findings

- Standard `urlencode` commonly uses `+` for spaces, while the documented
  examples use percent encoding. The contract now requires `quote(...,
  safe="")`, stable `path` then `prompt` order, and `%20`.
- Empty prompt handling was initially ambiguous. It is now a deterministic
  rejection.
- Invalid UTF-8 and NUL behavior were unspecified. Both are now explicit
  failures.
- JSON formatting and failure exits were under-specified. The contract pins
  sorted, indented JSON, a final newline, stable error code/message fields, exit
  `0` for success, and exit `2` for invalid input.
- Prompt-file type and bounded reading were under-specified. The contract now
  requires a regular file and reads at most 8,193 bytes.
- A Markdown output mode would be convenient but unnecessary. It is excluded
  from v0.1 to keep the helper small.

## Assumptions To Resolve

No assumption blocks the code-only implementation decision. These remain live
trial questions:

- installed desktop acceptance of the URL;
- practical length below the local ceiling;
- composer transformation behavior;
- what the user actually sends;
- whether a future wrapper leaks or logs the URL.

## Authority Gaps

- No implementation approval exists yet.
- No generated link may be opened.
- No task may be created or messaged.
- No live prompt, workspace, task ID, status, or transport observation is
  authorized.
- No dependency, credential, config, CLI repair, app-server/SDK/MCP, product
  repository, push, merge, PR, deployment, or worker authority is approved.

## Verification Gaps

- Deterministic encoding/decoding tests can prove only helper behavior.
- Source inspection can show absence of process/network/clipboard paths but
  cannot prove desktop behavior.
- Same-task builder and verifier work must not be described as independent.
- A pinned fixture does not prove that Codex will accept the link.
- The fixed byte ceiling is a Factory helper policy, not an observed Codex
  compatibility threshold.

## Fallback Triggers

The future implementation mission must halt on:

- any request to open or test a link;
- any need for shell prompt arguments, stdin, clipboard, GUI, browser, or OS
  handler integration;
- prompt input that is empty, invalid UTF-8, contains NUL, or exceeds 8,192
  bytes;
- workspace input that is relative, absent, or not a directory;
- encode/decode mismatch;
- any need for a dependency, network, Codex executable, credential, server, or
  task control;
- pressure to generalize into another transport or change the fixed input
  policy without approval;
- failed verification without separately bounded recovery authority.

## Recommended Repairs

All required repairs are incorporated in the formation contract:

1. file-only non-sensitive prompt input;
2. strict resolved workspace identity;
3. exact percent encoding and parameter order;
4. fixed local prompt ceiling and reported URL size;
5. input-only digest with explicit no-transport-proof flags;
6. deterministic JSON/error/exit contract;
7. direct forbidden-import and forbidden-effect checks;
8. manual copy/paste fallback and a separate future live-trial gate.
9. cross-machine pinned encoder fixtures separated from real path-validation
   tests.

## Execution Readiness

`READY_FOR_SEPARATE_SPONSOR_DECISION`.

Recommended approval, if the sponsor wants implementation, should name
`V3-CODEX-DL-001`, the exact authorized paths, the 8,192-byte v0.1 policy, and
the prohibition on opening a link or creating a task.

Challenge PASS is not execution authority. The candidate remains unapproved
until the sponsor explicitly approves its code-only mission contract.
