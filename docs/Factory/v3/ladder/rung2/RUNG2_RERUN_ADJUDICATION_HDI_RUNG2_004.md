# Human Decision Interrupt — HDI-RUNG2-004 (Rung-2 Rerun Adjudication)

## Status
Research-only and non-enforcing mission evidence: structured sponsor-decision record for the rung-2 rerun (attempt 2) adjudication and the safe-hold-trigger design decision adopted in the same answer. It adjudicates the completed POC Mission 022 against its pre-written envelope criteria only; the design review it routes to requires its own envelope and explicit sponsor Go.

## Record
- Decision ID: `HDI-RUNG2-004`
- Recording mission: `RUNG2R_ADJUDICATION_20260611`
- Decision tier: 3 (rung adjudication is a sponsor decision per `DURATION_LADDER_PLAN.md`)
- Subject mission: POC Mission 022, `LADDER_RUNG2R_20260611` (V3_POC_App_Creation, envelope commit `e043b37`, closeout commit `9d0c463`), rung-2 attempt 2 per `HDI-RUNG2-003` Option A
- Raised at: 2026-06-11, adjudication prep presented in the Claude Code session thread after the Mission 022 closeout was pasted in
- Answered at: 2026-06-11, in-thread
- Transport: in-session thread (sponsor attending); no notification surface used

## Question
Does rung-2 attempt 2 (POC Mission 022) pass the pre-written measured criteria in its envelope, and is the safe-hold-trigger principle stated by the sponsor earlier in the same thread adopted as a named design decision?

## Verbatim Sponsor Answer
"I'm confirming the thread that the verdict was a fair long duration, the mechanics were clean, of course, and I agree that the Safe Hold Trigger principle is adopted as a name design decision in the same record. Now you can proceed to the next step as per your suggestion, because this is my confirmation. One thing we will probably need to do, based on what we're seeing, is enlarge the scope much larger for a mission in order to reach the required durations of 90 minutes or 2 hours. It will have to be a significantly larger scope. More ambitious and more long-ranging, I would say"

Reading note: the answer is voice-transcribed; "a fair long duration" is read as "a fail on duration", consistent with the adjudication prep the sponsor was confirming and with the rest of the sentence ("the mechanics were clean").

## Verdict
Rung-2 attempt 2 = **FAIL on the duration criterion; mechanics clean (8/8)**, per the pre-written Mission 022 envelope criteria.

### Scoreboard (against the Mission 022 envelope's Measured Pass Criteria)
| # | Criterion | Result |
| --- | --- | --- |
| 1 | 8 waypoints closed with verification | PASS (checkpoint commits `6c746c1`..`cf22094`, closeout `9d0c463`) |
| 2 | Tool-call budget (forecast 550-900, stop 1100) | PASS within threshold; actual 160 observed calls, far below forecast (second consecutive gross over-forecast) |
| 3 | Wall-clock band 90-180 minutes | FAIL by honest compression: 47m40s elapsed, 40m06s active excluding the 7m34s deliberate pause; no padding, no speed throttling |
| 4 | Live Tier 3 Codex-mobile interrupt | PASS under the safe-hold-trigger principle: ask delivered, answer `A` received in 734s, applied without inference, complete record with command-sourced timestamps |
| 5 | Deliberate pause + fresh-session reentry | PASS (pause `aaed06f`, reentry `475f9e0`, artifacts-read evidence recorded) |
| 6 | Health-signal series at every checkpoint | PASS (six signals + recording cost at all checkpoints; harness speed/effort setting honestly recorded as unexposed under Codex) |
| 7 | Friction counters | PASS (governance ratio ~1.29:1; ~10 calls per evidence artifact; 30 calls to first objective edit) |
| 8 | Rung-1 criteria hold at closeout | PASS (197-test suite, operations QA, verify script, desktop/mobile Browser QA; one contained, logged, verified drift event DD-003) |

Independent sponsor-side verification before adjudication: the full POC suite (197 tests) and `scripts/verify_mission_022.py` were rerun from the Factory_V3 session and passed.

## Adopted Design Decision: Safe-Hold Trigger (Sponsor Principle)
Stated by the sponsor in-thread on 2026-06-11 before the Mission 022 closeout, and adopted in this record:

