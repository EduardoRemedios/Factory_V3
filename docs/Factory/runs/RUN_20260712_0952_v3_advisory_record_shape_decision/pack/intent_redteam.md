# Intent Red Team - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage B challenge review using `factory-challenge-mission`.

## Challenge Result
`CONDITIONAL PASS`

## Critical Findings
- None. The run is planning-only and grants no implementation or runtime authority.

## High Findings
### RT-H1 - Mission-control contract embedding would overgrow the replay record
Copying loop admission, next-action, safe-hold, re-entry, and proof structures into the v0.1 mission record would create a second mission-state source and violate the record's narrow purpose.

Repair: admit only fields tied directly to Mission 026 audit defects. Preserve authored envelope/checkpoint/state/closeout artifacts as authority.

### RT-H2 - Commit finalization is primarily a semantic/checking defect
Adding a second commit field would duplicate `mission.commit_after` and create disagreement risk.

Repair: retain the existing field and recommend later advisory consistency semantics for literal hash, `same_commit`, `not_recorded`, placeholder, and unavailable cases.

### RT-H3 - Actor independence can be overstated or leak vendor identity
Names such as “verification_worker” do not prove independence, while raw user/session identifiers create unnecessary data retention.

Repair: use coarse actor/session references and explicit relationship/independence enums. Never infer independence from script separation.

### RT-H4 - Replay provenance can become a proof ledger
An unconstrained event list would duplicate telemetry and raw command logs.

Repair: record bounded verification observations with references to external evidence; do not embed logs, transcripts, cognition, or event streams.

### RT-H5 - Endurance fields are premature in the base V3-OP-001 record
The evidence gap belongs to candidate `V3-OP-003`; adding profile-specific fields to every base record would create authoring burden before a stable natural-evidence pattern exists.

Repair: keep outcome in `record.decision_state`, keep observed exposure in authored checkpoint/closeout evidence, and defer record fields until at least two useful sustained missions show a stable need.

## Medium / Low Findings
- Visual evidence arrays need bounded cardinality or references only.
- Boundary claims need an explicit proof-scope vocabulary to prevent global absence claims from static diffs.
- New optional fields must not make pre-envelope or blocked records verbose.

## Assumptions To Resolve
- Existing schema routes remain accepted when every new object is absent.
- A later validator can add new checks without changing blocking effect from `none`.

## Authority Gaps
- No authority exists to edit templates, validator, fixtures, or canon in this run. Correctly deferred.

## Verification Gaps
- Later implementation must prove old deterministic outputs are unchanged or intentionally versioned.
- Later fixture coverage must include same-worker/same-session verification and hash-pass/visual-fail evidence.

## Fallback Triggers
- Route to `REVISE_AND_REVIEW` if the proposal needs a generic extension framework, migration, or required-field semantics.
- Route to `DEFER_ALL` if optional provenance cannot improve replay without duplicating source artifacts.

## Recommended Repairs
Adopt four narrow optional structures, revise existing commit semantics without a duplicate field, and defer endurance fields.

## Execution Readiness
Planning may continue. This challenge result is not approval to implement.
