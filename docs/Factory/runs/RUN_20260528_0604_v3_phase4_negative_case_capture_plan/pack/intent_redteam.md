# Intent Red Team: Phase 4 Negative-case Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage B red-team review.

## Iteration
Iteration: 1 of max 2

## Findings
### RT-01 Candidate could look like manufactured advisory failure
- Severity: High
- Why it matters: Choosing wording close to promotion or routing could bias the later mission toward creating an advisory finding instead of observing one naturally.
- Fix recommendation: State that the future docs update must have an ordinary product-status reason and that advisory FP/FN behavior is only observed if the existing advisory checks or reviewers naturally raise it.
- Status: Resolved in `intent.md` v0.2 and envelope constraints.

### RT-02 Telemetry decision was under-specified
- Severity: Medium
- Why it matters: The brief says no capture yet, but a later candidate may need an explicit telemetry choice.
- Fix recommendation: Require the later approval to choose `NO_TELEMETRY` or `OPTIONAL_ADVISORY_TELEMETRY_APPROVED`; do not decide it inside this pack.
- Status: Resolved in `intent.md` v0.2.

### RT-03 Non-event path needed stronger criteria
- Severity: Medium
- Why it matters: A successful docs-only run with no negative signal could be overstated as closing the Phase 3 gap.
- Fix recommendation: Add explicit clean non-event recording and keep the Phase 3 gap open unless a natural halt, fallback, or clarification-heavy event occurs.
- Status: Resolved in `intent.md` v0.2 and verification plan.

## Agent Failure Modes
- Treating the opportunity register as execution approval.
- Converting advisory threshold wording into routing authority.
- Recording an advisory warning as a true finding without human adjudication.
- Omitting a clean non-event note when the later run remains happy path.

## Verification Holes
- Later approval evidence is outside this planning run.
- Optional telemetry cannot be validated until a later decision approves or declines it.

## Critical Findings
- None unresolved.
