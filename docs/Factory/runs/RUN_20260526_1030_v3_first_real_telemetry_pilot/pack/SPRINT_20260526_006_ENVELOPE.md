# Sprint Envelope

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Envelope for first real telemetry pilot.

## Sprint ID
SPRINT_20260526_006

## Execution Mode
EXECUTION_ENABLED

## Authorized Files
- `CHANGELOG.md`
- `docs/CHANGELOG.md`
- `docs/ROADMAP.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_STATUS.md`
- `docs/Factory/v3/mission_records/MR_20260526_004_first_real_telemetry_pilot.json`
- `docs/Factory/v3/telemetry/pilots/PILOT_20260526_001_phase3_status_update/V3_TELEMETRY.jsonl`
- `docs/Factory/v3/telemetry/pilots/PILOT_20260526_001_phase3_status_update/OVERHEAD.md`
- `docs/Factory/v3/telemetry/pilots/PILOT_20260526_001_phase3_status_update/REDACTION_REVIEW.md`
- `docs/Factory/v3/telemetry/pilots/PILOT_20260526_001_phase3_status_update/REPLAY_REPORT.json`
- `docs/Factory/runs/RUN_20260526_1030_v3_first_real_telemetry_pilot/**`

## Allowed Commands
- V2 stage and pack lint.
- V3 advisory, operational-readiness, mission-record, and telemetry replay validators.
- Python compile checks for existing V3 advisory scripts.
- JSON formatting checks for changed JSON files.
- Git diff hygiene checks.

## File-Touch Budget
- Mission record: 1 JSON file.
- Telemetry pilot: 4 files.
- Status, roadmap, and changelog docs: up to 6 files.
- V2 run evidence: this run directory only.

## Forbidden Scope
- No script changes.
- No fixture expected-output changes.
- No dependency changes.
- No CI, `factoryctl`, or required-gate wiring.
- No runtime authority, proof, lease enforcement, governance routing, default-mode behavior, or V2 scaffolding removal.

## Verification
Use `pack/verification_plan.md` and `pack/verification_manifest.yaml`.

## SIMPLE-CODE-GATE
Use the smallest doc/data change that records the pilot. Do not add abstractions, dependencies, or broad process changes.

## Exit Criteria
PASS if the pilot artifacts exist, advisory checks pass, and telemetry remains optional and non-enforcing.
