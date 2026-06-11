# Factory V3 Anchor Registry

## Version
v0.15

## Change Log
- v0.15 (2026-06-11): Updated `V3-ANCHOR-004` with the rung-2 attempt-2 FAIL adjudication (`HDI-RUNG2-004`: mechanics 8/8, honest duration compression again); two consecutive duration failures make the ladder design review the next gate; the safe-hold-trigger principle is adopted for all future interrupt records in the lane.
- v0.14 (2026-06-11): Updated `V3-ANCHOR-004` with the rerun-path decision (`HDI-RUNG2-003`, Option A); next gate is the POC Mission 022 rerun envelope plus sponsor Go.
- v0.13 (2026-06-11): Updated `V3-ANCHOR-004` with the rung-2 attempt-1 FAIL adjudication (`HDI-RUNG2-002`): transport evidence item satisfied, duration criterion failed honestly; next gate is the rerun-path sponsor decision.
- v0.12 (2026-06-11): Updated `V3-ANCHOR-004` with the resolved rung-2 transport decision (`HDI-RUNG2-001`: Codex harness with Codex mobile); next gate is the rung-2 envelope in the POC repo plus sponsor Go.
- v0.11 (2026-06-10): Updated `V3-ANCHOR-004` with first local ladder evidence (rung 1 passed for mechanics, transport trial passed) and the `ladder/LADDER_STATUS.md` pickup aid.
- v0.10 (2026-06-10): Added the duration-ladder plan to the `V3-ANCHOR-004` read-first paths; the ladder also carries the `V3-ANCHOR-005` live non-executing skill trial at rung 3.
- v0.9 (2026-06-10): Added the interrupt-transport trial plan to the `V3-ANCHOR-004` read-first paths.
- v0.8 (2026-06-10): Updated `V3-ANCHOR-007` with the mission-health vocabulary; next gate is recording signals at checkpoints in duration-ladder rungs.
- v0.7 (2026-06-10): Updated `V3-ANCHOR-004` with the drafted candidate profile and decision pack; next gate is now gathering the evidence the pack names.
- v0.6 (2026-06-10): Added `V3-ANCHOR-010` for the advisory regulatory-crosswalk lane.
- v0.5 (2026-06-10): Added `SKILL_PROVENANCE_POLICY.md` to the `V3-ANCHOR-008` read-first paths.
- v0.4 (2026-06-10): Added `V3-ANCHOR-009` for the standing-authorization research lane.
- v0.3 (2026-06-10): Added `V3-ANCHOR-008` for the evidence-integrity-under-mutable-harness-state lane.
- v0.2 (2026-06-10): Replaced the mission-health placeholder evidence prose with `none_yet` and clarified that anchors without evidence artifacts must use an explicit placeholder marker.
- v0.1 (2026-06-10): Initial pointer-first registry for V3 anchor points, promotion load ratings, read-first paths, and next named gates.

## Status
Research-only orientation aid.

This registry does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime-control power, proof, lease enforcement, default-mode behavior, V3 profile promotion, public deployment, real-data use, live integrations, or Factory V2 build-support removal.

Factory V3 has one approved optional operational profile: `V3-OP-001 Bounded Code Change`. Every other anchor below remains research-only, advisory, candidate, or unapproved unless a separately approved mission or release decision names it.

