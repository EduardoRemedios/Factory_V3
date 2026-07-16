# Factory V3 Serial Mission-Graph Contract

## Version
v0.13

## Change Log
- v0.13 (2026-07-16): Recorded sponsor-approved `V3-CODEX-DL-ADOPT-001` as an optional attended aid that remains subordinate to exact graph/mission authority and cannot activate a child or start a worker by itself. The next evidence target is one natural eligible use inside a separately approved useful mission; no worker adapter or runtime authority is added.
- v0.12 (2026-07-16): Added challenged non-executing optional adoption candidate `V3-CODEX-DL-ADOPT-001` at `PASS`. Its contract requires graph/mission authority before any attended handoff and adds no child activation, worker dispatch, automatic task control, or runtime authority. The next gate is a separate sponsor adoption decision.
- v0.11 (2026-07-16): Recorded attended `V3-CODEX-DL-TRIAL-001` at `PASS_WITH_LIMITATIONS` without retry. It supplies bounded evidence for a human-reviewed deep-link handoff but adds no graph authority, worker adapter, automatic task control, dispatch, or runtime authority. The next separate gate is optional attended-aid adoption.
- v0.10 (2026-07-16): Added challenged attended `V3-CODEX-DL-TRIAL-001` as the next separate decision. Formation adds no workspace, link, task, worker adapter, or execution authority.
- v0.9 (2026-07-16): Recorded implemented code-only `V3-CODEX-DL-001`; the next gate is non-executing attended synthetic live-link trial formation. No link, task, worker adapter, or execution authority is added.
- v0.8 (2026-07-16): Added challenged non-executing `V3-CODEX-DL-001` as the next separate code-only decision. It retains human Send and adds no task, worker adapter, or execution authority.
- v0.7 (2026-07-16): Recorded completed no-probe `V3-CODEX-DISC-001` at `DEEPLINK_ASSIST_ONLY`. The next gate is separate non-executing deep-link helper formation; no task, worker adapter, or execution authority is added.
- v0.6 (2026-07-16): Recorded Same Second `V3-SS-EPIC-001` as the first bounded passed attended three-child product pilot. The next gate is the separate challenged `V3-CODEX-DISC-001` read-only task-surface decision; no worker adapter or execution authority is added.
- v0.5 (2026-07-14): Recorded Trial 003's successful three-child serial traversal after a 23/23 external re-entry comparison and its separate R1 product repair. The next gate is non-executing attended serial-epic pilot formation/challenge; no worker adapter or execution authority is added.
- v0.4 (2026-07-13): Recorded Trial 002's fail-closed pre-brief exposure of its co-located key and prior-trial content. The next evidence gate is non-executing Trial 003 commitment-and-reveal formation; no worker adapter or execution authority is added.
- v0.3 (2026-07-13): Recorded that live Trial 001 failed closed at 19/23 before child C02 started. A repaired Trial 002 is the next separate evidence gate; the graph contract gains no dispatch or runtime authority.
- v0.2 (2026-07-12): Linked the separately approved deterministic authored-state kernel implementation. The kernel remains advisory and adds no worker dispatch, runtime authority, concurrency, or required gate.

## Status
Research-only and non-enforcing.

This contract does not approve worker dispatch, concurrent execution, unattended
operation, runtime authority, required gates, governance routing, a new V3
profile, or `V3-OP-003` promotion.

## Purpose
Define the minimum deterministic contract for governing an epic as a parent
mission containing multiple bounded feature missions. The first design is
serial: no more than one child may be active, and each child must pass its own
authority, dependency, verification, evidence, and continuation gates.

## Core Rules
1. The parent mission defines an authority ceiling, not blanket child authority.
2. Every child has a bounded objective, dependencies, authority, verification,
   evidence status, and continuation gate.
3. Child dependencies must exist and form an acyclic graph.
4. A child cannot become eligible or active until every dependency is complete.
5. No more than one child may be active, awaiting verification, or authorized
   to start.
6. Child paths and commands must remain within the parent authority ceiling.
7. A completed child requires passing verification and `PROVED` evidence.
8. Parent completion requires every required child to be complete plus separate
   parent-level verification.
9. Authored mission state remains the source of truth. Eligibility cursors and
   next-child recommendations are derived and grant no authority.
10. Session memory is never sufficient for continuation or re-entry.

## Parent And Child Boundary
Factory V3 owns the parent objective, authority ceiling, dependency graph,
feature admission, continuation gates, checkpoint policy, safe hold, and
parent closeout. Workers own tactical implementation inside one active child
envelope. A worker may propose the next child but cannot activate it.

## State Model
The contract describes authored state and transition invariants; it is not a
runtime coordinator. A later separately approved state-kernel spike may derive
eligible children from this contract and an authored mission-state file.

The first transition vocabulary is:

```text
pending -> eligible -> active -> verification_pending -> completed
                     |          |                       |
                     +----------+-> blocked/safe_hold/halted
```

`skipped` is allowed only as an authored decision. A required dependency is
satisfied only by `completed`, not by `skipped`.

## Advisory Implementation
- Template: `templates/V3_SERIAL_MISSION_GRAPH_TEMPLATE.json`
- Validator: `scripts/factory_v3_serial_mission_graph_lint.py`
- Fixtures: `tests/fixtures/factory_v3_serial_mission_graph/`

Run:

```bash
python3 scripts/factory_v3_serial_mission_graph_lint.py \
  --target tests/fixtures/factory_v3_serial_mission_graph \
  --expect tests/fixtures/factory_v3_serial_mission_graph/expected/all.json \
  --json
```

The validator always reports `blocking_effect: none`. It is not wired into
`factoryctl`, mission lint, pack lint, stage lint, knowledge lint, CI, or any
required gate.

## Deterministic State Kernel
The separately approved research implementation now exists at
`SERIAL_MISSION_STATE_KERNEL.md`, with a stdlib-only CLI, authored-state and
event templates, and deterministic fixtures/tests. It calculates and persists
admitted transitions without executing commands or dispatching workers.

## Next Evidence Gate
The three-sample evidence-integrity review is complete at
`KEEP_OPTIONAL_NO_SCHEMA_CHANGE`. Live Trial 001 failed closed at 19/23, and
Trial 002 failed closed before a brief after reported exposure of its co-located
key. Trial 003 then passed 23/23 under external commitment-and-reveal and
traversed its three-child graph to parent closeout; a separately authorized R1
repaired a product ordering defect found after closeout. The next separate
evidence gate was then satisfied by attended Same Second `V3-SS-EPIC-001`, whose
three children and separate parent verification closed at revision 18/event 19. The
approved no-probe `V3-CODEX-DISC-001` then returned
`DEEPLINK_ASSIST_ONLY`: documented deep links can prefill workspace/prompt but
still require human Send. The next gate is separate non-executing helper
formation. Separately approved `V3-CODEX-DL-001` then implemented a
deterministic text-only helper with human Send retained and no transport proof.
The next gate was non-executing attended synthetic live-link trial formation.
Separately approved `V3-CODEX-DL-TRIAL-001` then completed once at
`PASS_WITH_LIMITATIONS` without retry. It supports a bounded human-reviewed
handoff observation only; it does not prove byte-level transport, task status,
hidden-tool absence, automatic task creation, or worker dispatch. The next
separate gate was challenged candidate `V3-CODEX-DL-ADOPT-001`, which is now
sponsor-approved as an optional attended aid. It remains subordinate to exact
authored graph/mission authority and cannot activate a child or start a worker
by itself. The next evidence target is one natural eligible use inside a
separately approved useful mission. Worker adapters and runtime authority remain
outside this contract.
