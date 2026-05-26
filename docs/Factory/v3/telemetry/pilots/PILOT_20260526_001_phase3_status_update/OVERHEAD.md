# Pilot Overhead

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Overhead notes for first real Phase 3 telemetry pilot.

## Mission
- Mission ID: `MR_20260526_004_first_real_telemetry_pilot`
- Pilot ID: `PILOT_20260526_001_phase3_status_update`
- Profile: `V3-OP-001`
- Mission type: small docs-only status update

## Counts
- Telemetry events: 26
- Estimated telemetry minutes: 20
- Commands represented in telemetry: 11
- Verification commands represented in telemetry: 11
- Fields marked `not_recorded`: `occurred_at`, model, final commit hash before commit creation
- Redactions made: none required beyond summary-only event payloads
- Replay findings: none for the real pilot log

## Friction Notes
- The event log is readable and replayable, but manually recording paired `command_run` and `verification_run` events is verbose.
- The log improved replay over the mission record alone by preserving authority, file scope, command labels, and closeout order in one machine-readable stream.
- Later pilots should test whether fewer command events preserve enough replay value.

## Advisory Status
This pilot is research-only, optional, and non-enforcing. It does not approve required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal.
