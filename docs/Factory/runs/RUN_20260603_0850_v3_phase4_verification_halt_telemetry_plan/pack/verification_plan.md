# Verification Plan: Phase 4 Verification-halt Telemetry Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-03): Initial Stage F verification plan.

## Verification Tiers
- V0 artifact proof: required planning artifacts exist and are internally linked.
- V1 static/mechanical: stage-lint, pack-lint, and `git diff --check`.
- V2 focused advisory checks: V3 advisory lint and operational-readiness docs eval.
- V3 fixture stability: mission-record and telemetry replay fixture expected-output checks.

## Required Planning Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl stage-lint --run RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan --stage <STAGE>`
- `./scripts/factoryctl pack-lint --run RUN_20260603_0850_v3_phase4_verification_halt_telemetry_plan`
- `git diff --check`

## Future Candidate Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target tests/fixtures/factory_v3_operational_readiness_eval --expect tests/fixtures/factory_v3_operational_readiness_eval/expected.json --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`

## Future Evidence Review Checks
- Confirm harness was explicitly named and locally available.
- Confirm exact fixture and expected-output files were approved before edits.
- Confirm any expected-output change is explained by a real approved input change.
- Confirm evidence artifacts are summary-only and contain no excluded data.
- Confirm file touches, commands, verification, human decisions, and residual risks are replayable.
- Confirm a failed verification halted work until human decision, fallback, or closeout.
- Confirm a passing verification is recorded as a clean non-event, not as closed halt/fallback evidence.
- Confirm no routing, enforcement, telemetry completeness, runtime authority, proof, lease, default-mode, V3 promotion, or V2-removal language was introduced.

## Halt Rules
- Halt if future approval does not name exact harness, scope, commands, evidence artifacts, and telemetry decision.
- Halt if the future edit would require files outside the approved fixture/expected-output budget.
- Halt if future verification fails without a human decision, fallback, or closeout.
- Halt if future output implies routing, enforcement, required gates, default-mode behavior, telemetry completeness, V3 promotion, or V2 removal.

## Exit Criteria Status
- PASS
