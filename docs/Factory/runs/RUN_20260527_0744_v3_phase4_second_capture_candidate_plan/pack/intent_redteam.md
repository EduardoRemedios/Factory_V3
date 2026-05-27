# Intent Red Team: Phase 4 Second Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage B review.

## Iteration
- Iteration: 1 of max 2

## Findings

### F1 - Critical - Candidate planning could become implicit execution
- Why it matters: The capture plan requires separate mission approval.
- Fix recommendation: state that result summary and harness profile are future outputs only.

### F2 - High - Docs-only candidate could be too trivial
- Why it matters: Phase 4 needs execution reliability signals, not only document compliance.
- Fix recommendation: require command, verification, evidence-gap, and FP/FN fields even for a docs-only index update.

### F3 - High - No telemetry could miss the natural negative-case gap
- Why it matters: `NO_TELEMETRY` cannot close the Phase 3 gap.
- Fix recommendation: keep the gap explicit and do not claim closure.

### F4 - High - Index wording could imply promotion evidence
- Why it matters: the first capture triggered a natural-language pilot warning before wording was tightened.
- Fix recommendation: require same-paragraph non-promotion wording anywhere V3 approval or operational status is referenced.

## Blocking Findings
- None after hardening.
