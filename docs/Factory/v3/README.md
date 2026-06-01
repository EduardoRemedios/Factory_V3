# Factory v3

## Version
v1.22

## Change Log
- v1.22 (2026-06-01): Recorded the third Phase 4 negative-case capture candidate as a clarification-before-edit signal and moved the next research step toward dynamic/parallel evidence-export planning.
- v1.21 (2026-05-30): Generalized dynamic-workflow harness research to a capability class and added Codex as an official-docs `insufficient_evidence` sibling profile.
- v1.20 (2026-05-30): Added research-only Claude Code dynamic workflows harness profile and Phase 4 planning path with `insufficient_evidence` status.
- v1.19 (2026-05-28): Recorded two approved Phase 4 negative-case capture candidates that produced clean non-events and kept the Phase 3 natural negative-case gap open.
- v1.18 (2026-05-27): Recorded Codex Security scan follow-up hardening for advisory mission-record and telemetry replay validator false negatives.
- v1.17 (2026-05-27): Recorded the Phase 4 negative-case opportunity register and third happy-path real-run evidence pair.
- v1.16 (2026-05-27): Recorded Phase 4 corpus and harness-profile indexes plus the second happy-path real-run evidence pair.
- v1.15 (2026-05-27): Recorded the first Phase 4 real-run corpus result summary and harness capability profile.
- v1.14 (2026-05-27): Added Phase 4 real-run corpus capture plan and real-run result summary template.
- v1.13 (2026-05-26): Added Phase 4 eval expansion planning, the harness capability profile template, and synthetic operational-readiness fixture expansion.
- v1.12 (2026-05-26): Added the Phase 3 telemetry evidence review and conditional optional-advisory recommendation.
- v1.11 (2026-05-26): Recorded the third real advisory Phase 3 telemetry pilot and evidence-review prep.
- v1.10 (2026-05-26): Recorded the second real advisory Phase 3 telemetry pilot.
- v1.9 (2026-05-26): Recorded the first real advisory Phase 3 telemetry pilot.
- v1.8 (2026-05-26): Added the planning-only Phase 3 real mission telemetry capture plan.
- v1.7 (2026-05-26): Added the fixture-first advisory telemetry replay validator and deterministic fixtures.
- v1.6 (2026-05-26): Added the Phase 3 fixture-first telemetry/replay implementation approval.
- v1.5 (2026-05-26): Added the planning-only Phase 3 telemetry/replay plan.
- v1.4 (2026-05-26): Added the Phase 2.5 mission-record adoption decision recommending optional shadow use.
- v1.3 (2026-05-26): Added a fresh real pre-envelope fallback mission record for Phase 2.5 adoption evidence.
- v1.2 (2026-05-26): Started Phase 2.5 mission-record adoption evidence with backfilled real Factory V3 repository mission records.
- v1.1 (2026-05-25): Added a valid Phase 2 blocked-state shadow mission-record fixture and advisory blocked-state consistency checks.
- v1.0 (2026-05-25): Clarified that V2 is temporary build-support and fallback during V3 maturation, not a V3 product dependency; future V2 deprecation in this repo requires explicit V3 confidence and release evidence.
- v0.9 (2026-05-25): Added valid Phase 2 shadow mission-record fixtures for halted verification failure and stale reentry, plus advisory halted-state consistency checks.
- v0.8 (2026-05-24): Added the standalone advisory V3 mission-record validator, malformed-record fixtures, and deterministic expected outputs.
- v0.7 (2026-05-24): Added Phase 2 shadow mission-record v0 design and trial-derived JSON fixtures.
- v0.6 (2026-05-24): Added Phase 1 trial operating plan and trial index.
- v0.5 (2026-05-22): Added Phase 1 real-project trial capture template for `V3-OP-001` evidence collection.
- v0.4 (2026-05-22): Added roadmap pre-mortem and golden-fixture backlog for V3 operationalization.
- v0.3 (2026-05-22): Added vision and roadmap documents for the path from `V3-OP-001` to the full mission-governance runtime vision.
- v0.2 (2026-05-22): Updated status after optional `V3-OP-001` operational release approval and user-guide addition.
- v0.1 (2026-05-18): Initial research-only namespace for Factory v3 planning.

## Status
Factory v3 has one approved optional operational profile:

- `V3-OP-001 Bounded Code Change`

Approval is recorded at `OPERATIONAL_RELEASE_APPROVAL_V3_OP_001.md`.

This directory does not make Factory v3 the default mode, deprecate Factory v2, alter the `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> I2` planning pipeline, or change any required validator behavior.

At the current maturity level, Factory v2 remains supported and available as fallback.

