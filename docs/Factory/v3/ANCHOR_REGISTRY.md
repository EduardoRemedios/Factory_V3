# Factory V3 Anchor Registry

## Version
v0.1

## Change Log
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
- `evidence_paths` must point to source artifacts, not summarize them as replacement evidence.
- `guardrail_refs` should point to existing boundary docs instead of restating all boundaries here.
- `excluded_uses` is advisory language for orientation only; the source boundary docs remain authoritative.

## Anchor Register

| Anchor ID | Anchor | Promotion Load Rating | Current Status | Read First | Evidence Paths | Next Named Gate | Guardrail Refs | Excluded Uses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `V3-ANCHOR-001` | Optional bounded code-change profile | Approved optional named profile; no default-mode or release promotion | `V3-OP-001-eligible` when the task is bounded and authorized | `USER_GUIDE.md`; `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`; `OPERATIONAL_RELEASE_APPROVAL_V3_OP_001.md` | `PHASE1_DECISION_REVIEW_V3_OP_001.md`; `trials/TRIAL_INDEX.md`; `mission_records/` | Keep using as optional bounded profile; do not generalize to default mode | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Default V3 mode, required gates, deployment/infrastructure authority, broad architecture |
| `V3-ANCHOR-002` | Phase 4 negative-case opportunity register | Level 0 research register | `research-only` | `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`; `PHASE4_EVAL_EXPANSION_PLAN.md` | `real_run_corpus/INDEX.md`; `harness_profiles/INDEX.md`; `telemetry/pilots/` | Separately approve any future candidate before execution | `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`; `PROMOTION_CRITERIA.md` | Router input, threshold table, promotion evidence, approval for future candidates |
| `V3-ANCHOR-003` | Standalone V3-only POC evidence | Candidate operational-readiness evidence for named POC scope | `candidate-evidence-only` | `ROADMAP_TO_FULL_VISION.md`; `docs/PROJECT_STATE.md`; POC eval records in the POC repo | POC repo `.factory-v3/evals/V3_POC_EVAL_RECORD_20260609.json`; POC repo `.factory-v3/evals/V3_POC_EVAL_ADJUDICATION_NOTE_20260609.md` | Decide which evidence transfers into a Factory V3 decision, if any | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Real-data approval, live Garmin, live Telegram, ambient runtime, public deployment, production infrastructure, runtime-control power, V2 removal |
| `V3-ANCHOR-004` | Candidate `V3-OP-003` long-running remote-interrupt profile | Candidate; not promoted | `research-only` | `ADAPTIVE_MISSION_CONTROL.md`; `ROADMAP_TO_FULL_VISION.md`; POC Mission 012/013 records in the POC repo | POC Mission 012 and 013 closeout, checkpoint, human-decision-interrupt, and mission-state artifacts | Draft a decision pack with `PASS`, `CONDITIONAL PASS`, and `NO PROMOTION YET` outcomes | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Promotion from POC evidence alone, live messaging automation, default long-running missions, runtime-control power |
| `V3-ANCHOR-005` | Mission formation and challenge skills | Level 0 research; possible future advisory intake aid | `research-only` | `MISSION_FORMATION_DIRECTION.md`; `.agents/skills/factory-mission-formation/SKILL.md`; `.agents/skills/factory-challenge-mission/SKILL.md` | `skill_trials/mission_formation/` | Run live non-executing trials before any recommendation | `PROMOTION_CRITERIA.md`; `NON_GOALS_AND_BOUNDARIES.md` | Execution authority, default intake, non-coding autonomous work, treating conversation as approval |
| `V3-ANCHOR-006` | Codex SDK/MCP orchestration as governed worker runtime | Level 0 research | `research-only` | `CODEX_SDK_ORCHESTRATION_DIRECTION.md`; `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md` | `harness_profiles/HP_20260530_002_codex_subagent_workflows_research.md`; `harness_profiles/HP_20260601_004_codex_phase4_dynamic_evidence_export_candidate.md` | Start with read-only orchestration discovery/challenge evidence | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Unattended execution, production actions, credential use, runtime-control power, hidden governance replacement |
| `V3-ANCHOR-007` | Mission health and continuation judgment | Level 0 research lane | `research-only` | `ROADMAP_TO_FULL_VISION.md`; `PROMOTION_CRITERIA.md` | Later mission-health notes or decision packs when approved | Define advisory vocabulary before schema, validator, or gate proposals | `NON_GOALS_AND_BOUNDARIES.md`; `PROMOTION_CRITERIA.md` | Required checkpoint fields, routing authority, runtime-control power, schema promotion without evidence |

## Closeout Rule
When evidence changes an anchor's status, update this registry in the same change cycle as the source state docs or explicitly record why no registry update was needed.

Do not add a new anchor if it only restates project state. Add one only when it improves cold-start routing, points to source evidence, or names a future gate that a later model can safely prepare.
