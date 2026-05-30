# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-05-30): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260530_0820_v3_phase4_clarification_capture_plan
- Effective Scope: RUN_20260530_0820_v3_phase4_clarification_capture_plan
- Attempted Scopes: RUN_20260530_0820_v3_phase4_clarification_capture_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: NO
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-05-30T07:22:19Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 2
- Artifact types: {"factory_run_root_artifact": 2}
- Focus terms: P4-NEG-OPP-001, clarification-heavy, PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER, PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN, ROADMAP_TO_FULL_VISION
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 0
- Evidence: None

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
- Result count: 0
- Evidence: None

### Q6. `P4-NEG-OPP-001`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260530_0820_v3_phase4_clarification_capture_plan/raw_brief.md:6` [Raw Brief: Phase 4 Clarification-heavy Capture Candidate Plan > Context]

### Q7. `clarification-heavy`
- Result count: 4
- Evidence:
  - `docs/Factory/runs/RUN_20260530_0820_v3_phase4_clarification_capture_plan/raw_brief.md:6` [Raw Brief: Phase 4 Clarification-heavy Capture Candidate Plan > Context]
  - `docs/Factory/runs/RUN_20260530_0820_v3_phase4_clarification_capture_plan/RETRO.md:6` [Retro: RUN_20260530_0820_v3_phase4_clarification_capture_plan > Notes]
  - `docs/Factory/runs/RUN_20260530_0820_v3_phase4_clarification_capture_plan/raw_brief.md:1` [Raw Brief: Phase 4 Clarification-heavy Capture Candidate Plan]
  - `docs/Factory/runs/RUN_20260530_0820_v3_phase4_clarification_capture_plan/raw_brief.md:12` [Raw Brief: Phase 4 Clarification-heavy Capture Candidate Plan > Required Output]

### Q8. `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER`
- Result count: 0
- Evidence: None

### Q9. `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN`
- Result count: 0
- Evidence: None

### Q10. `ROADMAP_TO_FULL_VISION`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
