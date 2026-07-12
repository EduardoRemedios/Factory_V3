# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_0927_v3_recall_sync_endurance_canon
- Effective Scope: docs/Factory
- Attempted Scopes: RUN_20260712_0927_v3_recall_sync_endurance_canon, docs/Factory/v3, docs/Factory, docs, docs/Factory/runs, docs/Factory/ProductOwner/phases
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-12T08:28:11Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 1389
- Artifact types: {"canonical_doc": 196, "factory_run_pack_artifact": 1004, "factory_run_root_artifact": 189}
- Focus terms: direct-source, endurance, V3-OP-003
- Trace IDs: None
- Required refs: docs/Factory/v3/V3_OP_003_DECISION_PACK.md, docs/Factory/v3/DURATION_LADDER_PLAN.md, docs/Factory/ORCHESTRATION.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 1119
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/runs/RUN_20260522_1220_v3_release_user_guide/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/EXECUTION_CLOSEOUT.md:27` [Execution Closeout - V3 Confidence Pilot Batch > Pilot Results]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/execution_evidence/CONFIDENCE_PILOT_BATCH_ROLLUP.md:15` [V3 Confidence Pilot Batch Rollup > Results]

### Q2. `Critical`
- Result count: 397
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260518_1100_factory_v3_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 198
- Evidence:
  - `docs/Factory/runs/RUN_20260518_1235_v3_advisory_lint_impl_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 363
- Evidence:
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:57` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:671` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/VISION.md:70` [Factory v3 Vision > Full Vision]

### Q5. `scope expansion`
- Result count: 305
- Evidence:
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `direct-source`
- Result count: 8
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:1` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:115` [Factory v3 Roadmap To Full Vision > Loop-Governance Primitives From Loop-Library Review]
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:9` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair > Objective]
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:67` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair > Verification Expectations]
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:6` [Factory V3 Anchor Registry > Change Log]

### Q7. `endurance`
- Result count: 3
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:16` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair > Required Outcomes]
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:1` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair]
  - `docs/Factory/runs/RUN_20260712_0927_v3_recall_sync_endurance_canon/raw_brief.md:9` [Raw Brief - Direct-Source Recall Sync And Endurance Canon Repair > Objective]

### Q8. `V3-OP-003`
- Result count: 43
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:671` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/README.md:6` [Factory v3 > Change Log]
  - `docs/Factory/v3/ladder/rung1/RUNG1_MISSION_STATE.md:17` [Rung 1 Mission State — LADDER_RUNG1_20260610 > WP1 Findings (audit)]
  - `docs/Factory/v3/ladder/LADDER_STATUS.md:26` [V3-OP-003 Ladder Status — Pickup Aid > Where Things Stand (end of 2026-06-10)]

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/V3_OP_003_DECISION_PACK.md` (canonical_doc)

### R2. `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/DURATION_LADDER_PLAN.md` (canonical_doc)

### R3. `docs/Factory/ORCHESTRATION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/ORCHESTRATION.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
