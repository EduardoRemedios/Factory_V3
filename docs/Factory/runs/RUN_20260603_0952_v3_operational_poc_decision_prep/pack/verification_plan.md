# Verification Plan: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface verification.
- v0.2 (2026-06-03): Added V3-only POC and Garmin research verification.
- v0.1 (2026-06-03): Initial Stage F verification plan.

## Planning-Pack Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl stage-lint --run RUN_20260603_0952_v3_operational_poc_decision_prep --stage <STAGE>` for stages A, B, C, D, E, F, G, H, I, J, and I2.
- `./scripts/factoryctl pack-lint --run RUN_20260603_0952_v3_operational_poc_decision_prep`
- `git diff --check`

## V3 Advisory Verification
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`

## Manual Review Checks
- Confirm the future POC build is explicitly V3-only.
- Confirm V2 is allowed only for current repository planning and is barred from POC design/build/test/deploy/governance.
- Confirm Garmin work is a research spike only, with no credentials, API calls, app code, or integration implementation authorized.
- Confirm Hermes work is a research spike only, with no install, configuration, credentials, execution, memory adoption, MCP wiring, scheduling, subagent use, or sandbox/backend use authorized.
- Confirm internal/private deployment does not authorize public deployment or production infrastructure.
- Confirm synthetic data is allowed but cannot close Garmin-backed ingestion evidence by itself.
- Confirm Hermes-assisted evidence, if later approved, is labeled separately and cannot be used to hide a missing V3 standalone capability.
- Confirm the pack does not claim default V3 production readiness or V2 deprecation.

## Future POC Verification Placeholder
Future POC verification must be defined in a separate V3-only POC plan. That plan must include evidence that:
- V3 alone drove the app design, build, test, and deployment workflow.
- No V2 command, pack, stage, lint, recovery, or validation step was used during POC execution.
- Garmin integration evidence, if included, is labeled by source path: official API, open-source client, manual export/import, or synthetic-only.
- Hermes evidence, if included after separate approval, is labeled by surface and authority: CLI/TUI, desktop, gateway, memory, skills, MCP, scheduling, subagent, browser/search, or sandbox/backend.
