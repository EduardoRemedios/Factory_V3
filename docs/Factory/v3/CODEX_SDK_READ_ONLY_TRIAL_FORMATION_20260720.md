# Codex SDK Read-Only Trial Formation - 2026-07-20

## Status

Research-only, non-enforcing, and non-executing mission-formation output for
candidate `V3-CODEX-SDK-RO-001`.

This artifact does not install a runtime or SDK, authenticate, inspect or
change credentials, start Codex, start app-server/MCP, create or resume a
thread, create a trial workspace, send a prompt, modify Same Second, implement
an adapter, or add runtime-control power.

## Source Evidence

- `CODEX_SDK_ORCHESTRATION_DIRECTION.md`
- `CODEX_TASK_SURFACE_DISCOVERY_FORMATION_20260716.md`
- `CODEX_TASK_SURFACE_DISCOVERY_CHALLENGE_20260716.md`
- `task_surface_discovery/V3-CODEX-DISC-001/DECISION.md`
- `CODEX_DEEPLINK_ASSIST.md`
- `deeplink_assist/V3-CODEX-DL-ADOPT-001/DECISION.md`
- `ATTENDED_MVP_READINESS_EPIC_001_REVIEW_20260718.md`
- `PHASE0_DECISION_CLOSURE_GATE_001_REVIEW_20260720.md`
- `MISSION_CONTROL_CONTRACT.md`
- `SERIAL_MISSION_STATE_KERNEL.md`
- `GOVERNANCE_BOUNDARIES.md`
- OpenAI Codex documentation refreshed 2026-07-20:
  - [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk)
  - [Codex as an MCP server](https://learn.chatgpt.com/docs/mcp-server#running-codex-as-an-mcp-server)

Official documentation describes SDK thread start/resume and read-only sandbox
configuration. It establishes a possible interface, not local readiness,
sandbox enforcement, authentication readiness, or trial success.

Local read-only formation inspection found:

- no `node` or `npm` on `PATH`;
- macOS `/usr/bin/python3` at 3.9.6, below the documented Python SDK minimum;
- the separate framework Python 3.12 path has previously hung even on
  `--version` in this harness and was not repaired or used;
- a current app-bundled Codex executable exists, but it was not launched and
  does not prove SDK availability;
- no SDK package, compatible controller runtime, package integrity pin, or
  approved authentication path has been established.

These are current-harness observations, not universal Codex product claims.

## Mission Formation Result

### Route

`CANDIDATE_V3_ENVELOPE`

The attended manual and deep-link evidence justifies forming one bounded SDK
trial candidate. Current runtime, dependency, and authentication prerequisites
are not ready, so the candidate cannot proceed directly to execution approval.

### Problem Statement

Factory V3 has observed a manual fresh-task handoff and one optional deep-link
use, but a human still creates/sends the task and returns results. Official SDK
sources describe programmatic thread start and resume, yet no local evidence
shows that this harness can use that surface with a read-only sandbox, durable
thread identity, observable events, bounded authentication, and no target
workspace mutation.

The missing evidence is one synthetic transport/runtime observation. It is not
permission to implement a worker adapter or connect the state kernel to Codex.

### Desired Outcome

After a later exact sponsor Go that resolves the prerequisite gap, run one
attended synthetic trial that:

1. uses one exact disposable target workspace containing one non-sensitive
   read-only fixture;
2. uses one separately isolated controller environment;
3. starts exactly one SDK thread with the narrowest documented read-only
   sandbox;
4. asks the worker to read only the pinned fixture and return one exact
   acknowledgment;
5. resumes that same thread exactly once with a second fixed no-tool
   acknowledgment prompt;
6. records the durable thread ID, SDK event stream, terminal results, sandbox
   request, controller/runtime identity, and before/after target snapshot;
7. stops on the first mismatch without retry, repair, or surface substitution;
8. closes with bounded supported and unsupported claims.

### Non-Goals

- No Same Second or other product work.
- No Factory state-kernel-to-worker adapter.
- No MCP, app-server, Agents SDK, subagent, concurrency, scheduler, daemon,
  background process, standing authorization, or unattended run.
- No workspace-write or full-access sandbox.
- No automatic activation, next-action decision, verification admission,
  evidence promotion, closeout, retry, or recovery.
- No product commands, tests, Git mutation, browser control, external-service
  selection, deployment, push, merge, PR, or production action.
- No credential value inspection, logging, storage, creation, or rotation.
- No claim of filesystem isolation, malicious-worker resistance, hidden-tool
  absence, portability, production readiness, or runtime authority.

### Assumptions

- Factory-authored artifacts remain the only mission authority. SDK thread
  state and model output are evidence inputs only.
- The sponsor is present for prerequisite approval, pre-start inspection,
  start, pre-resume inspection, resume, and closeout.
- A future exact Go may approve a pinned isolated SDK installation and existing
  non-exported authentication use; neither is approved here.
- Worker network use is forbidden. The controller's two Codex service calls
  are an external effect that must be explicit in the later Go.
- The target snapshot can prove observed content stability, not enforcement of
  every filesystem or process boundary.

### Unknowns

- Which compatible controller runtime will be used.
- The exact SDK package version and registry integrity digest.
- Whether an existing authentication path is available without credential
  mutation or disclosure.
- Exact installed SDK event and error shapes.
- Whether the SDK can bind the exact working directory and read-only sandbox in
  this desktop/account environment.
- Whether start and resume expose one stable durable thread ID.
- Whether worker tool calls, approval requests, and terminal status are
  completely observable.
- Whether the target remains unchanged after the observed thread lifecycle.

## Proposed Exact Trial Shape

These paths and inputs are candidates to pin in the later prerequisite record;
they are not created by this formation.

### Target workspace

```text
/Users/eduardodosremedios/codex_sdk_ro_trial_001_workspace
```

The path must be absent before approved preparation. Preparation may create only
the directory and one regular UTF-8 fixture:

```text
TRIAL_INPUT.txt
```

Exact proposed fixture content, including final newline:

```text
V3-CODEX-SDK-RO-001 START INPUT 6A91D4C2
```

The final prerequisite artifact must pin its byte count and SHA-256 before any
thread starts.

### Controller workspace

```text
/Users/eduardodosremedios/codex_sdk_ro_trial_001_controller
```

The controller must be isolated from Factory V3, Same Second, and the target
workspace. Any runtime/package installation must remain inside this exact
mission-owned controller path and be separately authorized with exact version
and integrity evidence.

### Start prompt

The later execution artifact must pin exact UTF-8 bytes and SHA-256 for a prompt
that:

- identifies `V3-CODEX-SDK-RO-001`;
- permits reading only `TRIAL_INPUT.txt` in the exact target workspace;
- forbids every other file read, write, command beyond the minimum read,
  network action, permission request, or scope expansion;
- requires exactly:
  `V3-CODEX-SDK-RO-001 START ACK 6A91D4C2`.

### Resume prompt

The later execution artifact must pin exact UTF-8 bytes and SHA-256 for a
no-tool prompt that resumes the recorded thread ID and requires exactly:

```text
V3-CODEX-SDK-RO-001 RESUME ACK B7E20F61
```

### Action ceilings

- one controller environment;
- one target workspace;
- one SDK package and version;
- one authentication preflight;
- one thread start;
- one start prompt;
- one resume of the same thread;
- one resume prompt;
- no retry, alternate surface, prompt rewrite, second thread, or recovery.

## Human Decisions Needed

Before execution can be considered:

1. Provide or approve one exact working controller runtime compatible with the
   official SDK.
2. Pin one exact SDK package, version, source, and integrity digest.
3. Approve or reject an isolated installation at the exact controller path.
4. Approve or reject use of an existing non-exported authentication context and
   the two external Codex service calls; any login, token entry, or credential
   change requires another decision.
5. Approve the exact final target fixture, prompts, hashes, cleanup/retention
   policy, and evidence fields.
6. After a repaired challenge, approve or reject execution of the one attended
   trial.

## Pre-Resolved Decisions

- SDK only; do not substitute MCP, app-server, CLI `exec`, desktop deep links,
  native task tools, Agents SDK, browser control, or GUI automation.
- Factory and Same Second are never worker target workspaces.
- Read-only sandbox is mandatory; any unavailable or weaker setting halts.
- The controller may carry an already-approved action but may not derive or
  grant authority.
- Start and resume use the same recorded thread ID.
- The start turn may read only the exact fixture. The resume turn may use no
  tool.
- Any write, extra read, extra command, network tool, permission request,
  unexpected event, wrong response, missing identity, or target change fails
  safe.
- No retry or automatic fallback.

## Verification And Evidence Needs

Future evidence directory:

```text
docs/Factory/v3/codex_sdk_ro/V3-CODEX-SDK-RO-001/
```

Required future artifacts:

- `PREREQUISITES.json`
- `TRIAL_INPUT.txt`
- `START_PROMPT.txt`
- `RESUME_PROMPT.txt`
- `BEFORE_SNAPSHOT.json`
- `SDK_EVENT_STREAM.jsonl`
- `TRIAL_RESULT.json`
- `AFTER_SNAPSHOT.json`
- `CLOSEOUT.md`

Required evidence:

- exact runtime executable/version and controller path;
- exact SDK package/version/source/integrity and lock metadata;
- authentication disposition without credential values;
- exact target path, fixture/prompt bytes, and SHA-256 values;
- controller-requested sandbox and working directory;
- durable thread ID from start and the same ID used for resume;
- ordered SDK items/events for both turns, including tool/command, approval,
  error, status, and final-response observations;
- before/after target file list, type, size, mode, and content digest;
- process exit/termination and no remaining listener/background process;
- explicit separation of observed configuration from enforcement claims;
- builder/verifier actor and session provenance;
- supported and unsupported boundary claims;
- setup friction, false-positive/false-negative observations, and no-retry
  outcome.

## Candidate Mission Contract

### Mission ID

`V3-CODEX-SDK-RO-001`

### Objective

Observe exactly one attended Codex SDK thread start and one resume against a
pinned synthetic read-only target while keeping Factory V3 as the sole mission
authority and preserving complete bounded evidence.

### Success Criteria

1. The later sponsor Go names the exact runtime, SDK version/integrity,
   isolated controller path, authentication disposition, target, prompts, and
   action ceilings.
2. Target and controller paths are newly created, exact, separate, and outside
   Factory V3 and Same Second.
3. The target contains only the pinned fixture before start.
4. One SDK thread starts with the exact target and read-only sandbox.
5. The start turn reads only the exact fixture and returns the exact start
   acknowledgment.
6. The same durable thread ID is resumed once and returns the exact resume
   acknowledgment with no tool call.
7. Ordered SDK evidence exposes both turns, tool/activity observations,
   terminal results, and errors without credential content.
8. The target before/after snapshots match exactly by path, type, size, mode,
   and content digest.
9. No extra thread, retry, fallback surface, permission escalation, product
   action, or lingering process occurs.
10. Closeout limits claims to this one local, synthetic, attended observation.

### Authorized Scope

Only after a later exact execution approval:

- create the exact controller and target paths when absent;
- create the pinned fixture and evidence artifacts;
- install one exact approved SDK package into the controller path only;
- use an exact approved compatible runtime;
- use an approved existing authentication context without reading or recording
  credential values;
- make exactly two controller-originated Codex service turns: one start and one
  resume;
- allow the worker to read only the exact target fixture on the start turn;
- record local evidence and update active Factory canons after closeout.

### Forbidden Scope

- Any action before the later exact Go.
- Same Second writes or worker access.
- Factory V3 as worker target.
- MCP, app-server, CLI substitution, Agents SDK, subagents, concurrency,
  automation, scheduler, daemon, background or unattended continuation.
- Workspace-write/full-access sandbox, permission escalation, worker network,
  broad filesystem inspection, Git, product commands, verification commands,
  browser/GUI control, deployment, push, merge, or PR.
- Credential values in prompts, logs, events, evidence, or repository files.
- Adapter implementation, state-kernel integration, automatic task activation,
  evidence admission, verification judgment, closeout, retry, or recovery.
- Required gates, runtime authority, governance routing, profile promotion, or
  Factory V2 removal.

### Dependency Policy

No dependency is approved by formation. A later execution Go must name one
exact SDK package/version/source/integrity, one compatible runtime, and the
isolated installation path. Any additional package, runtime installation,
repair, package-manager bootstrap, global install, credential action, or
surface substitution safe-holds.

### Budget And Checkpoint Rules

- No duration, token, call, file, or output floor.
- Two model turns maximum: one start and one resume.
- Checkpoint after prerequisite verification, preparation, start result,
  pre-resume review, resume result, snapshot comparison, and closeout.
- Human attendance is mandatory at every action boundary.
- Stop on success or the first mismatch.

### Human Interrupt Rules

Tier 3 approval is required for the final prerequisite pack and trial Go.
During execution, any login, credential/config change, package/runtime
deviation, unexpected network requirement, permission request, write, wrong
workspace, missing event field, retry, repair, cleanup, or scope expansion
safe-holds for a new decision.

### Halt And Fallback Rules

Halt without starting a thread when prerequisites, hashes, paths, sandbox,
authentication, or before-snapshot evidence differ.

After start, safe-hold on any unexpected event, file/tool access, command,
permission, network action, response mismatch, missing thread ID, target change,
or process ambiguity. Preserve evidence and do not resume or retry.

After successful start, resume only when the sponsor confirms the recorded
thread ID, exact prompt, clean event state, unchanged target, and exactly one
safe next action. Any ambiguity ends the trial without resume.

There is no automatic fallback. A later repaired attempt would be a new mission.

### Re-Entry Instructions

A future execution task must read this formation, its challenge, the final
prerequisite artifact, current Factory canons, official SDK documentation, and
current repository state. It must verify the exact later sponsor approval and
derive one safe action from authored artifacts. Session memory, SDK thread
memory, copied summaries, or model output are never authority.

## Recommended Next Step

Resolve the runtime/package/authentication prerequisite gap without installing
or starting anything, then repair and re-challenge the exact candidate for a
separate sponsor execution decision.

This is candidate mission-formation output only. It does not authorize
execution until the human explicitly approves the mission contract.
