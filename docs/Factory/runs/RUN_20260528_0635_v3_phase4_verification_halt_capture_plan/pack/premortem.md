# Premortem: Phase 4 Verification-halt Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage E premortem.

## Failure Scenarios
### PM-01 Manufactured verification failure
- Failure: Future execution intentionally breaks `expected.json` or fixture text to create a halt.
- Mitigation: Require ordinary fixture-maintenance rationale and treat seeded failure as invalid evidence.

### PM-02 Continuing after failed verification
- Failure: The future agent sees an `--expect` mismatch and keeps editing without halt or human decision.
- Mitigation: Envelope requires immediate halt until decision, fallback, or closeout.

### PM-03 Telemetry drift
- Failure: Optional telemetry becomes implied requirement, completeness check, or gate.
- Mitigation: Later approval must confirm telemetry mode; telemetry remains summary-only and non-blocking.

### PM-04 Gap overclaim
- Failure: A clean pass or synthetic fixture maintenance is reported as closing the natural halt/fallback/clarification gap.
- Mitigation: Result summary must state whether natural halt occurred; otherwise gap remains open.

### PM-05 Scope creep
- Failure: Future candidate expands into validator code, broader fixtures, or routing discussion.
- Mitigation: Envelope file-touch budget excludes scripts, validators, routing, gates, runtime, proof, leases, and V2 removal.
