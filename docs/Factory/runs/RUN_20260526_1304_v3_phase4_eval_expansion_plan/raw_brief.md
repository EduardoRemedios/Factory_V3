# Raw Brief: Factory V3 Phase 4 Eval Expansion Plan

## Execution Mode
PLANNING_ONLY

## Request
Start Factory V3 Phase 4 with a Factory V2-governed planning run. Phase 4 is eval expansion and harness capability profiling only.

## Current State
- Factory V3 lives in its own repository at `/Users/eduardodosremedios/Factory_V3`.
- Factory V2 process docs, templates, scripts, and helper tooling remain present as temporary build-support scaffolding for building V3.
- Factory V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`.
- Phase 3 telemetry evidence review is complete.
- Phase 3 decision: `RECOMMEND_OPTIONAL_ADVISORY_TELEMETRY_WITH_CONDITIONS`.
- Telemetry may continue only as optional advisory shadow evidence for selected narrow `V3-OP-001` evidence missions.
- Phase 3 did not capture a natural halted/fallback/clarification-heavy telemetry pilot; carry this as an evidence gap.
- Current roadmap next move: plan Phase 4 eval expansion and capability profiling.

## Strict Scope
- Create a Factory V2 `PLANNING_ONLY` planning pack.
- Do not implement Phase 4 tooling until the planning pack passes and the user approves execution.
- Do not add governance routing, enforcement, telemetry completeness checks, required gates, CI wiring, runtime authority, proof, lease enforcement, default-mode behavior, or V2 scaffolding removal.
- Do not deprecate or replace Factory V2.
- Preserve V3 as advisory/optional unless canonical docs explicitly approve otherwise.
- Apply SIMPLE-CODE-GATE: smallest clear change, no dependency creep, no broad abstractions, no silent failures.

## Planning Objective
Design Phase 4 evaluation expansion so V3 can measure:
- harness capability,
- execution reliability,
- scope discipline,
- verification quality,
- interruption recovery,
- evidence quality,
- false-positive / false-negative behavior,
- fitness for later governance-routing decisions without implementing a router.

## Required Pre-mortem Focus
- Harness capability scores becoming overconfident or universal when they are actually harness/profile-specific.
- Evals measuring document compliance while missing real execution reliability.
- Negative fixtures becoming too synthetic and not matching real failure modes.
- Phase 4 accidentally designing or implementing the Phase 5 governance router too early.
- Threshold language implying routing, reduced governance, or default-mode promotion before evidence exists.
- Phase 3 telemetry gaps being forgotten, especially the missing natural halted/fallback/clarification-heavy case.
- V2 fallback or non-deprecation language weakening.

## Expected Planning Outputs
Prepare, but do not implement without later approval:
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`
- `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`
- fixture expansion plan for `tests/fixtures/factory_v3_operational_readiness_eval/`
- false-positive / false-negative rollup shape
- thresholds discussion for later routing, clearly marked advisory and non-operational

## Required Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260526_1304_v3_phase4_eval_expansion_plan --output docs/Factory/runs/RUN_20260526_1304_v3_phase4_eval_expansion_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260526_1304_v3_phase4_eval_expansion_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260526_1304_v3_phase4_eval_expansion_plan`
- `git diff --check`