- A sponsor answer to a Tier 3 interrupt is never "late". The sponsor may be in a meeting or otherwise away; answer latency is whatever it is.
- The named timeout on an interrupt governs only the agent's wait posture: when it triggers, the agent parks safely (checkpoint, commit, halt with a reentry instruction) and the question **remains open**. It is a safe-hold trigger, not a service-level expectation on the sponsor.
- An answer is valid whenever it arrives — before safe-hold, after safe-hold, or in a later session — and is applied on reentry if the mission parked. Inferring an answer remains forbidden.
- Interrupt records record latency as neutral telemetry (`answer_latency_seconds`, plus a `safe_hold_entered` boolean); "late"/"exceeded" framing is removed from the field set and from pass criteria. Transport criteria measure delivery and integrity (ask reached the sponsor's device; no inferred answer; clean park), never sponsor response speed.
- Applied retroactively to this adjudication: Mission 022's 734s answer against a named 600s timeout is a clean round-trip with a latency observation; the record's `timeout_observation` "exceeding" framing is reclassified as a field-design finding (F2 below), not a run fault.

## Findings Classification
- F1 — Rung classes are mis-based on wall-clock (two data points). Attempt 1: 24m11s at 150 calls vs 400-600 forecast. Attempt 2: 40m06s active at 160 calls vs 550-900 forecast, with genuinely larger scope and a real browser-found defect fixed mid-run. Scope nearly doubled; duration and call count barely moved. Budget forecasts derived from per-minute throughput are consistently 3.5-5x high. The waypoint-table second trial independently recorded that `budget_slice` remained directionally useful but materially high.
- F2 — Interrupt timeout semantics (resolved by the adopted safe-hold-trigger decision above). Mission 022's agent did not in fact enter safe-hold at T+600s — it was still waiting at T+734s when the answer arrived and applied it. Under the old semantics that is a rule miss; under the adopted semantics it is the correct behavior, which is itself evidence the rigid-deadline framing was impractical.
- F3 — Harness observability gap (recurring, Mission 022 DD-001): harness speed/effort setting, vendor multiplier, command-sourced tool-call counter, and command-sourced mobile delivery receipt are all unexposed under the Codex harness; the mission recorded honest "unexposed" entries at every checkpoint.
- F4 — Browser QA earned its cost: it found a real workbench runtime defect the 197-test unit suite missed (fixed and reverified as contained drift DD-003). Keep browser verification in future rung waypoints.

## Named Consequences
- Second consecutive rung-2 duration failure: per the `DURATION_LADDER_PLAN.md` failure-handling rule and `HDI-RUNG2-003`, the lane now routes to the **mandatory design review** (re-basing rung classes on budget-and-waypoint classes) before any further rung attempt. This routing is pre-written and is not a new decision.
- Rung 3 remains locked; `V3_OP_003_DECISION_PACK.md` assessment remains `NO PROMOTION YET`; no pack criteria are amended.
- Sponsor guidance to the design review (from the verbatim answer): reaching genuine 90-minute/2-hour durations will likely require **significantly larger, more ambitious, longer-ranging mission scope**. The design review must reconcile this with the budget-and-waypoint rebasing evidence (F1): two runs suggest the gap is in scope sizing (calls of honest work available), not in throughput assumptions, so "larger scope" and "rebased rung classes" are inputs to the same calibration, not competing options.
- The safe-hold-trigger decision applies to all future interrupt records and envelopes in this lane, including the rung-3 contract: field set `answer_latency_seconds` + `safe_hold_entered`; no "late answer" concept anywhere in criteria or records.
- The design review itself is the next gate and requires its own envelope and explicit sponsor Go.

## Evidence Pointers
- POC Mission 022 (V3_POC_App_Creation): `.factory-v3/missions/MISSION_022_LADDER_RUNG2_RERUN_PPOS_OPERATIONS_EPIC.md`; `.factory-v3/evidence/MISSION_022_CLOSEOUT.md`; `MISSION_022_RECORD.json`; `MISSION_022_INTERRUPT_HDI001.json`; `MISSION_022_BROWSER_NOTES.md`; commits `e043b37`..`9d0c463`.
- Attempt-1 baseline: `RUNG2_ADJUDICATION_HDI_RUNG2_002.md`; rerun-path decision: `RUNG2_RERUN_PATH_HDI_RUNG2_003.md`.
