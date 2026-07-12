# Execution Prompt - Advisory Record Shape Implementation

## Authorization
- Human Go received: 2026-07-12.
- Run: `RUN_20260712_1009_v3_advisory_record_shape_impl`.
- Mode: `EXECUTION_ENABLED`.
- Approved pack: `pack/` under this run root.
- Closeout workflow: `factory-execution-closeout`.

## Objective
Implement four optional evidence-integrity structures in the Factory V3 shadow mission record, add MR081-MR085 advisory checks and deterministic fixture coverage, and reconcile seven active canon pointers.

## Required Sequence
1. Capture baseline full, invalid, completed, blocked, halted-verification, and stale-reentry outputs before edits.
2. Update only the two design/template files.
3. Add the fixture README update and five named fixtures.
4. Re-run representative old fixtures before editing expected outputs.
5. Add direct validator helpers and deterministic temporary MR083 coverage.
6. Regenerate only `expected/all.json` and `expected/invalid.json` after old behavior remains exact.
7. Reconcile seven named canon/status files.
8. Run every verification-plan and manifest check and close with `factory-execution-closeout`.

## Boundaries
- Touch no more than the 18 exact product paths in the envelope.
- Missing optional fields must remain a no-op.
- Do not modify historical records or the POC.
- Do not add endurance fields, dependencies, schema engines, generic registries, runtime authority, telemetry, routing, CI/required gates, promotion, or V2 removal.
- Do not commit or push without separate authorization.

## Halt
Halt on old-fixture mismatch, unauthorized path, sixth repository fixture, nineteenth product file, optional completeness finding, `not_recorded` regression, visual FAIL rejection, or any enforcement/authority implication.
