# Raw Brief: Factory V3 Phase 4 Negative-case Capture Plan

## Execution Mode
PLANNING_ONLY

## Request
Plan the first narrow Phase 4 negative-case real-run capture candidate from `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`.

## Current State
- Factory V3 has one approved optional operational profile: `V3-OP-001 Bounded Code Change`.
- Phase 4 eval expansion and capability profiling are in progress.
- Three happy-path docs-only Phase 4 real-run corpus records exist with matching harness profiles.
- The Phase 4 negative-case opportunity register exists as a research-only planning aid.
- The Phase 3 evidence gap remains open: no natural halted, fallback, or clarification-heavy telemetry pilot has been captured.
- The advisory mission-record and telemetry replay validators have recent evidence-integrity hardening, but they remain advisory and non-blocking.

## Candidate To Plan
Plan, but do not execute, the first negative-case capture candidate:

- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-001`
- Source opportunity: `P4-NEG-OPP-005`
- Natural signal to watch: advisory false-positive or false-negative behavior around wording close to promotion, routing, or threshold language.
- Profile: `V3-OP-001 Bounded Code Change`
- Mission shape: narrow docs-only advisory wording/status update with known verification.
- Optional telemetry decision for this planning pack: not approved; the later execution approval must choose `NO_TELEMETRY` or `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`.
- Expected evidence if later approved: one result summary, one harness capability profile, advisory eval output, FP/FN human adjudication, halt/fallback/clarification observation notes, and a clean non-event record if no negative-case behavior naturally occurs.

## Strict Scope
- Do not execute the real-run capture in this run.
- Do not implement new tooling.
- Do not collect telemetry.
- Do not create the future real-run result summary or harness profile in this run.
- Do not add governance routing, enforcement, required gates, CI wiring, telemetry completeness checks, default-mode behavior, runtime authority, proof, lease enforcement, V3 promotion, or Factory V2 build-support removal.
- Preserve V3 as advisory/optional.
- Preserve Factory V2 fallback and non-deprecation language.
- Apply SIMPLE-CODE-GATE: smallest clear change, no dependency creep, no broad abstractions, no silent failures.

## Expected Future Execution Scope
If later approved, the candidate mission may touch only:
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`
- `docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`
- `docs/Factory/v3/real_run_corpus/INDEX.md`
- `docs/Factory/v3/harness_profiles/INDEX.md`
- `docs/Factory/v3/real_run_corpus/RR_<future>_001_phase4_advisory_threshold_wording.md`
- `docs/Factory/v3/harness_profiles/HP_<future>_001_codex_phase4_advisory_threshold_wording.md`

The future candidate should not manufacture a failure. It should capture advisory FP/FN, halt, fallback, clarification-heavy, stale-reentry, evidence-quality, verification-quality, or scope-discipline signals only if they naturally occur. If none occur, it must record a clean non-event and keep the Phase 3 gap open.

## Verification Commands
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl context-report --profile stage-a --scope RUN_20260528_0604_v3_phase4_negative_case_capture_plan --output docs/Factory/runs/RUN_20260528_0604_v3_phase4_negative_case_capture_plan/CONTEXT_RECALL_REPORT.md`
- `./scripts/factoryctl stage-lint --run RUN_20260528_0604_v3_phase4_negative_case_capture_plan --stage <STAGE>` for A, B, C, D, E, F, G, H, I, J, I2
- `./scripts/factoryctl pack-lint --run RUN_20260528_0604_v3_phase4_negative_case_capture_plan`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`
