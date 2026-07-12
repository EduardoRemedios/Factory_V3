# Intent Synthesis - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage C Blue synthesis.

## Recommendation
`ADOPT_NARROW_SET`

## Field-Family Decisions
| Family | Decision | Proposed treatment | Evidence basis |
| --- | --- | --- | --- |
| Final-commit consistency | `REVISE` | Keep `mission.commit_after`; define later advisory semantics/checks for literal hash, `same_commit`, `not_recorded`, placeholders, and unavailable commits. Do not add a duplicate field | M026-FN-01; existing design already defines `same_commit` |
| Original versus replay provenance | `ADOPT` | Optional `execution.verification.observations[]` with bounded source kind, captured date, actor/session refs, result, evidence refs, and `supersedes_original: false` | M026-C09-C13; replay must not overwrite original summaries |
| Verifier provenance | `ADOPT` | Optional `reviews.verifier_provenance` with builder/verifier refs, actor relationship, session relationship, independence status, evidence refs, and unresolved gap | M026-C12; M026-FP-01 |
| Per-artifact visual evidence | `ADOPT` | Optional `execution.visual_evidence[]` with artifact ref, hash, hash verdict, visual verdict, viewport, reviewer ref, reviewed date, and findings | M026-C07-C08/C19; M026-FN-02 |
| Bounded absence claims | `ADOPT` | Optional `reviews.boundary_claims[]` with claim, proof status, proof scope, evidence refs, and explicit limit | M026-C14-C16; M026-FP-02 |
| Mission/exposure/endurance separation | `DEFER` field addition | Keep `record.decision_state` authoritative for mission outcome. Keep exposure/coverage in checkpoints, closeout, and decision packs until at least two natural sustained missions support a stable profile-specific shape | M026-C20; decision-pack items 1/3 remain insufficient |

## Candidate Vocabularies
- Verification observation source kind: `original_run`, `replay`, `post_run_audit`.
- Actor relationship: `different_actor`, `same_actor`, `unknown`.
- Session relationship: `different_session`, `same_session`, `unknown`.
- Independence status: `independent`, `deterministic_separation_only`, `not_independent`, `unknown`.
- Hash verdict: `match`, `mismatch`, `not_checked`, `not_applicable`.
- Visual verdict: `pass`, `fail`, `limited`, `not_checked`, `not_applicable`.
- Claim proof status: `PROVED`, `WEAK`, `MISSING`, `CONTRADICTED`.
- Claim proof scope: `change_range`, `repository_static`, `runtime_trace`, `artifact_only`, `self_attested`, `unknown`.

## Compatibility Rules
1. Every new object/array is optional.
2. Absence produces no finding for v0.1 records.
3. Existing `execution.verification` remains valid and authoritative for the record's summary.
4. Observations append provenance and never supersede original evidence.
5. Pre-envelope, blocked, and halted records may omit all additions.
6. No historical record is rewritten solely to adopt the shape.
7. Validator blocking effect remains `none`.

## Source-Of-Truth Rule
The mission record indexes and summarizes evidence. It does not replace the authored mission envelope, checkpoints, mission state, verification output, closeout, Git history, screenshots, or decision pack.

## Resolved Red-Team Findings
- RT-H1: four bounded structures only; no mission-control embedding.
- RT-H2: existing commit field retained.
- RT-H3: coarse refs and explicit independence status.
- RT-H4: bounded observations reference external evidence; no logs/events.
- RT-H5: endurance fields deferred.

## Later Implementation Decision
A later fixture-first advisory run is justified, but only after human review of this pack. It should begin with template/docs and deterministic fixtures, then add the smallest validator checks needed for internally contradictory supplied fields. It must not require new fields or rewrite old outputs silently.
