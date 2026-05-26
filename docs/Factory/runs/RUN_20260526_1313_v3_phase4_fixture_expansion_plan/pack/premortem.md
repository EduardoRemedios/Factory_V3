# Premortem: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage E premortem.

## Failure Scenarios
- PM1 Critical: Threshold fixture language becomes a routing recommendation. Mitigation: only detect risky wording; never route work.
- PM2 Critical: Evaluator output stops being advisory. Mitigation: keep `blocking_effect: none` and `promotion_decision: not_authorized`.
- PM3 High: Synthetic fixtures are treated as real negative-case evidence. Mitigation: label all eight planned fixtures as synthetic design coverage.
- PM4 High: Script changes become a schema or scoring framework. Mitigation: add direct trigger checks only.
- PM5 High: Expected JSON is updated inconsistently. Mitigation: run deterministic fixture eval with `--expect`.
- PM6 High: V2 fallback language weakens in fixture text. Mitigation: include V2 fallback preservation fixture.
- PM7 Medium: FP/FN rollup support claims human adjudication that did not occur. Mitigation: model shape and missing fields only.
- PM8 Medium: Phase 3 gap disappears from new fixtures. Mitigation: include an evidence-quality fixture for explicit gap retention.

## Planning Consequence
The future execution should be small, mechanical, and fully covered by expected fixture output.
