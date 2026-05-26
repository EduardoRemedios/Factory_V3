# Risk Register: Phase 4 Fixture Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| RISK-01 | Critical | Threshold checks imply routing. | Detect risky wording only and preserve non-operational language. | TRACE-01 |
| RISK-02 | Critical | Advisory eval gains blocking behavior. | Preserve `blocking_effect: none`. | TRACE-02 |
| RISK-03 | High | Synthetic fixtures are overstated. | Label all `V3-P4-*` cases synthetic. | TRACE-03 |
| RISK-04 | High | Evaluator change becomes broad parser. | Add direct trigger checks only. | TRACE-04 |
| RISK-05 | High | Expected JSON drifts. | Run fixture eval with `--expect`. | TRACE-05 |
| RISK-06 | High | V2 fallback language weakens. | Include V2 fallback risk coverage. | TRACE-06 |
| RISK-07 | Medium | FP/FN rollup shape is too vague. | Add exact classification finding. | TRACE-07 |
