# Factory v3 Mission Record Design v0

## Version
v0.8

## Change Log
- v0.8 (2026-06-10): Added model-identity recording guidance and an optional `model_routing` template field under the mutable-harness-state principle; new records should record model identity when the harness exposes it, retiring reliance on the Phase 3 missing-model-identity acceptability note.
- v0.7 (2026-06-08): Added nested standalone POC safety-flag checks for optional real-data, synthetic-only, live-integration, and dependency-use claims, with malformed fixture coverage.
- v0.6 (2026-06-06): Added optional passive evidence replay mode for mission-record claims, including record-file filtering, evidence-root resolution, file/reference checks, JSON parse checks, checkpoint/interrupt lookup, and external verification evidence checks.
- v0.5 (2026-06-05): Added advisory schema-version routing for Factory V3 shadow records, standalone POC nested records, standalone POC adaptive mission control records, standalone POC flat records, and legacy flat POC migration warnings.
- v0.4 (2026-05-25): Added a valid blocked missing-authority shadow fixture, with advisory blocked-state consistency checks.
- v0.3 (2026-05-25): Added valid halted verification-failure and stale-reentry shadow fixtures, with advisory halted-state consistency checks.
- v0.2 (2026-05-24): Added malformed-record fixture coverage and a standalone advisory mission-record validator with deterministic expected outputs.
- v0.1 (2026-05-24): Initial shadow mission-record design derived from the first five Phase 1 `V3-OP-001` trials.

## Status
Research-only shadow design. This document is non-enforcing: it does not make Factory v3 the default, approve new V3 profiles, deprecate Factory v2, wire V3 into required gates, or implement runtime authority.

## Purpose
Define the smallest useful machine-readable mission record for optional `V3-OP-001` work.

The record is a replay aid for bounded coding missions. It is not a runtime governance kernel, not a proof ledger, not a telemetry system, and not a replacement for Factory v2.

## Source Evidence
This design is derived from:

- `docs/Factory/v3/PHASE1_DECISION_REVIEW_V3_OP_001.md`
- `docs/Factory/v3/trials/TRIAL_INDEX.md`
- the five Phase 1 trial records under `docs/Factory/v3/trials/`

## Primary Artifact
Template:

```text
docs/Factory/v3/templates/V3_MISSION_RECORD_TEMPLATE.json
```

Backfilled examples:

```text
tests/fixtures/factory_v3_mission_record/
```

Advisory validator:

```text
scripts/factory_v3_mission_record_lint.py
```

## Design Principles

1. Capture observed Phase 1 evidence before adding new concepts.
2. Represent pre-envelope rejection as a valid terminal decision state.
3. Represent thread-local mission envelopes without forcing file-scope expansion.
4. Keep local command evidence first-class.
5. Preserve V2 fallback as an explicit field.
6. Keep advisory checks optional because adopting repos may not have starter-kit scripts.
7. Avoid chain-of-thought, full chat transcripts, and vendor-private cognition state.
8. Avoid runtime-kernel authority, production proof, lease enforcement, telemetry, or governance routing.

## Decision States

| State | Meaning |
|---|---|
| `pre_envelope_fallback` | V3 was considered but stopped before mission-envelope creation because authority, scope, commands, verification, or profile eligibility was missing. |
| `completed_with_v3` | V3 executed within `V3-OP-001` scope and verification completed without fallback. |
| `halted` | V3 started and then stopped because verification did not pass, scope expanded, authority was missing, or another halt rule fired. No further execution is implied by this state. |
| `blocked` | The work could not safely proceed and no execution occurred. |

Phase 1 produced `pre_envelope_fallback` and `completed_with_v3` records. Phase 2 now includes synthetic valid `halted` fixtures for verification failure and stale reentry, plus a synthetic valid `blocked` fixture for missing authority.

## Required Field Groups

| Group | Purpose |
|---|---|
| `record` | Schema identity, status, profile, decision state, and source evidence. |
| `mission` | Objective, repository, harness, user, and envelope mode. |
| `authority` | Authorized files, forbidden scope, allowed commands, dependency policy, and V2 fallback requirement. |
| `execution` | Files changed, verification commands, command results, halt/fallback result, and advisory checks. |
| `reviews` | SIMPLE-CODE-GATE, fallback/halt review, friction notes, and false-positive/false-negative notes. |
| `phase2_design_signals` | Lessons that should shape later schema, validator, or fixture work. |

