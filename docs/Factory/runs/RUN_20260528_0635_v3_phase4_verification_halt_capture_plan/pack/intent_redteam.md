# Intent Red Team: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage B red-team review.

## Iteration
Iteration: 1 of max 2

## Findings
### RT-01 Candidate could manufacture a verification failure
- Severity: Critical
- Why it matters: A negative-case candidate can become invalid if the agent intentionally breaks an expected-output file to force a halt.
- Fix recommendation: State that the future edit must have an ordinary fixture-maintenance reason and that halt evidence is valid only if the deterministic check fails naturally.
- Status: Resolved in `intent.md` v0.2 and envelope constraints.

### RT-02 Telemetry recommendation could be mistaken for approval
- Severity: High
- Why it matters: Telemetry remains optional advisory evidence and cannot be collected without explicit later approval.
- Fix recommendation: Separate recommendation from authorization and require later Go to confirm telemetry mode.
- Status: Resolved in `intent.md` v0.2.

### RT-03 Halt path needed explicit closeout behavior
- Severity: High
- Why it matters: A failed check is useful evidence only if work stops and the decision path is recorded.
- Fix recommendation: Require halt until human decision, V2 fallback, or closeout; do not continue editing through failure.
- Status: Resolved in `intent.md` v0.2 and verification plan.

## Agent Failure Modes
- Seeding a mismatch to create a halt.
- Continuing after `--expect` mismatch without human decision.
- Treating advisory telemetry as required or gate-enforced.
- Overstating a clean pass as closing the Phase 3 gap.

## Verification Holes
- Future real-run evidence cannot be validated until execution is separately approved.

## Critical Findings
- None unresolved.
