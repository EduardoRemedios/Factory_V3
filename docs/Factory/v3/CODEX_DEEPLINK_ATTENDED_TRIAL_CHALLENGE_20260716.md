# Codex Deep-Link Attended Trial Challenge - 2026-07-16

## Status

Research-only, non-enforcing, and non-executing challenge over
`CODEX_DEEPLINK_ATTENDED_TRIAL_FORMATION_20260716.md`.

This review does not create a workspace or prompt file, generate/open a link,
create a task, send a prompt, capture a screenshot, start a worker, add a
dependency/credential, modify Same Second, or add runtime-control power.

## Challenge Result

### Verdict

`CONDITIONAL PASS` for a separate attended-trial sponsor decision.

The trial is bounded enough to execute only if the later approval explicitly
authorizes the disposable workspace creation, prompt artifact, one helper run,
one human click, one human Send, one no-tool/no-write task, sponsor screenshots
or honest absence, and one sponsor-mediated result return.

## Critical Findings

None after repair.

Opening the link and pressing Send are real task-creation/execution effects.
They remain outside this formation approval and require the separate exact Go.

## High Findings

1. The originating Factory task cannot observe the new task directly.
   - Risk: response, tool-use, workspace, and task-ID claims could rely only on
     a copied success sentence.
   - Repair adopted: require structured sponsor observation, preferred pre/post
     screenshots, before/after workspace evidence, and explicit unknown values.
     Worker echo is supplementary only.

2. Visual prompt comparison is not byte-level transport proof.
   - Risk: line endings, Unicode, hidden characters, or edits may differ despite
     a visually plausible composer.
   - Repair adopted: full PASS is limited to installed-desktop acceptance and
     visual prefill observation. The closeout must keep `transport_proof: false`
     and must not claim byte preservation.

3. Workspace binding may be ambiguous.
   - Risk: the app may open a new task without visibly showing the exact
     resolved folder.
   - Repair adopted: the exact workspace is pinned, sponsor observation is
     required, and `unknown` cannot yield full PASS. Wrong workspace safe-holds
     before Send.

4. A no-tool prompt does not enforce zero tools.
   - Risk: global instructions, model behavior, or hidden surface behavior may
     still cause commands, reads, or permissions.
   - Repair adopted: empty disposable workspace, fixed response-only prompt,
     visible activity observation, before/after snapshot, and immediate
     fail-safe on any tool/command/file/permission signal.

5. The trial could accidentally become a retry loop.
   - Risk: a mismatch might lead to prompt edits, another click, or a second
     task that hides the first failure.
   - Repair adopted: one generation/click/Send/task maximum and no recovery
     authority. First mismatch ends at safe hold with evidence preserved.

6. Workspace creation is an external local write.
   - Risk: formation approval could be misread as permission to create it now
     or overwrite existing content.
   - Repair adopted: exact path is pinned; creation requires trial Go; non-empty
     preexistence safe-holds; no deletion or cleanup is implied.

## Medium/Low Findings

- Screenshots may not expose a technical task ID. Record `unknown`; do not infer
  identity from the nonce.
- The fixed acknowledgment proves instruction-following only. It does not prove
  which prompt bytes the transport supplied.
- The sponsor still transfers the short result back to the Factory task. This
  trial reduces task creation/prompt-copy friction, not all cross-task friction.
- Opening a link may cause app/OS logging outside repository evidence. The
  prompt is deliberately non-sensitive.
- An empty non-Git directory differs from a real coding workspace. This is
  intentional because the trial tests transport, not product execution.
- The directory is retained after closeout; cleanup needs a later explicit
  decision.

## Assumptions To Resolve

No assumption blocks a separate attended-trial decision. The sponsor must be
available to perform and report the human checkpoints.

The following remain trial observations, not preconditions:

- desktop link acceptance;
- exact visible workspace;
- screenshot feasibility;
- task ID visibility;
- zero visible tool activity;
- unchanged workspace after Send.

## Authority Gaps

- Trial execution is not approved yet.
- No directory or prompt artifact may be created yet.
- No link may be generated, rendered, opened, or clicked.
- No task or worker may be started.
- No Send, screenshot capture, or result-return request is approved.
- No product repository, dependency, credential, SDK/MCP, automatic task
  control, cleanup, retry, push, merge, or adapter is approved.

## Verification Gaps

- Sponsor screenshots/attestation are not independent machine telemetry.
- The current harness exposes no task-reading API for cross-checking the new
  task.
- No byte-level composer or sent-message export is available.
- No malicious-worker or hidden-tool proof exists.
- A single successful synthetic trial will not establish reliability across
  versions, accounts, workspaces, prompts, or long missions.

## Fallback Triggers

Future execution must safe-hold on:

- non-empty pre-existing workspace;
- prompt byte/hash mismatch;
- helper error or field mismatch;
- link-open failure;
- not-new task;
- wrong or unobservable workspace;
- composer mismatch or inability to review;
- any pre-Send ambiguity;
- response mismatch or extra prose;
- any visible tool, command, read, write, permission, network, or activity card;
- workspace after-state change;
- missing sponsor observations required for the claimed verdict;
- request for retry, cleanup, alternate input, or broader authority.

## Recommended Repairs

All required repairs are incorporated:

1. exact durable disposable workspace with non-empty fail-safe;
2. exact 245-byte prompt, digest, nonce, and expected response;
3. one-action ceilings for generation/click/Send/task;
4. sponsor checkpoint before Send;
5. preferred pre/post screenshots and structured observation fields;
6. explicit `unknown` handling and no full PASS without workspace confirmation;
7. before/after workspace snapshot;
8. no-tool/no-write response-only task;
9. no retry or recovery authority;
10. retained evidence and manual fallback.

## Execution Readiness

`CONDITIONAL READY FOR SEPARATE SPONSOR DECISION`.

Recommended future approval must name `V3-CODEX-DL-TRIAL-001`, the exact
workspace and prompt, one helper run, one human click/Send, sponsor observation,
no-tool/no-write task boundary, retained artifacts, and no retry.

Challenge conditional PASS is not execution authority. The trial remains
unapproved until the sponsor approves the exact candidate contract.
