# Factory v3 Phase 3 Telemetry And Evidence Replay Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial planning-only telemetry/replay plan.

## Status
Planning-only. This document is research-only and non-enforcing: it does not implement telemetry, approve telemetry emitters, add replay validators, wire V3 into required gates, create runtime authority, create proof, enforce leases, add governance routing, promote V3 as default, or remove V2 build-support scaffolding.

## Purpose
Define the smallest future telemetry/replay shape that could make `V3-OP-001` execution evidence easier to replay and diagnose.

This plan starts from the Phase 2.5 decision to keep mission records as optional shadow evidence. It defines what a later implementation pack should build first, and what it must not collect.

## Scope
Applies only to future optional shadow telemetry for `V3-OP-001 Bounded Code Change`.

The future telemetry log is a replay aid. It is not a governance kernel, audit-proof ledger, enforcement system, CI gate, or replacement for V2 planning while V3 remains maturing.

## Design Principles
1. Collect only operational facts needed to replay mission state.
2. Keep the mission record as the primary shadow context.
3. Make telemetry append-only in shape, but advisory in effect.
4. Prefer summaries and references over large payloads.
5. Avoid chain-of-thought, full chat transcripts, secrets, private vendor cognition state, and external governance-kernel proof.
6. Keep the first implementation small enough to validate with deterministic fixtures.

## Proposed Artifact Shape
Future implementation should start with a mission-local JSON Lines file.

```text
V3_TELEMETRY.jsonl
```

This filename is provisional. The implementation pack may place fixtures under `tests/fixtures/factory_v3_telemetry_replay/` before recommending any real-run artifact location.

Each line should be one JSON object with a shared envelope plus a type-specific `payload`.

## Common Event Fields

| Field | Required | Meaning |
|---|---|---|
| `schema_version` | yes | Telemetry schema version, starting at `0.1`. |
| `mission_id` | yes | Mission identifier matching the V3 mission record. |
| `record_id` | yes | Mission-record identifier when available. |
| `sequence` | yes | Monotonic integer starting at 1. |
| `event_id` | yes | Stable event identifier unique within the mission. |
| `event_type` | yes | One of the approved event types. |
| `occurred_at` | yes | Timestamp or `not_recorded` if unavailable in backfill. |
| `actor` | yes | `human`, `agent`, `tool`, or `system`. |
| `source` | yes | `live`, `backfill`, or `fixture`. |
| `summary` | yes | Short human-readable operational summary. |
| `payload` | yes | Type-specific object. |

## Initial Event Types

| Event Type | Purpose | Minimal Payload |
|---|---|---|
| `mission_considered` | Record that V3 was considered for work. | `profile_id`, `decision_state`. |
| `envelope_created` | Record mission-envelope creation or thread-local envelope reference. | `envelope_mode`, `reference`. |
| `authority_declared` | Record allowed files, forbidden scope, allowed commands, and dependency policy. | `authorized_files`, `forbidden_scope`, `allowed_commands`, `dependency_policy`. |
| `command_run` | Record execution of an allowed command. | `command_label`, `command_kind`, `result`, `exit_code`. |
| `file_change_summary` | Record touched files without storing file contents. | `paths`, `change_kinds`. |
| `verification_run` | Record verification command result. | `command_label`, `result`, `exit_code`. |
| `halt_triggered` | Record a halt condition. | `reason_codes`, `evidence_ref`. |
| `reentry_checked` | Record stale-reentry or resume checks. | `status`, `evidence_ref`. |
| `fallback_triggered` | Record V2 fallback or pre-envelope rejection. | `reason_codes`, `fallback_target`. |
| `human_decision` | Record approval, rejection, override, or clarification. | `decision`, `scope`, `evidence_ref`. |
| `closeout_recorded` | Record terminal mission outcome. | `decision_state`, `verification_result`, `residual_risks`. |

## Excluded Data

| Data | Rule |
|---|---|
| Chain-of-thought or hidden reasoning | Never store. |
| Full chat transcripts | Never store by default. Use short summaries or references. |
| Secrets, tokens, keys, cookies, credentials | Never store. Redact if accidentally observed. |
| Raw environment dumps | Never store. |
| Full command output | Do not store by default. Store result, exit code, and a short summary. |
| Source file contents or diffs | Do not store. Use paths and change categories. |
| Vendor-private cognition state or model internals | Never store. |
| External governance-kernel proof or private policy state | Never store in public Factory V3 artifacts. Use project-local adapters later if separately approved. |
| Personal data unrelated to mission replay | Do not store. Summarize or omit. |

## Data-Minimization Rules
1. Prefer `summary`, `evidence_ref`, and result codes over payload copies.
2. Keep command text limited to allowlisted commands or stable command labels.
3. Store file paths only when needed to compare against authorized scope.
4. Store failed verification evidence as result metadata, not full logs.
5. Require an explicit redaction note if a payload is omitted for privacy.
6. Treat backfilled events as lower-confidence by setting `source: backfill`.

## Future Fixture Shape
The first implementation pack should add fixtures before real-run telemetry.

Minimum valid fixtures:
- happy-path bounded code change,
- verification halt,
- pre-envelope fallback,
- stale reentry check,
- human clarification before execution.

Minimum invalid fixtures:
- non-monotonic sequence,
- command outside declared authority,
- file outside authorized scope,
- verification did not pass and later execution appears without a human decision,
- event after terminal closeout,
- payload containing excluded data marker.

## Replay Checks
Future advisory replay checks should reconstruct mission status from the mission record plus telemetry log.

Initial checks:
1. `mission_id` and `record_id` match the mission record.
2. Event sequence is monotonic and gap-free.
3. Authority is declared before command or file-change events.
4. Commands match allowed command labels or are explicitly marked fallback-only.
5. File paths stay within authorized files or are classified as violations.
6. Failed verification leads to `halt_triggered`, `fallback_triggered`, or an explicit human decision before further execution.
7. Terminal closeout appears once.
8. No execution events appear after terminal closeout.
9. Excluded-data markers are absent.
10. Backfilled events remain distinguishable from live events.

These checks remain advisory unless a later Factory run and explicit human approval promote them.

## Overhead Measurement Plan
When implementation exists, each pilot should record:
- event count,
- time spent creating telemetry,
- commands run,
- verification commands run,
- fields marked `not_recorded`,
- redactions made,
- replay findings,
- operator friction notes.

The overhead report should compare telemetry use against ordinary V2 and `V3-OP-001` closeout. Telemetry should not become recommended if it adds disproportionate burden for low-risk work.

## Source-Of-Truth Rule
Mission records remain optional shadow evidence. Telemetry is derived execution evidence. Neither replaces V2 run packs, human decisions, git history, or any project-owned source of truth.

## Promotion Criteria For Future Implementation
Future Phase 3 implementation may be proposed only after a separate V2-governed implementation pack names exact files, fixtures, validators, and verification commands.

Recommended telemetry use requires later evidence:
- telemetry fixture corpus,
- replay pass/fail fixtures,
- at least 3 real mission telemetry logs,
- overhead report,
- data-minimization review,
- false-positive and false-negative review,
- explicit non-enforcement confirmation.

## Next Step
Prepare a separate Phase 3 implementation pack for telemetry fixtures and an advisory replay validator.

That future pack must stay fixture-first and advisory-only unless a later human approval explicitly changes scope.
