# Raw Brief: Factory V3 Phase 4 Real-run Corpus Plan

## Execution Mode
PLANNING_ONLY

## Request
Proceed with the next best Phase 4 move: plan real-run corpus and harness capability profile capture for selected narrow `V3-OP-001` evidence work.

## Research Decision
No external web search is included in this run. The work is internal Factory evidence planning. Any literature scan or latest-paper benchmarking should be handled as a separate bounded external-research run with an explicit source allowlist.

## Current State
- Phase 4 eval expansion plan exists at `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`.
- Harness capability profile template exists at `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`.
- Synthetic `V3-P4-*` operational-readiness fixtures exist.
- Phase 4 remains research-only and non-enforcing.
- The missing natural halted, fallback, or clarification-heavy telemetry case remains an evidence gap.
- Factory V3 remains optional/advisory except approved optional `V3-OP-001`.
- Factory V2 remains supported and available as fallback.

## Planning Objective
Prepare, but do not execute, a bounded evidence-capture plan for selected narrow `V3-OP-001` missions that will produce real-run result summaries and harness capability profiles.

## Strict Scope
- Do not execute real missions in this planning run.
- Do not collect real telemetry in this planning run.
- Do not implement scripts, validators, CI wiring, required gates, routing, enforcement, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 build-support removal.
- Keep optional telemetry as advisory shadow evidence only when separately approved for selected narrow evidence missions.
- Preserve `blocking_effect: none` for advisory eval output.

## Expected Future Planning Outputs
Prepare future execution scope for:
- `docs/Factory/v3/PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`
- `docs/Factory/v3/templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md`
- one or two selected narrow `V3-OP-001` evidence mission candidates,
- harness capability profile capture workflow,
- false-positive / false-negative human adjudication workflow,
- explicit treatment of the missing natural halted/fallback/clarification-heavy case.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260527_0712_v3_phase4_real_run_corpus_plan --output docs/Factory/runs/RUN_20260527_0712_v3_phase4_real_run_corpus_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260527_0712_v3_phase4_real_run_corpus_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260527_0712_v3_phase4_real_run_corpus_plan`
- `git diff --check`
