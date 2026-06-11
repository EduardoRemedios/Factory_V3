# V3-OP-003 Ladder Status — Pickup Aid

## Version
v0.4

## Change Log
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
| 1. Duration ladder (3 rungs) | Rung 1 of 3 passed (mechanics); rungs 2-3 not started |
| 2. Live transport trial | Partially satisfied: answered round-trip and timeout-to-safe-hold both proven, but on the desktop/in-session surface; phone round-trip outstanding (rung-2 requirement) |
| 3. Health signals at checkpoints | First real data at rung 1 (six signals, 10-15 lines/checkpoint); pack requires 2h and 4h rungs |
| 4. Natural negative case at duration | Open; do not seed and relabel |
| 5. FP/FN review over ladder evidence | Open; runs after rung 3 |

## Resolved Gates
- Rung-2 transport choice: RESOLVED 2026-06-11 by sponsor decision `HDI-RUNG2-001` (`rung2/RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`) — option (b): rung 2 runs under the Codex harness with Codex mobile as the transport, the trial plan's secondary candidate, already proven by POC Mission 013's two phone-answered interrupts. Background: Claude Code Remote Control returned "disabled by your organization's policy" when the sponsor tried to enable it (2026-06-10) — transport availability is itself org-policy-gated runtime state (an observation in the `MUTABLE_HARNESS_STATE.md` spirit); option (a) may be renamed in a future trial if the org policy changes.

## Remaining Gates (in order; each needs envelope + sponsor Go)
1. Rung 2 — POC repo, 2-hour class measured by budget-and-waypoint criteria with genuine duration required (a compressed run does not pass, per `HDI-TT-001`); one live Tier 3 interrupt answered from the sponsor's phone via Codex mobile per `HDI-RUNG2-001`; sponsor genuinely away from the terminal when the interrupt fires (focus suppression finding); rung-2 envelope drafted in the POC repo; rung runs under the Codex harness, with harness and model identity recorded per `MUTABLE_HARNESS_STATE.md`. The envelope also carries the structured-waypoint-table trial and the friction counters per `DURATION_LADDER_PLAN.md` v0.4.
2. Rung 3 — 4-hour class; mission contract drafted with the mission-formation skill and red-teamed with the challenge skill (the named `V3-ANCHOR-005` live trial); natural interrupts only.
3. False-positive/false-negative review over the full ladder corpus.
4. Assemble the pack and take the sponsor promotion decision against the pre-written `PASS` / `CONDITIONAL PASS` / `NO PROMOTION YET` criteria.

## Parked Named Follow-ups (not gates, not approved)
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
