# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-05-26): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: docs/Factory/v3
- Effective Scope: docs/Factory/v3
- Attempted Scopes: docs/Factory/v3, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: NO
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-05-26T12:14:24Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 55
- Artifact types: {"canonical_doc": 55}
- Focus terms: Phase 4 eval expansion fixture family false-positive false-negative rollup operational readiness evaluator
- Trace IDs: None
- Required refs: docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md, docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md, docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md, docs/Factory/v3/ROADMAP_TO_FULL_VISION.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 30
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:76` [Factory v3 Advisory Validator Plan > Candidate Output Shape]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVIDENCE_ROLLUP.md:17` [Factory v3 Operational Readiness Evidence Rollup > Evidence Inputs]
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md:95` [Factory v3 Mission Record Design v0 > Advisory Validator]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md:86` [Factory v3 Operational Readiness Eval Plan > Eval Families Needed > E4 - Verification And Halt Behavior]

### Q2. `Critical`
- Result count: 12
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:40` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A001 - v2 Core Preservation]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:52` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A003 - Shadow Schema Isolation]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:58` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A004 - External Governance Kernel Optionality]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:64` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A005 - Runtime Kernel Boundary]

### Q3. `deferral`
- Result count: 0
- Evidence: None

### Q4. `human GO`
- Result count: 38
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/VISION.md:70` [Factory v3 Vision > Full Vision]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:421` [Factory v3 Roadmap To Full Vision > Phase 9 - V3 Product Independence Decision]
  - `docs/Factory/v3/VISION.md:15` [Factory v3 Vision > Purpose]
  - `docs/Factory/v3/VISION.md:41` [Factory v3 Vision > Core Thesis]

### Q5. `scope expansion`
- Result count: 25
- Evidence:
  - `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md:65` [Factory v3 Phase 1 Decision Review For V3-OP-001 > Findings]
  - `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md:96` [Factory V3 Phase 4 Eval Expansion Plan > Fixture Expansion Plan]
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md:76` [Factory v3 Phase 1 Decision Review For V3-OP-001 > Decision Options]
  - `docs/Factory/v3/PHASE1_TRIAL_PLAN.md:168` [Factory v3 Phase 1 Trial Plan > Expected Decision Outputs]

### Q6. `Phase 4 eval expansion fixture family false-positive false-negative rollup operational readiness evaluator`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md` (canonical_doc)

### R2. `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md` (canonical_doc)

### R3. `docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md` (canonical_doc)

### R4. `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
