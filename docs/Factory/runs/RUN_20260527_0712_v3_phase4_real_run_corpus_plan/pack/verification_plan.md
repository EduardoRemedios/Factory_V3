# Verification Plan: Phase 4 Real-run Corpus Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage F verification plan.

## Current Planning Checks
- V1-C1: `bash scripts/knowledge_lint.sh`; expect PASS.
- V1-C2: `./scripts/factoryctl context-index`; expect rebuild.
- V1-C3: `./scripts/factoryctl stage-lint --run RUN_20260527_0712_v3_phase4_real_run_corpus_plan --stage A` through `I2`; expect PASS.
- V1-C4: `./scripts/factoryctl pack-lint --run RUN_20260527_0712_v3_phase4_real_run_corpus_plan`; expect PASS.
- V1-C5: `git diff --check`; expect PASS.

## Future Implementation Checks
- V1-F1: `bash scripts/knowledge_lint.sh`; expect PASS.
- V1-F2: `./scripts/factoryctl context-index`; expect rebuild.
- V1-F3: `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; expect advisory PASS.
- V1-F4: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; expect advisory PASS.
- V1-F5: `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`; expect advisory PASS.
- V1-F6: `git diff --check`; expect PASS.

## Manual Reviews
- Confirm future artifacts do not authorize live mission execution.
- Confirm no router, enforcement, telemetry completeness, required gate, runtime authority, proof, lease, default-mode, promotion, or V2-removal language.
- Confirm Phase 3 missing natural halted, fallback, or clarification-heavy case remains explicit.