The intended product direction for this dedicated repository is V3 independence: once V3 is built, confidence-backed, and explicitly approved, this repo may deprecate/remove V2 build-support scaffolding here. V2 remains preserved in the separate V2-only repository. Until that explicit release evidence exists, V2 fallback and non-deprecation language remains current.

The prior research and decision-prep evidence remains part of the approval basis; V3 docs remain non-enforcing for required repository gates unless a future integration run explicitly changes that.

## Purpose
This namespace captures Factory v3 operating guidance, release evidence, starter templates, and continuing research for mission-governed autonomous execution by coding agents.

## Current Scope
- Provide user guidance for optional `V3-OP-001` use.
- Provide starter templates for V3 mission envelopes, closeout, fallback review, and SIMPLE-CODE-GATE review.
- Preserve the external governance kernel and runtime-kernel boundary.
- Keep V2 fallback explicit.
- Capture evals, stress tests, pilot evidence, decision reports, and promotion criteria.
- Provide a shadow `V3_MISSION_RECORD` design and standalone advisory validator for Phase 2 replay and evidence-shape testing, including regression coverage for unsafe path shapes in self-attested scope evidence.
- Provide an advisory telemetry replay validator with regression coverage for duplicate telemetry event IDs, missing terminal replay events, unsafe path shapes in self-attested scope evidence, and excluded-data markers.
- Track research-only dynamic/parallel workflow harness planning with `insufficient_evidence` status until local Factory V3 evidence exists; Claude Code is an external-announcement signal and Codex is an official-docs source signal.
- Continue research for any future V3 profile before promotion.

## Non-authority Rule
Files in this directory are authoritative only for the approved optional `V3-OP-001` profile unless a future release explicitly promotes another profile.

They do not change:
- `docs/Factory/ORCHESTRATION.md`
- `docs/Factory/Spec/STAGE_CONTRACTS.md`
- `docs/Factory/Spec/DEFINITIONS.md`
- `scripts/factory_stage_lint.py`
- `scripts/factory_pack_lint.py`
- `scripts/knowledge_lint.sh`

They also do not approve payment, authentication, compliance, production deployment, infrastructure authority, runtime-kernel authority, or production action mediation.

## Relationship To External Governance Kernels
Factory v3 should be compatible with external governance kernels but does not require one.

If an adopting repository uses a separate lower-level autonomy governance kernel, Factory should act as the SDLC mission-governance profile for coding work while the kernel remains the runtime authority and proof layer.

If an adopting repository does not use a separate governance kernel, Factory v2 and optional `V3-OP-001` remain usable without one.

## Approved Profile
Use `V3-OP-001` only for bounded code-changing work where:

- the objective is clear,
- files or modules can be named,
- commands and verification are known,
- dependencies are authorized,
- V2 fallback triggers are explicit,
- no payment, authentication, compliance, deployment, runtime-kernel, or infrastructure concern is implicated.

Start with `USER_GUIDE.md`.

## Promotion Rule
Any V3 profile beyond `V3-OP-001`, any default-mode promotion, or any required-gate integration requires evidence, human approval, and Factory governance.

## Key Research Artifacts
- `VISION.md`
- `ROADMAP_TO_FULL_VISION.md`
- `ROADMAP_PREMORTEM.md`
- `MISSION_RECORD_DESIGN_V0.md`
- `PHASE3_TELEMETRY_REPLAY_PLAN.md`
- `PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_APPROVAL.md`
- `PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_STATUS.md`
- `PHASE3_REAL_MISSION_TELEMETRY_CAPTURE_PLAN.md`
- `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`
- `PHASE4_EVAL_EXPANSION_PLAN.md`
- `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md`
- `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`
- `PHASE1_DECISION_REVIEW_V3_OP_001.md`
- `PHASE1_TRIAL_PLAN.md`
- `USER_GUIDE.md`
- `OPERATIONAL_RELEASE_APPROVAL_V3_OP_001.md`
- `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`
- `OPERATIONAL_READINESS_DECISION_REPORT_V3_OP_001.md`
- `STRATEGY.md`
- `NON_GOALS_AND_BOUNDARIES.md`
- `PROMOTION_CRITERIA.md`
- `OPERATIONAL_READINESS_EVAL_PLAN.md`
- `OPERATIONAL_READINESS_DECISION_REPORT_TEMPLATE.md`
- `templates/`

## Phase 1 Trial Capture
Use `PHASE1_TRIAL_PLAN.md` to run the first real-project trial batch.

Use `templates/V3_PHASE1_TRIAL_CAPTURE_TEMPLATE.md` for real-project `V3-OP-001` trials.

