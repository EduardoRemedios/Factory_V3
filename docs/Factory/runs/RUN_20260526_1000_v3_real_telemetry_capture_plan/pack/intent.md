# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Intent for real telemetry capture planning.

## Purpose
Define the first real `V3-OP-001` telemetry capture process before collecting any real mission logs.

## Goal
Create `docs/Factory/v3/PHASE3_REAL_MISSION_TELEMETRY_CAPTURE_PLAN.md` and update roadmap/status docs so future pilots have a bounded capture workflow.

## Non-goals
- No real telemetry collection.
- No validator implementation changes.
- No telemetry storage directories for pilots.
- No required-gate integration.
- No runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.

## Principles
- Plan before capture.
- Keep first pilots small and comparable.
- Link telemetry to mission records.
- Prefer summaries and references over payload copies.
- Preserve data minimization and advisory-only posture.

## Acceptance Criteria
- Storage location is named.
- First pilot count and selection criteria are named.
- Event subset is named.
- Redaction and data-minimization rules are named.
- Operator workflow and overhead fields are named.
- Stop conditions are named.
- V2 and V3 advisory checks pass.

## Go or No-go Rule
Go if the plan enables future real telemetry pilots without collecting telemetry now. No-go if the plan implies enforcement, runtime authority, or default-mode promotion.
