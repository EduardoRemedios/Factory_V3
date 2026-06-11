# Mission Envelope — Backlog Research Spike (Waypoints, Economics, Fresh-Worker Reentry, Friction)

## Status
Active mission envelope (file artifact) for a docs-only research spike. Research-only and non-enforcing with respect to gates; executes under `V3-OP-001` authority. This envelope approves this mission only — it promotes no profile, approves no validator, schema file, gate, or new research-lane anchor, and approves no trial execution.

## Sponsor Approval
- Sponsor: Eduardo dos Remedios
- Approval: given in the Claude Code session thread on 2026-06-11 — "ok agree GO", following a sponsor-requested red-team review of the improvement-idea list (challenge, refine, sequence) delivered in the same thread
- Approval scope: authoring the four named research artifacts only; the fresh-worker reentry trial, the rung-2 run, any economics recording, and any schema or lane promotion each require their own envelope and sponsor Go

## Mission Identity
- Mission ID: `BACKLOG_RESEARCH_SPIKE_20260611`
- Profile authority: `V3-OP-001`
- Harness: Claude Code; model at start: `claude-fable-5` (routing not enabled)
- Base commit: `1408913`
- Start timestamp (command-sourced): 2026-06-11T07:30:54Z

## Objective
Convert the sponsor's reviewed improvement ideas into evidence-first research artifacts that instrument the duration ladder before rung 2 runs: a waypoint shadow-schema candidate, a mission-economics vocabulary, a fresh-worker reentry trial plan, and ladder friction-measurement requirements.

## Success Criteria
1. `SHADOW_SCHEMA_CANDIDATES.md` gains a `mission_waypoint` candidate shape with an essential/optional field split and the restriction-projection authority boundary stated.
2. `MISSION_ECONOMICS_VOCABULARY.md` exists with at most five terms, anti-theater grounding rules (including the sunk-cost prohibition), and a recording cadence that adds no required rung-2 checkpoint load.
3. `FRESH_WORKER_REENTRY_TRIAL_PLAN.md` exists with allowed/forbidden inputs, the sealed answer-key protocol, pass/fail criteria, evidence requirements, and an explicit statement of how it differs from POC Mission 012/013 fresh-session resumes.
4. `DURATION_LADDER_PLAN.md` (v0.4) names the rung-2-onward friction counters as advisory observations, never targets.
5. `ladder/LADDER_STATUS.md` (v0.4) reflects the new artifacts in its follow-ups and rung-2 gate description.
6. No boundary or approval language is weakened anywhere; every new artifact carries research-only and non-enforcing posture language.
7. Advisory suite passes at closeout.

## Non-Goals
No validator, fixture, template, schema-file, or skill changes; no anchor-registry rows added; no trial execution; no POC-repo changes; no rung-2 envelope content; no economics recording; no new approvals or promotions.

## Waypoints
- WP1: Add the `mission_waypoint` candidate shape to `SHADOW_SCHEMA_CANDIDATES.md` (v0.3). Verification: entry present with required-boundary and enforcement-status lines matching the file's existing pattern.
- WP2: Author `MISSION_ECONOMICS_VOCABULARY.md` (v0.1). Verification: advisory lint + NL pilot pass; grounding rules include the sunk-cost prohibition.
- WP3: Author `FRESH_WORKER_REENTRY_TRIAL_PLAN.md` (v0.1). Verification: advisory lint + NL pilot pass; plan states it executes only after rung 2 with its own approval.
- WP4: Update `DURATION_LADDER_PLAN.md` (v0.4 friction counters) and `ladder/LADDER_STATUS.md` (v0.4 follow-ups + rung-2 gate note). Verification: advisory lint + NL pilot pass.
- WP5: Closeout mission record `MR_20260611_022`, full advisory suite, scoped commit per `same_commit` convention.

## Decision Plan
- Tier 1 (pre-resolved): the idea-by-idea verdicts and sequencing were reviewed and agreed by the sponsor in-thread on 2026-06-11 before this envelope was written (waypoints as shadow candidate now; economics vocabulary-only now with the lane decision gated on rung-2 cost data; fresh-worker trial planned now and executed after rung 2 in cross-harness form; friction counters as ladder requirements).
- Tier 2 (resolve-and-log): wording, ordering, and section placement within authorized files.
- Tier 3: none planned; halt and ask if any edit would require weakening boundary language.

## Authorized Files
- `docs/Factory/v3/missions/MISSION_V3OP001_20260611_BACKLOG_RESEARCH_SPIKE.md`
- `docs/Factory/v3/SHADOW_SCHEMA_CANDIDATES.md`
- `docs/Factory/v3/MISSION_ECONOMICS_VOCABULARY.md`
- `docs/Factory/v3/FRESH_WORKER_REENTRY_TRIAL_PLAN.md`
- `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/mission_records/MR_20260611_022_backlog_research_spike.json`

## Forbidden Scope
Validators, fixtures, templates, skills, schema files under any path, anchor-registry rows, top-level README, `GOVERNANCE_BOUNDARIES.md`, any new approval/promotion language, transport use, POC repo, rung-2 envelope content.

## Allowed Commands
Read/search/status commands; `date -u`; the five advisory verification commands from the top-level README; `git diff --check`; scoped `git add`/`commit`/`push` after sponsor-approved closeout.

## Budget
- Soft tool-call budget 50 from envelope creation; stop threshold 70 tool calls.
- Checkpoint cadence: single closeout checkpoint in the mission record; no separate mission-state file for this docs-only spike.

## Halt And Safe-Hold Rules
- Halt on failed verification not resolvable within authorized scope.
- Halt if any edit would weaken boundary/approval language.
- V2 fallback triggers: scope expansion beyond authorized files, unresolved advisory finding, contradiction inside this envelope.

## Reentry Rule
On any reentry: reread this envelope and `git status`/diff; verify scope unchanged before continuing.
