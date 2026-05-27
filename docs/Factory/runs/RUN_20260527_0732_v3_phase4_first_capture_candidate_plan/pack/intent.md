# Intent: Phase 4 First Capture Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-27): Hardened after red-team review.
- v0.1 (2026-05-27): Initial Stage A intent.

## Purpose
Plan the first candidate mission for Phase 4 real-run corpus capture without executing it.

## Goal
Define a bounded `V3-OP-001` candidate that, if later approved, can produce one real-run result summary and one harness capability profile.

## Candidate
- Candidate ID: `P4-CAPTURE-CANDIDATE-001`
- Mission shape: docs-only Phase 4 status/candidate-record update.
- Profile: `V3-OP-001 Bounded Code Change`
- Telemetry decision: `NO_TELEMETRY`
- Capture outputs after future approval: one result summary and one harness profile.

## Non-goals
- No candidate execution in this run.
- No result summary, harness profile, telemetry, script, validator, fixture, router, enforcement, required gate, CI, runtime authority, proof, lease, default-mode behavior, V3 promotion, or V2 removal.

## Principles
- Keep candidate scope narrow and reviewable.
- Preserve V2 fallback and non-deprecation language.
- Preserve Phase 3 missing natural halted, fallback, or clarification-heavy evidence gap unless it naturally occurs in a later approved mission.
- Treat future evidence as advisory and non-blocking.

## Requirements
- R1 [SOURCE: PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md] Candidate mission needs separate human approval before execution.
- R2 [SOURCE: V3_REAL_RUN_RESULT_SUMMARY_TEMPLATE.md] Future result summary must cover commands, verification, evidence gaps, FP/FN adjudication, and residual risk.
- R3 [SOURCE: V3_HARNESS_CAPABILITY_PROFILE_TEMPLATE.md] Future harness profile must bind observations to harness, model when known, repo, mission profile, tools, date, and evidence.
- R4 [SOURCE: OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md] Candidate must remain bounded with named files and known verification.

## Acceptance Criteria
- The planning pack passes stage-lint and pack-lint.
- The envelope names exact future files and verification.
- Candidate execution remains blocked until explicit approval.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- User must approve `P4-CAPTURE-CANDIDATE-001` before execution.

## Go or No-Go Rule
Go for human review only after all validators pass. Candidate execution is a separate Go decision.
