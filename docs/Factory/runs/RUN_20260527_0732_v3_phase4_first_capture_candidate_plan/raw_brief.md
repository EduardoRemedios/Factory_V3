# Raw Brief: Factory V3 Phase 4 First Capture Candidate Plan

## Execution Mode
PLANNING_ONLY

## Request
Proceed to the next logical Phase 4 step after creating the real-run corpus capture plan and result summary template.

## Current State
- Phase 4 real-run corpus capture plan exists.
- Phase 4 real-run result summary template exists.
- No real evidence mission, result summary, harness capability profile, or telemetry capture has been approved or executed yet.
- Phase 4 remains research-only and non-enforcing.

## Candidate To Plan
Plan, but do not execute, the first real-run capture candidate:

- Candidate ID: `P4-CAPTURE-CANDIDATE-001`
- Profile: `V3-OP-001 Bounded Code Change`
- Mission shape: docs-only status/candidate-record update tied to Phase 4 real-run corpus capture.
- Optional telemetry decision: `NO_TELEMETRY`
- Expected evidence if later approved: one result summary and one harness capability profile.

## Strict Scope
- Do not execute the candidate mission in this run.
- Do not create real-run result summaries or harness profiles in this run.
- Do not collect telemetry.
- Do not add scripts, validators, fixtures, required gates, CI wiring, routing, enforcement, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 build-support removal.

## Expected Future Execution Scope
If later approved, the candidate mission may create:
- `docs/Factory/v3/real_run_corpus/RR_20260527_001_phase4_candidate_status_update.md`
- `docs/Factory/v3/harness_profiles/HP_20260527_001_codex_phase4_candidate_status_update.md`
- up to two canonical status updates documenting that the first capture evidence exists.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260527_0732_v3_phase4_first_capture_candidate_plan --output docs/Factory/runs/RUN_20260527_0732_v3_phase4_first_capture_candidate_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260527_0732_v3_phase4_first_capture_candidate_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260527_0732_v3_phase4_first_capture_candidate_plan`
- `git diff --check`
