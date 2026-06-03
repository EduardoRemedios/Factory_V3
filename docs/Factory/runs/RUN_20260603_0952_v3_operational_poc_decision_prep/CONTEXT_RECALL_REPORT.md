# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-06-03): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260603_0952_v3_operational_poc_decision_prep
- Effective Scope: RUN_20260603_0952_v3_operational_poc_decision_prep
- Attempted Scopes: RUN_20260603_0952_v3_operational_poc_decision_prep, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: NO
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-06-03T09:00:56Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 29
- Artifact types: {"factory_run_pack_artifact": 26, "factory_run_root_artifact": 3}
- Focus terms: None
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 25
- Evidence:
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/PACK_AUDIT_REPORT.md:33` [Pack Audit Report: V3 Operational POC Decision Prep > Findings]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/HANDOFF/HANDOFF_STAGE_A.md:41` [Handoff Stage A > Open Issues > BLOCKING]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/HANDOFF/HANDOFF_STAGE_A.md:44` [Handoff Stage A > Open Issues > NON-BLOCKING]

### Q2. `Critical`
- Result count: 12
- Evidence:
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/SPRINT_20260603_0952_V3_OPERATIONAL_POC_DECISION_PREP_ENVELOPE_REDTEAM.md:12` [Envelope Red Team: V3 Operational POC Decision Prep > Findings]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/intent_redteam.md:11` [Intent Red Team: V3 Operational POC Decision Prep > Findings]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/risk_register.md:6` [Risk Register: V3 Operational POC Decision Prep > Change Log]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q3. `deferral`
- Result count: 6
- Evidence:
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/PACK_CHECKLIST.md:27` [Pack Checklist: V3 Operational POC Decision Prep > Conditional]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/intent_lock_report.md:6` [Intent Lock Report: V3 Operational POC Decision Prep > Change Log]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/intent_lock_report.md:31` [Intent Lock Report: V3 Operational POC Decision Prep > Bounded Deferrals]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/HANDOFF/HANDOFF_STAGE_D.md:34` [Handoff Stage D > Changes Made]

### Q4. `human GO`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:58` [Context Recall Report > Recall Queries > Q4. `human GO`]

### Q5. `scope expansion`
- Result count: 2
- Evidence:
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/pack/HANDOFF/HANDOFF_STAGE_C.md:40` [Handoff Stage C > Assumptions]

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
