# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_1002_v3_m026_claim_proof_adjudication
- Effective Scope: docs/Factory/v3
- Attempted Scopes: RUN_20260712_1002_v3_m026_claim_proof_adjudication, docs/Factory/v3/ladder/rung3, docs/Factory/v3, docs, docs/Factory/runs, docs/Factory/ProductOwner/phases
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-12T09:03:59Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 158
- Artifact types: {"canonical_doc": 158}
- Focus terms: Mission_026, claim-to-proof, FP/FN, V3-OP-003
- Trace IDs: None
- Required refs: docs/Factory/v3/V3_OP_003_DECISION_PACK.md, docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md, docs/Factory/v3/DURATION_LADDER_PLAN.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 50
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:76` [Factory v3 Advisory Validator Plan > Candidate Output Shape]
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md:115` [Factory v3 Mission Record Design v0 > Advisory Validator]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVIDENCE_ROLLUP.md:17` [Factory v3 Operational Readiness Evidence Rollup > Evidence Inputs]
  - `docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md:87` [Factory v3 Operational Readiness Eval Plan > Eval Families Needed > E4 - Verification And Halt Behavior]

### Q2. `Critical`
- Result count: 17
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/ladder/rung3/RUNG3_CHALLENGE_REVIEW_20260702.md:17` [Rung 3 Formation Challenge Review - 2026-07-02 > Critical Findings]
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_CHALLENGE_REVIEW_20260702.md:15` [Rung 3 Option A Challenge Review - 2026-07-02 > Critical Findings]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:40` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A001 - v2 Core Preservation]
  - `docs/Factory/v3/ADVISORY_VALIDATOR_PLAN.md:52` [Factory v3 Advisory Validator Plan > Candidate Checks > V3-A003 - Shadow Schema Isolation]

### Q3. `deferral`
- Result count: 1
- Evidence:
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_EXECUTION_ENVELOPE_20260702.md:43` [Rung 3 Option A Execution Envelope - 2026-07-02 > Selected Option]

### Q4. `human GO`
- Result count: 113
- Evidence:
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:58` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:672` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/v3/VISION.md:70` [Factory v3 Vision > Full Vision]

### Q5. `scope expansion`
- Result count: 56
- Evidence:
  - `docs/Factory/v3/GOVERNANCE_BOUNDARIES.md:17` [Factory V3 Governance Boundaries > Boundaries]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:58` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md:65` [Factory v3 Phase 1 Decision Review For V3-OP-001 > Findings]
  - `docs/Factory/v3/PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md:123` [Factory V3 Phase 4 Dynamic Workflows Harness Research Plan > Evaluation Questions]

### Q6. `Mission_026`
- Result count: 6
- Evidence:
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_EXECUTION_ENVELOPE_20260702.md:55` [Rung 3 Option A Execution Envelope - 2026-07-02 > Authorized Scope For Future Execution]
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_EXECUTION_ENVELOPE_20260702.md:116` [Rung 3 Option A Execution Envelope - 2026-07-02 > Allowed Commands]
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md:8` [Rung 3 Option A Post-Run Evidence Review - 2026-07-02 > Source Evidence]
  - `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md:28` [Factory V3 Mission-Control Contract > Source Evidence]
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_EXECUTION_ENVELOPE_20260702.md:87` [Rung 3 Option A Execution Envelope - 2026-07-02 > Target Epics And Waypoints]

### Q7. `claim-to-proof`
- Result count: 29
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:6` [Factory V3 Anchor Registry > Change Log]
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:58` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:102` [Factory v3 Roadmap To Full Vision > Current Decision Queue]
  - `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md:6` [Factory V3 Mission-Control Contract > Change Log]

### Q8. `FP/FN`
- Result count: 29
- Evidence:
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:58` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:672` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:102` [Factory v3 Roadmap To Full Vision > Current Decision Queue]
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:6` [Factory V3 Anchor Registry > Change Log]
  - `docs/Factory/v3/DURATION_LADDER_PLAN.md:113` [Factory V3 Endurance Evidence Ladder Plan > Named Follow-ups (Not Approved Here)]

### Q9. `V3-OP-003`
- Result count: 44
- Evidence:
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:672` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/README.md:6` [Factory v3 > Change Log]
  - `docs/Factory/v3/ladder/rung1/RUNG1_MISSION_STATE.md:17` [Rung 1 Mission State — LADDER_RUNG1_20260610 > WP1 Findings (audit)]
  - `docs/Factory/v3/ladder/LADDER_STATUS.md:27` [V3-OP-003 Ladder Status — Pickup Aid > Where Things Stand (updated 2026-07-12)]

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/V3_OP_003_DECISION_PACK.md` (canonical_doc)

### R2. `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md` (canonical_doc)

### R3. `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/DURATION_LADDER_PLAN.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
