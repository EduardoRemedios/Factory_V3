# Intent: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-28): Hardened after red-team review.
- v0.1 (2026-05-28): Initial Stage A intent.

## Purpose
Plan the second Phase 4 negative-case real-run capture candidate without executing the candidate.

## Goal
Define a separately approvable `V3-OP-001` candidate from `P4-NEG-OPP-002` that can naturally exercise verification-halt behavior during deterministic fixture or expected-output maintenance.

## Candidate
- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-002`
- Source opportunity: `P4-NEG-OPP-002`
- Mission shape: narrow maintenance of `tests/fixtures/factory_v3_operational_readiness_eval/cases/V3-P4-VERIFY-001/input.md` and `tests/fixtures/factory_v3_operational_readiness_eval/expected.json`.
- Profile: `V3-OP-001 Bounded Code Change`
- Telemetry: recommended for later approval as `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`, but not approved or collected by this planning run.
- Future capture outputs after separate approval: command evidence, halt/fallback/human-decision notes if verification fails, clean non-event notes if verification passes, one result summary, and one harness capability profile.

## Non-goals
- No real-run capture execution in this run.
- No fixture or expected-output edits in this run.
- No telemetry collection in this run.
- No result summary, harness profile, script, validator, router, enforcement, required gate, CI wiring, telemetry completeness check, runtime authority, proof, lease, default-mode behavior, V3 promotion, or V2 build-support removal.

## Principles
- Do not seed or manufacture a verification failure.
- Let deterministic verification decide whether a natural halt signal exists.
- If verification fails later, halt until human decision, fallback, or closeout is recorded.
- Preserve V3 advisory and optional semantics.
- Preserve Factory V2 fallback and non-deprecation language.
- Preserve the Phase 3 natural halted, fallback, or clarification-heavy gap unless real later evidence closes it.
- Keep future work narrow and reviewable under SIMPLE-CODE-GATE.

## Requirements
- R1 [SOURCE: `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`] `P4-NEG-OPP-002` remains an opportunity until a later approval names it for execution.
- R2 [SOURCE: `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`] Future capture must produce a result summary and harness profile with commands, verification, evidence gaps, residual risk, and FP/FN adjudication.
- R3 [SOURCE: `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`] Optional advisory telemetry may be used only for selected narrow evidence missions and must remain summary-only and non-blocking.
- R4 [SOURCE: `PHASE4_EVAL_EXPANSION_PLAN.md`] Failed checks must lead to halt, fallback, or explicit human decision.
- R5 [SOURCE: `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`] Future execution must have named files, known commands, clear verification, no dependency addition, and explicit fallback triggers.
- R6 [SOURCE: user approval] This run plans the verification-halt candidate and does not execute it.

## Acceptance Criteria
- The planning pack passes Stage A through I2 lint and pack-lint.
- The envelope names the future fixture/expected-output target, verification command, evidence artifacts, telemetry recommendation, success/non-success criteria, and stop conditions.
- The plan explains how to record a natural verification halt and how to record a clean non-event.
- The plan states that the Phase 3 evidence gap remains open until real evidence exists.
- Candidate execution remains blocked until later approval.

## Open Questions
### BLOCKING
- None.

### NON-BLOCKING
- Later approval must confirm whether optional advisory telemetry is approved and assign final dated result/profile IDs.

## Go or No-Go Rule
Go for human review only after all planning validators pass. Real-run capture remains a separate Go decision.
