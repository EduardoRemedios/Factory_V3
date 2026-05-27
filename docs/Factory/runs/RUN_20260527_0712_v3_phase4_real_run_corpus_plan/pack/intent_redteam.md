# Intent Red Team: Phase 4 Real-run Corpus Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage B red-team review.

## Iteration
- Iteration: 1 of max 2

## Findings

### F1 - Critical - Planning could drift into live mission execution
- Why it matters: Real-run corpus language can be misread as permission to run missions now.
- Fix recommendation: future scope must create capture plan and templates only; actual mission candidates need later approval.

### F2 - Critical - Capability profiles could imply routing readiness
- Why it matters: Phase 5 routing is not approved.
- Fix recommendation: mark profiles as advisory snapshots and block any operational routing or governance reduction language.

### F3 - High - Optional telemetry could become routine
- Why it matters: Phase 3 allows only selected narrow advisory shadow telemetry.
- Fix recommendation: require separate approval per mission and preserve summary-only payload rules.

### F4 - High - Positive-only real runs could mask failure modes
- Why it matters: The missing halted, fallback, or clarification-heavy case remains a gap.
- Fix recommendation: require gap tracking and candidate selection that can record fallback or halt if it naturally occurs.

## Verification Holes
- Future implementation must run V3 advisory lint and operational-readiness evals.
- Future capture plan must include no-go language for router and enforcement drift.

## Blocking Findings
- None after hardening.
