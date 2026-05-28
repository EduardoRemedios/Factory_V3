# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-05-28): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260528_0604_v3_phase4_negative_case_capture_plan
- Effective Scope: RUN_20260528_0604_v3_phase4_negative_case_capture_plan
- Attempted Scopes: RUN_20260528_0604_v3_phase4_negative_case_capture_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: NO
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-05-28T05:06:01Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 2
- Artifact types: {"factory_run_root_artifact": 2}
- Focus terms: None
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260528_0604_v3_phase4_negative_case_capture_plan/raw_brief.md:9` [Raw Brief: Factory V3 Phase 4 Negative-case Capture Plan > Current State]

### Q2. `Critical`
- Result count: 0
- Evidence: None

### Q3. `deferral`
- Result count: 0
- Evidence: None

### Q4. `human GO`
- Result count: 0
- Evidence: None

### Q5. `scope expansion`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260528_0604_v3_phase4_negative_case_capture_plan/raw_brief.md:38` [Raw Brief: Factory V3 Phase 4 Negative-case Capture Plan > Expected Future Execution Scope]

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
