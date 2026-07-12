# Verification Plan - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F verification design.

## Planning-Pack Checks
| ID | Tier | Check | Expected |
| --- | --- | --- | --- |
| VP-001 | V0 | Field-family decision table covers all six families | Each is ADOPT, REVISE, or DEFER |
| VP-002 | V1 | Search pack for implementation/promotion implications | None |
| VP-003 | V1 | Compare proposal to representative current routes | Completed, halted, stale, blocked, and pre-envelope remain valid by omission |
| VP-004 | V1 | Stage/pack lint | PASS |

## Later Implementation Checks
| ID | Tier | Constraint | Check | Expected |
| --- | --- | --- | --- | --- |
| VI-001 | V1 | R-001 | Parse updated template and all JSON fixtures | PASS |
| VI-002 | V3 | R-001 | Run current deterministic fixture corpus before and after | Existing per-record outputs unchanged |
| VI-003 | V2 | R-007 | Valid original-plus-replay fixture | Both observations retained; no supersession |
| VI-004 | V2 | R-004 | Same-actor verifier fixture | `deterministic_separation_only`, never independent |
| VI-005 | V2 | R-005 | Hash-match/visual-fail fixture | Contradiction/finding is emitted without changing hash verdict |
| VI-006 | V2 | R-006 | Change-range boundary claim fixture | Scope and limit retained; no global inference |
| VI-007 | V2 | R-008 | Completed record with placeholder commit | Advisory finalization finding |
| VI-008 | V2 | R-008 | `same_commit`, literal, `not_recorded`, unavailable cases | Documented valid/limited outcomes |
| VI-009 | V1 | R-003 | Validator output shape | `blocking_effect: none`; no gate wiring |
| VI-010 | V3 | all | Mission-record fixtures with deterministic expected output | Exact match |
| VI-011 | V3 | all | Knowledge lint, V3 advisory lint, operational readiness, diff check | PASS or unchanged known non-blocking findings |

## Interpretation
The later implementation should fail only for internally contradictory fields that are supplied. Absence of optional additions is not an error or warning.

## Manifest Decision
No `verification_manifest.yaml` is needed for this `PLANNING_ONLY` pack. The later execution-enabled run should include one.