## Envelope Modes

| Mode | Meaning |
|---|---|
| `not_created_pre_envelope_fallback` | No mission envelope was created because V3 was rejected before authority was granted. |
| `thread_local` | The envelope stayed in the chat thread because creating an artifact would have expanded the authorized file scope. |
| `file_artifact` | A repository file contains the mission envelope and is inside the authorized artifact scope. |

## Shadow Record Rules

- A mission record may be created after the fact from closeout evidence.
- A mission record must not imply enforcement.
- A mission record must not expand authorized files during execution.
- A mission record must identify missing evidence with explicit `not_recorded` or `not_run` values.
- A mission record must preserve whether V2 fallback was used or retained.
- A mission record should record model identity when the harness exposes it; `not_recorded` remains valid only where the harness does not expose model identity, and the gap stays explicit.

## Model Identity And Mutable Harness State

`MUTABLE_HARNESS_STATE.md` names model identity, skill state, and credential state as harness-resident state that can mutate independently of the mission record.

For records, the advisory guidance is:

- Record the `model` value when the harness exposes it (for example a model ID string).
- When vendor model routing or automatic model selection is enabled, use the optional `model_routing` template object to mark routing as enabled and list the observed model set when known.
- Records authored before v0.8, and records from harnesses that hide model identity, remain valid with `not_recorded`; nothing here invalidates existing evidence.
- Any skill relied on for verification should have its identity and version named in the record, per the `HP_20260530_001` watchpoints.

Advisory validator support for these fields is a named follow-up requiring a separately approved change; this section adds no validator behavior.

## Advisory Validator

The standalone advisory validator reads one mission-record JSON file or a directory of JSON files:

```bash
python3 scripts/factory_v3_mission_record_lint.py --target tests/fixtures/factory_v3_mission_record --json
```

It emits JSON with `blocking_effect: none` and only advisory statuses:

- `ADVISORY_PASS`
- `ADVISORY_WARN`
- `ADVISORY_FAIL_NON_BLOCKING`

The validator is a replay and fixture aid only. It is not wired into `factoryctl`, CI, merge preflight, `knowledge_lint.sh`, `stage-lint`, `pack-lint`, mission lint, or any required Factory v2 gate.

Deterministic expected outputs live under:

```text
tests/fixtures/factory_v3_mission_record/expected/
```

The validator reports `checked_schema_versions` for every scanned JSON record. Supported advisory schema routes are:

| Route | Meaning |
|---|---|
| `factory_v3_shadow_v0_1` | Current V3 shadow record shape used by `V3-OP-001` fixtures. |
| `poc_standalone_v0_1` | Nested standalone POC record without adaptive mission control evidence. |
| `poc_standalone_v0_1_amc` | Nested standalone POC record with adaptive mission control evidence. |
| `poc_standalone_flat_v0_1` | Top-level standalone POC closeout/evidence record shape. |
| `poc_legacy_flat` | Earlier flat POC evidence shape; accepted with an advisory migration warning when otherwise well-formed. |

Optional passive evidence replay can be enabled with:

```bash
python3 scripts/factory_v3_mission_record_lint.py \
  --target <record-or-directory> \
  --record-files-only \
  --replay-evidence \
  --evidence-root <repo-root> \
  --json
```

Evidence replay does not execute recorded commands. It resolves referenced files, parses referenced JSON, checks checkpoint and interrupt references, and searches related evidence files for verification-command or verification-label mentions. Replay findings are advisory only and keep `blocking_effect: none`.

Valid shadow fixtures currently cover completed missions, pre-envelope fallback, halted verification failure, halted stale reentry, and blocked missing authority.

Malformed-record fixtures currently cover missing authorized files, missing allowed commands, missing verification result, halted-state inconsistency, blocked-state inconsistency, fallback without reason code, thread-local envelope without reference, and unsafe approval-scope flags.

## Out Of Scope For v0

- JSON Schema validation.
- `factoryctl` integration.
- CI or merge-preflight checks.
- Continuous telemetry.
- Runtime authority enforcement.
- Governance routing.
- Capability profiling.
- External governance-kernel adapters.

## Next Step
Use the advisory validator against future shadow records. Future fixture additions should come from real evidence or an approved Phase 2 design task.
