# Intent: Factory V3 Phase 4 Eval Expansion Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-26): Hardened after intent red-team review.
- v0.1 (2026-05-26): Initial Stage A intent.

## Purpose
Create a Factory V2-governed `PLANNING_ONLY` pack for Factory V3 Phase 4 eval expansion and harness capability profiling.

## Goal
Plan, but do not implement, the next V3 artifacts needed to measure harness capability, execution reliability, scope discipline, verification quality, interruption recovery, evidence quality, false-positive and false-negative behavior, and later governance-routing fitness without creating a router.

## Non-goals
- No Phase 4 tooling, fixtures, scripts, templates, or product docs are implemented in this run.
- No governance routing, enforcement, telemetry completeness checks, required gates, CI wiring, runtime authority, proof, lease enforcement, default-mode behavior, or V2 build-support removal.
- No V3 promotion beyond optional `V3-OP-001 Bounded Code Change`.
- No weakening of Factory V2 fallback or non-deprecation language.

## Principles
- Source Phase 4 from current roadmap and Phase 3 review evidence.
- Keep capability claims harness-specific, model-specific when known, profile-specific, and evidence-backed.
- Treat thresholds as advisory planning language only.
- Preserve telemetry as optional shadow evidence for selected narrow `V3-OP-001` evidence missions.
- Carry the missing natural halted, fallback, or clarification-heavy telemetry case as a named evidence gap.
- Apply SIMPLE-CODE-GATE to any later implementation plan: smallest clear change, no dependency creep, no broad abstractions, no silent failures.

## Roles
- Root Planner: create run evidence and enforce `PLANNING_ONLY`.
- Intent Contractor: bound Phase 4 objective and non-goals.
- Red Team: attack scope drift, router creep, overconfident scoring, and weak verification.
- Synthesis: harden the intent and envelope.
- Purple Gate: decide whether the planning pack is safe to hand to a human for execution approval.

## Requirements
- R1 [SOURCE: raw_brief.md] The run must produce the normal Factory V2 planning pack artifacts.
- R2 [SOURCE: docs/Factory/v3/ROADMAP_TO_FULL_VISION.md] Phase 4 must expand evals beyond document drift toward execution reliability and capability profiling.
- R3 [SOURCE: docs/Factory/v3/PHASE3_TELEMETRY_EVIDENCE_REVIEW.md] Phase 3 telemetry remains optional advisory shadow evidence only, with the negative-case gap carried forward.
- R4 [SOURCE: docs/PROJECT_STATE.md] V3 remains optional/advisory except approved optional `V3-OP-001`.
- R5 [SOURCE: docs/ROADMAP.md] Do not add required gates, default-mode promotion, telemetry enforcement, runtime authority, governance routing, or V2 scaffolding removal.
- R6 [SOURCE: docs/Factory/v3/OPERATIONAL_READINESS_EVAL_PLAN.md] Phase 4 planning must preserve V2 guarantees and test ambiguity, scope expansion, authority, verification halt, stale reentry, SIMPLE-CODE-GATE, and V2 fallback behavior.

## Acceptance Criteria
- A complete V2 `PLANNING_ONLY` planning pack exists under this run root.
- The pack names future artifacts only as planned outputs requiring later human approval.
- The premortem covers harness overconfidence, doc-only eval weakness, synthetic negative fixtures, premature router design, threshold drift, Phase 3 telemetry gaps, and V2 fallback drift.
- Verification commands pass: knowledge lint, context index/report, stage-lint for A through I2, pack-lint, and `git diff --check`.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- Future execution approval must decide exact fixture IDs, report schema fields, and whether a lightweight JSON output shape is sufficient before writing Phase 4 files.

## Go or No-Go Rule
Go for human review only if this planning pack passes `stage-lint` for A through I2 and `pack-lint`; execution remains blocked until the user explicitly approves a later implementation run.
