# Codex Deep-Link Optional Attended-Aid Adoption Formation - 2026-07-16

## Status

Research-only, advisory, non-enforcing, and non-executing mission-formation
output for candidate `V3-CODEX-DL-ADOPT-001`.

This artifact does not adopt the helper, authorize its future use, generate or
open a link, create or send a Codex task, start a worker, change an operational
profile, add a required gate, or begin full automation.

## Mission Formation Result

### Route

`CANDIDATE_V3_ENVELOPE`

The deterministic helper is implemented and one separately approved attended
synthetic trial completed at `PASS_WITH_LIMITATIONS`. The smallest coherent
next decision is whether to recognize the helper as an optional attended
handoff aid inside future missions that already possess exact execution
authority.

### Problem Statement

Manual task creation and prompt copy/paste caused avoidable sponsor friction in
the Same Second attended pilot. The helper demonstrated that it can prepare a
reviewable desktop deep link for a short non-sensitive prompt while retaining
human Send, but it does not prove transport integrity, task identity, task
status, automatic execution, or worker control.

Without a bounded adoption rule, future tasks may either repeat unnecessary
copy/paste or over-generalize one synthetic trial into default or automated
authority.

### Desired Outcome

Prepare a separate sponsor decision that can, if later approved:

1. recognize the existing helper as an optional attended handoff aid;
2. restrict use to already-approved missions that explicitly name the aid;
3. preserve authored graph/state, committed handoff artifacts, and the mission
   envelope as the only sources of state and authority;
4. require deterministic preparation evidence plus human workspace/prompt
   review and Send;
5. require manual task creation/copy-paste or mission safe hold on mismatch;
6. keep all automation, task-status, SDK/MCP, adapter, and worker-runtime work
   outside the adoption.

### Non-Goals

- No default Factory V3 mode or operational-profile promotion.
- No standing authorization to create tasks or start workers.
- No automatic link opening, Send, retry, task reading, task status, resume,
  interrupt, archive, pin, or handoff.
- No Codex CLI repair, app-server, SDK, MCP, Agents SDK, dependency, credential,
  plugin, connector, scheduler, daemon, background process, or concurrency.
- No sensitive, secret, credential-bearing, regulated, production, or real-data
  prompt content in a URL.
- No replacement for authored mission state, graph authority, committed
  re-entry artifacts, or current repository checks.
- No byte-level transport, full-path UI, hidden-tool, malicious-worker,
  reliability, or production-readiness claim.
- No Same Second modification, product integration, deployment, push, or merge.

### Assumptions

- Human review and Send remain acceptable for the attended lane.
- Future mission formation can name the aid and its exact workspace/prompt
  evidence before use.
- Short non-sensitive prompt artifacts are sufficient for selected handoffs;
  larger or sensitive handoffs retain manual fallback.
- The helper's existing 8,192-byte ceiling remains a local safety policy, not a
  measured Codex product limit.
- One successful synthetic observation supports optional attended use only,
  not default or unattended use.

### Unknowns

- Reliability across desktop versions, accounts, long prompts, real product
  workspaces, and different task types.
- Whether future desktop surfaces expose full absolute workspace identity or a
  technical task ID.
- Whether a later task API can remove the remaining human click/Send and result
  transfer without weakening Factory authority.
- Whether repeated attended use materially reduces total mission friction once
  evidence preparation is counted.

## Evidence Basis

- `CODEX_DEEPLINK_ASSIST.md`
- `deeplink_assist/V3-CODEX-DL-001/CLOSEOUT.md`
- `CODEX_DEEPLINK_ATTENDED_TRIAL_FORMATION_20260716.md`
- `CODEX_DEEPLINK_ATTENDED_TRIAL_CHALLENGE_20260716.md`
- `deeplink_assist/V3-CODEX-DL-TRIAL-001/PREPARE.json`
- `deeplink_assist/V3-CODEX-DL-TRIAL-001/HUMAN_OBSERVATION.md`
- `deeplink_assist/V3-CODEX-DL-TRIAL-001/POST_RESPONSE_SCREENSHOT.png`
- `deeplink_assist/V3-CODEX-DL-TRIAL-001/CLOSEOUT.md`

The evidence supports one bounded installed-desktop observation. It does not
prove general reliability or full automation.

## Options

| Option | Value | Risk / limitation | Formation verdict |
| --- | --- | --- | --- |
| A. Adopt as an optional attended aid inside explicitly approved missions | Removes manual prompt copying while preserving human review and mission authority | Still needs one click, Send, and honest observation; transport/task status remain unproved | Recommended |
| B. Keep as trial-only research | Maximizes conservatism | Repeats known copy/paste friction and gathers no natural usage evidence | Acceptable fallback |
| C. Make it default or automate task control | Removes more human action | Unsupported by evidence and requires new runtime/dependency/authority decisions | Reject and defer |

## Proposed Eligibility Rule

The aid is eligible only when all conditions are true:

1. a separately approved mission envelope already authorizes the target worker
   task and exact workspace;
2. that envelope explicitly names the deep-link aid as an allowed attended
   handoff mechanism;
3. the prompt is an existing regular UTF-8 file, non-empty, NUL-free, at most
   8,192 bytes, and classified non-sensitive;
4. the prompt points to authored durable state and does not treat session memory
   as authority;
5. the workspace is an existing absolute directory and its resolved path is
   reviewed;
6. the human sponsor is present to inspect the preparation output, open the
   link, verify workspace/project and complete visible prompt, and press Send;
7. a manual task-creation/copy-paste fallback is available.

If any condition is false or unknown, the aid is ineligible.

## Proposed Use Protocol

