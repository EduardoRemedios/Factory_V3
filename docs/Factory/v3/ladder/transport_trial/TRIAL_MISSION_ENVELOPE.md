# Interrupt-Transport Trial — Mission Envelope

## Status
Active mission envelope (file artifact) for the live interrupt-transport trial per `INTERRUPT_TRANSPORT_TRIAL_PLAN.md`. Research-only and non-enforcing with respect to gates; executes as a synthetic docs-only mission under `V3-OP-001` authority. This envelope approves this trial only; it does not approve any other live transport use, scheduled operation, or messaging automation.

## Sponsor Approval (per trial plan requirement)
- Sponsor (participating human): Eduardo dos Remedios
- Approval: given in the Claude Code session thread on 2026-06-10 — "I approve the interrupt transport trial go ahead"
- Transport named: Claude Code notification surface (desktop notification; pushes to phone when Remote Control is connected) with the synced session as the answer path — the trial plan's primary candidate
- Window: 2026-06-10, this session and its immediate reentry session
- Transport caveat: whether delivery lands on desktop or phone depends on the sponsor's Remote Control connection state; the pre-mission delivery test records which surface actually received it. A desktop-only delivery is valid trial evidence with the surface honestly recorded.

## Mission Identity
- Mission ID: `TRANSPORT_TRIAL_20260610`
- Profile authority: `V3-OP-001` (synthetic docs-only mission)
- Harness: Claude Code; model at start: `claude-fable-5` (routing not enabled)
- Start timestamp (command-sourced): 2026-06-10T13:36:55Z

## Objective
Produce decision-pack evidence item 2: one answered Tier 3 interrupt round-trip over the named transport and one deliberately timed-out interrupt reaching safe-hold and clean halt, each with a complete transport-independent record, plus reentry completing the mission.

## Trial Work (synthetic but genuine)
The docs-only carrier work is recording two genuinely pending rung-1 adjudications into `DURATION_LADDER_PLAN.md` (v0.2) and `docs/Factory/v3/ladder/rung1/RUNG1_MISSION_STATE.md`:

- Decision 1 (Interrupt `HDI-TT-001`, to be answered): does rung 1 pass as mechanics evidence given its ~7-minute actual duration, or must it re-run with genuinely larger scope before rung 2?
- Decision 2 (Interrupt `HDI-TT-002`, deliberately timed out): should ladder rungs keep hour-based names or move to budget-and-waypoint classes (per MR_019 design signal)? The sponsor is instructed NOT to answer this within its timeout; the mission records the timeout, checkpoints, enters safe-hold, and halts cleanly. The answer is obtained at reentry.

## Protocol (per trial plan)
1. Pre-mission delivery test: send a test notification; sponsor confirms in-session that it arrived and names the surface (desktop or phone). No Go without confirmed delivery.
2. Interrupt 1 (`HDI-TT-001`): notification + structured question; sponsor answers; record answer/interpretation/plan delta; apply Decision 1 to the ladder plan.
3. Interrupt 2 (`HDI-TT-002`): notification + structured record; named timeout: the end of the turn in which it is raised (sponsor deliberately does not answer it; any reply addresses only non-interrupt matters). On timeout: record outcome, checkpoint, safe-hold (no further file changes), clean halt with reentry instruction.
4. Reentry session: reread envelope, mission state, interrupt records; obtain the pending Decision 2 answer; apply it; close out with mission record `MR_20260610_020`.

## Authorized Files
- `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- `docs/Factory/v3/ladder/rung1/RUNG1_MISSION_STATE.md`
- `docs/Factory/v3/ladder/transport_trial/TRIAL_MISSION_ENVELOPE.md`
- `docs/Factory/v3/ladder/transport_trial/TRIAL_MISSION_STATE.md`
- `docs/Factory/v3/ladder/transport_trial/TRIAL_INTERRUPT_HDI_TT_001.md`
- `docs/Factory/v3/ladder/transport_trial/TRIAL_INTERRUPT_HDI_TT_002.md`
- `docs/Factory/v3/mission_records/MR_20260610_020_interrupt_transport_trial.json`

## Forbidden Scope
Any transport beyond the named one; Telegram bot/token/polling/webhook; validators, fixtures, templates, skills; any non-listed file; credential use; unattended continuation past safe-hold.

## Allowed Commands
Read/search/status commands; `date -u`; the advisory verification commands; `git diff --check`; scoped `git add`/`commit`/`push` at closeout.

## Data Minimization
Interrupt records store question, options, answer, command-sourced timestamps, and the transport surface name only — no device identifiers, account identifiers, or platform metadata.

## Budget
Soft tool-call budget 60; checkpoint at each protocol step.

## Halt, Safe-Hold, Reentry
Safe-hold per `CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`: after `HDI-TT-002` timeout, no further file changes except the timeout record, checkpoint, and halt note; clean halt; reentry rereads authored artifacts and resolves the open interrupt before any further change. V2 fallback triggers: delivery test fails twice, scope expansion, unresolved advisory finding.
