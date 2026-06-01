# Intent: Phase 4 Dynamic/Parallel Evidence-export Candidate Plan

## Version
v0.2

## Change Log
- v0.2 (2026-06-01): Hardened after intent red-team review.
- v0.1 (2026-06-01): Initial Stage A intent.

## Purpose
Plan the next Phase 4 negative-case evidence-capture candidate without executing it.

## Goal
Define a separately approvable candidate from `P4-NEG-OPP-006` that can test whether a dynamic/parallel workflow harness exposes enough safe, summary-level evidence for Factory V3 replay and closeout review.

## Candidate
- Candidate ID: `P4-NEG-CAPTURE-CANDIDATE-004`
- Source opportunity: `P4-NEG-OPP-006`
- Mission shape: future review-only or evidence-only dynamic/parallel harness probe over selected Factory V3 Phase 4 docs, indexes, and prior records.
- Preferred future harness: Codex subagent workflows if locally available and explicitly approved; otherwise the future candidate must record `harness_capability_unavailable` or name a separately approved harness.
- Profile: future candidate starts as `V3-OP-001` intake only; execution is eligible only after exact read/write scope, allowed commands, optional telemetry decision, evidence artifacts, and fallback triggers are explicit.
- Telemetry: recommended for later decision as `OPTIONAL_ADVISORY_TELEMETRY_APPROVED` because the opportunity is evidence-export focused, but not approved or collected by this planning run.
- Future capture outputs after separate approval: evidence-export adequacy decision, optional summary-only telemetry, result summary, harness capability profile, index/register updates, and gap-status notes.

## Non-goals
- No dynamic/parallel workflow execution in this run.
- No subagent fanout, telemetry collection, code edits, script edits, validator edits, CI, router, enforcement, required gate, telemetry completeness, runtime authority, proof, lease, default-mode, V3 promotion, or V2 build-support removal changes in this run.
- No capture of chain-of-thought, vendor-private cognition state, raw transcripts, secrets, source file dumps, raw command-output dumps, or broad workflow internals.
- No manufactured ambiguity, seeded failure, or scripted fallback.

## Principles
- Treat dynamic/parallel workflows as a harness capability under Factory governance, not as Factory authority.
- Prefer a read-only or evidence-only future candidate before implementation ambition.
- Preserve summary-only evidence boundaries.
- Record missing evidence honestly if the harness cannot expose task partitioning, file touches, commands, verification, decisions, or closeout.
- Preserve V3 advisory and optional semantics.
- Preserve Factory V2 fallback and non-deprecation language.
- Distinguish local execution evidence from external announcement or official-docs source signals.

## Requirements
- R1 [SOURCE: `ROADMAP_TO_FULL_VISION.md`] The recommended next move is a Phase 4 dynamic/parallel evidence-export candidate from the opportunity register.
- R2 [SOURCE: `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md`] `P4-NEG-OPP-006` remains unapproved and must not execute without a later Go.
- R3 [SOURCE: `PHASE4_DYNAMIC_WORKFLOWS_HARNESS_RESEARCH_PLAN.md`] Dynamic/parallel workflow candidates must be separately planned and may preserve only reviewable execution evidence, not chain-of-thought or vendor-private cognition state.
- R4 [SOURCE: `PHASE4_EVAL_EXPANSION_PLAN.md`] Capability observations must not be generalized beyond harness, profile, repository, and verification conditions.
- R5 [SOURCE: `PHASE4_REAL_RUN_CORPUS_CAPTURE_PLAN.md`] Future capture must produce a result summary and harness profile with commands, verification, evidence gaps, residual risk, and FP/FN adjudication.
- R6 [SOURCE: `PHASE3_TELEMETRY_EVIDENCE_REVIEW.md`] Optional advisory telemetry may be used only for selected narrow evidence missions, summary-only, non-blocking, and not gate-enforced.
- R7 [SOURCE: `OPERATIONAL_PROFILE_V3_OP_001_BOUNDED_CODE_CHANGE.md`] Future execution requires named files, known commands, no dependency creep, clear verification, halt rules, and fallback triggers.
- R8 [SOURCE: user approval] This run plans the candidate and does not execute it.

## Acceptance Criteria
- The planning pack passes Stage A through I2 lint and pack-lint.
- The envelope names the future dynamic/parallel evidence-export candidate, intake rules, possible file budgets, verification commands, evidence artifacts, telemetry decision point, success/non-success criteria, and stop conditions.
- The plan explains how to record sufficient evidence export, insufficient evidence export, unavailable harness capability, pre-envelope fallback, or clean non-event outcomes.
- The plan states that telemetry, failed-verification halt, fallback, recovery, and routing-threshold gaps remain open until real later evidence exists.
- Candidate execution remains blocked until later approval.

## Open Questions
### BLOCKING
- None for this planning run.

### NON-BLOCKING
- Later approval must name the exact harness, exact user prompt, telemetry decision, dated result/profile IDs, authorized evidence artifacts, and whether any edits beyond evidence records are allowed.

## Go or No-Go Rule
Go for human review only after all planning validators pass. Real-run capture remains a separate Go decision.
