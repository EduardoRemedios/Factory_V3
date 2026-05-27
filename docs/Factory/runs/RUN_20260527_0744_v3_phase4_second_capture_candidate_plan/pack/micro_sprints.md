# Micro-sprints: Phase 4 Second Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage G micro-sprints.

## MS-01 Candidate Approval Record
- Objective: If approved later, record `P4-CAPTURE-CANDIDATE-002` as the second capture candidate.
- Inputs: capture plan, first capture evidence, scratchpad pitfall, and templates.
- Outputs: approved future file list and no-execution confirmation.
- Entry criteria: explicit user Go for the candidate.
- Exit criteria: no mission execution starts before approval.
- Stop or go gate: stop if candidate scope expands.

## MS-02 Candidate Execution And Evidence
- Objective: Execute the approved docs-only index update and preserve command evidence.
- Inputs: candidate approval, allowed files, verification commands.
- Outputs: corpus index, harness-profile index, and committed docs-only change evidence.
- Entry criteria: MS-01 complete.
- Exit criteria: verification passes or halt/fallback is recorded.
- Stop or go gate: stop on verification failure without human decision.

## MS-03 Capture Records
- Objective: Fill one result summary and one harness capability profile for the index update.
- Inputs: execution evidence from MS-02.
- Outputs: real-run result summary and harness profile.
- Entry criteria: MS-02 complete.
- Exit criteria: FP/FN adjudication and residual risk recorded.
- Stop or go gate: stop if records imply routing, promotion, or reduced governance.
