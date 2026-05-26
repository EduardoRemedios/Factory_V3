# Intent

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Locked intent for the Phase 2.5 mission-record adoption decision.

## Purpose
Decide whether V3 shadow mission records should continue into Phase 3 as optional advisory evidence.

## Goal
Produce `docs/Factory/v3/PHASE2_5_MISSION_RECORD_ADOPTION_DECISION.md` and update roadmap/status docs to reflect the decision.

## Non-goals
- No telemetry implementation.
- No runtime authority.
- No governance router.
- No required-gate integration.
- No V2 scaffolding removal.

## Principles
- Preserve advisory-only V3 posture.
- Keep V2 fallback and build-support scaffolding current.
- Prefer evidence from real records over synthetic fixture assumptions.
- Fail closed on promotion language.

## Acceptance Criteria
- The decision names one Phase 2.5 outcome.
- Evidence cites current real mission records.
- Source-of-truth conflict review is explicit.
- V3 advisory checks pass.
- Phase 3 is unblocked only for planning, not implementation.

## Go or No-go Rule
Go if the current mission records validate and improve replayability without creating authority conflicts. No-go if they imply enforcement, telemetry, or default-mode promotion.
