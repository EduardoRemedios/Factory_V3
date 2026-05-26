# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Intent for third real telemetry pilot.

## Purpose
Capture the third real advisory Phase 3 telemetry pilot without manufacturing a false halt or fallback scenario.

## Goal
Record the third telemetry pilot, add evidence-review prep, and move the roadmap to the Phase 3 telemetry evidence review.

## Non-goals
- No recommendation that telemetry become standard or required.
- No validator behavior changes.
- No CI, `factoryctl`, required-gate wiring, runtime authority, proof, lease enforcement, governance routing, default-mode promotion, or V2 scaffolding removal.

## Principles
- Do not manufacture negative evidence.
- Preserve advisory-only posture.
- Keep the change docs/data-only.
- Use V2 governance while V3 matures.

## Roles
- Owner: Eduardo Remedios.
- Executor: Codex.
- V2 governance: execution pack and verification.
- V3 artifacts: advisory telemetry, mission record, and evidence-review prep.

## Acceptance Criteria
- Third pilot telemetry, overhead, redaction, and replay report files exist.
- Mission record exists and lints cleanly.
- Phase 3 status shows 3 of 3 logs captured, with gap note for missing natural halted/fallback case.
- Roadmap next move becomes Phase 3 telemetry evidence review.
- V2 and V3 verification checks pass.

## Go or No-Go Rule
Go only if the pilot stays advisory and docs/data-only. No-go if it requires enforcement, runtime authority, governance routing, script changes, dependency changes, or broader promotion.

## Open Questions
- BLOCKING: none.
- NON-BLOCKING: evidence review should decide whether another negative pilot is needed before Phase 4.
