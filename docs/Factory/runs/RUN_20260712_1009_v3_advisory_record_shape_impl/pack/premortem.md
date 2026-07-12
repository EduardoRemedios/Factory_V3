# Pre-Mortem - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E pre-mortem.

Assume implementation passed aggregate lint but damaged the advisory contract.

## Failure Modes
1. Expected outputs were regenerated over unintended old findings.
   - Signal: representative old fixture mismatch before regeneration.
   - Control: MS-00 baseline and named old-fixture checks gate MS-03.
2. Optional fields became completeness requirements.
   - Signal: any old record gains MR081-MR084.
   - Control: helpers return no findings when objects are absent.
3. MR085 flags `not_recorded` or pre-envelope records.
   - Signal: old historical fixtures change.
   - Control: narrow placeholder pattern plus completed-state condition.
4. Visual FAIL is rejected instead of preserved.
   - Signal: rich valid fixture fails because visual verdict is `fail`.
   - Control: validate vocabulary/shape only.
5. Validator logic becomes a generic schema engine.
   - Signal: registry, recursive walker, dependency, or route abstraction added.
   - Control: direct local helpers and SIMPLE-CODE-GATE.
6. Canon implies promotion or enforcement.
   - Signal: optional/non-blocking/`NO PROMOTION YET` missing from same context.
   - Control: advisory lint and pointer review.

## Verdict
Proceed only with compatibility-first fixture gates and direct checks.