The template is designed to capture fallback decisions, user friction, advisory false positives and false negatives, SIMPLE-CODE-GATE evidence, and roadmap pre-mortem watchpoints before Phase 2 structured mission records are designed.

Track trial records in `trials/TRIAL_INDEX.md`.

## Phase 2 Shadow Mission Records
Phase 2 shadow mission-record design is approved only as research and replay work.

Use:

- `MISSION_RECORD_DESIGN_V0.md`
- `templates/V3_MISSION_RECORD_TEMPLATE.json`
- `tests/fixtures/factory_v3_mission_record/`
- `mission_records/`
- `PHASE2_5_MISSION_RECORD_ADOPTION_STATUS.md`
- `scripts/factory_v3_mission_record_lint.py`

The v0 record captures pre-envelope fallback, thread-local mission envelopes, bounded authority, command evidence, verification, halt/fallback review, SIMPLE-CODE-GATE review, and Phase 2 design signals.

The validator is standalone and advisory. It emits `blocking_effect: none`, supports deterministic `--expect` fixture checks, and is not wired into required Factory gates.

It does not approve enforcement, required gates, runtime authority, telemetry, governance routing, or new V3 profiles.

Valid shadow fixtures now include completed, pre-envelope fallback, halted verification-failure, halted stale-reentry, and blocked missing-authority examples. The halted and blocked fixtures are synthetic Phase 2 design examples, not operational promotion evidence.

Phase 2.5 adoption evidence now lives under `mission_records/`. These records include real V3 repository backfills and a fresh pre-envelope fallback decision for replayability evaluation, still advisory and non-blocking.

Phase 2.5 decision evidence is recorded at `PHASE2_5_MISSION_RECORD_ADOPTION_DECISION.md`. The decision recommends optional shadow mission-record use and allows Phase 3 telemetry/replay planning, but does not approve telemetry implementation or required gates.

## Phase 3 Telemetry And Evidence Replay
Phase 3 planning is recorded at `PHASE3_TELEMETRY_REPLAY_PLAN.md`.

The plan defines a future minimal event model, excluded data, fixture shape, replay checks, and data-minimization rules. It is planning-only and does not implement telemetry, replay validators, required gates, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, or V2 scaffolding removal.

Phase 3 implementation approval is recorded at `PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_APPROVAL.md`. It approves only the next fixture-first advisory replay-validator implementation step, with exact files and verification commands. It does not approve real mission telemetry collection, required gates, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, or V2 scaffolding removal.

Initial Phase 3 fixture-first implementation status is recorded at `PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_STATUS.md`. The standalone validator `scripts/factory_v3_telemetry_replay_lint.py` checks synthetic JSONL fixtures under `tests/fixtures/factory_v3_telemetry_replay/` and emits `blocking_effect: none`.

Real mission telemetry capture planning is recorded at `PHASE3_REAL_MISSION_TELEMETRY_CAPTURE_PLAN.md`. It defines the future pilot storage shape, event subset, redaction rules, operator workflow, overhead capture, and stop conditions, but adds no real telemetry logs and authorizes no enforcement.

The first three real advisory telemetry pilots are recorded under `telemetry/pilots/` and linked to shadow mission records:

- `PILOT_20260526_001_phase3_status_update/` links to `mission_records/MR_20260526_004_first_real_telemetry_pilot.json`.
- `PILOT_20260526_002_replay_fixture_maintenance/` links to `mission_records/MR_20260526_005_second_real_telemetry_pilot.json`.
- `PILOT_20260526_003_evidence_review_prep/` links to `mission_records/MR_20260526_006_third_real_telemetry_pilot.json`.

They remain optional, research-only, and non-enforcing. The third pilot records that no natural halted, fallback, or clarification-heavy case occurred; this is a gap for evidence review, not negative-case evidence.

Phase 3 evidence review is recorded at `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`. The review recommends optional advisory telemetry only for selected narrow `V3-OP-001` evidence-gathering missions and only with explicit conditions. It does not recommend routine required telemetry, telemetry completeness enforcement, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal. The missing natural halted/fallback/clarification-heavy pilot remains a gap to carry into Phase 4 planning and later evidence collection.

## Phase 4 Eval Expansion And Capability Profiling
Phase 4 planning is recorded at `PHASE4_EVAL_EXPANSION_PLAN.md`.

The harness capability profile template exists at `templates/V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md`.

Initial synthetic Phase 4 operational-readiness fixture expansion exists under `tests/fixtures/factory_v3_operational_readiness_eval/cases/` with `V3-P4-*` cases for capability profile completeness, execution reliability, scope discipline, verification quality, interruption recovery, evidence quality, false-positive/false-negative rollup shape, and advisory threshold wording.

