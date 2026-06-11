# V3-OP-003 Ladder Status — Pickup Aid

## Version
v1.1

## Change Log
- v1.1 (2026-06-11): Design review round 2 executed and adopted in one pass per sponsor decision `HDI-RUNG2-007` ("GO and then lets try option A and based on what we see we could do another one using the hybrid approach"): rung-2 attempt 4 at ~27 build waypoints with browser tooling enabled (Go-blocking pre-flight check), coefficients recalibrated from Mission 023 (~21 calls/build waypoint), forecast ~700-1050 calls; hybrid rung-3-class contract named as contingent follow-on either way. `DURATION_LADDER_PLAN.md` amended to v0.9. Next gate: Mission 024 envelope plus sponsor Go.
- v1.0 (2026-06-11): Rung-2 attempt 3 (POC Mission 023, `LADDER_RUNG2R2_20260611`) adjudicated FAIL on duration and budget floor per sponsor decision `HDI-RUNG2-006` (mechanics clean; honest 54m03s active and ~333 calls vs the 90-min/540-call floors; work quality acknowledged). First live use of the interrupt field set v2 passed. New sponsor-named finding: browser tooling was unexposed in the Codex session, shortening the run and weakening verification depth — enablement directed for future runs. Third duration failure routes the lane to design review round 2 (mandatory).
- v0.9 (2026-06-11): Design-review output ADOPTED per sponsor decision `HDI-RUNG2-005` ("i agree with option A", `design_review/LADDER_DESIGN_ADOPTION_HDI_RUNG2_005.md`): duration band stays a rung-2 criterion, guarded by the bottom-up sizing rule and scope-sufficiency precondition; `DURATION_LADDER_PLAN.md` amended to v0.7 with the adopted rung classes and interrupt field set v2. Next gate: the rung-2 re-attempt envelope (~3.5x Mission 022 scope, multi-epic, derivation shown) plus sponsor Go.
- v0.8 (2026-06-11): Ladder design review executed with sponsor GO (`design_review/LADDER_DESIGN_REVIEW_20260611.md`): diagnosis = duration failures are envelope-design failures (scope-to-calls conversion, not throughput); proposes a bottom-up measured sizing rule, a scope-sufficiency precondition, restated rung classes (rung 2 floor 540 calls / ~12-20 waypoints / stop 1300), and the interrupt field set v2. Adoption is the open sponsor decision `HDI-RUNG2-005` (Option A recommended: duration band stays a criterion, guarded by the sizing rule).
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
| 1. Duration ladder (3 rungs) | Rung 1 passed (mechanics); rung-2 attempts 1, 2, and 3 all FAILED on duration (attempt 3: mechanics clean at 3.5x scope, honest 54m03s active / ~333 calls, `HDI-RUNG2-006`); lane routed to design review round 2; rung 3 locked |
| 2. Live transport trial | SATISFIED: phone-answered round-trip with sponsor away (96s deliver-to-answer, Codex mobile, POC Mission 021) plus timeout-to-safe-hold (MR_020) |
| 3. Health signals at checkpoints | Recorded at rung 1 and both rung-2 attempts (six signals + recording cost per checkpoint), but not yet at genuine 2h/4h duration |
| 4. Natural negative case at duration | Open; do not seed and relabel |
| 5. FP/FN review over ladder evidence | Open; runs after rung 3 |

## Resolved Gates
- Rung-2 transport choice: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-001` (`rung2/RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`) — option (b): rung 2 runs under the Codex harness with Codex mobile as the transport, the trial plan's secondary candidate, already proven by POC Mission 013's two phone-answered interrupts. Background: Claude Code Remote Control returned "disabled by your organization's policy" when the sponsor tried to enable it (2026-06-10) — transport availability is itself org-policy-gated runtime state (an observation in the `MUTABLE_HARNESS_STATE.md` spirit); option (a) may be renamed in a future trial if the org policy changes.

- Rung-2 attempt 1: ADJUDICATED FAIL 2026-06-11 by sponsor decision `HDI-RUNG2-002` (`rung2/RUNG2_ADJUDICATION_HDI_RUNG2_002.md`) — POC Mission 021 closed honestly at 24m11s against the 90-180 min band; mechanics passed 7 of 8 including the live phone interrupt, pause/reentry, waypoint-table trial, and friction counters. The failed rung does not unlock rung 3.

- Rerun path: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-003` (`rung2/RUNG2_RERUN_PATH_HDI_RUNG2_003.md`) — Option A: genuinely larger scope under the unchanged wall-clock band, stop threshold raised to 1100; second duration failure routes to the design review.

