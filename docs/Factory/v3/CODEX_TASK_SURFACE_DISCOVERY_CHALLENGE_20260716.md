# Codex Task-Surface Discovery Challenge - 2026-07-16

## Status

Research-only, non-executing challenge review over
`CODEX_TASK_SURFACE_DISCOVERY_FORMATION_20260716.md`.

This review does not approve `V3-CODEX-DISC-001`, create or message a Codex
task, repair or install Codex, start app-server/MCP, authorize a dependency,
modify Same Second, or grant worker/runtime authority.

## Challenge Result

### Verdict

`CONDITIONAL PASS` for sponsor-Go readiness.

The candidate is bounded enough for a separate research execution decision.
The default approved interpretation must be documentation and capability
inspection only. A live synthetic task probe is not included unless the
sponsor's later Go names it explicitly.

## Critical Findings

None after repair.

Starting a task from this formation artifact without a later exact Go would be
an authority violation because task creation and prompt send are external
worker-execution effects.

## High Findings

1. Native task tooling is not currently available.
   - Observation: the current Factory task exposes no create/list/read/send
     Codex task controls.
   - Risk: an execution task might improvise another surface or treat docs as
     proof of local availability.
   - Repair adopted: capability preflight is mandatory; absent native tools
     produce `DEEPLINK_ASSIST_ONLY` or `NO_ADAPTER_CANDIDATE`, not installation,
     repair, or automatic surface substitution.

2. The local CLI path is broken.
   - Observation: the Node wrapper exists, but its packaged Darwin ARM64 binary
     is missing and version/help calls fail with `ENOENT`.
   - Risk: a seemingly read-only spike could expand into package repair,
     dependency installation, authentication, or long-running app-server work.
   - Repair adopted: record the failure once and stop; all repair/install/auth
     work requires a new formation mission and sponsor decision.

3. A read-only sandbox does not prove that the worker took no actions.
   - Risk: a synthetic probe could still read files, invoke tools, request
     permissions, or use network capability while making no filesystem write.
   - Repair adopted: the optional probe must use a no-tool prompt, the narrowest
     read-only/no-escalation settings available, record tool-call evidence, and
     fail on any worker tool call or permission request.

4. Worker echo is not transport-integrity proof.
   - Risk: asking the worker to repeat a digest proves only its output claim,
     not which bytes the transport actually submitted.
   - Repair adopted: bind the prompt hash to transport-recorded input or
     canonical request JSON; use a returned nonce only as supplementary
     evidence.

## Medium/Low Findings

- Deep links are a useful documented control but do not meet the no-copy/paste
  objective because the user must press Send. They should remain a baseline,
  not be presented as an adapter success.
- A desktop-native task tool may be harness-private or rollout-dependent. The
  final recommendation must label portability and support status explicitly.
- The original candidate left its evidence directory to the later approval.
  This was repaired to the exact path
  `docs/Factory/v3/task_surface_discovery/V3-CODEX-DISC-001/`.
- Scheduled tasks are not a safe substitute: they introduce unattended
  execution and use a different continuity model.
- App-server's thread/turn primitives are strategically relevant, but its
  process, auth, schema/version, and dependency surfaces make it a later lane.

## Assumptions To Resolve

- Whether a later Codex task exposes supported native task controls.
- Whether those controls distinguish new/non-forked creation and expose the
  sent input, workspace, sandbox, status, and task ID.
- Whether task-control output remains readable after the new task terminates.
- Whether the approved harness can force zero worker tool calls or only observe
  them after the fact.

## Authority Gaps

- No live synthetic task creation or prompt send is approved yet.
- No SDK/CLI/package repair or installation is approved.
- No credential, authentication, config, plugin, or MCP change is approved.
- No app-server or MCP process is approved.
- No workspace-write, Same Second, Git mutation, worker command, sub-agent,
  concurrent, scheduled, background, or unattended action is approved.

## Verification Gaps

- Official documentation establishes possible interfaces, not availability in
  this exact desktop task.
- Current-session absence does not prove the tools are unavailable in every
  task type or future release.
- No live prompt-transport trace, task ID, status, or halt evidence exists.
- No task-surface FP/FN corpus exists; the first approved spike should record
  observed mismatches without proposing validator enforcement.
- The broken local CLI prevents even help/schema replay through that install;
  documentation must be labeled separately from local capability evidence.

## Fallback Triggers

The future discovery task must halt or return a bounded negative decision on:

- native task tools absent at preflight;
- non-forked semantics not explicit;
- exact workspace or input not observable;
- any task creation not explicitly included in sponsor Go;
- any worker tool call, write, permission escalation, auth request, or network
  action during an approved probe;
- missing task ID or terminal status;
- local CLI failure;
- pressure to install, repair, authenticate, start a server, or switch to
  scheduled/SDK/MCP orchestration;
- stale official sources, repository drift, or contradictory evidence.

## Recommended Repairs

The following repairs are incorporated into the formation artifact:

1. Pin the exact evidence directory and required output files.
2. Make native-surface availability a fail-closed preflight.
3. Require transport-recorded input for prompt-integrity evidence.
4. Require zero worker tool calls in any separately approved synthetic probe.
5. Treat CLI failure as terminal evidence rather than repair authority.
6. Preserve deep links as assistive prefill only and SDK/MCP as later research.

## Execution Readiness

`CONDITIONAL READY FOR SPONSOR DECISION`.

Recommended default approval is the no-probe read-only discovery pass. If the
sponsor wants the single synthetic task probe, the approval must say so
explicitly and preserve the zero-tool, zero-write, non-forked, fixed-prompt
conditions.

Challenge PASS is not execution authority. `V3-CODEX-DISC-001` remains
unapproved until the sponsor approves the exact candidate contract.
