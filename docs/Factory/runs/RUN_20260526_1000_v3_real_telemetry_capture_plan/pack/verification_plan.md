# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for real telemetry capture planning.

## Commands
- `./scripts/factoryctl stage-lint --run RUN_20260526_1000_v3_real_telemetry_capture_plan --stage <STAGE>`
- `./scripts/factoryctl pack-lint --run RUN_20260526_1000_v3_real_telemetry_capture_plan`
- `bash scripts/knowledge_lint.sh`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`

## Verification Tiers
- V0: planning artifact presence.
- V1: advisory docs and deterministic replay checks.

## Exit Criteria
PASS when required checks pass and no real telemetry files are added.
