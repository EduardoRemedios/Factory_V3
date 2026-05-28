# Sprint Envelope: SPRINT_20260528_0604_PHASE4_NEGATIVE_CAPTURE_PLAN

## Version
v0.2

## Change Log
- v0.2 (2026-05-28): Hardened after envelope red-team review.
- v0.1 (2026-05-28): Initial Stage H envelope.

## Sprint ID
- `SPRINT_20260528_0604_PHASE4_NEGATIVE_CAPTURE_PLAN`

## Execution Mode
- PLANNING_ONLY for this run.
- Future real-run capture requires explicit user Go naming `P4-NEG-CAPTURE-CANDIDATE-001`.

## Objective
Prepare a bounded future negative-case capture candidate from `P4-NEG-OPP-005` without executing it.

## Candidate Selection Rationale
- `P4-NEG-OPP-005` is the narrowest first candidate because it can use a docs-only `V3-OP-001` update with known advisory verification commands.
- Promotion-adjacent threshold wording has a natural chance to produce advisory FP/FN adjudication without seeding a failure.
- The candidate can also record cleanly if no halt, fallback, clarification, stale reentry, evidence weakness, verification weakness, or scope pressure occurs.

## Future File-touch Budget
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`: optional narrow advisory wording/status update only.
- `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`: optional candidate-status note only.
- `docs/Factory/v3/real_run_corpus/INDEX.md`: add one future result-summary row only.
- `docs/Factory/v3/harness_profiles/INDEX.md`: add one future harness-profile row only.
- `docs/Factory/v3/real_run_corpus/RR_<dated>_001_phase4_advisory_threshold_wording.md`: new future result summary after execution.
- `docs/Factory/v3/harness_profiles/HP_<dated>_001_codex_phase4_advisory_threshold_wording.md`: new future harness profile after execution.
- No scripts, validators, fixtures, CI, gates, telemetry completeness checks, router files, runtime files, proof files, lease files, or V2 removal files.

## Evidence Artifacts Expected Later
- Candidate approval note or equivalent human Go.
- Command and verification summaries with exit status.
- Advisory eval output and human FP/FN adjudication.
- Halt, fallback, clarification, stale-reentry, evidence-quality, verification-quality, or scope-discipline observation notes if naturally present.
- Clean non-event note if none of those behaviors occur.
- Result summary and harness capability profile.

## Success Criteria
- Future candidate stays within `V3-OP-001`, named files, and known verification.
- Future records preserve advisory-only, non-promotion, and V2 fallback language.
- Advisory findings are adjudicated by a human.
- Phase 3 gap is closed only by real natural halted, fallback, or clarification-heavy evidence; otherwise it remains open.

## Non-success Criteria
- Execution approval is missing.
- Candidate becomes broad, ambiguous, or tooling-related.
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
- A natural halt/fallback/clarification signal is ignored instead of recorded.
- Advisory evidence is used as authority.
- Any output weakens Factory V2 fallback or claims V2 deprecation.
