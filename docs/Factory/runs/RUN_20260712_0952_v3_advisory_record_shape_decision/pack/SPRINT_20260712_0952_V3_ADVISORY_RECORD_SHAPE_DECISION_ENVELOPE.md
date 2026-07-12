# Sprint Envelope - Advisory Mission-Record Shape Decision

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage H planning-only envelope.

## Sprint Identity
- Sprint ID: `SPRINT_20260712_0952_V3_ADVISORY_RECORD_SHAPE_DECISION`
- Run ID: `RUN_20260712_0952_v3_advisory_record_shape_decision`
- Execution mode: `PLANNING_ONLY`
- Recommendation: `ADOPT_NARROW_SET`

## Objective
Deliver a reviewable decision pack for four optional evidence-provenance structures, revised semantics on the existing final-commit field, and deferral of base-record endurance fields.

## Authorized Current-Run Files
Only files under this run root. No V3 product/canon/template/validator/fixture file is authorized for change.

## Current File-Touch Budget
| Category | Maximum |
| --- | ---: |
| Product files | 0 |
| Planning artifacts under this run root | Required A-I2 artifact set only |

## Locked Candidate Shape
- Optional `execution.verification.observations[]`.
- Optional `reviews.verifier_provenance`.
- Optional `execution.visual_evidence[]`.
- Optional `reviews.boundary_claims[]`.
- Existing `mission.commit_after` receives later semantic/validator clarification; no duplicate field.
- Endurance/exposure fields remain deferred from the base record.

## Compatibility Contract
1. Every addition is optional.
2. Existing records and schema routes remain accepted unchanged.
3. Missing additions emit no finding.
4. Old per-record deterministic outputs remain stable.
5. New checks apply only when new fields are supplied or a completed record contains an explicit placeholder commit.
6. The record references evidence; it does not embed logs or replace authored mission artifacts.

## Candidate Later Implementation Envelope
This section is decision preparation, not authorization.

Likely product files:
- `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`
- `scripts/factory_v3_mission_record_lint.py`
- up to five new valid/invalid JSON fixtures under `tests/fixtures/factory_v3_mission_record/`
- `tests/fixtures/factory_v3_mission_record/expected/all.json`
- up to five directly affected active status/index/changelog files selected by a later pack

Candidate maximum: 14 product files. The later execution pack must inventory exact paths and may reduce this cap; it may not infer authority from this planning envelope.

## Allowed Later Commands (candidate only)
- JSON parse commands.
- Existing mission-record deterministic lint with `--expect`.
- V3 advisory and operational-readiness checks.
- Knowledge lint, stage/pack lint, context index, Python compile, and `git diff --check`.

No dependency install, network write, POC mutation, historical record rewrite, required-gate integration, CI wiring, runtime work, routing, promotion, commit, or push is implied.

## Verification Contract
- Run VP-001 through VP-004 for this planning pack.
- A later execution-enabled pack must run VI-001 through VI-011 and provide a verification manifest.
- Any changed existing fixture output requires explicit human review; silent output churn is a halt.

## Halt Conditions
- Any candidate becomes required.
- A new generic extension/plugin/schema framework is proposed.
- Authored mission state is duplicated.
- Raw logs, transcripts, cognition, secrets, or direct personal identifiers enter records.
- Same-worker verification is labeled independent.
- Hash identity is treated as visual correctness.
- Static evidence is treated as global runtime absence.
- Endurance fields or artificial duration floors enter the base record.
- Runtime, required-gate, routing, telemetry enforcement, or profile authority is implied.

## Completion Conditions
- Complete A-I2 pack with PASS.
- Human receives a clear `ADOPT_NARROW_SET` recommendation and field-level decisions.
- No product file changed.
- Later implementation remains separately gated.
