# Intent: Phase 4 Negative-case Capture Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-28): Hardened after red-team review.
- v0.1 (2026-05-28): Initial Stage A intent.

## Purpose
Plan the first narrow Phase 4 negative-case real-run capture candidate without executing the candidate.

## Goal
Define a separately approvable `V3-OP-001` candidate from the Phase 4 negative-case opportunity register that can naturally exercise advisory false-positive or false-negative behavior, and record halt, fallback, clarification, stale-reentry, evidence-quality, verification-quality, or scope-discipline signals only if they occur during later approved work.

## Candidate
- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-001`
- Source opportunity: `P4-NEG-OPP-005`
- Mission shape: narrow docs-only advisory wording/status update around Phase 4 threshold, routing, or promotion-adjacent language.
- Profile: `V3-OP-001 Bounded Code Change`
- Telemetry: not approved by this pack. Later approval must explicitly choose `NO_TELEMETRY` or `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`.
- Future capture outputs after separate approval: one result summary, one harness capability profile, advisory eval output, FP/FN adjudication, and negative-signal or non-event notes.

## Non-goals
- No real-run capture execution in this run.
- No result summary, harness profile, telemetry log, script, validator, fixture behavior change, router, enforcement, required gate, CI wiring, telemetry completeness check, runtime authority, proof, lease, default-mode behavior, V3 promotion, or V2 build-support removal.

## Principles
- Do not manufacture failure or ambiguity.
- Preserve V3 advisory and optional semantics.
- Preserve Factory V2 fallback and non-deprecation language.
- Preserve the Phase 3 natural halted, fallback, or clarification-heavy gap unless real later evidence closes it.
- Keep the future candidate narrow, file-bounded, and reviewable under SIMPLE-CODE-GATE.
- Treat advisory findings as evidence needing human adjudication, not authority.

## Requirements
- R1 [SOURCE: `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`] The selected opportunity must remain unapproved until a later Factory V2 or explicit human approval names it for execution.
- R2 [SOURCE: `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`] Future capture must produce a result summary and harness profile with commands, verification, evidence gaps, residual risk, and FP/FN adjudication.
- R3 [SOURCE: `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`] The natural halted, fallback, or clarification-heavy gap remains open until naturally observed.
- R4 [SOURCE: `PHASE4_EVAL_EXPANSION_PLAN.md`] Advisory threshold language must not become routing, reduced governance, default-mode behavior, or required-gate authority.
- R5 [SOURCE: `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`] Future execution must have named files, known commands, clear verification, no dependency addition, and explicit fallback triggers.
- R6 [SOURCE: `SCRATCHPAD.md` FP-002] Promotion-sensitive evidence records need same-paragraph non-promotion language.
- R7 [SOURCE: user brief] This planning run must not execute the capture or implement tooling.

## Acceptance Criteria
- The planning pack passes Stage A through I2 lint and pack-lint.
- The envelope names the future candidate, file-touch budget, evidence artifacts, success/non-success criteria, and stop conditions.
- The plan explains how to capture natural negative signals and how to record a clean non-event.
- The plan states that the Phase 3 evidence gap remains open until real evidence exists.
- Candidate execution remains blocked until later approval.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- Later approval must name the exact future mission, telemetry decision, and timestamped result/profile IDs.

## Go or No-Go Rule
Go for human review only after all planning validators pass. Real-run capture remains a separate Go decision.
