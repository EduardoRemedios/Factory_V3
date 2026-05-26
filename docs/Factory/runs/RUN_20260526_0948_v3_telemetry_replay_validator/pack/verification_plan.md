# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for telemetry replay validator implementation.

## Commands
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `python3 -m json.tool tests/fixtures/factory_v3_telemetry_replay/expected/all.json`
- `python3 -m py_compile scripts/factory_v3_telemetry_replay_lint.py`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl stage-lint --run RUN_20260526_0948_v3_telemetry_replay_validator --stage <STAGE>`
- `./scripts/factoryctl pack-lint --run RUN_20260526_0948_v3_telemetry_replay_validator`
- `git diff --check`

## Verification Tiers
- V1: static compile and advisory docs checks.
- V2: deterministic replay fixture checks.

## Exit Criteria
PASS when all required commands pass.
