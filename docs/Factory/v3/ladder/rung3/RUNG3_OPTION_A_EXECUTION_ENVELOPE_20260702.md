# Rung 3 Option A Execution Envelope - 2026-07-02

## Status
Research-only, non-enforcing candidate execution envelope only.

This artifact does not authorize execution until the sponsor explicitly approves this exact envelope. It does not promote `V3-OP-003`, approve default V3 use, runtime authority, scheduled or unattended execution, real-data use, live integrations, deployment, required gates, governance routing, or Factory V2 removal.

## Mission Formation Result

### Route
`CANDIDATE_V3_ENVELOPE`

### Candidate Mission
Run a rung-3-class, synthetic-first POC mission in `/Users/eduardodosremedios/V3_POC_App_Creation` that expands coaching/reporting/evidence-review capability while stress-testing Factory V3 checkpointing, interrupt handling, browser QA, verification, and closeout at roughly four-hour scale.

## Problem Statement
Factory V3 needs evidence that it can govern a larger real coding mission without becoming the worker. The POC app is the best current target because it has a green synthetic-only baseline, real product surfaces, governance primitives, prior interrupt/re-entry evidence, and explicit constraints that forbid real data and live integrations.

## Desired Outcome
A completed POC mission that:
- Delivers useful synthetic-first product/governance improvements.
- Records mission-health, checkpoint, interrupt, re-entry, browser, verification, and claim-to-proof evidence.
- Preserves all POC constraints.
- Provides rung-3 evidence for `V3-OP-003` decision-pack review without promoting the profile by itself.

## Non-Goals
- No real personal health or fitness data.
- No Garmin credentials, API calls, scraping, or live data retrieval.
- No live Telegram bot, token, webhook, polling, or message send/receive.
- No scheduler, cron, daemon, queue, background worker, proactive notification, or ambient runtime.
- No public deployment, production infrastructure, cloud storage, or credential-bearing work.
- No new dependency unless a Tier 3 interrupt explicitly approves it.
- No Factory V2 use to design, build, test, govern, lint, recover, validate, stage, pack, or deploy the POC mission.
- No artificial padding to satisfy duration or call floors.

## Assumptions
- POC commit `8f25437` is the baseline unless a newer sponsor-approved POC commit supersedes it before execution.
- Pre-existing untracked POC files `.factory-v3/.DS_Store` and `.factory-v3/missions/MISSION_014_IMPORTED_FACT_QUERY_SEMANTICS_AND_REVIEW_ERGONOMICS.md` are ignored unless the future worker receives explicit direction.
- Browser tooling is available and must pass pre-flight before execution.
- Codex mobile/thread remains the human interrupt surface unless the sponsor names another available surface before Go.
- Sponsor response latency is neutral telemetry; safe-hold timing controls worker posture, not answer validity.

## Selected Option
Option A: synthetic-first product/governance epic.

Option B remains the fallback if browser pre-flight fails, scope sufficiency cannot be proven, or the POC has drifted. Option C remains the deferral path if the POC baseline is no longer suitable.

## Authorized Repository
Future execution repository:

```text
/Users/eduardodosremedios/V3_POC_App_Creation
```

## Authorized Scope For Future Execution
Likely authorized paths, to be rechecked at Go:
- `.factory-v3/missions/MISSION_026_RUNG3_OPTION_A_SYNTHETIC_COHERENCE_AND_REVIEW.md`
- `.factory-v3/evidence/MISSION_026_*`
- `ppos_core/recommendations.py`
- `ppos_core/reports.py`
- `ppos_core/evidence_graph.py`
- `ppos_core/lineage.py`
- `ppos_core/manual_imports.py`
- `ppos_core/precedence.py`
- `ppos_core/quality.py`
- `ppos_core/workbench.py`
- `ppos_core/api.py`
- `ppos_core/cli.py`
- `workbench/index.html`
- `workbench/app.js`
- `workbench/styles.css`
- `tests/test_mission_026_*.py`
- Existing targeted tests when touched.
- Synthetic fixtures under `fixtures/` only when mission-owned and no real data is introduced.
- Mission-owned scripts `scripts/mission_026_*.py` and `scripts/verify_mission_026.py`.

