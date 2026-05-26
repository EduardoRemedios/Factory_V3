# Verification Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Verification plan for Phase 3 telemetry/replay planning.

## Verification Commands
- `./scripts/factoryctl stage-lint --run RUN_20260526_0702_v3_phase3_telemetry_replay_plan --stage <STAGE>`
- `./scripts/factoryctl pack-lint --run RUN_20260526_0702_v3_phase3_telemetry_replay_plan`
- `bash scripts/knowledge_lint.sh`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`
- `python3 -m py_compile scripts/factory_v3_advisory_lint.py scripts/factory_v3_mission_record_lint.py scripts/factory_v3_operational_readiness_eval.py`
- `git diff --check`

## Verification Tiers
- V0: artifact presence and readable documentation.
- V1: V2 and V3 advisory static checks.

## Non-Runnable Checks
- Confirm no telemetry implementation files were added.
- Confirm no required-gate or CI wiring changed.
- Confirm the plan defines event fields, excluded data, fixture shape, replay checks, and data-minimization rules.
