# Human Decision Interrupt — HDI-RUNG2-002 (Rung-2 Attempt 1 Adjudication)

## Status
Research-only and non-enforcing mission evidence: structured sponsor-adjudication record for duration-ladder rung-2 attempt 1. It records the adjudication only; it approves no rerun, no design review, and no promotion, and the failed rung does not unlock rung 3.

## Record
- Decision ID: `HDI-RUNG2-002`
- Mission adjudicated: `LADDER_RUNG2_20260611` (POC Mission 021, `V3_POC_App_Creation`, envelope commit `a5c2c9a`, closeout commit `63a0a99`)
- Recording mission: `RUNG2_ADJUDICATION_20260611`
- Decision tier: 3 (rung adjudication against pre-written envelope criteria is a sponsor decision per `DURATION_LADDER_PLAN.md`)
- Raised at: 2026-06-11, adjudication prep presented in the Claude Code session thread with the full scoreboard and three named options
- Answered at: 2026-06-11, in-thread
- Transport: in-session thread (sponsor attending); no notification surface used

## Question
Does rung-2 attempt 1 pass against the pre-written measured criteria in its envelope, given mechanics passed 7 of 8 but duration compressed to 24m11s against the 90-180 minute band?

## Options (as presented)
- Option A: FAIL as written; accept mechanics evidence into the pack; rerun rung 2 with genuinely larger scope (~550-750 objective tool calls) and a raised stop threshold, keeping the wall-clock band as pass criterion.
- Option B: FAIL as written; accept mechanics evidence into the pack; route the ladder to a design review that re-bases rung classes on budget-and-waypoint classes (wall clock becomes a recorded observation, aligning with the `ADAPTIVE_MISSION_CONTROL.md` time-as-guardrail principle) before any rerun.
- Option C: Amend the duration criterion retroactively and pass the run (presented with a recommendation against: moves the goalposts the pack exists to fix).

## Answer
- Answer source: sponsor, Claude Code session thread, 2026-06-11 ("for me its a fail as its still far short of the duration")
- Answer: rung-2 attempt 1 is adjudicated **FAIL** on the duration criterion, per the pre-written criteria. Option C is rejected. The choice between the Option A and Option B rerun paths is NOT resolved by this answer and remains the next open sponsor decision (see below).

## Adjudicated Scoreboard (from POC Mission 021 closeout, `.factory-v3/evidence/MISSION_021_CLOSEOUT.md`)
| Criterion | Result |
| --- | --- |
| 8 waypoints closed with verification | PASS |
| Tool-call budget (≤700) | PASS (150 actual; forecast 400-600 was 2.7-4x high) |
| Duration band 90-180 min genuine | FAIL (24m11s, honest, no padding) |
| Live Tier 3 phone interrupt | PASS (complete AMC record; deliver-to-answer 96s; sponsor away) |
| Pause + fresh-session reentry from artifacts | PASS (pause `47d4d48`, reentry `9acc975`, artifacts-read evidence) |
| Six health signals every checkpoint | PASS with gap (recorded throughout from an envelope-derived basis; vocabulary file absent in the standalone repo) |
| Friction counters | PASS (governance:objective 84:66 ≈ 1.27:1; ~10.5 calls per evidence artifact; Go-to-first-edit 6) |
| Rung-1 criteria hold | PASS with residual (184 tests, QA and verifier pass; browser pixel QA honestly blocked, no install allowed) |

## Findings Classification
1. Duration compression (criteria gap, honest): second consecutive rung compression (rung 1 ~8.6x, rung 2 ~5x). Measured throughput ~6.2 tool calls/minute means the 90-minute floor implies ~560 objective calls and the 120-minute headline ~745 — above the envelope's own 700-call stop threshold. The rung-2 envelope as written contained a latent contradiction between its duration band and its budget class.
2. Drafting defect (recording mission author's): the rung-2 envelope referenced Factory_V3 canon (`MISSION_HEALTH_VOCABULARY.md`, ladder plan) absent from the standalone POC repo. The worker's stricter-authority handling (POC DD-001) was correct. Fix before any rerun: vendor the referenced canon into the POC repo or inline it in the envelope.
3. Waypoint-table trial verdicts (first live evidence for the `mission_waypoint` candidate): `id`, `objective`, `named_scope`, `verification` earned their cost — `named_scope` surfaced the WP5 drift cleanly as an observation (POC DD-003), the restriction-projection design working as intended; `budget_slice` overestimated badly; `type` added little beyond grouping; `expected_artifacts` useful at closeout.
4. Friction data (first counters): at this mission size, governance consumed 56% of all tool calls. Small missions do not amortize governance; this is the first affordability datum for the mission-economics lane decision.
5. Mutable harness state, new instance: the Codex speed setting (sponsor-set to fast, vendor-stated 1.5x, higher token use) is org/user-controlled runtime state that scales wall clock and token burn. At 1x the run would still have been ~36 minutes — the setting does not explain the compression — but it must be recorded at mission start and on change, and economics burn comparisons across missions are invalid without it. Throttling harness speed to satisfy a wall-clock band would be padding by another name and is rejected as a fix.
6. Browser pixel QA residual: honestly blocked (no Playwright, dependency installs forbidden). A natural limitation event honestly recorded, but not at duration and not a halt/fallback/clarification — weak candidate for decision-pack item 4; the item stays open.

## Decision-Pack Effect
- Item 1 (duration ladder): rung 1 passed for mechanics; rung-2 attempt 1 FAILED (mechanics 7/8, duration failed). Rung 2 remains open; rung 3 stays locked.
- Item 2 (live transport trial): SATISFIED — phone-answered round-trip with sponsor away (96s; pre-mission delivery test 46s) plus the MR_020 timeout-to-safe-hold leg.
- Item 3 (health signals at 2h/4h rungs): signals recorded at a 2-hour-class attempt, not at duration; still open.
- Items 4 and 5: open.
- Assessment: `NO PROMOTION YET` (unchanged).

## Next Open Sponsor Decision (not resolved here)
Rerun path for rung 2 — Option A (rerun with genuinely larger scope under wall-clock rules, stop threshold raised to match) versus Option B (ladder design review first, re-basing rung classes on budget-and-waypoint classes with wall clock as a recorded observation). The recording mission's closeout asks this in-thread; per `DURATION_LADDER_PLAN.md` failure handling, a second consecutive rung-2 failure would route the lane to design review regardless.
