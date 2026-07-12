# Risk Register - Mission 026 Claim Audit

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E risk register.

| ID | Risk | Severity | Mitigation | Verification |
| --- | --- | --- | --- | --- |
| C-001 | Partial evidence causes profile promotion | Critical | Explicit `NO PROMOTION YET`; map all five decision items | advisory/NL eval; manual review |
| C-002 | POC source is mutated | Critical | exact-commit temporary clone; source status before/after | no-touch status comparison |
| H-001 | Replay is conflated with original logs | High | separate evidence columns and dates | audit structure review |
| H-002 | Absence claims are overgraded | High | require direct corroboration or `WEAK` | claim review |
| H-003 | Verifier independence is overstated | High | name builder/script/auditor roles | FP/FN review |
| H-004 | Screenshot claims lack visual proof | High | SHA-256 plus independent image inspection | hash and image evidence |
| H-005 | Claim ledger omits material closeout claims | High | source-to-claim coverage checklist | claim inventory reconciliation |
| H-006 | Stale record field is missed | High | mandatory contradiction row | JSON/source check |
| H-007 | Endurance false negative or false positive recurs | High | separate mission PASS and observed exposure | adjudication review |
| H-008 | Existing Factory working-tree changes are overwritten | High | no reversions; path/diff review | `git status`, diff review |
| M-001 | Replay fails due environment rather than product | Medium | record exact limitation; do not repair source | replay command evidence |
| M-002 | Canon updates expand beyond pointers | Medium | nine-file product cap | changed-path count |

## Residual Risk
This audit can strengthen evidence classification but cannot create organizationally independent verification or recover missing original command logs.
