# Candidate Advisory Record Fields

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Planning-only candidate shape.

This is design evidence, not an implemented schema or template.

## Existing Field Semantic Revision
`mission.commit_after` remains the only final-commit field.

| Value shape | Planned meaning |
| --- | --- |
| literal commit hash | Final commit claimed; optionally replay-checkable |
| `same_commit` | Record was introduced with the mission closeout commit |
| `not_recorded` | Evidence unavailable or historical; valid but limited |
| placeholder such as `pending_*` | Contradictory for completed records; advisory finding when supplied |
| unavailable literal commit | Replay limitation; do not silently rewrite |

## Optional `execution.verification.observations[]`
Fields: `source_kind`, `captured_date`, `actor_ref`, `session_ref`, `command_or_check_ref`, `result`, `evidence_refs`, `supersedes_original`.

Rules: `source_kind` is `original_run`, `replay`, or `post_run_audit`; `supersedes_original` must be false; reference evidence instead of embedding logs.

## Optional `reviews.verifier_provenance`
Fields: `builder_actor_ref`, `verifier_actor_ref`, `actor_relationship`, `session_relationship`, `independence_status`, `evidence_refs`, `unresolved_gap`.

Rules: same actor cannot be `independent`; script separation alone maps to `deterministic_separation_only`; refs are coarse and non-secret.

## Optional `execution.visual_evidence[]`
Fields: `artifact_ref`, `sha256`, `hash_verdict`, `visual_verdict`, `viewport`, `reviewer_actor_ref`, `reviewed_date`, `findings`.

Rules: hash and visual verdicts are independent; one artifact's PASS cannot override another artifact's FAIL.

## Optional `reviews.boundary_claims[]`
Fields: `claim`, `proof_status`, `proof_scope`, `evidence_refs`, `limit`.

Rules: statuses are `PROVED`, `WEAK`, `MISSING`, `CONTRADICTED`; static/change-range scope cannot imply global runtime absence; `limit` is required for positive claims.

## Deferred Family
Do not add mission outcome, observed exposure, or endurance coverage fields to the base record now. `record.decision_state` remains the mission outcome. Checkpoints, closeouts, and decision packs retain exposure/coverage evidence until natural sustained missions justify a stable profile-specific shape.

## Compatibility
All additions are optional. Their absence changes no current record status, finding, or deterministic output.