1. The mission controller prepares or selects the exact non-sensitive prompt
   artifact from authored mission records.
2. Run the existing helper once for that handoff.
3. Retain the deterministic JSON or its exact fields:
   - resolved workspace;
   - prompt byte count and SHA-256;
   - URL byte count;
   - `human_send_required: true`;
   - `transport_proof: false`.
4. The human reviews the workspace and prompt before Send.
5. On a match, the human may click and Send once under the existing mission
   authority.
6. On any mismatch, ambiguity, helper failure, sensitive-content concern, or
   unsuitable URL length, do not Send. Use the manual fallback or the mission's
   authored safe-hold rule.
7. Record the handoff result and any limitation in the mission evidence.

Screenshots are optional for ordinary eligible use and recommended for a new
desktop/harness version, anomaly, disputed observation, or later evidence
review. Screenshot capture must not expose sensitive content.

## Authority Model

The optional aid may transport a prompt only after mission authority already
exists. It cannot:

- authorize a child;
- activate a worker;
- expand paths or commands;
- satisfy dependency, verification, evidence, or closeout gates;
- replace expected-revision or repository-state checks;
- convert a derived cursor into authority;
- make session memory authoritative.

The human Send is an attended execution action admitted by the approved mission,
not by the helper or this adoption candidate.

## Human Decisions Needed

1. Approve, reject, or defer optional attended-aid adoption under the exact
   eligibility and protocol above.
2. Decide later, under a separate formation/challenge, whether any native task
   surface or SDK/MCP lane should be investigated for full automation.

## Pre-Resolved Decisions

- Candidate ID: `V3-CODEX-DL-ADOPT-001`.
- Option A is recommended.
- Adoption is optional and per-mission explicit, never default.
- Existing helper code, tests, limits, and `transport_proof: false` remain
  unchanged.
- Authored mission artifacts remain state and authority.
- Human inspection and Send remain mandatory.
- Manual copy/paste is the safe fallback.
- Screenshots are conditional evidence, not a universal required gate.
- No live use, implementation, dependency, profile promotion, or automation is
  included in the adoption decision.

## Verification And Evidence Needs

For the later adoption-recording decision:

- formation and challenge artifacts are present and mutually consistent;
- active canons describe optional per-mission use and explicit exclusions;
- helper unit tests and pinned fixtures still pass unchanged;
- V3 advisory/operational validators pass or retain only classified historical
  non-blocking findings;
- source review confirms no link-opening, task-control, process, network, SDK,
  MCP, credential, or workspace-write path;
- no live link or task is created while recording adoption.

For later natural use:

- exact mission authority reference;
- exact resolved workspace;
- prompt artifact reference, bytes, and SHA-256;
- confirmation of `human_send_required: true` and
  `transport_proof: false`;
- human pre-Send match or explicit mismatch;
- fallback/safe-hold result when not sent;
- limitations or anomalies relevant to the mission's claims.

## Candidate Adoption Contract

### Objective

Recognize the existing deterministic helper as an optional attended handoff aid
for short non-sensitive prompts inside future missions that already authorize
the exact worker task and explicitly name this mechanism.

### Success Criteria

1. Adoption remains optional, advisory, and non-default.
2. Each use is admitted only by an exact approved mission envelope.
3. Authored mission state and committed/durable handoff artifacts remain
   authoritative.
4. Input and deterministic preparation evidence meet the eligibility rule.
5. Human workspace/prompt review and Send remain mandatory.
6. Mismatch or uncertainty uses manual fallback or authored safe hold.
7. No transport integrity, task identity/status, hidden-tool, or automation
   claim is made.
8. Existing helper implementation and tests remain unchanged.

### Authorized Scope After Separate Adoption Approval

- Record the optional attended-aid policy in active Factory V3 canons.
- Permit future separately approved mission envelopes to name the existing
  helper as an allowed handoff mechanism under this contract.
- Collect bounded natural-use evidence without making it a required gate.

### Forbidden Scope

- Live helper use or task creation by adoption approval alone.
- Default use, standing task authority, automatic link open/Send, retry,
  worker dispatch, task status, task reading, interruption, resume, or adapter.
- Helper code or limit changes.
- Dependencies, credentials, CLI repair, app-server, SDK, MCP, Agents SDK,
  plugins, connectors, schedulers, daemons, background processes, concurrency,
  deployment, required gates, governance routing, runtime authority, profile
  promotion, V2 removal, push, or merge.

### Allowed Tools And Commands For Adoption Recording

- `apply_patch` for exact Factory V3 policy/canon artifacts;
- read-only repository inspection with `git`, `rg`, `sed`, `find`, `shasum`,
  and JSON parsing;
- existing repository tests, knowledge lint, context indexing, advisory
  validators, Python compilation, and `git diff --check`.

No helper run, link generation/open, task creation, Send, worker execution, or
external effect is allowed during adoption recording.

### Dependency Policy

Stdlib-only implementation remains unchanged. No dependency may be added.

### Halt And Fallback Rules

- Halt adoption recording on scope expansion, helper implementation change,
  validator/gate change, dependency request, live-use request, or automation
  request.
- For later eligible missions, do not Send on any mismatch or uncertainty.
- Manual task creation and prompt copy/paste remain the safe fallback.
- Failed mission verification follows the mission's authored safe-hold/recovery
  authority, never an automatic deep-link retry.

### Re-entry Instructions

Read the approved mission envelope, authored state, current repository state,
this adoption contract, and the helper documentation. Session memory alone is
insufficient. Derive exactly one safe next action from authored artifacts; the
aid grants no authority.

This is candidate mission-formation output only. It does not authorize adoption
or execution until the human explicitly approves the candidate contract.
