# Factory v3 Phase 3 Telemetry Evidence Review

## Version
v0.2

## Change Log
- v0.2 (2026-06-10): Retired the v0.1 acceptability of missing model identity for new records, following `MUTABLE_HARNESS_STATE.md`; existing pilot records remain valid historical evidence with the gap explicit.
- v0.1 (2026-05-26): Initial review after three real advisory telemetry pilots.

## Status
Research-only and non-enforcing.

This review does not approve required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, telemetry enforcement, or V2 build-support removal.

## Decision
`RECOMMEND_OPTIONAL_ADVISORY_TELEMETRY_WITH_CONDITIONS`

Interpretation:
- Telemetry may be used as optional advisory shadow evidence for selected narrow `V3-OP-001` evidence-gathering missions.
- Telemetry should remain non-blocking and manually reviewable.
- Telemetry is not recommended as a routine requirement for every small V3 task.
- Phase 3 does not approve enforcement or telemetry completeness checks.
- Phase 4 planning may begin, but must carry the missing natural negative-case evidence gap forward.

## Evidence Inputs
- `telemetry/pilots/PILOT_20260526_001_phase3_status_update/`
- `telemetry/pilots/PILOT_20260526_002_replay_fixture_maintenance/`
- `telemetry/pilots/PILOT_20260526_003_evidence_review_prep/`
- `mission_records/MR_20260526_004_first_real_telemetry_pilot.json`
- `mission_records/MR_20260526_005_second_real_telemetry_pilot.json`
- `mission_records/MR_20260526_006_third_real_telemetry_pilot.json`
- `PHASE3_TELEMETRY_EVIDENCE_REVIEW_PREP.md`

## Pilot Comparison

| Pilot | Mission type | Events | Minutes | Commands | Verification commands | Replay status | Redaction review |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `PILOT_20260526_001_phase3_status_update` | docs-only status update | 26 | 20 | 11 | 11 | `ADVISORY_PASS` | PASS |
| `PILOT_20260526_002_replay_fixture_maintenance` | fixture maintenance | 28 | 18 | 12 | 12 | `ADVISORY_PASS` | PASS |
| `PILOT_20260526_003_evidence_review_prep` | docs/data evidence prep | 29 | 18 | 12 | 12 | `ADVISORY_PASS` | PASS |

## Overhead Rollup
- Total telemetry events: 83.
- Average telemetry events per pilot: 27.7.
- Total estimated telemetry minutes: 56.
- Average estimated telemetry minutes per pilot: 18.7.
- Total command events represented: 35.
- Total verification command events represented: 35.

Assessment:
- The overhead is acceptable for low-frequency evidence pilots and validator-design work.
- The overhead is disproportionate for routine small documentation updates if used every time.
- Paired command and verification events were the largest friction point.

## Replay Value
Telemetry improved replay over mission records alone by making these facts machine-readable in one ordered stream:
- authority declaration before command and file-change evidence,
- allowed command labels,
- file-scope evidence,
- verification sequencing,
- human decision points,
- terminal closeout order.

The three real pilot replay reports returned `ADVISORY_PASS` with no findings and `blocking_effect: none`.

## Data-Minimization Review
All three pilot redaction reviews returned PASS.

The logs store summaries, labels, exit codes, and evidence references. They do not store chain-of-thought, full chat transcripts, secrets, raw environment dumps, full command output, source file contents, diffs, private vendor cognition state, external governance-kernel proof, private policy state, or unrelated personal data.

Assessment:
- The summary-only payload pattern is suitable for continued advisory pilots.
- Missing timestamps remain acceptable for current research evidence.
- The v0.1 acceptability of missing model identity is retired as of 2026-06-10: new mission records should record model identity per `MISSION_RECORD_DESIGN_V0.md` v0.8 and `MUTABLE_HARNESS_STATE.md`. The three Phase 3 pilot records keep their `not_recorded` values as valid historical evidence with the gap explicit.
- If later phases need elapsed-time measurement or harness profiling, those fields require separate approval and minimization review.

## False-Positive And False-Negative Classification
- False positives observed in real pilot logs: none.
- False negatives observed in real pilot logs: none.
- Replay findings: none.

Limit:
- The pilot set did not include a natural halted, fallback, or clarification-heavy mission.
- Therefore this review cannot claim negative-case coverage from real telemetry.

## Evidence Gap
The missing natural halted, fallback, or clarification-heavy pilot is a real Phase 3 gap.

This gap blocks:
- required telemetry,
- telemetry completeness enforcement,
- Phase 6 enforcement claims,
- default-mode claims,
- governance-router confidence claims.

It does not block Phase 4 planning, as long as Phase 4 treats the gap as an input and does not convert telemetry into an enforcement mechanism.

## Conditions For Continued Use
Optional advisory telemetry may continue only when:
- the work is narrow `V3-OP-001` evidence work,
- the operator can keep payloads summary-only,
- command output and source contents remain outside the telemetry log,
- replay reports keep `blocking_effect: none`,
- missing negative-case coverage is stated when relevant,
- telemetry is not wired into CI, `factoryctl`, required gates, or default workflows.

## Recommendation
Close Phase 3 with a conditional advisory recommendation:
- Continue optional telemetry for selected V3 evidence missions.
- Do not require telemetry for all V3 work.
- Do not implement enforcement, routing, runtime authority, proof, leases, or completeness checks.
- Start Phase 4 planning for eval expansion and capability profiling.
- Carry the natural negative-case pilot gap into Phase 4 and future Phase 3-adjacent evidence collection.

## Next Move
Plan Phase 4 eval expansion and capability profiling in a separate V2-governed run.

That planning run should define templates, fixtures, and evaluation questions only. It should not implement governance routing, enforcement, default-mode behavior, telemetry completeness checks, or V2 build-support removal.
