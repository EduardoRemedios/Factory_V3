# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Intent for first real telemetry pilot.

## Purpose
Capture the first real advisory Phase 3 telemetry pilot for a small docs-only `V3-OP-001` mission.

## Goal
Create one mission record, one pilot telemetry directory, and status/roadmap updates showing that pilot 1 of the Phase 3 capture set exists.

## Non-goals
- No telemetry enforcement.
- No validator behavior changes.
- No CI, `factoryctl`, or required-gate wiring.
- No runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.
- No application work or dependency changes.

## Principles
- Mission record first, telemetry second.
- Keep payloads summary-only.
- Treat all telemetry as advisory evidence.
- Use V2 governance for this execution while V3 matures.

## Roles
- Owner: Eduardo Remedios.
- Executor: Codex.
- V2 governance: planning, stage, pack, and verification scaffold.
- V3 artifacts: advisory telemetry and mission record only.

## Acceptance Criteria
- `MR_20260526_004_first_real_telemetry_pilot.json` exists and lints cleanly.
- `PILOT_20260526_001_phase3_status_update/` contains `V3_TELEMETRY.jsonl`, `OVERHEAD.md`, `REDACTION_REVIEW.md`, and `REPLAY_REPORT.json`.
- Phase 3 status records the first real advisory telemetry pilot.
- V2 stage and pack lint pass.
- V3 advisory checks pass or show only expected invalid-fixture findings.

## Go or No-Go Rule
Go only if the pilot stays docs-only, advisory, summary-only, and bounded to named files. No-go if telemetry requires excluded data, enforcement, runtime authority, governance routing, or broader V3 promotion.

## Open Questions
- BLOCKING: none.
- NON-BLOCKING: first-pilot overhead should be reviewed after closeout.
