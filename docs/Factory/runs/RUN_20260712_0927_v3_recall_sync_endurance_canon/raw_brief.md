# Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair

Execution Mode: EXECUTION_ENABLED

Execution Authorization: User approval in the active Codex thread on 2026-07-12: "I agree proceed" after reviewing the proposed direct-source recall synchronization and correction of four-hour duration semantics.

Downstream Fan-Out: NOT_APPROVED

## Objective

Deliver two bounded, sequential repairs:

1. Synchronize the Factory V2 build-support direct-source context-recall repair path from `factory-starter-kit` commit `06646d7` into this repository, preserving local V3 boundary wording and deterministic validation behavior.
2. Reconcile active Factory V3 canon so a roughly four-hour duration is treated as an endurance capability ceiling that the system should tolerate without drift or quality degradation, not as a workload floor that missions must pad or prolong to satisfy.

## Required Outcomes

- A generated `WEAK` Stage A recall remains blocking unless a valid `REPAIRED_DIRECT_SOURCE_CHECK` addendum proves direct local-source review after index refresh and fallback-scope attempts.
- Missing, external, unreadable, ambiguous, or materially unresolved sources cannot be used to repair recall.
- Stage A lint, pack lint, tests, and knowledge lint recognize the same repair contract.
- Existing Factory V3 advisory-only and V2-fallback boundaries remain unchanged.
- Canon clearly separates mission success from endurance-capability evidence.
- A mission that completes correctly in less than four hours is not failed and must not be padded.
- Lack of a naturally long mission may leave the upper endurance envelope insufficiently evidenced, but must not retroactively convert successful shorter missions into failures.
- Active next-step and evidence-status contradictions identified during reconnaissance are corrected without rewriting historical evidence.

## Candidate Source Scope

Factory V2 build-support sync:

- `docs/Factory/ORCHESTRATION.md`
- `docs/Factory/Spec/STAGE_CONTRACTS.md`
- `docs/Factory/templates/CONTEXT_RECALL_REPORT_TEMPLATE.md`
- `scripts/factory_pack_lint.py`
- `scripts/factory_stage_lint.py`
- `scripts/knowledge_lint.sh`
- `tests/test_context_recall_repair.py`

V3 canon reconciliation candidates:

- `README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
- `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- `docs/Factory/v3/CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ladder/rung3/README.md`

Factory planning evidence under this run root is also authorized.

## Non-Goals

- No V3 profile promotion.
- No runtime loop orchestration, scheduler, background worker, governance routing, telemetry enforcement, required-gate integration, runtime authority, or external governance-kernel adapter.
- No four-hour execution trial in this run.
- No artificial task padding, waypoint inflation, call-count inflation, or duration targeting.
- No Mission 026 claim-to-proof audit or mission-record schema extension in this run.
- No Factory V2 scaffolding removal.
- No changes to the separate `factory-starter-kit` repository.

## Verification Expectations

- `python3 -m unittest tests.test_context_recall_repair`
- `python3 -m unittest discover -s tests`
- `bash scripts/knowledge_lint.sh`
- `python3 -m py_compile scripts/factory_pack_lint.py scripts/factory_stage_lint.py scripts/factory_context_index.py scripts/factoryctl`
- Existing V3 advisory validators and deterministic fixture expectations.
- `git diff --check`
- Direct-source comparison against `factory-starter-kit` commit `06646d7` for the synchronized behavior, with local boundary wording reviewed rather than blindly overwritten.
- Manual no-promotion and no-padding language review.

## Go / No-Go Rule

Proceed to implementation only after the complete Factory pack passes Stage I2 and pack lint and the human gives explicit post-pack Go. Halt if the source delta cannot be separated from unrelated starter-kit changes, if deterministic fixtures would require unrelated churn, or if canon reconciliation would weaken current approval boundaries.
