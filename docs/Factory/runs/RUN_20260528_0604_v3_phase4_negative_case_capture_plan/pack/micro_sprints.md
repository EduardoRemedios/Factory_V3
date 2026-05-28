# Micro-sprints: Phase 4 Negative-case Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage G micro-sprints.

## MS-01 Later Candidate Approval
- Objective: Obtain explicit future approval for `P4-NEG-CAPTURE-CANDIDATE-001`.
- Inputs: this planning pack, Phase 4 capture plan, negative-case register, and current V3 status docs.
- Outputs: approval or no-go record naming candidate, files, commands, telemetry decision, and dated result/profile IDs.
- Entry criteria: planning pack passes I2 and pack-lint.
- Exit criteria: approval is explicit, or execution remains blocked.
- Stop or go gate: stop if approval is ambiguous or candidate no longer fits `V3-OP-001`.

## MS-02 Future Docs-only Candidate Execution
- Objective: If later approved, make the narrow advisory wording/status update for an ordinary docs reason.
- Inputs: approved file-touch budget, allowed commands, and verification plan.
- Outputs: bounded docs change and command evidence.
- Entry criteria: MS-01 has explicit Go.
- Exit criteria: verification passes, or halt/fallback/human decision is recorded.
- Stop or go gate: stop on scope growth, failed verification without decision, or promotion/routing drift.

## MS-03 Future Capture Records
- Objective: Record the real-run result summary and harness capability profile.
- Inputs: execution evidence from MS-02 and advisory eval outputs.
- Outputs: result summary, harness profile, FP/FN adjudication, negative-signal notes, or clean non-event note.
- Entry criteria: MS-02 has closeout evidence.
- Exit criteria: residual risks and Phase 3 gap status are explicit.
- Stop or go gate: stop if records imply routing, enforcement, required gates, default-mode behavior, V3 promotion, or V2 removal.
