# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for Phase 3 telemetry evidence review.

## Checks
- V2: `./scripts/factoryctl stage-lint --run RUN_20260526_1200_v3_phase3_telemetry_evidence_review --stage <STAGE>`
- V2: `./scripts/factoryctl pack-lint --run RUN_20260526_1200_v3_phase3_telemetry_evidence_review`
- V3: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- V3: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- V3: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- V3: `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`
- V3: `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- Python: `python3 -m py_compile scripts/factory_v3_telemetry_replay_lint.py scripts/factory_v3_advisory_lint.py scripts/factory_v3_mission_record_lint.py scripts/factory_v3_operational_readiness_eval.py`
- Git: `git diff --check`

## Exit Criteria
All checks exit 0. Expected invalid-fixture findings are acceptable only when the deterministic `--expect` check passes.