## Purpose
Give future agents and reviewers a compact map of the main V3 anchor points without duplicating the state narratives in `README.md`, `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, or `ROADMAP_TO_FULL_VISION.md`.

Use this file as a cold-start routing aid:

1. Read the anchor's `read_first` paths.
2. Follow `evidence_paths` to source records.
3. Treat `next_named_gate` as the next gate to prepare or evaluate, not as execution approval.
4. Apply the referenced guardrails before proposing edits.

## Field Rules
- `current_status` must not be a bare yes/no approval flag.
- `evidence_paths` must point to source artifacts, not summarize them as replacement evidence; use `none_yet` only when no evidence artifact exists.
- `guardrail_refs` should point to existing boundary docs instead of restating all boundaries here.
- `excluded_uses` is advisory language for orientation only; the source boundary docs remain authoritative.

## Anchor Register

| Anchor ID | Anchor | Promotion Load Rating | Current Status | Read First | Evidence Paths | Next Named Gate | Guardrail Refs | Excluded Uses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `V3-ANCHOR-001` | Optional bounded code-change profile | Approved optional named profile; no default-mode or release promotion | `V3-OP-001-eligible` when the task is bounded and authorized | `USER_GUIDE.md`; `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`; `OPERATIONAL_RELEASE_APPROVAL_V3_OP_001.md` | `PHASE1_DECISION_REVIEW_V3_OP_001.md`; `trials/TRIAL_INDEX.md`; `mission_records/` | Keep using as optional bounded profile; do not generalize to default mode | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Default V3 mode, required gates, deployment/infrastructure authority, broad architecture |
| `V3-ANCHOR-002` | Phase 4 negative-case opportunity register | Level 0 research register | `research-only` | `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`; `PHASE4_EVAL_EXPANSION_PLAN.md` | `real_run_corpus/INDEX.md`; `harness_profiles/INDEX.md`; `telemetry/pilots/` | Separately approve any future candidate before execution | `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`; `PROMOTION_CRITERIA.md` | Router input, threshold table, promotion evidence, approval for future candidates |
| `V3-ANCHOR-003` | Standalone V3-only POC evidence | Candidate operational-readiness evidence for named POC scope | `candidate-evidence-only` | `ROADMAP_TO_FULL_VISION.md`; `docs/PROJECT_STATE.md`; POC eval records in the POC repo | POC repo `.factory-v3/evals/V3_POC_EVAL_RECORD_20260609.json`; POC repo `.factory-v3/evals/V3_POC_EVAL_ADJUDICATION_NOTE_20260609.md` | Decide which evidence transfers into a Factory V3 decision, if any | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Real-data approval, live Garmin, live Telegram, ambient runtime, public deployment, production infrastructure, runtime-control power, V2 removal |
| `V3-ANCHOR-004` | Candidate `V3-OP-003` long-running remote-interrupt profile | Candidate; not promoted | `research-only`; decision pack at `NO PROMOTION YET`; rung 1 passed for mechanics; rung-2 attempts 1 and 2 both FAILED on duration (attempt 2 mechanics 8/8, `HDI-RUNG2-004`); transport evidence satisfied (phone round-trips, sponsor away); safe-hold-trigger principle adopted for interrupt records | `ladder/LADDER_STATUS.md`; `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`; `V3_OP_003_DECISION_PACK.md`; `DURATION_LADDER_PLAN.md` | `ladder/rung1/`; `ladder/transport_trial/`; `ladder/rung2/`; `mission_records/MR_20260610_019_ladder_rung1_state_doc_consistency.json`; `mission_records/MR_20260610_020_interrupt_transport_trial.json`; `mission_records/MR_20260611_023_rung2_adjudication.json`; `mission_records/MR_20260611_025_rung2_rerun_adjudication.json`; POC Mission 012/013/021/022 artifacts | Ladder design review (mandatory after two consecutive rung-2 duration failures): re-base rung classes on measured budget-and-waypoint evidence, with the sponsor's significantly-larger-scope guidance and the safe-hold-trigger interrupt-field redesign as named inputs; requires its own envelope and sponsor Go | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Promotion from partial evidence, live messaging automation, default long-running missions, unattended or scheduled operation, runtime-control power |
| `V3-ANCHOR-005` | Mission formation and challenge skills | Level 0 research; possible future advisory intake aid | `research-only` | `MISSION_FORMATION_DIRECTION.md`; `.agents/skills/factory-mission-formation/SKILL.md`; `.agents/skills/factory-challenge-mission/SKILL.md` | `skill_trials/mission_formation/` | Run live non-executing trials before any recommendation; the rung-3 contract drafting in `DURATION_LADDER_PLAN.md` is the named candidate trial | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Execution authority, default intake, non-coding autonomous work, treating conversation as approval |
| `V3-ANCHOR-006` | Codex SDK/MCP orchestration as governed worker runtime | Level 0 research | `research-only` | `CODEX_SDK_ORCHESTRATION_DIRECTION.md`; `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md` | `harness_profiles/HP_20260530_002_codex_subagent_workflows_research.md`; `harness_profiles/HP_20260601_004_codex_phase4_dynamic_evidence_export_candidate.md` | Start with read-only orchestration discovery/challenge evidence | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Unattended execution, production actions, credential use, runtime-control power, hidden governance replacement |
| `V3-ANCHOR-007` | Mission health and continuation judgment | Level 0 research lane | `research-only`; advisory vocabulary defined | `MISSION_HEALTH_VOCABULARY.md`; `ADAPTIVE_MISSION_CONTROL.md` | `none_yet` | Record the six signals at checkpoints in duration-ladder rungs before any schema, validator, or threshold proposal | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Required checkpoint fields, routing authority, runtime-control power, schema promotion without evidence |
| `V3-ANCHOR-008` | Evidence integrity under mutable harness state | Level 0 research principle | `research-only` | `MUTABLE_HARNESS_STATE.md`; `SKILL_PROVENANCE_POLICY.md`; `MISSION_RECORD_DESIGN_V0.md` | `harness_profiles/HP_20260530_001_claude_code_dynamic_workflows_research.md`; `mission_records/MR_20260610_010_readme_governance_boundaries_split.json` | Propose advisory validator and fixture support for model-identity and routing fields as a separately approved change | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Required record fields without approval, validator enforcement, vendor-claim promotion without local evidence |
| `V3-ANCHOR-009` | Standing authorization for future scheduled or ambient missions | Level 0 research lane | `research-only` | `SHADOW_SCHEMA_CANDIDATES.md`; `ADAPTIVE_MISSION_CONTROL.md`; repo-root `RESEARCH_SPIKE_20260604_interrupt_transport_surfaces.md` | `none_yet` | Refine grant and wake-record vocabulary and async-escalation semantics before any scheduled-execution proposal | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Scheduled or unattended execution, live messaging automation, credential use, cron or scheduler wiring, runtime-control power |
| `V3-ANCHOR-010` | Advisory regulatory crosswalk (EU AI Act / ISO 42001 themes) | Level 0 advisory orientation document | `research-only`; marked for human review | `REGULATORY_CROSSWALK.md` | `none_yet` | Human/legal review of crosswalk rows before any external use | `NON_GOALS_AND_BOUNDARIES.md`; `docs/Factory/ProductOwner/PO_ROLE_DEFINITION.md` | Compliance or certification claims, conformity assertions, external publication without human review, regulated-action scope |

## Closeout Rule
When evidence changes an anchor's status, update this registry in the same change cycle as the source state docs or explicitly record why no registry update was needed.

Do not add a new anchor if it only restates project state. Add one only when it improves cold-start routing, points to source evidence, or names a future gate that a later model can safely prepare.
