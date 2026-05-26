# Factory v3 Phase 2.5 Mission Record Adoption Decision

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Phase 2.5 adoption decision for shadow V3 mission records.

## Status
Decision complete. This document is research-only and non-enforcing: it does not approve telemetry, governance routing, runtime authority, required gates, V3 default-mode behavior, or V2 scaffolding removal.

## Decision Metadata
- Decision: RECOMMEND_OPTIONAL_SHADOW_USE
- Date: 2026-05-26
- Scope: `V3-OP-001` mission-record shadow evidence
- Human owner: Eduardo Remedios
- Required-gate integration approved: NO
- Telemetry implementation approved: NO
- Runtime authority approved: NO
- V3 default-mode promotion approved: NO
- V2 scaffolding removal approved: NO

## Decision Summary
Continue using `V3_MISSION_RECORD` as optional shadow evidence for suitable low-risk `V3-OP-001` work.

The records improved replayability enough to keep using them before Phase 3 planning. They made objective, authority, file scope, verification, fallback triggers, and decision state easier to inspect than prose-only closeout.

This decision does not make records required. It does not start telemetry implementation. It only allows Phase 3 telemetry/replay planning to begin from the current record shape.

## Evidence Inputs

| Evidence | Path | Result |
|---|---|---|
| Phase 2.5 status | `docs/Factory/v3/PHASE2_5_MISSION_RECORD_ADOPTION_STATUS.md` | Evidence requirements present. |
| Completed real record | `docs/Factory/v3/mission_records/MR_20260525_001_blocked_fixture_work.json` | Valid shadow record. |
| Completed real record | `docs/Factory/v3/mission_records/MR_20260525_002_roadmap_gate_refinement.json` | Valid shadow record. |
| Fresh fallback record | `docs/Factory/v3/mission_records/MR_20260526_003_white_mouse_app_pre_envelope_fallback.json` | Valid shadow record. |
| V2 decision pack | `docs/Factory/runs/RUN_20260526_0900_v3_phase2_5_adoption_decision/` | V2-governed decision evidence. |

## Requirement Review

| Requirement | Result | Evidence |
|---|---|---|
| At least 2 fresh real V3 repository mission records | PASS | Three real records under `docs/Factory/v3/mission_records/`. |
| At least 1 blocked, halted, or fallback real adoption record | PASS | White mouse app pre-envelope fallback record. |
| Validator reports for records | PASS | `factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`. |
| Replayability review | PASS WITH RISK | Records improved replay, but backfilled records were weaker than live records. |
| Source-of-truth conflict review | PASS | Records remain advisory evidence and do not replace Mission Mode, V2 run packs, or git history. |

## Findings

| Finding | Evidence | Treatment |
|---|---|---|
| Mission records improve replayability. | Completed and fallback records identify objective, authority, files, verification, and decision state. | Continue optional shadow use. |
| Backfilled records are weaker. | Two records reconstructed thread-local envelope details after commit. | Prefer live record capture during future missions. |
| Pre-envelope fallback is valuable. | White mouse app idea was rejected before implementation and preserved as evidence. | Keep fallback records first-class. |
| Source-of-truth conflict is controlled. | Records are explicitly advisory and non-blocking. | Do not wire into gates. |

## Decision
Decision: RECOMMEND_OPTIONAL_SHADOW_USE

Approved:
- Use V3 mission records as optional shadow evidence for suitable `V3-OP-001` work.
- Prefer creating records during the mission rather than after commit.
- Use current record shape as the base context for Phase 3 telemetry/replay planning.

Not approved:
- required gate integration,
- CI or `factoryctl` enforcement,
- telemetry implementation,
- governance routing,
- runtime authority,
- default-mode promotion,
- V2 build-support removal from this repository.

## Residual Risks

| Risk | Treatment |
|---|---|
| Records add process burden for small work. | Keep optional and shadow-only. |
| Records may drift from actual execution if backfilled late. | Prefer live record capture. |
| Users may mistake optional shadow records for required gates. | Keep non-enforcing language in README, roadmap, and validator output. |
| Phase 3 could overbuild telemetry. | Start with a separate planning task and data-minimization review. |

## Next Step
Start Phase 3 planning only.

The immediate next artifact should be a V2-governed plan for the minimal telemetry/replay format. It must define event fields, excluded data, fixture shape, replay checks, and data-minimization rules before any implementation.
