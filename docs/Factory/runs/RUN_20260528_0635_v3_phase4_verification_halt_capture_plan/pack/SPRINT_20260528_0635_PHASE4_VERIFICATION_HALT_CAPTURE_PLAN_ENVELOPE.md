# Sprint Envelope: SPRINT_20260528_0635_PHASE4_VERIFICATION_HALT_CAPTURE_PLAN

## Version
v0.2

## Change Log
- v0.2 (2026-05-28): Hardened after envelope red-team review.
- v0.1 (2026-05-28): Initial Stage H envelope.

## Sprint ID
- `SPRINT_20260528_0635_PHASE4_VERIFICATION_HALT_CAPTURE_PLAN`

## Execution Mode
- PLANNING_ONLY for this run.
- Future real-run capture requires explicit user Go naming `P4-NEG-CAPTURE-CANDIDATE-002`.

## Objective
Prepare a bounded future verification-halt capture candidate from `P4-NEG-OPP-002` without executing it.

## Candidate Selection Rationale
- `P4-NEG-OPP-002` best targets the open Phase 3 gap because deterministic fixture maintenance can naturally produce a failed check.
- `V3-P4-VERIFY-001` already exists as Phase 4 verification-quality fixture coverage and has an expected-output check.
- The `--expect` command provides a clear halt point if fixture or expected-output maintenance creates a mismatch.

## Future File-touch Budget
- `tests/fixtures/factory_v3_operational_readiness_eval/cases/V3-P4-VERIFY-001/input.md`: narrow fixture text maintenance only.
- `tests/fixtures/factory_v3_operational_readiness_eval/expected.json`: matching expected-output maintenance only.
- `docs/Factory/v3/real_run_corpus/INDEX.md`: add one future result-summary row only.
- `docs/Factory/v3/harness_profiles/INDEX.md`: add one future harness-profile row only.
- `docs/Factory/v3/real_run_corpus/RR_<dated>_002_phase4_verification_halt_fixture.md`: new future result summary after execution.
- `docs/Factory/v3/harness_profiles/HP_<dated>_002_codex_phase4_verification_halt_fixture.md`: new future harness profile after execution.
- No scripts, validators, CI, gates, telemetry completeness checks, router files, runtime files, proof files, lease files, or V2 removal files.

## Telemetry Recommendation
- Recommended later telemetry decision: `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`.
- This recommendation is not authorization. Later execution approval must confirm telemetry mode.
- Any telemetry must remain summary-only, non-blocking, and outside CI, `factoryctl`, required gates, and completeness checks.

## Evidence Artifacts Expected Later
- Candidate approval note or equivalent human Go.
- Pre-edit and post-edit command summaries with exit status.
- `--expect` verification result.
- Halt, fallback, or human-decision evidence if verification fails.
- Clean non-event note if verification passes.
- Result summary and harness capability profile.

## Success Criteria
- Future candidate stays within `V3-OP-001`, named files, and known verification.
- Future records preserve advisory-only, non-promotion, and V2 fallback language.
- Any failed verification halts work until decision, fallback, or closeout.
- Phase 3 gap is closed only by real natural halted, fallback, or clarification-heavy evidence; otherwise it remains open.

## Non-success Criteria
- Execution approval is missing.
- Verification failure is seeded or manufactured.
- Verification cannot run or fails without halt/fallback/human decision.
- Records imply routing, enforcement, required gates, default-mode behavior, runtime authority, proof, leases, V3 promotion, telemetry completeness, or V2 removal.

## Future Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`

## Stop Conditions
- Future candidate lacks explicit approval.
- The work touches files outside the approved budget.
- A verification failure occurs and work continues without halt, fallback, human decision, or closeout.
- Optional telemetry is treated as required or gate-enforced.
- Advisory evidence is used as authority.
- Any output weakens Factory V2 fallback or claims V2 deprecation.
