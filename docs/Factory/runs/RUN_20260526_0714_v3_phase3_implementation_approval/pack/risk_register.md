# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risk register for Phase 3 implementation approval.

| ID | Severity | Risk | Mitigation | Verification Hook |
|---|---|---|---|---|
| R1 | High | Required-gate drift. | Keep validator standalone with `blocking_effect: none`. | Advisory lint and diff review. |
| R2 | High | Sensitive data in fixtures. | Use synthetic excluded-data markers only. | Fixture review. |
| R3 | High | Runtime collection starts too early. | Approve fixture-first implementation only. | Approval artifact scope. |
| R4 | Medium | Validator abstraction bloat. | One script, no dependencies, direct checks. | SIMPLE-CODE-GATE review. |
| R5 | Medium | Mission record conflict. | Replay uses mission record as shadow context and does not replace it. | Source-of-truth checklist. |
