# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Intent for second real telemetry pilot.

## Purpose
Capture the second real advisory Phase 3 telemetry pilot through a small fixture-maintenance mission.

## Goal
Add one valid telemetry replay fixture, update the expected replay report, and record the mission as real advisory telemetry evidence.

## Non-goals
- No validator behavior changes.
- No telemetry enforcement.
- No CI, `factoryctl`, or required-gate wiring.
- No runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.
- No dependency changes.

## Principles
- Keep fixture maintenance small and deterministic.
- Preserve advisory-only posture.
- Link mission record, telemetry log, replay report, and expected fixture output.
- Use V2 governance while V3 matures.

## Roles
- Owner: Eduardo Remedios.
- Executor: Codex.
- V2 governance: execution pack and validation.
- V3 artifacts: advisory fixture, mission record, and telemetry log.

## Acceptance Criteria
- `tests/fixtures/factory_v3_telemetry_replay/valid/real_pilot_style.jsonl` exists.
- `tests/fixtures/factory_v3_telemetry_replay/expected/all.json` is regenerated deterministically.
- `MR_20260526_005_second_real_telemetry_pilot.json` exists and lints cleanly.
- `PILOT_20260526_002_replay_fixture_maintenance/` contains telemetry, overhead, redaction, and replay report files.
- V2 and V3 checks pass.

## Go or No-Go Rule
Go only if the mission remains bounded fixture maintenance and advisory telemetry. No-go if it needs script changes, enforcement, runtime authority, governance routing, dependency changes, or broader V3 promotion.

## Open Questions
- BLOCKING: none.
- NON-BLOCKING: compare pilot 2 overhead against pilot 1.
