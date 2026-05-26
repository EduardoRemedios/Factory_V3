# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-05-26): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260526_0702_v3_phase3_telemetry_replay_plan
- Effective Scope: docs/Factory/v3
- Attempted Scopes: RUN_20260526_0702_v3_phase3_telemetry_replay_plan, docs/Factory/v3, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-05-26T06:03:09Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 41
- Artifact types: {"canonical_doc": 41}
- Focus terms: None
- Trace IDs: None
- Required refs: docs/Factory/v3/ROADMAP_TO_FULL_VISION.md, docs/Factory/v3/PHASE2_5_MISSION_RECORD_ADOPTION_DECISION.md, docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 21
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:76` [Factory v3 Advisory Validator Plan > Candidate Output Shape]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVIDENCE_ROLLUP.md:17` [Factory v3 Operational Readiness Evidence Rollup > Evidence Inputs]
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md:95` [Factory v3 Mission Record Design v0 > Advisory Validator]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md:86` [Factory v3 Operational Readiness Eval Plan > Eval Families Needed > E4 - Verification And Halt Behavior]

### Q2. `Critical`
- Result count: 10
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:22` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:40` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A001 - v2 Core Preservation]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:52` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A003 - Shadow Schema Isolation]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:58` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A004 - External Governance Kernel Optionality]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:64` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A005 - Runtime Kernel Boundary]

### Q3. `deferral`
- Result count: 0
- Evidence: None

### Q4. `human GO`
- Result count: 36
- Evidence:
  - `docs/Factory/v3/VISION.md:67` [Factory v3 Vision > Full Vision]
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:22` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:402` [Factory v3 Roadmap To Full Vision > Phase 9 - V3 Product Independence Decision]
  - `docs/Factory/v3/VISION.md:14` [Factory v3 Vision > Purpose]
  - `docs/Factory/v3/VISION.md:38` [Factory v3 Vision > Core Thesis]

### Q5. `scope expansion`
- Result count: 24
- Evidence:
  - `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md:65` [Factory v3 Phase 1 Decision Review For V3-OP-001 > Findings]
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md:76` [Factory v3 Phase 1 Decision Review For V3-OP-001 > Decision Options]
  - `docs/Factory/v3/PHASE1_TRIAL_PLAN.md:168` [Factory v3 Phase 1 Trial Plan > Expected Decision Outputs]
  - `docs/Factory/v3/V2_GUARANTEE_PRESERVATION_MATRIX_V3_OP_001.md:21` [V2 Guarantee Preservation Matrix For V3-OP-001 > Matrix]

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` (canonical_doc)

### R2. `docs/Factory/v3/PHASE2_5_MISSION_RECORD_ADOPTION_DECISION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/PHASE2_5_MISSION_RECORD_ADOPTION_DECISION.md` (canonical_doc)

### R3. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
