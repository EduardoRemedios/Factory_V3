# Verification Plan: Phase 4 Dynamic/Parallel Evidence-export Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-01): Initial Stage F verification plan.

## Verification Tiers
- V0 artifact proof: required planning artifacts exist and are internally linked.
- V1 static/mechanical: stage-lint, pack-lint, and `git diff --check`.
- V2 focused advisory checks: V3 advisory lint and operational-readiness docs eval.
- V3 fixture stability: mission-record and telemetry replay fixture expected-output checks.

## Required Planning Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl stage-lint --run RUN_20260601_0635_v3_phase4_dynamic_evidence_export_plan --stage <STAGE>`
- `./scripts/factoryctl pack-lint --run RUN_20260601_0635_v3_phase4_dynamic_evidence_export_plan`
- `git diff --check`

## Future Candidate Verification
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --expect tests/fixtures/factory_v3_mission_record/expected/all.json --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `git diff --check`

## Future Evidence Review Checks
- Confirm harness was explicitly named and locally available.
- Confirm evidence artifacts are summary-only and contain no excluded data.
- Confirm subtask/work-partition evidence is present or the absence is recorded as a gap.
- Confirm file touches, commands, verification, human decisions, and residual risks are replayable.
- Confirm no routing, enforcement, telemetry completeness, runtime authority, proof, lease, default-mode, V3 promotion, or V2-removal language was introduced.

## Halt Rules
- Halt if future approval does not name exact harness, scope, commands, evidence artifacts, and telemetry decision.
- Halt if the dynamic/parallel harness cannot expose enough safe evidence and no human decision authorizes an alternate closeout.
- Halt if future verification fails without a human decision, fallback, or closeout.
- Halt if future output implies routing, enforcement, required gates, default-mode behavior, telemetry completeness, V3 promotion, or V2 removal.

## Exit Criteria Status
- PASS
