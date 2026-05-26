# Intent Red Team: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage B red-team review.

## Iteration
- Iteration: 1 of max 2

## Findings

### F1 - Critical - Fixture expansion could become router design
- Why it matters: Threshold fixtures are close to Phase 5 routing.
- Fix recommendation: future checks must flag operational routing wording only; they must not recommend modes or route work.

### F2 - High - Synthetic cases could be mistaken for real evidence
- Why it matters: Phase 3 lacks a natural halted, fallback, or clarification-heavy case.
- Fix recommendation: fixture text and expected reports must identify synthetic design coverage and keep the gap explicit.

### F3 - High - Evaluator changes could grow beyond trigger checks
- Why it matters: Broad parsing, scoring, or schemas would exceed SIMPLE-CODE-GATE.
- Fix recommendation: add only explicit `EVAL_TRIGGER` checks and matching expected output.

### F4 - Medium - FP/FN fixture could imply completed human adjudication
- Why it matters: Phase 4 rollup shape is planned, not populated with real reviewer decisions.
- Fix recommendation: fixture should test missing or invalid adjudication shape, not claim live review.

## Verification Holes
- Need deterministic expected JSON update.
- Need advisory lint and natural-language pilot after future implementation.

## Blocking Findings
- None after intent hardening.
