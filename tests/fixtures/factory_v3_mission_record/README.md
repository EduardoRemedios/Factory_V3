# Factory v3 Mission Record Fixtures

## Status
Research-only shadow fixtures. These examples are non-enforcing and do not approve new V3 profiles, make V3 the default, deprecate V2, or wire V3 into required gates.

## Purpose
Backfit the v0 mission-record shape against the first five Phase 1 `V3-OP-001` trials and synthetic Phase 2 design cases approved by the roadmap.

The root trial and synthetic design fixtures are valid shadow examples. `invalid/` contains malformed record-shape fixtures for the standalone advisory validator, and `expected/` contains deterministic output fixtures for valid, invalid, and mixed-directory checks.

The synthetic halted fixtures cover verification failure and stale reentry without approving telemetry, runtime authority, required gates, or V3 default-mode behavior.

The validator is `scripts/factory_v3_mission_record_lint.py`. It is advisory only, emits `blocking_effect: none`, and is not wired into `factoryctl`, CI, or any required Factory v2 gate.
