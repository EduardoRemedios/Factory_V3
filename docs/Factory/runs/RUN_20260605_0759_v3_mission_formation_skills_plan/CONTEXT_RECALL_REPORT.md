# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-06-05): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260605_0759_v3_mission_formation_skills_plan
- Effective Scope: docs
- Attempted Scopes: RUN_20260605_0759_v3_mission_formation_skills_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-06-05T08:00:21Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 1309
- Artifact types: {"canonical_doc": 145, "factory_run_pack_artifact": 978, "factory_run_root_artifact": 186}
- Focus terms: Factory V3 Phase 4.5 mission formation skills discovery challenge Codex SDK orchestration
- Trace IDs: None
- Required refs: docs/Factory/v3/MISSION_FORMATION_DIRECTION.md, docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md, docs/Factory/v3/ROADMAP_TO_FULL_VISION.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 1077
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/runs/RUN_20260522_1220_v3_release_user_guide/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/EXECUTION_CLOSEOUT.md:27` [Execution Closeout - V3 Confidence Pilot Batch > Pilot Results]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/execution_evidence/CONFIDENCE_PILOT_BATCH_ROLLUP.md:15` [V3 Confidence Pilot Batch Rollup > Results]

### Q2. `Critical`
- Result count: 378
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260518_1100_factory_v3_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 190
- Evidence:
  - `docs/Factory/runs/RUN_20260518_1235_v3_advisory_lint_impl_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 320
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/VISION.md:70` [Factory v3 Vision > Full Vision]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:492` [Factory v3 Roadmap To Full Vision > Phase 9 - V3 Product Independence Decision]
  - `docs/Factory/v3/VISION.md:15` [Factory v3 Vision > Purpose]

### Q5. `scope expansion`
- Result count: 287
- Evidence:
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `Factory V3 Phase 4.5 mission formation skills discovery challenge Codex SDK orchestration`
- Result count: 4
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:550` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/ROADMAP.md:13` [ROADMAP.md - Factory V3 Roadmap > Near-Term Work]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:306` [Factory v3 Roadmap To Full Vision > Phase 4.5 - Mission Formation Skills]
  - `docs/Factory/runs/RUN_20260605_0759_v3_mission_formation_skills_plan/raw_brief.md:6` [Raw Brief - V3 Mission Formation Skills Plan > Background]

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/MISSION_FORMATION_DIRECTION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/MISSION_FORMATION_DIRECTION.md` (canonical_doc)

### R2. `docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md` (canonical_doc)

### R3. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
