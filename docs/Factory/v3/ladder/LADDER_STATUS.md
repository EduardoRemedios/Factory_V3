# V3-OP-003 Ladder Status — Pickup Aid

## Version
v0.7

## Change Log
- v0.7 (2026-06-11): Rung-2 attempt 2 (POC Mission 022, `LADDER_RUNG2R_20260611`) adjudicated FAIL on duration per sponsor decision `HDI-RUNG2-004` (mechanics 8/8; honest 47m40s elapsed / 40m06s active vs 90-180 min band; actual 160 calls vs 550-900 forecast). Second consecutive duration failure routes the lane to the mandatory design review per the pre-written failure-handling rule. The sponsor's safe-hold-trigger principle (an answer is never "late"; the timeout governs agent wait posture only) is adopted as a named design decision in the same record.
- v0.6 (2026-06-11): Rerun-path gate resolved — sponsor decision `HDI-RUNG2-003` selected Option A: rerun rung 2 with genuinely larger scope (roughly 550-900 calls, stop threshold 1100) under the unchanged wall-clock band; a second duration failure routes to the Option B design review.
- v0.5 (2026-06-11): Rung-2 attempt 1 (POC Mission 021, `LADDER_RUNG2_20260611`) adjudicated FAIL on duration per sponsor decision `HDI-RUNG2-002` (mechanics 7/8; honest 24m11s vs 90-180 min band). Decision-pack item 2 (live transport) now satisfied by the phone-answered round-trip. Rerun path (bigger scope vs ladder design review) is the new open sponsor decision.
- v0.4 (2026-06-11): Backlog research spike landed: `mission_waypoint` shadow candidate, mission-economics vocabulary, fresh-worker reentry trial plan, and rung-2 friction counters (`DURATION_LADDER_PLAN.md` v0.4); rung-2 gate now includes the waypoint-table trial and friction counters.
- v0.3 (2026-06-11): Gate 1 resolved — sponsor decision `HDI-RUNG2-001` selected option (b): rung 2 runs under the Codex harness with Codex mobile as the transport (`rung2/RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`). Fixed the duplicate numbering in the remaining-gates list.
- v0.2 (2026-06-10): Recorded that Claude Code Remote Control is disabled by the sponsor's organization policy; rung-2 transport choice is an open sponsor decision with named options.
- v0.1 (2026-06-10): End-of-day pickup aid after rung 1 and the interrupt-transport trial.

## Status
Research-only and non-enforcing pointer-first pickup aid for the active long-running-mission lane. It duplicates no evidence; follow the pointers. It approves nothing — every remaining gate below requires its own envelope and explicit sponsor Go.

## Where Things Stand (end of 2026-06-10)
The named next operational-readiness decision is the `V3-OP-003` promotion decision (sponsor decision `HDI-RUNG1-001`), taken against the pre-written criteria in `V3_OP_003_DECISION_PACK.md` once the evidence exists. Today produced:

- Governance canon: `GOVERNANCE_BOUNDARIES.md` (README split), `MUTABLE_HARNESS_STATE.md`, `SKILL_PROVENANCE_POLICY.md`, `REGULATORY_CROSSWALK.md`, standing-authorization candidates (`SHADOW_SCHEMA_CANDIDATES.md` v0.2). Mission records now record model identity; `same_commit` convention active (design v0.9).
- Long-running lane: candidate profile (`CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`), decision pack at `NO PROMOTION YET`, `MISSION_HEALTH_VOCABULARY.md`, `INTERRUPT_TRANSPORT_TRIAL_PLAN.md`, `DURATION_LADDER_PLAN.md` (v0.3).
- Rung 1 (`LADDER_RUNG1_20260610`, `rung1/`, MR_019): PASSED for mechanics per `HDI-TT-001`; duration burden shifted to rung 2. Sponsor decisions taken: next named decision = V3-OP-003 promotion (`HDI-RUNG1-001`); rung naming = hour headline + budget-and-waypoint measured criteria (`HDI-TT-002`).
- Transport trial (`TRANSPORT_TRIAL_20260610`, `transport_trial/`, MR_020): PASSED its pre-written criteria. First controlled exercise of the no-response safe-hold rule worked as specified. Findings: desktop-only delivery while Remote Control inactive; focus-based notification suppression; phone round-trip untested.

## Decision-Pack Evidence Scoreboard

| Pack item | Status |
| --- | --- |
| 1. Duration ladder (3 rungs) | Rung 1 passed (mechanics); rung-2 attempts 1 and 2 both FAILED on duration (attempt 2: mechanics 8/8, honest 40m06s active, `HDI-RUNG2-004`); lane routed to the mandatory design review; rung 3 locked |
| 2. Live transport trial | SATISFIED: phone-answered round-trip with sponsor away (96s deliver-to-answer, Codex mobile, POC Mission 021) plus timeout-to-safe-hold (MR_020) |
| 3. Health signals at checkpoints | Recorded at rung 1 and both rung-2 attempts (six signals + recording cost per checkpoint), but not yet at genuine 2h/4h duration |
| 4. Natural negative case at duration | Open; do not seed and relabel |
| 5. FP/FN review over ladder evidence | Open; runs after rung 3 |

