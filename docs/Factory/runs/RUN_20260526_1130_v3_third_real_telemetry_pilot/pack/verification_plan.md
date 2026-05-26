# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for third telemetry pilot.

## Checks
- V2: `./scripts/factoryctl stage-lint --run RUN_20260526_1130_v3_third_real_telemetry_pilot --stage <STAGE>`
- V2: `./scripts/factoryctl pack-lint --run RUN_20260526_1130_v3_third_real_telemetry_pilot`
- JSON: `python3 -m json.tool docs/Factory/v3/mission_records/MR_20260526_006_third_real_telemetry_pilot.json`
- JSON: `python3 -m json.tool docs/Factory/v3/telemetry/pilots/PILOT_20260526_003_evidence_review_prep/REPLAY_REPORT.json`
- V3: `python3 scripts/factory_v3_telemetry_replay_lint.py --target docs/Factory/v3/telemetry/pilots/PILOT_20260526_003_evidence_review_prep/V3_TELEMETRY.jsonl --json`
- V3: `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- V3: `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`
- V3: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- V3: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- V3: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- Python: `python3 -m py_compile scripts/factory_v3_telemetry_replay_lint.py scripts/factory_v3_advisory_lint.py scripts/factory_v3_mission_record_lint.py scripts/factory_v3_operational_readiness_eval.py`
- Git: `git diff --check`

## Exit Criteria
All required checks exit 0. Expected invalid-fixture findings are acceptable only when the deterministic `--expect` check passes.