- Design review round 2: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-007` (`design_review/LADDER_DESIGN_REVIEW_ROUND2_HDI_RUNG2_007.md`) — Option A-final: attempt 4 at ~27 build waypoints with browser tooling enabled and verified at pre-flight; coefficients recalibrated from Mission 023 actuals; hybrid rung-3-class contract named as the contingent follow-on either way; Option B not adopted but remains available with four calibration points if attempt 4 compresses.

- Rung-2 attempt 3: ADJUDICATED FAIL 2026-06-11 by sponsor decision `HDI-RUNG2-006` (`rung2/RUNG2_ATTEMPT3_ADJUDICATION_HDI_RUNG2_006.md`) — POC Mission 023 (three epics, 16 build waypoints, 247 tests) closed honestly at 59m55s gross / 54m03s active with ~333 calls against the 90-min/540-call floors; mechanics clean including the first live field-set-v2 interrupt (86s, neutral) and pause/reentry. Calibration verdict: throughput calibrated (~6.2 calls/min, three runs), per-waypoint cost coefficient too high. Sponsor findings: browser tooling unexposed in the session shortened the run (enablement directed); a further ~2x scope jump is the only remaining Option A variant.

- Design-review adoption: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-005` (`design_review/LADDER_DESIGN_ADOPTION_HDI_RUNG2_005.md`) — Option A: the duration band remains a rung-2 pass criterion, guarded by the bottom-up measured sizing rule and the scope-sufficiency precondition; rung classes restated (rung 2: floor 540 calls/stop 1300; rung 3: floor 1100/stop 2000); interrupt field set v2 operative for all future lane envelopes. `DURATION_LADDER_PLAN.md` amended to v0.7.

- Rung-2 attempt 2: ADJUDICATED FAIL 2026-06-11 by sponsor decision `HDI-RUNG2-004` (`rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md`) — POC Mission 022 closed honestly at 47m40s elapsed (40m06s active) against the 90-180 min band with mechanics 8/8, including a clean live phone interrupt (734s answer latency recorded as neutral telemetry per the adopted safe-hold-trigger principle), pause/fresh-session reentry, friction counters, and the waypoint-table second trial. Two consecutive duration failures trigger the pre-written design-review routing.

## Remaining Gates (in order; each needs envelope + sponsor Go)
1. Rung-2 attempt 4 (POC Mission 024) under the adopted `HDI-RUNG2-007` class — ~27 build waypoints (~3 of them browser-QA), forecast ~700-1050 calls bottom-up from Mission 023-recalibrated coefficients, floor 540, stop 1300, band 90-180 min, interrupt field set v2, new live phone interrupt and pause/reentry; pre-flight must verify browser-tool availability (Go-blocking) — the sponsor enables the browser plugin at Codex session start.
2. Contingent hybrid follow-on per `HDI-RUNG2-007` (either way, for learning value): a rung-3-class contract drafted with the mission-formation skill and red-teamed with the challenge skill (the `V3-ANCHOR-005` trial); if attempt 4 compresses again, this absorbs the duration burden and the wall-clock criterion is re-presented with four calibration points.
3. Rung 3 — 4-hour class (class parameters to be confirmed or revised by design review round 2); mission contract drafted with the mission-formation skill and red-teamed with the challenge skill (the named `V3-ANCHOR-005` live trial); natural interrupts only. Locked until rung 2 resolves.
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