## Resolved Gates
- Rung-2 transport choice: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-001` (`rung2/RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`) — option (b): rung 2 runs under the Codex harness with Codex mobile as the transport, the trial plan's secondary candidate, already proven by POC Mission 013's two phone-answered interrupts. Background: Claude Code Remote Control returned "disabled by your organization's policy" when the sponsor tried to enable it (2026-06-10) — transport availability is itself org-policy-gated runtime state (an observation in the `MUTABLE_HARNESS_STATE.md` spirit); option (a) may be renamed in a future trial if the org policy changes.

- Rung-2 attempt 1: ADJUDICATED FAIL 2026-06-11 by sponsor decision `HDI-RUNG2-002` (`rung2/RUNG2_ADJUDICATION_HDI_RUNG2_002.md`) — POC Mission 021 closed honestly at 24m11s against the 90-180 min band; mechanics passed 7 of 8 including the live phone interrupt, pause/reentry, waypoint-table trial, and friction counters. The failed rung does not unlock rung 3.

- Rerun path: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-003` (`rung2/RUNG2_RERUN_PATH_HDI_RUNG2_003.md`) — Option A: genuinely larger scope under the unchanged wall-clock band, stop threshold raised to 1100; second duration failure routes to the design review.

- Rung-2 attempt 2: ADJUDICATED FAIL 2026-06-11 by sponsor decision `HDI-RUNG2-004` (`rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md`) — POC Mission 022 closed honestly at 47m40s elapsed (40m06s active) against the 90-180 min band with mechanics 8/8, including a clean live phone interrupt (734s answer latency recorded as neutral telemetry per the adopted safe-hold-trigger principle), pause/fresh-session reentry, friction counters, and the waypoint-table second trial. Two consecutive duration failures trigger the pre-written design-review routing.

## Remaining Gates (in order; each needs envelope + sponsor Go)
1. Ladder design review — re-base rung classes on measured budget-and-waypoint evidence (two calibration points: 150 calls/24m11s and 160 calls/40m06s active against 3.5-5x higher forecasts), incorporating the sponsor's named guidance that genuine 90-min/2-hour durations likely require significantly larger, more ambitious, longer-ranging mission scope, and the adopted safe-hold-trigger redesign of the interrupt-record field set (`answer_latency_seconds`, `safe_hold_entered`; no "late answer" concept).
2. Rung-2 re-attempt (or its redesigned equivalent) under the design-review output criteria.
3. Rung 3 — 4-hour class; mission contract drafted with the mission-formation skill and red-teamed with the challenge skill (the named `V3-ANCHOR-005` live trial); natural interrupts only. Locked until rung 2 passes.
4. False-positive/false-negative review over the full ladder corpus.
5. Assemble the pack and take the sponsor promotion decision against the pre-written `PASS` / `CONDITIONAL PASS` / `NO PROMOTION YET` criteria.

## Parked Named Follow-ups (not gates, not approved)
- Standalone-canon fix: vendor the Factory_V3 canon referenced by POC envelopes (health vocabulary, ladder artifacts) into the POC repo, or inline it (rung-2 attempt 1 finding, POC DD-001).
- Harness speed/effort setting recorded at mission start and on change, as mutable harness state (`HDI-RUNG2-002` finding 5); required context for any cross-mission economics burn comparison. Mission 022 attempted this and recorded an honest observability gap: the setting, vendor multiplier, command-sourced tool-call counter, and mobile delivery receipt are all unexposed under the Codex harness (`HDI-RUNG2-004` finding F3).
- Fresh-worker reentry trial (`FRESH_WORKER_REENTRY_TRIAL_PLAN.md`): cross-harness, sealed answer key; runs after rung 2 with its own envelope and Go.
- Mission-economics research-lane decision (`MISSION_ECONOMICS_VOCABULARY.md`): gated on rung-2 friction-counter evidence; first economics recording targeted at rung 3.
- `mission_waypoint` shadow-candidate refinement after the rung-2 waypoint-table trial.
- Advisory validator + fixture support for `model_routing` and a future `skills_relied_on` field.
- Retention statement in `MISSION_RECORD_DESIGN_V0.md` (Art. 26 six-month note in the crosswalk).
- Human/legal review of `REGULATORY_CROSSWALK.md` rows before any external use.
- Interim-halt event field design note (MR_020 false-positive note) for missions that halt and resume within one record.
- Harness capability profile observation for the Claude Code notification surface (delivery gating + focus suppression, from MR_020).

## Read First Tomorrow
`ANCHOR_REGISTRY.md` (row `V3-ANCHOR-004`) → `V3_OP_003_DECISION_PACK.md` → `DURATION_LADDER_PLAN.md` → this file's scoreboard. Mission records MR_010 through MR_020 are the day's evidence chain.
