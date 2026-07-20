# Codex SDK And MCP Orchestration Direction

## Version
v0.11

## Change Log
- v0.11 (2026-07-20): Recorded Same Second `V3-SS-PHASE0-GATE-001` as passed bounded decision closure with product result `BLOCKED_MISSING_DECISIONS`. Added non-executing SDK-only candidate `V3-CODEX-SDK-RO-001`, challenged at `MORE DISCOVERY` for one later attended synthetic read-only thread start/resume. No compatible runtime, pinned SDK integrity, or approved authentication is yet proved; the next gate is a file-only prerequisite pack and repaired challenge, not installation or execution.
- v0.10 (2026-07-18): Recorded Same Second `V3-SS-MVP-READINESS-001` as the first natural eligible use of the optional attended deep-link aid. The useful four-child mission retained an authored 243-byte prompt, deterministic preparation evidence, human review/Send, fresh-task replay, and manual safe-hold/recovery. The observation does not prove transport integrity, task identity/status, automatic Send, adapter behavior, or runtime authority. The next gate is a separate non-executing Phase 0 decision-closure candidate; full automation remains unapproved.
- v0.9 (2026-07-16): Recorded sponsor-approved `V3-CODEX-DL-ADOPT-001` as an optional attended aid under its exact per-mission eligibility, evidence, human review/Send, and fallback contract. Adoption alone creates no live-use or task authority. The next evidence target is one natural eligible use; full automation remains separately governed and unapproved.
- v0.8 (2026-07-16): Added formed/challenged non-executing optional adoption candidate `V3-CODEX-DL-ADOPT-001` at `PASS` for a separate sponsor decision. It requires existing exact mission authority, per-mission explicit use, non-sensitive prompts, authored-state control, deterministic evidence, human review/Send, and manual fallback. No live use, default use, automatic task control, task status, SDK/MCP, adapter, or runtime authority is approved.
- v0.7 (2026-07-16): Recorded attended `V3-CODEX-DL-TRIAL-001` at `PASS_WITH_LIMITATIONS` without retry. The installed desktop accepted the intended project/prompt and returned the exact acknowledgment with no visible tool/permission activity; the empty workspace remained unchanged. This is bounded attended evidence, not byte-level transport, task-status, hidden-activity, adapter, or automation proof. The next separate gate is optional attended-aid adoption; full automation remains a later lane.
- v0.6 (2026-07-16): Added challenged attended candidate `V3-CODEX-DL-TRIAL-001` as the next separate decision after helper implementation. It authorizes nothing by formation and keeps SDK/MCP, dependencies, credentials, automatic task control, retries, and runtime authority outside scope.
- v0.5 (2026-07-16): Recorded implemented code-only `V3-CODEX-DL-001` with deterministic stdlib encoding and explicit human-Send/no-transport-proof semantics. The next gate is separate attended synthetic live-link trial formation; no live task, SDK/MCP execution, dependency, credential, adapter, workspace write, or runtime authority is approved.
- v0.4 (2026-07-16): Added challenged non-executing `V3-CODEX-DL-001` as the next separate code-only decision after `DEEPLINK_ASSIST_ONLY`. The helper candidate retains human Send and does not approve link opening, task creation, SDK/MCP execution, dependency, credential, process, adapter, workspace write, or runtime authority.
- v0.3 (2026-07-16): Recorded approved no-probe `V3-CODEX-DISC-001` at `DEEPLINK_ASSIST_ONLY`. Native task controls were absent in the current task, the local CLI runtime is missing, and documented deep links can prefill workspace/prompt but cannot send or return status. The next gate is separate non-executing deep-link helper formation; no SDK/MCP execution, dependency, credential, task, adapter, or runtime authority is approved.
- v0.2 (2026-07-16): Recorded completion of the manual attended serial-epic prerequisite and linked the challenged non-executing `V3-CODEX-DISC-001` task-surface candidate. This does not approve a live task probe, SDK/MCP execution, dependency, credential, adapter, workspace write, or runtime authority.
- v0.1 (2026-06-05): Initial strategic note on using Codex SDK, Codex MCP, and Agents SDK as possible orchestration surfaces for Factory V3 and Harmony.

## Status
Strategic direction and research roadmap context only. This document does not make Factory V3 the default mode, approve a new operational profile, approve unattended execution, approve production actions, wire V3 into required gates, or grant runtime authority.

## Purpose
Record a second important V3 product direction:

```text
Codex should be treated as a programmable software-engineering worker, not as the whole governance brain.
```

The Codex SDK and Codex MCP surfaces suggest a useful architecture for Factory V3 and Harmony:

```text
Harmony / Factory = mission authority, routing, evidence, policy
Codex            = code-changing worker runtime
Agents SDK / MCP = orchestration substrate
Skills           = reusable worker behavior
Mission records  = replayable governance evidence
```

This is a strategic signal, not current operating authority.

## Source Signals
The official Codex SDK documentation describes programmatic control over Codex, including starting and resuming threads and using sandbox presets such as read-only, workspace-write, and full-access.

The official Codex with Agents SDK guide describes running Codex as an MCP server, exposing tools to start and continue Codex sessions, and orchestrating Codex inside multi-agent workflows with handoffs, guardrails, and traces.

These surfaces align with the V3 direction toward governed autonomous execution, but they do not replace Factory governance.

## Architectural Interpretation
Factory V3 should not treat Codex as the source of mission authority.

