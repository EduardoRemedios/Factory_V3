# Intent: Phase 4 Fixture Expansion Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-26): Hardened after red-team review.
- v0.1 (2026-05-26): Initial Stage A intent.

## Purpose
Plan the next Phase 4 implementation step: advisory operational-readiness fixture expansion for harness capability and execution-reliability signals.

## Goal
Prepare an execution-ready but not-yet-executed scope that adds exact Phase 4 eval triggers, eight fixture cases, and deterministic expected output updates.

## Non-goals
- No implementation in this planning run.
- No real-run corpus collection.
- No governance routing, enforcement, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 promotion, or V2 build-support removal.
- No weakening of Factory V2 fallback.

## Principles
- Preserve `blocking_effect: none`.
- Keep evaluator changes direct: add explicit trigger checks only.
- Keep fixture cases synthetic and labeled as design coverage, not real negative-case telemetry evidence.
- Preserve Phase 3 gap for missing natural halted, fallback, or clarification-heavy telemetry evidence.
- Apply SIMPLE-CODE-GATE to the later implementation.

## Requirements
- R1 [SOURCE: PHASE4_EVAL_EXPANSION_PLAN.md] Implement fixture families only after approval names exact files and outputs.
- R2 [SOURCE: raw_brief.md] Future scope may touch `scripts/factory_v3_operational_readiness_eval.py`, eight `V3-P4-*` fixture files, and `expected.json`.
- R3 [SOURCE: PHASE3_TELEMETRY_EVIDENCE_REVIEW.md] Telemetry remains optional, advisory, and non-enforcing.
- R4 [SOURCE: README.md] V3 remains optional/advisory except approved optional `V3-OP-001`.
- R5 [SOURCE: AGENTS.md] Keep deterministic fixture outputs stable when changing validator behavior.

## Acceptance Criteria
- The pack passes all V2 stage and pack validators.
- The future envelope names exact files and expected behavior.
- The future evaluator output remains advisory and non-blocking.
- Synthetic fixture status and Phase 3 natural negative-case gap remain explicit.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- A later real-run corpus step must be planned separately.

## Go or No-Go Rule
Go for human review only after `stage-lint` A through I2 and `pack-lint` pass. Future implementation still requires explicit user approval.
