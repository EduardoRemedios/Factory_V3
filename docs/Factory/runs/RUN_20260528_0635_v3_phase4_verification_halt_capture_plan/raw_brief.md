# Raw Brief: Factory V3 Phase 4 Verification-halt Capture Plan

## Execution Mode
PLANNING_ONLY

## Request
Plan the second Phase 4 negative-case real-run capture candidate from `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`.

## Current State
- Factory V3 has one approved optional operational profile: `V3-OP-001 Bounded Code Change`.
- Phase 4 real-run corpus contains three happy-path docs-only records and one approved advisory-threshold clean non-event.
- The Phase 4 negative-case opportunity register remains research-only and non-enforcing.
- The Phase 3 evidence gap remains open: no natural halted, fallback, or clarification-heavy telemetry pilot has been captured.
- Advisory validators remain advisory and non-blocking.

## Candidate To Plan
Plan, but do not execute, the second negative-case capture candidate:

- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-002`
- Source opportunity: `P4-NEG-OPP-002`
- Natural signal to watch: verification halt during deterministic fixture or expected-output maintenance.
- Profile: `V3-OP-001 Bounded Code Change`
- Mission shape: narrow maintenance of the existing `V3-P4-VERIFY-001` operational-readiness fixture and expected-output corpus.
- Optional telemetry recommendation: `OPTIONAL_ADVISORY_TELEMETRY_APPROVED` for the later execution decision, because this candidate is aimed at the missing halt/fallback/clarification evidence gap; no telemetry is collected by this planning run.
- Expected evidence if later approved: command evidence for operational-readiness eval with `--expect`, halt/fallback/human-decision record if verification fails, clean non-event record if verification passes, one result summary, and one harness capability profile.

## Strict Scope
- Do not execute the real-run capture in this run.
- Do not modify fixtures or expected outputs in this run.
- Do not collect telemetry in this run.
- Do not create the future real-run result summary or harness profile in this run.
- Do not implement tooling.
- Do not add governance routing, enforcement, required gates, CI wiring, telemetry completeness checks, default-mode behavior, runtime authority, proof, lease enforcement, V3 promotion, or Factory V2 build-support removal.
- Preserve V3 as advisory/optional.
- Preserve Factory V2 fallback and non-deprecation language.
- Apply SIMPLE-CODE-GATE: smallest clear change, no dependency creep, no broad abstractions, no silent failures.

## Expected Future Execution Scope
If later approved, the candidate mission may touch only:
- `tests/fixtures/factory_v3_operational_readiness_eval/cases/V3-P4-VERIFY-001/input.md`
- `tests/fixtures/factory_v3_operational_readiness_eval/expected.json`
- `docs/Factory/v3/real_run_corpus/INDEX.md`
- `docs/Factory/v3/harness_profiles/INDEX.md`
- `docs/Factory/v3/real_run_corpus/RR_<future>_002_phase4_verification_halt_fixture.md`
- `docs/Factory/v3/harness_profiles/HP_<future>_002_codex_phase4_verification_halt_fixture.md`

The future candidate must not manufacture a failure. If verification fails naturally after fixture or expected-output maintenance, execution must halt until a human decision, fallback, or closeout is recorded. If verification passes, it must record a clean non-event and keep the Phase 3 gap open.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260528_0635_v3_phase4_verification_halt_capture_plan --output docs/Factory/runs/RUN_20260528_0635_v3_phase4_verification_halt_capture_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260528_0635_v3_phase4_verification_halt_capture_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260528_0635_v3_phase4_verification_halt_capture_plan`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`
