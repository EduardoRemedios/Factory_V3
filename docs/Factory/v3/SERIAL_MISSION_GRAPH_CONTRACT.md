# Factory V3 Serial Mission-Graph Contract

## Version
v0.1

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

## Next Evidence Gate
Use the contract first in deterministic fixtures, then in a separately approved
attended serial-epic pilot. Worker dispatch and a persistent state kernel remain
separate decisions.
