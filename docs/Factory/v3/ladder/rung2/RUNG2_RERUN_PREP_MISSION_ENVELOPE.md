# Rung 2 Rerun Preparation — Mission Envelope (Path Decision Recording)

## Status
Active mission envelope (file artifact) for a small docs mission recording the rung-2 rerun-path sponsor decision. Research-only and non-enforcing with respect to gates; executes under `V3-OP-001` authority. This envelope approves this recording mission only — the rerun itself requires its own envelope in the POC repo and explicit sponsor Go.

## Sponsor Approval
- Sponsor: Eduardo dos Remedios
- Approval: given in the Claude Code session thread on 2026-06-11 — "lets go with option A" — answering the open rerun-path decision named in `HDI-RUNG2-002`
- Approval scope: recording the decision and updating ladder-lane state docs; rerun-envelope drafting in the POC repo is the follow-on activity under the same thread authority, and the rerun run needs its own Go

## Mission Identity
- Mission ID: `RUNG2_RERUN_PREP_20260611`
- Profile authority: `V3-OP-001`
- Harness: Claude Code; model at start: `claude-fable-5` (routing not enabled)
- Base commit: `affb5e4`
- Start timestamp (command-sourced): 2026-06-11T08:30:13Z

## Objective
Record sponsor decision `HDI-RUNG2-003` (rerun path = Option A: genuinely larger scope under the unchanged wall-clock band, with the budget class raised to resolve the stop-threshold contradiction) and update the ladder status and anchor registry.

## Success Criteria
1. Structured decision record exists with the options, answer, and named consequences (including the raised budget class and the pre-rerun standalone-canon fix).
2. `LADDER_STATUS.md` (v0.6) and `ANCHOR_REGISTRY.md` (v0.14) are consistent with the decision.
3. No boundary or approval language weakened; pack criteria unchanged.
4. Advisory suite passes at closeout.

## Non-Goals
No validator, fixture, template, or skill changes; no POC-repo changes within this mission (the rerun envelope is drafted in the POC repo afterward); no rerun execution; no transport use; no design-review execution (Option B not chosen; it remains the mandatory route if the rerun fails duration again).

## Waypoints
- WP1: Author `RUNG2_RERUN_PATH_HDI_RUNG2_003.md`. Verification: record contains options, verbatim answer, consequences.
- WP2: Update `LADDER_STATUS.md` and `ANCHOR_REGISTRY.md`. Verification: advisory lint + NL pilot pass.
- WP3: Closeout mission record `MR_20260611_024`, full advisory suite, scoped commit per `same_commit` convention.

## Decision Plan
- Tier 1 (pre-resolved): the rerun-path decision was taken by the sponsor in-thread; this mission records it without re-opening it.
- Tier 2 (resolve-and-log): wording and placement within authorized files.
- Tier 3: none planned.

## Authorized Files
- `docs/Factory/v3/ladder/rung2/RUNG2_RERUN_PREP_MISSION_ENVELOPE.md`
- `docs/Factory/v3/ladder/rung2/RUNG2_RERUN_PATH_HDI_RUNG2_003.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/mission_records/MR_20260611_024_rung2_rerun_path.json`

## Forbidden Scope
Validators, fixtures, templates, skills, top-level README, `GOVERNANCE_BOUNDARIES.md`, pack-criteria amendment, any new approval/promotion language, transport use, POC repo.

## Allowed Commands
Read/search/status commands; `date -u`; the five advisory verification commands from the top-level README; `git diff --check`; scoped `git add`/`commit`/`push` after sponsor-approved closeout.

## Budget
- Soft tool-call budget 35 from envelope creation; stop threshold 50 tool calls.
- Checkpoint cadence: single closeout checkpoint in the mission record.

## Halt And Safe-Hold Rules
- Halt on failed verification not resolvable within authorized scope; halt if any edit would weaken boundary/approval language.
- V2 fallback triggers: scope expansion beyond authorized files, unresolved advisory finding, contradiction inside this envelope.

## Reentry Rule
On any reentry: reread this envelope and `git status`/diff; verify scope unchanged before continuing.
