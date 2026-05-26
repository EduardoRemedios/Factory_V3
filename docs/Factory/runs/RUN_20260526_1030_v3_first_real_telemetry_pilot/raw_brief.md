# Raw Brief

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Raw brief for the first real Phase 3 telemetry pilot.

## Request
Proceed with the next Factory V3 step after the real telemetry capture plan.

## Interpretation
Run the first real Phase 3 telemetry pilot as a bounded docs-only `V3-OP-001` mission.

## Required Scope
- Use a separate execution-enabled V2-governed run before writing real telemetry.
- Create one shadow mission record for the pilot.
- Create one real telemetry pilot directory under `docs/Factory/v3/telemetry/pilots/`.
- Update Phase 3 status and roadmap docs to record that the first advisory pilot exists.
- Keep telemetry advisory, optional, research-only, and non-enforcing.

## Forbidden Scope
- No CI, `factoryctl`, or required-gate wiring.
- No runtime authority, proof, lease enforcement, governance routing, default-mode behavior, or V2 scaffolding removal.
- No source contents, diffs, secrets, full transcripts, or chain-of-thought in telemetry.
