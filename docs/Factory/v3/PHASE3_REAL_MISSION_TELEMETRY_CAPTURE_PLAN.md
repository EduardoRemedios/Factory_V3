# Factory v3 Phase 3 Real Mission Telemetry Capture Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial planning-only capture plan for the first real `V3-OP-001` telemetry pilots.

## Status
Planning-only, research-only, and non-enforcing. This document does not collect real mission telemetry and does not approve required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal.

## Purpose
Define the first real telemetry capture shape for Phase 3 after the synthetic replay validator has been implemented.

The goal is to collect a small number of real `V3-OP-001` mission logs that can be replayed by `scripts/factory_v3_telemetry_replay_lint.py` while preserving data minimization and advisory-only behavior.

## Scope
This plan applies only to future real `V3-OP-001 Bounded Code Change` telemetry pilots in this repository.

The first capture set is limited to 3 real V3 repository missions:

1. one small docs-only mission,
2. one small fixture or validator maintenance mission,
3. one halted, fallback, or clarification-heavy mission if a suitable real case occurs.

If no natural halted, fallback, or clarification-heavy mission occurs, do not manufacture one. Record the gap and continue with a later pilot.

## Proposed Storage Location
Future real telemetry pilots should use:

```text
docs/Factory/v3/telemetry/pilots/<PILOT_ID>/
```

Each pilot directory should contain:

- `V3_TELEMETRY.jsonl`
- `OVERHEAD.md`
- `REDACTION_REVIEW.md`
- `REPLAY_REPORT.json`

The pilot should link to the corresponding shadow mission record under:

```text
docs/Factory/v3/mission_records/
```

No real telemetry files are added by this plan.

## Pilot ID Format
Use:

```text
PILOT_YYYYMMDD_NNN_<short_slug>
```

Example:

```text
PILOT_20260526_001_docs_status_update
```

## Event Subset For First Pilots
Use only these event types for the first 3 real pilots:

- `mission_considered`,
- `authority_declared`,
- `command_run`,
- `file_change_summary`,
- `verification_run`,
- `halt_triggered`,
- `fallback_triggered`,
- `human_decision`,
- `closeout_recorded`.

Do not use `envelope_created` or `reentry_checked` in the first real pilots unless the mission naturally requires them. This keeps the first real logs small and comparable.

## Required Event Rules
Each pilot log must:

1. start at `sequence: 1`,
2. keep sequence values gap-free and monotonic,
3. use one `mission_id` and one `record_id`,
4. include `authority_declared` before any command or file-change event,
5. use command labels from `authority_declared.payload.allowed_commands`,
6. keep file paths within `authority_declared.payload.authorized_files`,
7. record failed verification with `halt_triggered`, `fallback_triggered`, or `human_decision` before further execution,
8. end with exactly one `closeout_recorded` or `fallback_triggered`,
9. pass `scripts/factory_v3_telemetry_replay_lint.py`.

## Redaction And Data-Minimization Rules
Real pilot logs must not store:

- chain-of-thought,
- full chat transcripts,
- secrets, tokens, keys, cookies, or credentials,
- raw environment dumps,
- full command output,
- source file contents,
- diffs,
- private vendor cognition state,
- external governance-kernel proof or private policy state,
- personal data unrelated to mission replay.

Use short summaries and evidence references instead of payload copies.

If a field is omitted for privacy, record that in `REDACTION_REVIEW.md`, not in the JSONL payload.

## Operator Workflow
For each future pilot:

1. Create or update the mission record first.
2. Confirm `V3-OP-001` eligibility and explicit file/command authority.
3. Create the pilot directory only after the mission is approved for telemetry capture.
4. Append events during the mission, using synthetic-style summaries rather than full logs.
5. Run the replay validator before closeout.
6. Record `OVERHEAD.md` and `REDACTION_REVIEW.md`.
7. Store validator JSON output as `REPLAY_REPORT.json`.
8. Update Phase 3 status with lessons, overhead, false positives, false negatives, and missing event fields.

## Overhead Capture
`OVERHEAD.md` should record:

- mission id,
- pilot id,
- number of telemetry events,
- estimated minutes spent creating telemetry,
- number of commands run,
- number of verification commands run,
- fields marked `not_recorded`,
- redactions made,
- replay findings,
- operator friction notes,
- whether the telemetry improved replay over mission record alone.

## Replay And Verification Commands
For each future pilot:

```bash
python3 scripts/factory_v3_telemetry_replay_lint.py --target docs/Factory/v3/telemetry/pilots/<PILOT_ID>/V3_TELEMETRY.jsonl --json
python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json
python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
git diff --check
```

## Stop Conditions
Stop before or during a future pilot if:

- the mission is not eligible for `V3-OP-001`,
- telemetry capture would expand authorized files,
- telemetry would require storing excluded data,
- real command output or diffs would need to be copied into the log,
- the mission needs runtime authority, proof, lease enforcement, governance routing, or required-gate behavior,
- the replay validator cannot parse the pilot log,
- telemetry overhead is disproportionate for the mission size.

## Promotion Limits
Real pilot telemetry remains optional shadow evidence.

Three real pilot logs are evidence for Phase 3 analysis only. They do not make telemetry recommended, required, or gate-enforced. Recommendation still requires an overhead report, data-minimization review, and false-positive or false-negative classification.

## Next Step
Create a separate execution-enabled V2 run for the first real telemetry pilot.

That run must name the exact pilot mission, files, commands, storage path, and verification commands before writing any real telemetry log.
