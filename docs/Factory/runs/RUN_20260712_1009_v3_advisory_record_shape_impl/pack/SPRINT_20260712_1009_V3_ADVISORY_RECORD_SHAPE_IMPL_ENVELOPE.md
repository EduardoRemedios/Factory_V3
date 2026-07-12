# Sprint Envelope - Advisory Record Shape Implementation

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Stage I hardening binds deterministic temporary MR083 coverage and old-subset comparison before expected-output regeneration.
- v0.1 (2026-07-12): Stage H execution envelope.

## Identity
- Sprint ID: `SPRINT_20260712_1009_V3_ADVISORY_RECORD_SHAPE_IMPL`
- Run ID: `RUN_20260712_1009_v3_advisory_record_shape_impl`
- Execution mode: `EXECUTION_ENABLED`
- Status: awaiting I2 PASS and explicit post-pack human Go

## Objective
Implement the accepted narrow optional evidence-integrity shape in the Factory V3 shadow mission record with deterministic fixtures and non-blocking validator support.

## Authorized Product Files
1. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
2. `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
3. `scripts/factory_v3_mission_record_lint.py`
4. `tests/fixtures/factory_v3_mission_record/README.md`
5. `tests/fixtures/factory_v3_mission_record/fixture_evidence_integrity_optional.json`
6. `tests/fixtures/factory_v3_mission_record/invalid/evidence_observation_supersedes_original.json`
7. `tests/fixtures/factory_v3_mission_record/invalid/verifier_same_actor_claims_independent.json`
8. `tests/fixtures/factory_v3_mission_record/invalid/boundary_proved_without_limit.json`
9. `tests/fixtures/factory_v3_mission_record/invalid/completed_with_placeholder_commit.json`
10. `tests/fixtures/factory_v3_mission_record/expected/all.json`
11. `tests/fixtures/factory_v3_mission_record/expected/invalid.json`
12. `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
13. `docs/Factory/v3/README.md`
14. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
15. `docs/Factory/v3/ANCHOR_REGISTRY.md`
16. `docs/PROJECT_STATE.md`
17. `docs/ROADMAP.md`
18. `docs/CHANGELOG.md`

Run-root closeout files and deterministic temporary files under `/tmp` are authorized and excluded from the product cap.

## File-Touch Budget
| Micro-sprint | Maximum product files |
| --- | ---: |
| MS-00 | 0 |
| MS-01 | 2 |
| MS-02 | 6 |
| MS-03 | 3 |
| MS-04 | 7 |
| MS-05 | 0 additional |
| Total unique | 18 |

## Locked Behavior
- Optional verification observations preserve original/replay/audit provenance and cannot supersede original evidence.
- Optional verifier provenance distinguishes actor/session relationship and independence status.
- Optional visual evidence separates hash identity from visual verdict per artifact.
- Optional boundary claims bind status to proof scope, evidence refs, and limit.
- Existing `mission.commit_after` remains the only final-commit field.
- MR081-MR085 are advisory findings on supplied contradictions; absent optional fields are a no-op.
- Existing POC schema routes and historical records are untouched.
- Endurance fields remain deferred.

## Allowed Implementation
- Direct edits to exact paths only.
- Direct helper functions called from the Factory V3 shadow-record lint path.
- Five named repository fixtures.
- Deterministic `/tmp` malformed-visual derivative for MR083 verification only.
- Expected-output regeneration only after old representative fixtures pass unchanged.

## Forbidden Implementation
- Dependency, schema engine, registry, generic recursive validator, migration, historical backfill, POC repair, raw logs/transcripts, secrets/PII, telemetry, runtime authority, routing, CI/factoryctl/required-gate wiring, profile promotion, V2 removal, commit, or push.

## Verification Contract
Run every manifest and verification-plan check. Before regenerating expected files:
1. save baseline full/invalid reports in `/tmp`;
2. run dedicated expected checks for completed, blocked, halted-verification, and stale-reentry fixtures;
3. after validator edits, rerun those dedicated checks unchanged;
4. create a deterministic `/tmp` malformed visual fixture and verify MR083;
5. only then regenerate `all.json` and `invalid.json` for the five named fixture additions.

`visual_verdict: fail` remains valid evidence. MR083 covers malformed shape/vocabulary only.

## SIMPLE-CODE-GATE
Prefer small explicit helpers near `_check_execution`/`_check_reviews`; reuse existing finding construction and type checks. Do not add abstractions for future schema variants.

## Halt Conditions
- Baseline or old representative output mismatch.
- Need for a sixth repository fixture or nineteenth product file.
- Missing optional object emits a finding.
- `not_recorded` commit becomes invalid.
- Same-worker verification can be marked independent.
- Visual FAIL becomes structurally invalid.
- Boundary `PROVED` can omit scope/evidence/limit.
- Any authority, enforcement, routing, runtime, endurance-floor, migration, or dependency implication.

## Completion Conditions
- AC1-AC14 pass.
- Exactly 18 authorized product files or fewer changed.
- MR081-MR085 and rich valid fixture are deterministic.
- Existing representative outputs remain exact.
- All repository and Factory gates pass.
- Closeout records authoring-friction and endurance-field deferrals.
