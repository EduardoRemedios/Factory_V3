# Intent: Phase 4 Real-run Corpus Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-27): Hardened after red-team review.
- v0.1 (2026-05-27): Initial Stage A intent.

## Purpose
Plan the next Phase 4 evidence step: real-run corpus and harness capability profile capture for selected narrow `V3-OP-001` work.

## Goal
Prepare a future implementation scope that creates planning artifacts for collecting real-run summaries and harness capability profiles without executing missions in this run.

## Non-goals
- No real mission execution.
- No real telemetry collection.
- No script, validator, fixture, CI, required-gate, router, enforcement, telemetry-completeness, runtime-authority, proof, lease, default-mode, V3-promotion, or V2-removal work.
- No external web research or latest-paper synthesis.

## Principles
- Keep Phase 4 research-only and non-enforcing.
- Use only selected narrow `V3-OP-001` evidence missions for later capture.
- Treat optional telemetry as shadow evidence only when separately approved.
- Preserve the missing natural halted, fallback, or clarification-heavy case as an explicit gap.
- Bind capability observations to harness, model when known, mission profile, repository, tools, date, and evidence.
- Preserve Factory V2 fallback and non-deprecation language.

## Requirements
- R1 [SOURCE: PHASE4_EVAL_EXPANSION_PLAN.md] Real-run result summaries must record harness, model when known, repository, mission profile, objective, authority, commands, verification, interruptions, evidence gaps, human decisions, FP/FN classifications, reviewer notes, and residual risk.
- R2 [SOURCE: V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md] Capability profiles must be evidence snapshots, not universal scorecards.
- R3 [SOURCE: ROADMAP_TO_FULL_VISION.md] Real-run corpus is required Phase 4 evidence and has not started.
- R4 [SOURCE: PROJECT_STATE.md] Phase 4 remains research-only and non-enforcing.
- R5 [SOURCE: raw_brief.md] External research is out of scope for this run.

## Acceptance Criteria
- A complete V2 planning pack exists and passes validators.
- The future envelope names exact planning artifacts, not live mission execution.
- Future capture criteria include selected narrow `V3-OP-001` candidates and explicit no-go conditions.
- The Phase 3 natural negative-case evidence gap remains visible.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- Later approval must choose actual evidence missions and whether optional telemetry is used.

## Go or No-Go Rule
Go for human review only after stage-lint A through I2 and pack-lint pass. Future artifact creation or mission capture requires explicit user approval.
