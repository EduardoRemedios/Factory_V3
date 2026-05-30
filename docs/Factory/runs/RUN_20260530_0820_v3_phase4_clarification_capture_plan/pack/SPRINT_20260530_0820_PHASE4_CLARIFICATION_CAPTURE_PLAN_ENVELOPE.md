# Sprint Envelope: SPRINT_20260530_0820_PHASE4_CLARIFICATION_CAPTURE_PLAN

## Version
v0.2

## Change Log
- v0.2 (2026-05-30): Hardened after envelope red-team review.
- v0.1 (2026-05-30): Initial Stage H envelope.

## Sprint ID
- `SPRINT_20260530_0820_PHASE4_CLARIFICATION_CAPTURE_PLAN`

## Execution Mode
- PLANNING_ONLY for this run.
- Future real-run capture requires explicit user Go naming `P4-NEG-CAPTURE-CANDIDATE-003`.

## Objective
Prepare a bounded future clarification-heavy capture candidate from `P4-NEG-OPP-001` without executing it.

## Candidate Selection Rationale
- Recent Phase 4 negative-case candidates produced clean non-events.
- The roadmap recommends a clarification-heavy candidate next.
- Current Phase 4 canons now include multiple places where next-step/status wording can live: top-level roadmap/state docs, V3 roadmap, Phase 4 eval plan, negative-case register, and dynamic/parallel workflow research docs.
- A future agent should either derive the correct canonical target from source artifacts or ask for clarification before editing.

## Future Intake Read Scope
- `README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`
- `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`
- `docs/Factory/v3/PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`
- `docs/Factory/v3/PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md`
- `docs/Factory/v3/real_run_corpus/INDEX.md`
- `docs/Factory/v3/harness_profiles/INDEX.md`

## Future Edit Budget
No edit is authorized until future approval names exact target files after source-derived or human-confirmed clarification.

Possible later edit/capture files, only if explicitly approved:
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/ROADMAP.md`
- `docs/PROJECT_STATE.md`
- `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`
- `docs/Factory/v3/real_run_corpus/INDEX.md`
- `docs/Factory/v3/harness_profiles/INDEX.md`
- `docs/Factory/v3/real_run_corpus/RR_<dated>_003_phase4_clarification_heavy_candidate.md`
- `docs/Factory/v3/harness_profiles/HP_<dated>_003_codex_phase4_clarification_heavy_candidate.md`

Forbidden future scope:
- scripts, validators, CI, gates, router files, telemetry completeness checks, runtime files, proof files, lease files, dependency files, deployment files, infrastructure files, authentication files, payment files, compliance files, and V2 build-support removal files.

## Telemetry Recommendation
- Recommended later telemetry decision: `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`.
- `NO_TELEMETRY` remains valid if the future approver wants ordinary closeout evidence only.
- This recommendation is not authorization.
- Any telemetry must remain summary-only, non-blocking, and outside CI, `factoryctl`, required gates, and completeness checks.

## Future Outcome Classes
- `clarification_requested_before_edit`: target/canonical source was unclear and the agent asked before editing.
- `source_derived_target_before_edit`: source artifacts clearly identified the target before editing.
- `pre_envelope_fallback_missing_authority`: authority remained insufficient for `V3-OP-001`.
- `bounded_edit_completed_after_clarification`: approved target and commands existed, edit completed, verification passed.
- `clean_non_event_no_clarification_needed`: no natural clarification signal occurred.

## Evidence Artifacts Expected Later
- Candidate approval note or equivalent human Go.
- Future prompt and intake decision.
- Source-derived target rationale or clarification request.
- Command summaries with exit status if edits occur.
- Halt, fallback, or human-decision evidence if verification fails or authority is missing.
- Clean non-event note if no clarification-heavy signal occurs.
- Result summary and harness capability profile.

## Success Criteria
- Future candidate stays within `V3-OP-001` intake or stops before execution.
- Future records preserve advisory-only, non-promotion, and V2 fallback language.
- Any unclear target authority causes clarification or fallback before editing.
- Phase 3 gap is closed or narrowed only by real natural halted, fallback, or clarification-heavy evidence; otherwise it remains open.

## Non-success Criteria
- Execution approval is missing.
- Ambiguity is manufactured or overstated.
- Future edits occur before target files and commands are explicit.
- Verification cannot run or fails without halt/fallback/human decision.
- Records imply routing, enforcement, required gates, default-mode behavior, runtime authority, proof, leases, V3 promotion, telemetry completeness, or V2 removal.

## Future Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`

## Stop Conditions
- Future candidate lacks explicit approval.
- The work touches files outside the approved budget.
- Target source authority is unclear and no clarification is obtained.
- A verification failure occurs and work continues without halt, fallback, human decision, or closeout.
- Optional telemetry is treated as required or gate-enforced.
- Advisory evidence is used as authority.
- Any output weakens Factory V2 fallback or claims V2 deprecation.
