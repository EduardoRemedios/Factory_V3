# Intent: Phase 4 Clarification-heavy Capture Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-05-30): Hardened after red-team review.
- v0.1 (2026-05-30): Initial Stage A intent.

## Purpose
Plan the next Phase 4 negative-case evidence-capture candidate without executing it.

## Goal
Define a separately approvable candidate from `P4-NEG-OPP-001` that can naturally exercise clarification-heavy behavior before any edit occurs.

## Candidate
- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-003`
- Source opportunity: `P4-NEG-OPP-001`
- Mission shape: future bounded intake for a Phase 4 next-step/canon-alignment update where the correct canonical target may be ambiguous between top-level status docs and V3 Phase 4 docs.
- Profile: candidate starts as `V3-OP-001` intake only; execution is eligible only after target files, commands, verification, and fallback triggers are explicit.
- Telemetry: recommended for later decision as `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`, but not approved or collected by this planning run.
- Future capture outputs after separate approval: clarification request or source-derived clarification evidence, command evidence if edits occur, result summary, harness capability profile, and gap-status notes.

## Non-goals
- No candidate execution in this run.
- No status, roadmap, index, fixture, script, validator, CI, router, enforcement, required gate, telemetry completeness, runtime authority, proof, lease, default-mode, V3 promotion, or V2 build-support removal changes in this run.
- No manufactured ambiguity, seeded failure, or scripted fallback.

## Principles
- Use the current canons as the source of natural ambiguity; do not invent ambiguity.
- Future work must stop before editing if target files or canonical source authority cannot be derived from source artifacts.
- A clarification request, pre-envelope fallback, or no-edit closeout is valid evidence.
- If source artifacts make the target clear, future work may proceed only inside an explicit file-touch budget.
- Preserve V3 advisory and optional semantics.
- Preserve Factory V2 fallback and non-deprecation language.
- Preserve the Phase 3 natural halted/fallback/clarification-heavy gap unless real later evidence closes or narrows it.

## Requirements
- R1 [SOURCE: `ROADMAP_TO_FULL_VISION.md`] The recommended next move is a Phase 4 clarification-heavy candidate from the opportunity register.
- R2 [SOURCE: `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`] `P4-NEG-OPP-001` remains unapproved and must not execute without a later Go.
- R3 [SOURCE: `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`] Future capture must produce a result summary and harness profile with commands, verification, evidence gaps, residual risk, and FP/FN adjudication.
- R4 [SOURCE: `PHASE4_EVAL_EXPANSION_PLAN.md`] Capability observations must not be generalized beyond harness, profile, repository, and verification conditions.
- R5 [SOURCE: `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`] Future execution requires named files, known commands, no dependency creep, clear verification, halt rules, and fallback triggers.
- R6 [SOURCE: user approval] This run plans the candidate and does not execute it.

## Acceptance Criteria
- The planning pack passes Stage A through I2 lint and pack-lint.
- The envelope names the future clarification candidate, intake rules, possible file budgets, verification commands, evidence artifacts, telemetry decision point, success/non-success criteria, and stop conditions.
- The plan explains how to record clarification, pre-envelope fallback, bounded execution, or clean non-event outcomes.
- The plan states that the Phase 3 evidence gap remains open until real evidence exists.
- Candidate execution remains blocked until later approval.

## Open Questions
### BLOCKING
- None for this planning run.

### NON-BLOCKING
- Later approval must name the exact user prompt, telemetry decision, dated result/profile IDs, and whether the future candidate may edit after source-derived clarification.

## Go or No-Go Rule
Go for human review only after all planning validators pass. Real-run capture remains a separate Go decision.
