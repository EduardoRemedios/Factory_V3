# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_1009_v3_advisory_record_shape_impl
- Effective Scope: docs
- Attempted Scopes: RUN_20260712_1009_v3_advisory_record_shape_impl, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-12T10:10:30Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 1485
- Artifact types: {"canonical_doc": 201, "factory_run_pack_artifact": 1082, "factory_run_root_artifact": 202}
- Focus terms: ADOPT_NARROW_SET mission record optional provenance exact 18 file implementation
- Trace IDs: None
- Required refs: docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/PACK_AUDIT_REPORT.md, docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/fixtures/advisory_record_shape/candidate_fields.md, docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 1221
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/runs/RUN_20260522_1220_v3_release_user_guide/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/EXECUTION_CLOSEOUT.md:27` [Execution Closeout - V3 Confidence Pilot Batch > Pilot Results]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/execution_evidence/CONFIDENCE_PILOT_BATCH_ROLLUP.md:15` [V3 Confidence Pilot Batch Rollup > Results]

### Q2. `Critical`
- Result count: 438
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260518_1100_factory_v3_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 225
- Evidence:
  - `docs/Factory/runs/RUN_20260518_1235_v3_advisory_lint_impl_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 404
- Evidence:
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:59` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/ROADMAP.md:25` [ROADMAP.md - Factory V3 Roadmap > Near-Term Work]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:671` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]

### Q5. `scope expansion`
- Result count: 331
- Evidence:
  - `docs/ROADMAP.md:25` [ROADMAP.md - Factory V3 Roadmap > Near-Term Work]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `ADOPT_NARROW_SET mission record optional provenance exact 18 file implementation`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/PACK_AUDIT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/PACK_AUDIT_REPORT.md` (factory_run_pack_artifact)

### R2. `docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/fixtures/advisory_record_shape/candidate_fields.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0952_v3_advisory_record_shape_decision/pack/fixtures/advisory_record_shape/candidate_fields.md` (factory_run_pack_artifact)

### R3. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
