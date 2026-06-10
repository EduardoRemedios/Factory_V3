# Duration Ladder Rung 1 — Mission Envelope

## Status
Active mission envelope (file artifact) for the first duration-ladder rung per `DURATION_LADDER_PLAN.md`. Research-only and non-enforcing with respect to gates; executes under `V3-OP-001` authority per waypoint. This envelope approves this mission only.

## Sponsor Approval
- Sponsor: Eduardo dos Remedios
- Approval: given in the Claude Code session thread on 2026-06-10 — "yes approved with the lowest risk approach to start the ladder"
- Approval scope: rung 1 only; rung 2 requires the interrupt-transport trial first; no transport use in this mission

## Mission Identity
- Mission ID: `LADDER_RUNG1_20260610`
- Profile authority: `V3-OP-001` per waypoint (V3-OP-003 remains candidate; this mission gathers its evidence)
- Harness: Claude Code; model at start: `claude-fable-5` (routing not enabled)
- Base commit: `3b107ba`
- Start timestamp (command-sourced): 2026-06-10T13:28:16Z

## Objective
Bring the repository state narratives into consistency with the nine missions completed on 2026-06-10 (MR_010 through MR_018), exercising rung-1 mechanics: waypoints, checkpoints with mission-health signals, authored mission state, one thread-based Tier 3 interrupt, and full closeout.

## Success Criteria
1. State docs accurately reflect: governance-boundaries split, new canon (mutable harness state, skill provenance, regulatory crosswalk, standing-authorization candidates), the V3-OP-003 candidate + decision pack, mission-health vocabulary, trial plans, and anchors 008-010.
2. No boundary or approval language is weakened anywhere.
3. Checkpoint series complete with all six `MISSION_HEALTH_VOCABULARY.md` signals cited at each checkpoint.
4. Advisory suite passes at closeout.

## Non-Goals
No validator, fixture, template, or skill changes; no new approvals or promotions; no transport use; no POC-repo changes.

## Waypoints
- WP1: Audit the five state docs against today's mission records; produce findings list in mission state. Verification: findings list cites specific stale passages.
- WP2: Update `docs/Factory/v3/README.md` and `docs/Factory/v3/USER_GUIDE.md`. Verification: advisory lint + NL pilot pass.
- WP3: Update `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`. Verification: advisory lint + NL pilot pass. Note: WP3 contains a planned Tier 3 decision (see Decision Plan).
- WP4: Full verification sweep, closeout mission record `MR_20260610_019`, rung-1 evidence summary in mission state.

## Decision Plan
- Tier 1 (pre-resolved): today's artifacts are described as research-only/candidate exactly as their own status sections state; README (top-level) is already current and out of scope; anchor registry is already current (v0.10) and out of scope except if audit finds an inconsistency.
- Tier 2 (resolve-and-log): wording, ordering, and which stale passages to touch within authorized files.
- Tier 3 (planned interrupt): the "next operational-readiness decision" language in state docs currently centers the V3-only POC application scope. Whether the named next decision should remain POC-centric or become the V3-OP-003 ladder is a sponsor roadmap decision. The mission will raise this as a thread-based interrupt with a structured record before executing WP3.

## Authorized Files
- `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`
- `docs/Factory/v3/README.md`, `docs/Factory/v3/USER_GUIDE.md`, `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md` (only if the audit finds an inconsistency; change-log entry required)
- `docs/Factory/v3/ladder/rung1/` (envelope, mission state, checkpoints, interrupt record)
- `docs/Factory/v3/mission_records/MR_20260610_019_ladder_rung1_state_doc_consistency.json`

## Forbidden Scope
Validators, fixtures, templates, skills, top-level README, GOVERNANCE_BOUNDARIES.md, any new approval/promotion language, transport use, POC repo.

## Allowed Commands
Read/search/status commands; `date -u`; the five advisory verification commands from the top-level README; `git diff --check`; scoped `git add`/`commit`/`push` after sponsor-approved closeout.

## Budget
- Plan target: roughly 60-90 minutes wall clock measured by command-sourced timestamps; soft tool-call budget 120 from envelope creation; stop threshold 180 tool calls or 3 hours.
- Checkpoint cadence: end of each waypoint, plus before raising the Tier 3 interrupt.

## Halt And Safe-Hold Rules
- Halt on failed verification not resolvable within authorized scope.
- Halt if any edit would weaken boundary/approval language.
- The Tier 3 interrupt has no fixed timeout (sponsor is in-session); if the session ends before an answer, the mission is paused at its checkpoint and reenters per stale-reentry discipline: reread envelope, mission state, and diff before continuing.
- V2 fallback triggers: scope expansion beyond authorized files, unresolved advisory finding, contradiction inside this envelope.

## Reentry Rule
On any reentry: reread this envelope, the mission state file, and `git status`/diff; verify scope unchanged; resolve any open interrupt before further edits.
