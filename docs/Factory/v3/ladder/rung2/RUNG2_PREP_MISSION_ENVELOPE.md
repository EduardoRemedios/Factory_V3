# Rung 2 Preparation — Mission Envelope (Transport Decision Recording)

## Status
Active mission envelope (file artifact) for a small docs mission recording the rung-2 transport sponsor decision. Research-only and non-enforcing with respect to gates; executes under `V3-OP-001` authority. This envelope approves this mission only — it does not approve rung 2 itself, any transport use, or any POC-repo change.

## Sponsor Approval
- Sponsor: Eduardo dos Remedios
- Approval: given in the Claude Code session thread on 2026-06-11 — "sure proceed with mission A"
- Approval scope: this recording mission only; rung-2 envelope drafting in the POC repo is a separately approved mission; the rung-2 run itself requires its own envelope and sponsor Go

## Mission Identity
- Mission ID: `RUNG2_PREP_20260611`
- Profile authority: `V3-OP-001`
- Harness: Claude Code; model at start: `claude-fable-5` (routing not enabled)
- Base commit: `8299317`
- Start timestamp (command-sourced): 2026-06-11T06:41:09Z

## Objective
Record the sponsor decision `HDI-RUNG2-001` (rung-2 transport = Codex harness with Codex mobile, option b from `LADDER_STATUS.md` gate 1) as a structured decision record, and bring the ladder status and anchor registry into consistency with it.

## Success Criteria
1. Structured decision record exists with the question, options, answer, answer source, and named consequences.
2. `LADDER_STATUS.md` shows gate 1 resolved and the remaining-gates list correctly numbered.
3. `ANCHOR_REGISTRY.md` row `V3-ANCHOR-004` names the chosen transport in its next gate.
4. No boundary or approval language is weakened anywhere; the decision record approves the transport choice only, not the rung-2 run.
5. Advisory suite passes at closeout.

## Non-Goals
No validator, fixture, template, or skill changes; no transport use in this mission; no POC-repo changes; no rung-2 envelope drafting (that is the next mission); no new approvals or promotions beyond recording the named sponsor decision.

## Waypoints
- WP1: Author the decision record `RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`. Verification: record contains question, options, answer source quote, and consequences.
- WP2: Update `LADDER_STATUS.md` (v0.3) and `ANCHOR_REGISTRY.md` (`V3-ANCHOR-004` row + change log); add change-log entry to `INTERRUPT_TRANSPORT_TRIAL_PLAN.md` recording the selection. Verification: advisory lint + NL pilot pass.
- WP3: Closeout mission record `MR_20260611_021`, full advisory suite, scoped commit per `same_commit` convention.

## Decision Plan
- Tier 1 (pre-resolved): the transport decision itself was taken by the sponsor in-thread before this envelope was written; this mission records it, it does not re-open it.
- Tier 2 (resolve-and-log): wording and placement of the updates within authorized files.
- Tier 3: none planned; halt and ask if any edit would require weakening boundary language.

## Authorized Files
- `docs/Factory/v3/ladder/rung2/RUNG2_PREP_MISSION_ENVELOPE.md`
- `docs/Factory/v3/ladder/rung2/RUNG2_TRANSPORT_DECISION_HDI_RUNG2_001.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/INTERRUPT_TRANSPORT_TRIAL_PLAN.md` (change-log entry and transport-selection note only)
- `docs/Factory/v3/mission_records/MR_20260611_021_rung2_transport_decision.json`

## Forbidden Scope
Validators, fixtures, templates, skills, top-level README, `GOVERNANCE_BOUNDARIES.md`, any new approval/promotion language, transport use, POC repo, rung-2 envelope content.

## Allowed Commands
Read/search/status commands; `date -u`; the five advisory verification commands from the top-level README; `git diff --check`; scoped `git add`/`commit`/`push` after sponsor-approved closeout.

## Budget
- Soft tool-call budget 40 from envelope creation; stop threshold 60 tool calls.
- Checkpoint cadence: this mission is small enough for a single closeout checkpoint in the mission record; no separate mission-state file.

## Halt And Safe-Hold Rules
- Halt on failed verification not resolvable within authorized scope.
- Halt if any edit would weaken boundary/approval language.
- V2 fallback triggers: scope expansion beyond authorized files, unresolved advisory finding, contradiction inside this envelope.

## Reentry Rule
On any reentry: reread this envelope and `git status`/diff; verify scope unchanged before continuing.
