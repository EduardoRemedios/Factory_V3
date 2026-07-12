# Raw Brief - Advisory Mission-Record Shape Implementation Pack

## Request
Prepare the exact-path implementation pack for the human-accepted `ADOPT_NARROW_SET` decision from `RUN_20260712_0952_v3_advisory_record_shape_decision`.

## Execution Posture
- Execution Mode: `EXECUTION_ENABLED`
- Execution Authorization: user accepted `ADOPT_NARROW_SET` in the active Codex thread on 2026-07-12.
- Post-pack requirement: implementation must not start until explicit human Go after I2 PASS.
- Downstream Fan-Out: `NOT_APPROVED`

## Objective
Plan a fixture-first advisory implementation of four optional evidence-provenance structures plus final-commit consistency semantics, preserving current records, non-blocking behavior, and authored-artifact authority.

## Locked Decisions
- Add optional verification observations, verifier provenance, visual evidence, and boundary claims.
- Keep `mission.commit_after`; add no duplicate final-commit field.
- Defer base-record endurance/exposure fields.
- Missing optional additions emit no finding.
- Existing records and schema routes remain valid.
- Replay never supersedes original-run provenance.

## Exact Product Scope
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

## Hard Boundaries
- No historical mission-record or POC repair/backfill.
- No required fields, migration, JSON Schema framework, generic plugin/extension layer, telemetry, runtime authority, routing, CI, required gates, profile promotion, or V2 removal.
- No raw logs, transcripts, chain of thought, secrets, direct personal identifiers, or vendor-private session IDs.
- No endurance field or duration/workload floor.
- No commit or push unless separately requested after implementation.

## Required Verification
- Capture baseline deterministic outputs before edits.
- JSON-parse template and every fixture.
- Existing valid fixtures remain accepted when additions are absent.
- Same-actor verifier cannot claim independent.
- Replay observation cannot supersede original.
- Positive boundary claim requires proof scope, evidence, and limit.
- Completed record placeholder commit produces an advisory finding.
- Hash and visual verdicts remain separate, including hash-match/visual-fail valid evidence.
- Expected `all.json` and `invalid.json` match exactly.
- Knowledge lint, V3 advisory/readiness checks, Python compile, context index, stage/pack lint, and diff check pass.

## Human Decision
This run may prepare an execution-ready pack. Actual implementation requires a new explicit Go after the pack is complete.
