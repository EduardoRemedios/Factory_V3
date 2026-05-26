# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Intent for telemetry replay validator implementation.

## Purpose
Implement the first Phase 3 fixture-first advisory telemetry replay validator.

## Goal
Add a standalone JSONL replay validator, deterministic fixture corpus, expected output, and status/docs updates within the approved scope.

## Non-goals
- No real mission telemetry collection.
- No required-gate integration.
- No CI or `factoryctl` wiring.
- No runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.

## Principles
- Keep implementation direct and dependency-free.
- Emit `blocking_effect: none`.
- Keep expected output deterministic.
- Treat all findings as advisory and non-blocking.
- Use synthetic fixtures only.

## Roles
- Root Planner: maintain V2 run evidence.
- Implementer: add script, fixtures, and docs.
- Verification Specialist: run deterministic fixture and advisory checks.
- Purple Gate: verify scope and evidence.

## Acceptance Criteria
- `scripts/factory_v3_telemetry_replay_lint.py` exists.
- Telemetry replay fixtures cover approved valid and invalid cases.
- `--json` and `--expect` work.
- The validator emits only advisory statuses.
- V3 advisory checks pass.
- Pack and stage lints pass.

## Go or No-go Rule
Go if implementation stays within approved fixture-first advisory scope. No-go if real telemetry collection, required gates, or runtime authority are needed.
