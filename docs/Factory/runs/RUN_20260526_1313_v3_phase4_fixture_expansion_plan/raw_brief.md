# Raw Brief: Factory V3 Phase 4 Fixture Expansion Plan

## Execution Mode
PLANNING_ONLY

## Request
Proceed to the next bounded Phase 4 stage after the approved Phase 4 eval expansion plan and harness capability profile template.

## Current State
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md` exists and is research-only/non-enforcing.
- `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md` exists and is advisory evidence only.
- Phase 4 fixture families are planned but not implemented.
- Factory V3 remains optional/advisory except for approved optional `V3-OP-001`.
- Factory V2 remains supported and available as fallback.

## Planning Objective
Create a Factory V2-governed `PLANNING_ONLY` pack that names the exact future implementation scope for Phase 4 operational-readiness fixture expansion and false-positive/false-negative rollup support.

## Strict Scope
- Do not implement fixture files or evaluator changes in this run.
- Do not add governance routing, enforcement, telemetry completeness checks, required gates, CI wiring, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 build-support removal.
- Preserve advisory-only semantics and `blocking_effect: none`.
- Keep changes small and direct under SIMPLE-CODE-GATE.

## Expected Future Implementation Scope
Prepare, but do not implement without later approval:
- Add explicit Phase 4 trigger checks to `scripts/factory_v3_operational_readiness_eval.py`.
- Add exact fixture cases under `tests/fixtures/factory_v3_operational_readiness_eval/cases/`:
  - `V3-P4-CAP-001/input.md`
  - `V3-P4-REL-001/input.md`
  - `V3-P4-SCOPE-001/input.md`
  - `V3-P4-VERIFY-001/input.md`
  - `V3-P4-RECOVER-001/input.md`
  - `V3-P4-EVID-001/input.md`
  - `V3-P4-FPN-001/input.md`
  - `V3-P4-THRESH-001/input.md`
- Update `tests/fixtures/factory_v3_operational_readiness_eval/expected.json`.
- Do not collect real-run corpus data yet.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260526_1313_v3_phase4_fixture_expansion_plan --output docs/Factory/runs/RUN_20260526_1313_v3_phase4_fixture_expansion_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260526_1313_v3_phase4_fixture_expansion_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260526_1313_v3_phase4_fixture_expansion_plan`
- `git diff --check`
