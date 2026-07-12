# Verification Plan - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F verification plan.

| ID | Tier | Constraint | Check | Expected |
| --- | --- | --- | --- | --- |
| V3-001 | V3 | R-001 | Run full mission-record corpus with current `expected/all.json` before edits | PASS baseline |
| V3-002 | V3 | R-001 | Re-run existing representative completed/blocked/halted/stale fixtures against their dedicated expected files | Exact PASS before and after |
| V1-003 | V1 | AC1/AC2 | Parse template and all fixtures | Valid JSON |
| V1-004 | V1 | R-003 | Static review for source-of-truth and reference-only language | No embedded logs/state authority |
| V2-005 | V2 | R-004 | `evidence_observation_supersedes_original.json` | MR081 |
| V2-006 | V2 | R-005 | `verifier_same_actor_claims_independent.json` | MR082 |
| V2-007 | V2 | R-006 | rich valid fixture with hash match and visual fail | No MR083; visual fail preserved |
| V2-008 | V2 | R-007 | `boundary_proved_without_limit.json` | MR084 |
| V2-009 | V2 | R-008 | `completed_with_placeholder_commit.json` | MR085; old `not_recorded` valid |
| V1-010 | V1 | R-009 | Count changed authorized product paths | At most 18; no unauthorized path |
| V1-011 | V1 | R-010 | Search new fixtures for secrets/direct identifiers | None |
| V3-012 | V3 | R-002 | Full `all.json` and `invalid.json` deterministic checks | Exact match; blocking none |
| V1-013 | V1 | code | Python compile validator | PASS |
| V1-014 | V1 | canon | V3 advisory lint and readiness evals | No new authority finding |
| V3-015 | V3 | repo | knowledge lint, stage/pack lint, context index, diff check | PASS |

## Baseline Preservation
Do not regenerate expected output until V3-002 passes after code changes. Aggregate output may add only the five named fixture paths and corresponding MR081-MR085 findings.

## Failure Policy
Halt on old-fixture mismatch, optional-field completeness finding, unauthorized path, dependency, enforcement implication, or required-gate wiring.
