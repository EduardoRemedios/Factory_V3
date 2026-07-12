# Intent Synthesis - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage C synthesis.

## Bound Repairs
- BR-1: capture baseline report before edits; after edits, compare all pre-existing checked-record entries, schema routes, and findings exactly. Aggregate growth is allowed only for five named fixtures.
- BR-2: MR085 matches explicit `pending`, `placeholder`, or equivalent unfinished text only for `completed_with_v3`; `same_commit`, plausible literal hashes, and `not_recorded` do not trigger it.
- BR-3: visual `pass`, `fail`, `limited`, `not_checked`, and `not_applicable` are valid. MR083 checks missing/invalid fields, not product quality.
- BR-4: optional arrays/objects absent = no-op. Boundary claim proof requirements activate only for supplied `PROVED` claims.
- BR-5: product scope is exactly 18 named paths; seven canon pointers receive status-only reconciliation.

## Implementation Shape
1. Document and template optional fields.
2. Add rich valid fixture and four contradiction fixtures.
3. Add direct helper functions to the existing shadow-record lint path; no framework or route abstraction.
4. Regenerate only `expected/all.json` and `expected/invalid.json` after subset comparison passes.
5. Reconcile seven active pointers with same-context advisory/non-promotion language.

## SIMPLE-CODE-GATE
Use direct validation helpers owned by `_lint_record`; avoid schema engines, registries, plugin layers, generic walkers, or dependencies.

## Remaining Issues
None blocking.
