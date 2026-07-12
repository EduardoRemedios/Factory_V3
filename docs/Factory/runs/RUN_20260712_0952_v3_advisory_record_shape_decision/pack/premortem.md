# Pre-Mortem - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E pre-mortem.

Assume a later implementation failed despite passing fixtures.

## Failure Modes
1. Optional fields became de facto mandatory through validator findings.
   - Early signal: old valid records change status or expected output.
   - Prevention: absence of every new field must be a no-op.
2. The record became a second mission-state or proof ledger.
   - Early signal: raw logs, checkpoint state, or next-action authority appears inline.
   - Prevention: evidence references only; authored artifacts remain authoritative.
3. Same-worker verification was labeled independent.
   - Early signal: independence derived from different script names.
   - Prevention: explicit relationship enums and unresolved gaps.
4. Screenshot hashes were treated as visual correctness.
   - Early signal: one combined browser PASS hides per-artifact failures.
   - Prevention: separate hash and visual verdict fields.
5. Static diff evidence supported global absence claims.
   - Early signal: `PROVED` with `change_range` scope is rendered as universal absence.
   - Prevention: mandatory proof scope and limit when a boundary claim object is present.
6. Endurance fields introduced artificial duration pressure.
   - Early signal: base records request elapsed targets or coverage PASS for short missions.
   - Prevention: defer the field family; preserve no-padding canon.
7. Actor/session references retained personal or vendor-private identifiers.
   - Early signal: emails, tokens, thread IDs, or full transcripts enter fixtures.
   - Prevention: coarse pseudonymous refs only; no secrets or cognition state.

## Pre-Mortem Verdict
The narrow set is viable only with explicit no-op absence behavior, reference-only evidence, and stable existing fixture outputs.
