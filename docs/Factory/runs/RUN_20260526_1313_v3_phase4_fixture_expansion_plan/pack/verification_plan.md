# Verification Plan: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage F verification plan.

## Current Planning Checks
- V1-C1: `bash scripts/knowledge_lint.sh`; expect PASS.
- V1-C2: `./scripts/factoryctl context-index`; expect rebuild.
- V1-C3: `./scripts/factoryctl stage-lint --run RUN_20260526_1313_v3_phase4_fixture_expansion_plan --stage A` through `I2`; expect PASS.
- V1-C4: `./scripts/factoryctl pack-lint --run RUN_20260526_1313_v3_phase4_fixture_expansion_plan`; expect PASS.
- V1-C5: `git diff --check`; expect PASS.

## Future Implementation Checks
- V2-F1: `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`; expect PASS.
- V1-F2: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; expect advisory PASS.
- V1-F3: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; expect advisory PASS.
- V1-F4: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; expect advisory PASS.
- V1-F5: `git diff --check`; expect PASS.

## Manual Reviews
- Confirm only named files are touched.
- Confirm no router, enforcement, required gate, telemetry completeness, runtime authority, proof, lease, default-mode, V3 promotion, or V2-removal language appears.
- Confirm synthetic status and Phase 3 evidence gap remain explicit.
