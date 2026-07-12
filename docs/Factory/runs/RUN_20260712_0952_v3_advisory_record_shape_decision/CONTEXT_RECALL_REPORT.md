# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_0952_v3_advisory_record_shape_decision
- Effective Scope: docs
- Attempted Scopes: RUN_20260712_0952_v3_advisory_record_shape_decision, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-12T09:53:32Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 1456
- Artifact types: {"canonical_doc": 201, "factory_run_pack_artifact": 1056, "factory_run_root_artifact": 199}
- Focus terms: Mission 026 advisory record shape backward compatibility verifier provenance replay visual evidence endurance coverage
- Trace IDs: None
- Required refs: docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md, docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md, docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md, docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json
- Unresolved required refs: docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json

## Recall Queries
### Q1. `BLOCKING`
- Result count: 1189
- Evidence:
  - `docs/Factory/v3/FINDING_CLASSIFICATION_ROLLUP_V3_OP_001.md:45` [Finding Classification Rollup For V3-OP-001 > Seeded Drift Classification]
  - `docs/Factory/runs/RUN_20260522_1220_v3_release_user_guide/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/EXECUTION_CLOSEOUT.md:27` [Execution Closeout - V3 Confidence Pilot Batch > Pilot Results]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/execution_evidence/CONFIDENCE_PILOT_BATCH_ROLLUP.md:15` [V3 Confidence Pilot Batch Rollup > Results]

### Q2. `Critical`
- Result count: 428
- Evidence:
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260518_1100_factory_v3_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 214
- Evidence:
  - `docs/Factory/runs/RUN_20260518_1235_v3_advisory_lint_impl_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260522_0836_v3_nl_detection_pilot/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 396
- Evidence:
  - `docs/Factory/v3/ANCHOR_REGISTRY.md:59` [Factory V3 Anchor Registry > Anchor Register]
  - `docs/ROADMAP.md:25` [ROADMAP.md - Factory V3 Roadmap > Near-Term Work]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:6` [Factory v3 Roadmap To Full Vision > Change Log]
  - `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md:671` [Factory v3 Roadmap To Full Vision > Recommended Next Move]
  - `docs/Factory/v3/ROADMAP_PREMORTEM.md:23` [Factory v3 Roadmap Pre-Mortem > Red Team Failure Modes]

### Q5. `scope expansion`
- Result count: 325
- Evidence:
  - `docs/ROADMAP.md:25` [ROADMAP.md - Factory V3 Roadmap > Near-Term Work]
  - `docs/Factory/runs/RUN_20260521_0815_v3_operational_readiness_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0939_v3_eval_evolution_decision_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260521_0948_v3_confidence_pilot_execution/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260522_0824_v3_real_halt_reentry_pilot/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `Mission 026 advisory record shape backward compatibility verifier provenance replay visual evidence endurance coverage`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md` (canonical_doc)

### R2. `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md` (canonical_doc)

### R3. `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md` (canonical_doc)

### R4. `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair
- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK
- Unresolved Generated Refs: `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS

## Direct Sources Read
- `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
- `docs/Factory/v3/templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`
- `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- `tests/fixtures/factory_v3_mission_record/trial_003_harmony_faq_ingestion.json`
- `tests/fixtures/factory_v3_mission_record/fixture_halted_verification_failure.json`
- `tests/fixtures/factory_v3_mission_record/fixture_halted_stale_reentry.json`
- `tests/fixtures/factory_v3_mission_record/fixture_blocked_missing_authority.json`
- `tests/fixtures/factory_v3_mission_record/trial_001_pre_envelope_no_bounded_code.json`

## Source Summaries
### `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- Summary: The v0.1 template is a compact replay aid organized around record, mission, authority, execution, reviews, and design signals; it has no current fields for replay, verifier, visual, or bounded-claim provenance.

### `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- Summary: The design requires explicit missing evidence, V2 fallback, and `same_commit` support while keeping authored envelopes and closeouts authoritative and existing records valid.

### `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
- Summary: The mission-control contract contains richer governance concepts but requires optional additive record candidates rather than wholesale embedding or runtime authority.

### `docs/Factory/v3/templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`
- Summary: The template demonstrates next-action, verifier, evidence, safe-hold, and re-entry structures that can inform field semantics without being copied into the smaller mission record.

### `docs/Factory/v3/ladder/rung3/MISSION_026_CLAIM_TO_PROOF_AUDIT_20260712.md`
- Summary: The audit identifies observed gaps in commit finalization, replay provenance, verifier independence, per-artifact visual review, bounded absence claims, and endurance coverage.

### `docs/Factory/v3/ladder/rung3/MISSION_026_FP_FN_ADJUDICATION_20260712.md`
- Summary: The adjudication keeps `NO PROMOTION YET`, requires backward-compatible advisory work, and forbids historical POC repair or inferred endurance proof.

### `tests/fixtures/factory_v3_mission_record/trial_003_harmony_faq_ingestion.json`
- Summary: The completed fixture proves current v0.1 records can represent bounded successful work and thread-local envelopes without richer provenance fields.

### `tests/fixtures/factory_v3_mission_record/fixture_halted_verification_failure.json`
- Summary: The halted fixture proves failed verification and fallback are already represented through existing decision-state, verification, halt, and fallback fields.

### `tests/fixtures/factory_v3_mission_record/fixture_halted_stale_reentry.json`
- Summary: The stale-reentry fixture records a pre-execution halt without requiring runtime state; future additions must not replace authored re-entry evidence.

### `tests/fixtures/factory_v3_mission_record/fixture_blocked_missing_authority.json`
- Summary: The blocked fixture proves no-execution outcomes remain valid with empty authority and explicit fallback reasons.

### `tests/fixtures/factory_v3_mission_record/trial_001_pre_envelope_no_bounded_code.json`
- Summary: The pre-envelope fixture demonstrates that record-shape additions must remain optional for tasks rejected before a mission envelope exists.

No unresolved human approval, external source, or ambiguous artifact remains material to Stage A. This run is planning-only and authorizes no implementation.
