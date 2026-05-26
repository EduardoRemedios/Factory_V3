# Execution Prompt - SPRINT_20260526_004

## Objective
Execute the approved fixture-first advisory telemetry replay validator implementation.

## Required Reading
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/Factory/ORCHESTRATION.md`
- `docs/Factory/Spec/STAGE_CONTRACTS.md`
- `docs/Factory/v3/PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_APPROVAL.md`
- `docs/Factory/runs/RUN_20260526_0948_v3_telemetry_replay_validator/pack/SPRINT_20260526_004_ENVELOPE.md`
- `docs/Factory/runs/RUN_20260526_0948_v3_telemetry_replay_validator/pack/verification_plan.md`

## Constraints
- Keep validator standalone and advisory.
- Emit `blocking_effect: none`.
- Use synthetic fixtures only.
- Do not collect real mission telemetry.
- Do not wire into CI, `factoryctl`, or required gates.
- Do not add runtime authority, proof, lease enforcement, governance routing, default-mode behavior, or V2 scaffolding removal.

## Verification
Run the checks in `pack/verification_manifest.yaml` plus any relevant V3 advisory commands before closeout.