Instead:
- Factory or Harmony creates the mission envelope.
- Factory or Harmony defines constraints, allowed tools, sandbox, budget, verification, and halt rules.
- Codex executes only within the granted mission authority.
- Factory or Harmony validates evidence and decides whether to continue, interrupt, halt, or escalate.

This preserves the V3 distinction between:
- conversation,
- evidence,
- human approval,
- execution authority.

## Candidate Workflow
A future research workflow could look like:

```text
Discovery Skill
  -> Challenge Skill
  -> Candidate Mission Contract
  -> Human Approval
  -> Factory/Harmony Orchestrator
  -> Codex Worker Runtime
  -> Verification Agent
  -> Governance Review
  -> Closeout / Learning
```

For Harmony-style systems, this may later support:
- integration adapter generation,
- feed/API sandbox work,
- test generation and repair,
- evidence-pack creation,
- PR preparation,
- review and verification passes.

## Research Spike
The first useful spike should be small and non-operational.

Recommended sequence:

1. Design the mission-formation and challenge skills.
2. Trial those skills manually.
3. Create a Codex SDK or Codex MCP orchestration research spike.
4. Run read-only discovery/challenge trials first.
5. Record thread IDs, prompts, outputs, sandbox modes, decisions, and closeout evidence.
6. Only after evidence exists, consider a controlled workspace-write execution trial under an explicit mission envelope.

## Required Boundaries
Any SDK/MCP orchestration work must preserve:
- no runtime authority,
- no default execution,
- no production actions,
- no hidden replacement for V3 governance,
- no credential or deployment authority without separate approval,
- no use of Codex worker output as approval authority,
- no treatment of orchestration traces as a substitute for mission records.

Codex is a worker. Factory remains the authority layer.

## Evidence To Collect
Before SDK/MCP orchestration becomes recommended V3 tooling, collect:
- setup and dependency friction,
- sandbox behavior evidence,
- thread resume behavior,
- trace/evidence completeness,
- human interrupt behavior,
- failure and halt behavior,
- comparison with manual Codex app execution,
- false confidence or runaway orchestration risks,
- whether the workflow improves mission replayability.

## Current Evidence Gate

Same Second `V3-SS-EPIC-001` now supplies the required manual attended
serial-epic evidence: three bounded children completed across a fresh
non-forked task boundary, with child and parent verification and authored
revision 18/event 19 closeout. See
`ATTENDED_SERIAL_EPIC_PILOT_001_REVIEW_20260716.md`.

`CODEX_TASK_SURFACE_DISCOVERY_FORMATION_20260716.md` and its challenge defined
approved no-probe mission `V3-CODEX-DISC-001`. Its exact evidence now lives at
`task_surface_discovery/V3-CODEX-DISC-001/` and records
`DEEPLINK_ASSIST_ONLY`: native desktop task controls were not exposed in this
task, the local CLI runtime is missing, and deep links can carry an absolute
workspace and prefilled prompt but still require human Send and expose no task
ID or status.

`V3-CODEX-DL-001` now implements one deterministic stdlib link builder with
human Send retained and `transport_proof: false`; see
`CODEX_DEEPLINK_ASSIST.md` and
`deeplink_assist/V3-CODEX-DL-001/CLOSEOUT.md`. It has no link-opening or
task-creation path. Separately approved `V3-CODEX-DL-TRIAL-001` completed once
at `PASS_WITH_LIMITATIONS` without retry; retained evidence under
`deeplink_assist/V3-CODEX-DL-TRIAL-001/` shows desktop acceptance of the
intended project and visible prompt plus the exact response, while task identity,
status, byte-level transport, full-path UI proof, and hidden activity remain
unproved. `CODEX_DEEPLINK_ATTENDED_ADOPTION_FORMATION_20260716.md` and its
challenge defined `V3-CODEX-DL-ADOPT-001`, which is now sponsor-approved as an
optional attended aid. The decision at
`deeplink_assist/V3-CODEX-DL-ADOPT-001/DECISION.md` keeps exact mission
authority, per-mission naming, human Send, deterministic evidence, and manual
fallback controlling. Adoption alone permits no live use. App-server, SDK,
exec, and MCP remain later lanes requiring their own runtime, dependency,
credential, process, probe, and authority decisions.

Same Second `V3-SS-PHASE0-GATE-001` subsequently completed as
`PASS_BOUNDED_DECISION_CLOSURE` while the activation result remained
`BLOCKED_MISSING_DECISIONS`. That product decision does not grant worker
transport authority.

`CODEX_SDK_READ_ONLY_TRIAL_FORMATION_20260720.md` and its challenge now define
non-executing SDK-only candidate `V3-CODEX-SDK-RO-001`. The trial shape is one
attended synthetic read-only thread start and one same-thread resume, with an
isolated controller, fixture-only target, event/snapshot evidence, human
checkpoints, and no retry or adapter behavior. Challenge verdict is
`MORE DISCOVERY`: this harness lacks Node/npm, `/usr/bin/python3` is below the
documented Python SDK minimum, no healthy compatible alternative is pinned, and
SDK package integrity plus authentication remain unapproved. The next gate is a
file-only prerequisite pack and repaired challenge. No runtime, SDK, process,
thread, external call, or worker action has occurred.

## Boundary
This document does not change the current approved optional operational profile:

```text
V3-OP-001 Bounded Code Change
```

Codex SDK, Codex MCP, Agents SDK orchestration, multi-agent workflow execution, and Harmony-driven worker orchestration remain research direction until separately planned, trialed, evidenced, and approved.
