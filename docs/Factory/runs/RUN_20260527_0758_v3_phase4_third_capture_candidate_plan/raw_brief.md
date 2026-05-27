# Raw Brief: Factory V3 Phase 4 Third Capture Candidate Plan

## Execution Mode
PLANNING_ONLY

## Request
Proceed to the next logical Phase 4 step after two happy-path docs-only captures and canonical status updates.

## Current State
- Phase 4 real-run corpus capture plan exists.
- Phase 4 real-run result summary template exists.
- Two happy-path real-run result summaries and harness capability profiles exist.
- Canonical status docs record that these captures do not close the Phase 3 natural halted/fallback/clarification-heavy gap.
- Phase 4 remains research-only and non-enforcing.

## Candidate To Plan
Plan, but do not execute, the third real-run capture candidate:

- Candidate ID: `P4-CAPTURE-CANDIDATE-003`
- Profile: `V3-OP-001 Bounded Code Change`
- Mission shape: docs-only negative-case opportunity register for future Phase 4 capture candidates.
- Optional telemetry decision: `NO_TELEMETRY`
- Expected evidence if later approved: one opportunity register, index updates, one result summary, and one harness capability profile.

## Strict Scope
- Do not execute the candidate mission in this run.
- Do not create real-run result summaries or harness profiles in this run.
- Do not collect telemetry.
- Do not add scripts, validators, fixtures, required gates, CI wiring, routing, enforcement, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 build-support removal.

## Expected Future Execution Scope
If later approved, the candidate mission may create:
- `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`
- update `docs/Factory/v3/real_run_corpus/INDEX.md`
- update `docs/Factory/v3/harness_profiles/INDEX.md`
- `docs/Factory/v3/real_run_corpus/RR_20260527_003_phase4_negative_case_opportunity_register.md`
- `docs/Factory/v3/harness_profiles/HP_20260527_003_codex_phase4_negative_case_opportunity_register.md`

The future candidate should classify possible future opportunities for natural halted, fallback, clarification-heavy, or reentry evidence. It must not manufacture a failure, claim the gap is closed, or approve any listed future candidate for execution.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260527_0758_v3_phase4_third_capture_candidate_plan --output docs/Factory/runs/RUN_20260527_0758_v3_phase4_third_capture_candidate_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260527_0758_v3_phase4_third_capture_candidate_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260527_0758_v3_phase4_third_capture_candidate_plan`
- `git diff --check`
