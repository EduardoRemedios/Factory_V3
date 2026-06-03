# Raw Brief: Phase 4 Verification-halt Telemetry Candidate Plan

## Date
2026-06-03

## Request
Plan the next Factory V3 Phase 4 evidence-capture step after the dynamic/parallel summary-export signal was recorded and the canons moved the recommended next step to failed-verification halt or fallback evidence with optional advisory telemetry.

## Human Approval Context
User approved proceeding after the canonical next-step summary that recommended:
- first committing a small canon-status update, and
- then planning a `P4-NEG-OPP-002` follow-up as the next Phase 4 candidate.

## Execution Mode
PLANNING_ONLY.

This run does not authorize fixture edits, expected-output edits, telemetry collection, code edits, validator changes, routing, required gates, runtime authority, proof, lease enforcement, V3 profile promotion, default-mode behavior, or Factory V2 build-support removal.

## Objective
Create a Factory V2-governed planning pack for a future `P4-NEG-OPP-002` follow-up candidate that can test whether a deterministic fixture or expected-output maintenance task naturally produces failed-verification halt, fallback, or human-decision evidence.

## Candidate Source
`docs/Factory/v3/PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`:
- `P4-NEG-OPP-002`: Verification halt.

## Planning Scope
The pack should define:
- future candidate objective,
- allowed read scope,
- possible authorized files if a later human Go executes the candidate,
- forbidden files and forbidden evidence capture,
- optional advisory telemetry recommendation,
- expected-output drift and failed-verification evidence expectations,
- stop/fallback conditions,
- verification commands,
- expected result and harness-profile artifacts.

## Guardrails
- Keep Factory V3 advisory-only except for approved optional `V3-OP-001`.
- Preserve Factory V2 fallback and non-deprecation language.
- Do not manufacture ambiguity, failure, or fallback.
- Do not capture chain-of-thought, vendor-private cognition state, raw transcripts, secrets, source file dumps, or broad workflow internals.
- Do not infer verification-halt evidence from the prior clean non-event.
- Do not wire telemetry, validators, or evidence checks into required gates.
- Do not execute fixture or expected-output maintenance without a later explicit Go naming exact target files, command families, evidence artifacts, telemetry decision, and stop conditions.

## Desired Output
A complete planning-only Factory pack through Stage I2, suitable for human review before any future candidate execution.
