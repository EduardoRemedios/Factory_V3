# Raw Brief - Mission-Control Advisory Record Shape Decision

## Request
Prepare the next Factory V3 planning slice recommended after the Mission 026 claim-to-proof and FP/FN adjudication.

## Execution Posture
- Execution Mode: `PLANNING_ONLY`
- Execution Authorization: none; planning artifacts only.
- Downstream Fan-Out: `NOT_APPROVED`

## Goal
Produce an evidence-backed, backward-compatible advisory mission-record shape proposal and an explicit `ADOPT`, `REVISE`, or `DEFER` recommendation. The proposal should determine which Mission 026 audit findings merit optional record fields before any template, validator, fixture, or historical-record implementation is authorized.

## Candidate Field Families
1. final-commit consistency;
2. original-run versus replay evidence provenance;
3. verifier actor/session provenance and independence status;
4. per-artifact browser hash plus visual verdict;
5. bounded absence-claim scope;
6. mission outcome, observed exposure, and endurance coverage as separate values.

## Evidence Base
- `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
- `docs/Factory/v3/templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`
- existing completed, halted, stale-reentry, blocked, and pre-envelope mission-record fixtures.

## Required Planning Outputs
- field-by-field candidate proposal with purpose, optionality, allowed values, source-of-truth relationship, and migration behavior;
- compatibility analysis against existing record routes and fixtures;
- duplication/second-source-of-truth analysis;
- validator and fixture implications, explicitly deferred to a later separately approved run;
- adoption criteria and a clear `ADOPT`, `REVISE`, or `DEFER` recommendation;
- bounded implementation envelope for a possible later fixture-first advisory change.

## Hard Boundaries
- No edits to mission-record or mission-control templates, validators, fixtures, historical POC records, or active product canon in this run.
- No POC repair or backfill.
- No required gate, CI wiring, runtime authority, telemetry enforcement, governance routing, scheduled execution, profile promotion, or V2 removal.
- Existing mission records must remain valid under any recommended future shape.
- Authored mission envelopes, checkpoints, state, verification output, and closeouts remain source evidence; the advisory record must not replace them.
- No duration, call, waypoint, test, file, or scope floors.

## Acceptance Criteria
1. Each candidate field family is adopted, revised, or deferred with evidence.
2. The proposal is additive and backward-compatible.
3. Missing optional fields never invalidate existing records.
4. Mission outcome and endurance coverage are separate.
5. Same-worker deterministic verification is not mislabeled independent.
6. Replay evidence cannot overwrite original-run provenance.
7. Screenshot hash identity and visual correctness are separate.
8. Absence claims state their bounded proof scope.
9. Final-commit consistency handles `same_commit`, literal hashes, placeholders, and unavailable commits.
10. A later implementation envelope names exact likely files and deterministic checks without authorizing execution.

## Human Decision
The user approved this planning slice in the active Codex thread on 2026-07-12 by saying “Ok do it.” This is approval to prepare the planning pack only.
