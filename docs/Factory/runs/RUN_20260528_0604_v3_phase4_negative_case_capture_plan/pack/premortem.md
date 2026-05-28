# Premortem: Phase 4 Negative-case Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-28): Initial Stage E premortem.

## Failure Scenarios
### PM-01 Manufactured negative case
- Failure: Future execution writes risky wording just to trigger an advisory finding.
- Mitigation: Require an ordinary docs-status reason and treat findings as observed, not scripted.

### PM-02 Promotion drift
- Failure: Threshold or routing language implies reduced governance, default V3 use, required gates, or V2 deprecation.
- Mitigation: Same-paragraph non-promotion language and advisory lint/NL pilot checks.

### PM-03 Phase 3 gap overstated
- Failure: A happy-path or advisory-only signal is reported as closing the halted/fallback/clarification gap.
- Mitigation: Result summary must record either natural negative signal or clean non-event; gap stays open unless real evidence exists.

### PM-04 Verification weakness
- Failure: Later capture records command names without meaningful pass/fail evidence or skipped-check reasons.
- Mitigation: Verification plan requires exit status summaries and skipped-check rationale.

### PM-05 Scope creep
- Failure: Future candidate expands beyond docs-only evidence capture into tooling, validators, telemetry enforcement, or routing.
- Mitigation: Envelope file-touch budget and stop conditions block expansion.
