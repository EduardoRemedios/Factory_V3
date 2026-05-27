# Intent: Phase 4 Third Capture Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-27): Hardened after red-team review.
- v0.1 (2026-05-27): Initial Stage A intent.

## Purpose
Plan the third candidate mission for Phase 4 real-run corpus capture without executing it.

## Goal
Define a bounded `V3-OP-001` candidate that, if later approved, can create a research-only negative-case opportunity register and capture that docs-only execution as one result summary plus one harness capability profile.

## Candidate
- Candidate ID: `P4-CAPTURE-CANDIDATE-003`
- Mission shape: docs-only Phase 4 negative-case opportunity register.
- Profile: `V3-OP-001 Bounded Code Change`
- Telemetry decision: `NO_TELEMETRY`
- Capture outputs after future approval: opportunity register, index updates, one result summary, and one harness profile.

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
- R5 [SOURCE: RR_20260527_001_phase4_candidate_status_update.md and RR_20260527_002_phase4_corpus_index_update.md] Future opportunity-register language must preserve that existing captures are happy-path evidence only.
- R6 [SOURCE: SCRATCHPAD.md] Any V3 operational-status or approval wording must include same-paragraph non-promotion language.
- R7 [SOURCE: PHASE3_TELEMETRY_EVIDENCE_REVIEW.md] The natural halted/fallback/clarification-heavy gap remains open until naturally observed in a separately approved candidate.

## Acceptance Criteria
- The planning pack passes stage-lint and pack-lint.
- The envelope names exact future files and verification.
- The future candidate preserves the open Phase 3 natural halted/fallback/clarification-heavy gap.
- The future candidate does not approve or execute any listed opportunity.
- Candidate execution remains blocked until explicit approval.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- User must approve `P4-CAPTURE-CANDIDATE-003` before execution.

## Go or No-Go Rule
Go for human review only after all validators pass. Candidate execution is a separate Go decision.