These fixtures are synthetic design coverage only. They are not real negative-case telemetry evidence, do not approve governance routing, and do not reduce V2 governance. The missing natural halted/fallback/clarification-heavy telemetry case remains a Phase 4 evidence gap.

The Phase 4 real-run corpus index is `real_run_corpus/INDEX.md`; the harness-profile index is `harness_profiles/INDEX.md`.

The first separately approved Phase 4 real-run corpus record is `real_run_corpus/RR_20260527_001_phase4_candidate_status_update.md`, with matching harness profile `harness_profiles/HP_20260527_001_codex_phase4_candidate_status_update.md`.

The second separately approved Phase 4 real-run corpus record is `real_run_corpus/RR_20260527_002_phase4_corpus_index_update.md`, with matching harness profile `harness_profiles/HP_20260527_002_codex_phase4_corpus_index_update.md`.

The third separately approved Phase 4 real-run corpus record is `real_run_corpus/RR_20260527_003_phase4_negative_case_opportunity_register.md`, with matching harness profile `harness_profiles/HP_20260527_003_codex_phase4_negative_case_opportunity_register.md`.

The first approved Phase 4 negative-case capture candidate record is `real_run_corpus/RR_20260528_001_phase4_advisory_threshold_wording.md`, with matching harness profile `harness_profiles/HP_20260528_001_codex_phase4_advisory_threshold_wording.md`. It produced a clean advisory FP/FN non-event with `NO_TELEMETRY`.

The second approved Phase 4 negative-case capture candidate record is `real_run_corpus/RR_20260528_002_phase4_verification_halt_fixture.md`, with matching harness profile `harness_profiles/HP_20260528_002_codex_phase4_verification_halt_fixture.md`. It produced a clean verification-halt non-event with `NO_TELEMETRY`.

The third approved Phase 4 negative-case capture candidate record is `real_run_corpus/RR_20260530_003_phase4_clarification_heavy_candidate.md`, with matching harness profile `harness_profiles/HP_20260530_003_codex_phase4_clarification_heavy_candidate.md`. It produced a natural clarification-before-edit signal with `NO_TELEMETRY`; broad roadmap/status edits and optional telemetry were not performed because exact target files and telemetry authority were not explicit after Go.

The Phase 4 negative-case opportunity register is `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`.

The dynamic/parallel workflows research plan is `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md`, with initial Claude Code profile `harness_profiles/HP_20260530_001_claude_code_dynamic_workflows_research.md` and Codex subagent-workflows profile `harness_profiles/HP_20260530_002_codex_subagent_workflows_research.md`. Both have evidence band `insufficient_evidence`; the Claude profile is external-announcement-driven research context, and the Codex profile is official-docs-driven research context. They do not authorize dynamic-workflow execution, routing, governance reduction, required gates, profile promotion, or V2 build-support removal.

The first three records are happy-path docs-only evidence with `NO_TELEMETRY`, the first two approved negative-case candidates are clean non-events with `NO_TELEMETRY`, and the third approved negative-case candidate is a clarification-before-edit signal with `NO_TELEMETRY`. They narrow the clarification evidence gap but do not close telemetry, failed-verification halt, fallback, recovery, or routing-threshold gaps and do not support governance routing, reduced governance, required gates, default-mode behavior, V3 promotion, or V2 build-support removal.

The next Phase 4 step should prefer separately planned `P4-NEG-OPP-006` dynamic/parallel evidence-export research from the opportunity register. Do not execute any local dynamic/parallel workflow without a separate Factory V2-governed candidate plan, explicit approval, exact file authority, summary-only evidence rules, and V2 fallback triggers.

Real-run corpus capture planning is recorded at `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`.

Use `templates/V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md` for future result summaries after a specific `V3-OP-001` evidence mission is separately approved.

The capture plan does not authorize live mission execution, telemetry collection, routing, reduced governance, required gates, runtime authority, proof, leases, default-mode behavior, V3 promotion, or V2 build-support removal.

## Advisory Eval Tooling
- `scripts/factory_v3_advisory_lint.py` checks research-posture and promotion-evidence drift in V3 docs.
- `scripts/factory_v3_operational_readiness_eval.py` checks standalone operational-readiness fixture scenarios, including Phase 4 synthetic fixture triggers, and emits advisory-only reports.
- `scripts/factory_v3_mission_record_lint.py` checks shadow V3 mission-record JSON files and malformed-record fixtures in advisory mode.
- `scripts/factory_v3_telemetry_replay_lint.py` checks synthetic telemetry replay JSONL fixtures in advisory mode.
- These tools are not wired into required Factory v2 gates and do not authorize broader V3 promotion.
