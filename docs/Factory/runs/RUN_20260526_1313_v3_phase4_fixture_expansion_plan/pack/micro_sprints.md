# Micro-sprints: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage G micro-sprints.

## MS-01 Evaluator Trigger Checks
- Objective: Add direct `V3-P4-*` trigger checks to `scripts/factory_v3_operational_readiness_eval.py`.
- Inputs: current `CHECKS` pattern.
- Outputs: eight new check tuples.
- Entry criteria: human approval after this pack.
- Exit criteria: no parser, scoring, routing, or blocking behavior added.
- Stop or go gate: stop if code grows beyond direct trigger checks.

## MS-02 Synthetic Fixture Cases
- Objective: Add eight synthetic fixture case directories and `input.md` files.
- Inputs: Phase 4 plan fixture family table.
- Outputs: `V3-P4-CAP-001`, `REL-001`, `SCOPE-001`, `VERIFY-001`, `RECOVER-001`, `EVID-001`, `FPN-001`, and `THRESH-001`.
- Entry criteria: MS-01 complete.
- Exit criteria: each fixture has clear trigger text and synthetic labeling.
- Stop or go gate: stop if fixture text claims real negative-case evidence.

## MS-03 Expected Output Update
- Objective: Update `expected.json` for deterministic fixture output.
- Inputs: evaluator output from MS-01 and fixtures from MS-02.
- Outputs: updated expected JSON.
- Entry criteria: MS-01 and MS-02 complete.
- Exit criteria: `--expect` fixture command passes.
- Stop or go gate: stop if `blocking_effect` changes from `none`.

## MS-04 Verification And Closeout
- Objective: Verify scoped implementation.
- Inputs: changed files.
- Outputs: command results and scope review.
- Entry criteria: MS-03 complete.
- Exit criteria: all future implementation checks pass.
- Stop or go gate: stop on router, enforcement, gate wiring, telemetry completeness, runtime authority, proof, lease, default-mode, promotion, or V2-removal drift.
