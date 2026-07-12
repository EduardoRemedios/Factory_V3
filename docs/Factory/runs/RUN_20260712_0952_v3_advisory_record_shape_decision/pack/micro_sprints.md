# Micro-Sprints - Later Advisory Record Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage G planning sequence; not authorized for execution.

## MS-00 - Compatibility Baseline
- Objective: capture current deterministic outputs and exact existing-record behavior.
- Entry: later execution-enabled pack has I2 PASS and human Go.
- Exit: per-record expected outputs identified; no product edit.
- Stop/go: STOP if baseline is not reproducible.

## MS-01 - Design And Template
- Objective: update mission-record design and template with only the four optional structures and commit semantic clarification.
- Entry: MS-00 GO and exact product paths authorized.
- Likely files: `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`, `docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json`.
- Exit: JSON parses; existing required groups unchanged; endurance fields absent.
- Stop/go: STOP on required-field or migration need.

## MS-02 - Fixture-First Coverage
- Objective: add valid and invalid fixtures for replay, verifier, visual, boundary claim, and commit consistency cases.
- Entry: MS-01 GO; updated template parses.
- Likely files: new files under `tests/fixtures/factory_v3_mission_record/`; deterministic expected outputs.
- Exit: existing fixture outputs unchanged; new cases express locked semantics.
- Stop/go: STOP if old records need rewriting.

## MS-03 - Smallest Advisory Validator Support
- Objective: check only internally contradictory supplied fields.
- Entry: MS-02 GO; fixture semantics locked.
- Likely file: `scripts/factory_v3_mission_record_lint.py`.
- Exit: optional absence is a no-op; `blocking_effect: none`; exact expected outputs pass.
- Stop/go: STOP on generic framework, schema migration, CI/factoryctl wiring, or status promotion.

## MS-04 - Active Canon Reconciliation
- Objective: update only directly affected status/index/changelog surfaces.
- Entry: MS-03 GO and exact pointer inventory approved.
- Likely files: V3 README/roadmap, project state/roadmap, changelog; exact set requires later envelope.
- Exit: same-paragraph advisory/non-promotion language retained.
- Stop/go: STOP on unrelated roadmap churn.

## MS-05 - Independent Closeout
- Objective: run all deterministic and advisory checks and verify scope.
- Entry: MS-04 GO; complete candidate diff available.
- Exit: compatibility, fixture, validator, knowledge, advisory, pack, and diff checks pass.
- Stop/go: STOP on changed old outputs, new authority, or required-gate behavior.

## Authorization Boundary
These micro-sprints are a candidate sequence only. A later `EXECUTION_ENABLED` pack and post-I2 human Go are required.

## Bounded Deferral Hooks
- D-001 Template/fixture/validator implementation -> MS-00 through MS-05 in a later approved run.
- D-002 Endurance/exposure record fields -> MS-05 records continued deferral until at least two natural sustained missions support a stable profile-specific shape.
- D-003 Historical POC repair/backfill -> MS-05 confirms historical records remain untouched unless a different future envelope explicitly authorizes repair.
