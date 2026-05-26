# Verification Plan: Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage F verification plan.

## Required Checks
- V1-C1: Run `bash scripts/knowledge_lint.sh`; expect PASS.
- V1-C2: Run `./scripts/factoryctl context-index`; expect context index rebuild.
- V1-C3: Run `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260526_1304_v3_phase4_eval_expansion_plan --focus "Factory V3 Phase 4 eval expansion and harness capability profiling planning" --required-ref docs/Factory/v3/PHASE3_TELEMETRY_EVIDENCE_REVIEW.md --required-ref docs/Factory/v3/ROADMAP_TO_FULL_VISION.md --required-ref docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md --output docs/Factory/runs/RUN_20260526_1304_v3_phase4_eval_expansion_plan/CONTEXT_RECALL_REPORT.md`; expect sufficient coverage.
- V1-C4: Run `./scripts/factoryctl stage-lint --run RUN_20260526_1304_v3_phase4_eval_expansion_plan --stage A` through `I2`; expect PASS for every stage.
- V1-C5: Run `./scripts/factoryctl pack-lint --run RUN_20260526_1304_v3_phase4_eval_expansion_plan`; expect PASS.
- V1-C6: Run `git diff --check`; expect no whitespace errors.

## Artifact Reviews
- V0-A1: Confirm this run does not create `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`.
- V0-A2: Confirm this run does not create `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`.
- V0-A3: Confirm future fixture work remains a plan for `tests/fixtures/factory_v3_operational_readiness_eval/`, not an implementation.
- V0-A4: Confirm Phase 3 natural halted, fallback, or clarification-heavy telemetry gap is present in intent, premortem, and traceability.
- V0-A5: Confirm threshold language remains advisory and non-operational.
- V0-A6: Confirm V2 fallback and non-deprecation language remains explicit.

## Verification Tiers
- V0 artifact proof covers planning-only content and no-touch constraints.
- V1 static/mechanical checks cover Factory validators and whitespace.
- Higher tiers are deferred to the future execution-approved Phase 4 implementation run.
