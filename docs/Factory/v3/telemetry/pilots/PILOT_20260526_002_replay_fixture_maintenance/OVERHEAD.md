# Pilot Overhead

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Overhead notes for second real Phase 3 telemetry pilot.

## Mission
- Mission ID: `MR_20260526_005_second_real_telemetry_pilot`
- Pilot ID: `PILOT_20260526_002_replay_fixture_maintenance`
- Profile: `V3-OP-001`
- Mission type: small fixture-maintenance update

## Counts
- Telemetry events: 28
- Estimated telemetry minutes: 18
- Commands represented in telemetry: 12
- Verification commands represented in telemetry: 12
- Fields marked `not_recorded`: `occurred_at`, model, final commit hash before commit creation
- Redactions made: none required beyond summary-only event payloads
- Replay findings: none for the real pilot log

## Friction Notes
- The second pilot was slightly faster than pilot 1 because the event pattern was already established.
- The paired command and verification events are still verbose for small maintenance work.
- The fixture expected-output regeneration step benefits from explicit telemetry because it makes the intended drift narrow and reviewable.

## Advisory Status
This pilot is research-only, optional, and non-enforcing. It does not approve required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal.