Any additional file requires Tier 2 logging if it is an obvious local test/helper extension inside the same scope, or Tier 3 interrupt if it expands authority, dependencies, data handling, integrations, deployment, or runtime behavior.

## Forbidden Scope For Future Execution
- Files outside the POC repository.
- Factory_V3 repository edits during execution, except final evidence-transfer follow-up in a separate mission.
- `.factory-v3/.DS_Store`.
- Old untracked Mission 014 draft, unless separately approved.
- Real data, credentials, live integrations, scheduler/background behavior, deployment, production infrastructure, public exposure, or new dependency without interrupt approval.
- Git push, pull, fetch, branch, merge, rebase, tag, reset, checkout, remote changes, or init unless separately approved.

## Target Epics And Waypoints

| WP | Epic | Outcome | Acceptance Evidence | Forecast Calls |
| --- | --- | --- | --- | ---: |
| 0 | Pre-flight | Read POC canons, status, latest mission evidence, browser availability, and baseline git state. | Re-entry/state note, browser pre-flight note, current head recorded. | 40-70 |
| 1 | Baseline verification | Confirm Mission 025 baseline. | Full unit suite PASS; Mission 024 verifier PASS; Mission 025 record parses. | 50-90 |
| 2 | Mission 026 scaffolding | Create mission envelope/state/checkpoints with command-sourced timestamps and waypoint table. | Mission-owned evidence files parse/read cleanly. | 70-110 |
| 3 | Coaching boundary consolidation | Extend recommendation outputs so each candidate exposes evidence refs, excluded conflicts, authority boundary, uncertainty, and follow-up state. | Focused unit tests; no fact mutation. | 100-160 |
| 4 | Report coherence | Add morning/evening/weekly-style synthetic report summary improvements using precedence, quality, snapshot, and governance boundary context. | Report tests; prohibited-claim/safety checks. | 100-160 |
| 5 | Evidence review ergonomics | Improve local workbench evidence review across recommendation/report/provenance/conflict status without enabling real data. | UI/static tests plus browser screenshot evidence. | 120-190 |
| 6 | Synthetic approval rehearsal | Exercise import/export approval posture with visible-but-inert real-data controls and local-only export governance. | API/CLI tests; approval state remains inert. | 100-160 |
| 7 | Fixture-only future-surface rehearsal | Add synthetic-only fixture/schema tests for nutrition/medical/report inputs without OCR/PDF/vision/API/live files. | Fixture validation tests; no dependency added. | 110-170 |
| 8 | Browser QA sweep 1 | Desktop rendered checks over reports, recommendations, imports, evidence, and console. | Screenshots, DOM markers, console errors empty or explained. | 90-150 |
| 9 | Browser QA sweep 2 | Responsive/mobile viewport checks over modified surfaces. | Screenshots and no material overflow/overlap. | 80-130 |
| 10 | Verification hardening | Add/update `mission_026` QA and verifier scripts. | QA script PASS; verifier PASS. | 100-160 |
| 11 | Full regression | Run full test suite and targeted scripts; repair in-scope failures only. | Full suite PASS; diff check PASS; JSON parse PASS. | 100-170 |
| 12 | Claim-to-proof closeout | Close mission with mission-health series, command evidence, budget, interrupt/re-entry notes, residual risks, and next recommendation. | Closeout, record, checkpoints complete. | 100-160 |

Bottom-up forecast: `1160-1880` visible calls. Rung-3 floor target: `1100` visible calls. Stop threshold: `2000` visible calls. The mission must close honestly if work completes below the floor; it must not pad.

## Budget And Checkpoint Rules
- Target class: 200-300 minutes wall-clock, but command-sourced timestamps and visible tool calls are evidence; model-estimated minutes are not measurement.
- Call budget: forecast 1160-1880; stop threshold 2000.
- Checkpoint after every waypoint.
- Checkpoint before/after any Tier 3 interrupt.
- Checkpoint before any pause or fresh-session re-entry.
- Record mission-health signals: budget burn, objective value, confidence, drift, risk, continuation judgment.
- Record browser availability state at pre-flight and before browser QA waypoints.

