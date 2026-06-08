# Factory v3 Mission Record Fixtures

## Change Log
- v0.3 (2026-06-08): Added malformed nested POC safety-flag regression coverage for real-data, synthetic-only, live-integration, and dependency-use flags.
- v0.2 (2026-06-05): Added versioned POC standalone fixtures for nested, nested adaptive mission control, flat standalone, and legacy flat migration-warning shapes.
- v0.1 (2026-05-27): Added unsafe path-shape regression fixture for advisory scope evidence.

## Status
Research-only shadow fixtures. These examples are non-enforcing and do not approve new V3 profiles, make V3 the default, deprecate V2, or wire V3 into required gates.

## Purpose
Backfit the v0 mission-record shape against the first five Phase 1 `V3-OP-001` trials and synthetic Phase 2 design cases approved by the roadmap.

The root trial and synthetic design fixtures are valid shadow examples. `invalid/` contains malformed record-shape fixtures for the standalone advisory validator, and `expected/` contains deterministic output fixtures for valid, invalid, and mixed-directory checks.

`versioned/` contains compact schema-routing fixtures for `factory_v3_shadow_v0_1`, `poc_standalone_v0_1`, `poc_standalone_v0_1_amc`, `poc_standalone_flat_v0_1`, and legacy flat POC migration warnings.

The synthetic halted and blocked fixtures cover verification failure, stale reentry, and missing authority without approving telemetry, runtime authority, required gates, or V3 default-mode behavior.

The validator is `scripts/factory_v3_mission_record_lint.py`. It is advisory only, emits `blocking_effect: none`, and is not wired into `factoryctl`, CI, or any required Factory v2 gate.