## Allowed Commands
- `git status --short --branch`
- `git log --oneline -n <N>`
- `git diff --stat`
- `git diff --check`
- `rg`, `sed`, `find`, `ls`
- `date -u +%Y-%m-%dT%H:%M:%SZ`
- `python3 -B -m unittest discover -s tests`
- Targeted `python3 -B -m unittest tests.test_mission_026_*`
- Existing targeted tests for touched modules.
- `python3 -B scripts/verify_mission_024.py`
- `python3 -B scripts/verify_mission_026.py`
- `python3 -B scripts/mission_026_*.py --db <tmp sqlite path> --host 127.0.0.1 --port <localhost port>`
- `python3 -m json.tool <mission_026_json_path>`
- Local stdlib server commands already used by the POC, with temp SQLite DB only.
- Browser automation against localhost POC workbench only, if available.

## Dependency Policy
No new dependency by default.

A new dependency requires Tier 3 interrupt with package name, purpose, risk, install command, rollback plan, and verification command. Absence of approval means halt or descope.

## Git Policy
Allowed during future execution:
- `git status --short --branch`
- `git diff --stat`
- `git log --oneline -n <N>`
- `git add <authorized paths only>`
- `git commit -m "Mission 026 checkpoint <NNN>: <summary>"`
- Final `git commit -m "Mission 026 closeout: <summary>"`

Forbidden unless separately approved:
- push, pull, fetch, branch, merge, rebase, tag, reset, checkout, remote changes, init.

## Human Interrupt Rules
Tier 3 interrupt required for:
- real data, credentials, live integration, deployment, scheduler/background behavior, or external write;
- new dependency;
- expanding authorized paths beyond the envelope;
- failed verification where repair would require out-of-scope changes;
- browser unavailable after pre-flight;
- contradictory mission state or stale re-entry;
- budget stop threshold or continuation uncertainty near threshold.

Safe-hold if a Tier 3 interrupt is pending and no authorized parallel work remains.

## Halt And Fallback Rules
Halt or safe-hold if:
- POC baseline is not green and repair is outside scope;
- browser pre-flight fails and browser QA is required;
- V2 is needed;
- a forbidden scope appears;
- evidence artifacts become stale or contradictory;
- full verification cannot be run;
- stop threshold is reached;
- the mission completes early.

Fallback to Option B or heavier planning if Option A scope no longer has enough genuine work to justify rung-3 class.

## Re-Entry Protocol
Before continuing after pause or session restart, read:
1. Active Mission 026 envelope.
2. Mission 026 state.
3. Latest Mission 026 checkpoint.
4. Open interrupt files.
5. Current `git status --short --branch`.
6. Latest verification output.

If any authored state contradicts repo state, safe-hold rather than continue.

## Verification Requirements
- Baseline full unit suite before feature work.
- Focused tests for each changed module.
- Full unit suite after implementation.
- Mission 024 verifier remains PASS unless a documented, in-scope replacement explains why.
- Mission 026 verifier PASS.
- JSON parse checks for record, audit summary, interrupts, and any loop/mission records.
- Browser desktop and responsive evidence for modified workbench surfaces.
- Claim-to-proof table in closeout.
- Explicit no-go scan for real data, live integrations, scheduler/background behavior, deployment, and new dependencies.

## Execution Readiness
`CONDITIONAL READY FOR SPONSOR GO`

The envelope is concrete enough to challenge and approve as a rung-3 execution candidate, assuming:
- POC repo state at Go still matches or intentionally supersedes commit `8f25437`;
- browser pre-flight passes;
- sponsor accepts the waypoint table and git policy;
- sponsor explicitly authorizes execution in a later message.

This is candidate mission-formation output only. It does not authorize execution until the human explicitly approves the mission contract.
