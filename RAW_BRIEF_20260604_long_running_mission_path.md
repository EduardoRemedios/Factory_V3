# Raw Brief: Path From Standalone POC Evidence To Long-Running Remote-Interrupt Missions

## Status
Sponsor input / raw brief only. Research-only and non-approving. This document does not approve any mission, profile, bridge, deployment, enforcement, promotion, or V2 removal. It is intended as the raw brief for the next planning run(s).

## Date
2026-06-04

## Target End State (Sponsor Vision)
Subject to available tokens on the Claude or Codex plan, a single V3 mission can run for several hours, pausing only to ask the sponsor a question or clarification through an asynchronous surface: a Telegram bridge, the Codex app on Android, or the Claude app on the phone. The mission continues from authored artifacts after each answer, halts cleanly on failure or budget exhaustion, and produces replayable evidence throughout.

## Where We Are (as of 2026-06-04)
- Factory_V3 repo: Phases 0–2.5 complete, Phase 3 telemetry conditionally recommended (advisory only), Phase 4 eval expansion in progress, research-only. Only approved operational profile: `V3-OP-001 Bounded Code Change`.
- POC repo (seeded from `docs/Factory/v3/standalone_bootstrap/`): standalone V3 execution evidence through Mission 011 with Codex — synthetic-only, local-only, no-new-dependency missions. Provisional read: `PASS_WITH_LIMITATIONS` on the POC rubric (deployment and real-data boundaries unproven).
- `ADAPTIVE_MISSION_CONTROL.md` v0.1 already defines the long-running architecture: checkpoints, authored mission state, human decision interrupts, plan deltas, and a 4-step phased Telegram path. None of it is yet proven on a real long mission.
- `PROMOTION_CRITERIA.md` v0.3 already names long-running mission promotion inputs (checkpoint, mission-state, interrupt, plan-delta, verification side-effect, git-authority evidence).
- Mission record schemas have diverged: POC Missions 002–006 and 010–011 use the richer `v0.1-poc-standalone` shape; 007–009 use a simpler flat shape with `duration_band`. The Factory_V3 validator does not version-handle both. Strictly there are three variants: 010–011 add an `adaptive_mission_control` block that 002–006 lack.

## POC Repo Review Findings (2026-06-04, `V3_POC_App_Creation`)
- The app is real: `ppos_core` (~3,800 lines, stdlib-only, SQLite), a no-build workbench UI, 35+ DTU fixtures, 9 manual-export fixtures, 148 passing tests, per-mission verify scripts and QA harnesses, and browser-verified UI evidence through Mission 011.
- Long-horizon missions already exist. Missions 007–011 ran in a `one_to_two_hours` duration band; 010–011 used checkpoints, authored mission state, and AMC-shaped records. So "multi-hour mission on artifacts" is partially proven — what is unproven is cross-session resume after a genuine context break, and any real mid-mission human interrupt (every record shows `interrupts: none`).
- Budget state is not instrumented. Every checkpoint records `Token budget: not explicitly set`. The checkpoint template carries the field; no mission has filled it with measured data.
- Git write authority has never been granted. Mission 011 closed out with changes uncommitted because the envelope did not authorize commits. For multi-hour unattended missions, scoped checkpoint commits are effectively required (durable evidence, rollback points); AMC already defines the git-authority envelope sections.
- There are two distinct Telegram tracks with different owners. Track 1 is a POC app feature: Telegram as a surface where the app's user registers intent (coaching chat, per `POC_VISION.md`); it is app code, lives in the POC repo, and is approved through POC missions. Track 2 is a Factory V3 product feature: Telegram as a surface through which a running V3 mission asks the mission author / human orchestrator for clarification; it is POC-agnostic, homed in the Factory_V3 repo, governed by AMC's bridge boundary, and usable by any V3 mission in any project. One research spike on bot/token handling, identity allowlisting, timeout, and replay logging can inform both, but findings feed two separate approval paths in two repos, and the two surfaces must never share bots, tokens, or state.
- Mission 006's size-class guidance (micro/standard/long-horizon with duration bands) predates AMC v0.1, which deliberately rejects time/size classes as the sizing primitive. Missions 007–009's flat records are artifacts of that era. The back-port should reconcile the two: AMC supersedes size classes; duration bands remain operational guardrails only.
- Mission 011's own recommended next step (Mission 012: manual-import hardening with explicit real-data approval interrupt design) is a natural host for the first deliberate interrupt trial — the mission genuinely needs a human decision, so the interrupt evidence would not be artificial.

## Gap Analysis
The vision requires five capabilities the current evidence does not yet cover:

1. Continuation from artifacts over hours. Partially proven: Missions 007–011 ran 1–2h on checkpoints and mission state within a single session. Unproven: resume in a fresh session after a real context break, and continuation across an answered interrupt.
2. Asynchronous human interrupts. No mission has ever raised one (`interrupts: none` in every record); no transport exists.
3. Trustworthy unattended halt/recovery. Negative-path evidence (failed verification, recovery, unresolved interrupt, stale reentry, fallback) is still mostly missing. You cannot leave a mission alone until halting is proven, because you will not be there to catch it.
4. Budget-aware execution. "Subject to enough tokens" must become an operational behavior: measure burn, checkpoint-and-halt gracefully at budget exhaustion, resume cleanly in a fresh session. Today every checkpoint records `Token budget: not explicitly set`.
5. A mission runner. Something must keep the mission alive across sessions: re-invoke the harness from mission state, distinguish halt from completion, and respect enforcement. This is a minimal early slice of Phase 7 (persistent mission runtime) and should be named as such.
6. Git authority for durable evidence. Long missions need scoped commit authority at checkpoints (Mission 011 ended uncommitted for lack of it). AMC defines the envelope sections; no mission has exercised them.

## Proposed Workstreams

### Track A — Consolidate the POC (immediate, low risk)
- A1. DONE (2026-06-04). Interim adjudication approved by the sponsor: `PASS_WITH_LIMITATIONS`, 17/22, at the Mission 011 checkpoint. Artifacts: `V3_POC_App_Creation/.factory-v3/evals/V3_POC_EVAL_RECORD_20260604.json` and `V3_POC_EVAL_ADJUDICATION_NOTE_20260604.md`. Eight named limitations include deployment (localhost smoke only), no negative-path evidence, unproven interrupt lifecycle, no cross-session resume, unfilled budget fields, no git mission authority, and record-schema divergence.
- A2. Back-port the evidence: update `PROJECT_STATE.md`, `ROADMAP.md`, and `ROADMAP_TO_FULL_VISION.md` so the POC is recorded as having standalone V3 execution evidence through Mission 011, not merely candidate/future status.
- A3. Versioned mission-record validator: add a `schema_version` discriminator to `factory_v3_mission_record_lint.py`, support the Factory_V3 v0.1 shape, `v0.1-poc-standalone` with and without the `adaptive_mission_control` block, and the flat 007–009 shape (validate or migrate), with fixtures for each. Prerequisite for any runner or replay tooling that must trust record format. The back-port should also reconcile Mission 006 size-class guidance with AMC v0.1 (AMC supersedes; duration bands stay guardrails only).

### Track B — Negative/recovery evidence (parallel with A)
Deliberately seeded POC missions producing real records for: failed-verification halt, recovery after failed check, unresolved human interrupt with timeout behavior, stale reentry rejection, and fallback/no-go. Use the existing `PHASE4_NEGATIVE_CASE_OPPORTUNITY_REGISTER.md` discipline. This track gates everything unattended.

### Track C — Deployment scope (anytime before full PASS upgrade)
One separately authorized POC mission: private local deployment with explicit deployment boundary, secrets policy, rollback, and smoke verification. Closes the `Deployment evidence` rubric dimension. Not blocking for Track D.

### Track D — Long-running mission capability (the new work)
- D1. File-based interrupt trial (AMC phased path step 1): host it in Mission 012 (manual-import hardening with real-data approval interrupt design, already recommended by Mission 011's closeout). The mission genuinely requires human decisions, so interrupts answered by the sponsor editing the interrupt JSON produce non-artificial evidence for the interrupt lifecycle, plan deltas, and continuation. Include at least one deliberate cross-session resume: end the session at a checkpoint mid-mission and resume in a fresh session from artifacts only.
- D2. Budget instrumentation: fill the existing checkpoint `Budget State` fields with measured token/usage burn per phase during D1; add graceful checkpoint-and-halt on budget exhaustion and verified clean resume. Also grant scoped git commit authority at checkpoints per AMC's git-authority envelope sections, so multi-hour evidence is durable and rollbackable.
- D3. Harness session research spike (planning-only): compare, with current documentation and hands-on checks, (a) Codex CLI headless/exec and Codex cloud tasks plus the Codex Android app surface for follow-up questions, (b) Claude Code headless/resume and Claude mobile surfaces, (c) a self-built Telegram bridge. Evaluate: unattended session limits, resume semantics, notification/reply path to the phone, identity control, credential handling, replayability of the Q&A, cost. The harness-native mobile surfaces may already deliver most of the vision and should be evaluated before building a bridge. Scope the Telegram portion to serve both consumers — the V3 mission-interrupt bridge and the PPOS app's planned Telegram coaching surface (`POC_VISION.md`) — while keeping the two separately approved and state-isolated.
- D4. Interrupt bridge implementation (only after D3 and separate approval, per AMC boundary): a V3 product capability homed in the Factory_V3 repo, agnostic of any particular mission or project — a small local relay that watches mission interrupt files for `pending` interrupts, notifies the chosen surface, validates an allowlisted identity, writes the answer back into the interrupt record, and keeps a replay log. Timeout behavior must default to halt. The POC repo is its first consumer/testbed, not its home. This is distinct from any POC app Telegram adapter, which is product code approved through POC missions.
- D5. Mission runner (minimal Phase 7 slice, separately approved): a script (candidate: `factoryctl mission-run`) that loops — read mission state, invoke harness session with a continue-from-artifacts prompt, detect checkpoint/halt/interrupt/completion, stop on anything unresolved. No daemonization or production authority.
- D6. Partial enforcement for unattended profiles (Phase 6 subset, separately approved): before any genuinely unattended multi-hour run, promote a minimal enforced set for the named profile only: forbidden-path check, file-touch budget, required-verification presence, halt-on-failure closeout validation. Advisory-only is acceptable while attended; it is not acceptable unattended.
- D7. New named profiles, each with its own approval: candidate `V3-OP-002 Long-Running Attended Mission` (file-based interrupts, sponsor present) and candidate `V3-OP-003 Long-Running Remote-Interrupt Mission` (phone surface, sponsor away).
- D8. Trial ladder: ~1h attended (D1) → 2–4h semi-attended with remote interrupts → overnight. Each rung produces mission records, optional advisory telemetry, and an eval score before the next rung is attempted.

## Dependency Order
A1 → A2 first (small, immediate). A3 and B run in parallel next. D1–D3 can start now (D1 needs only existing templates). D4 and D5 require D3 plus approval. D6 gates the unattended rungs of D8. C is independent and needed only for upgrading the POC verdict.

## Suggested Next Three Moves
1. A2: back-port the approved adjudication into Factory_V3 governed docs (PROJECT_STATE, ROADMAP, ROADMAP_TO_FULL_VISION), citing the eval record paths above. (A1 complete 2026-06-04.)
2. A3: versioned mission-record validator with migration fixtures.
3. Mission 012 as the D1 interrupt trial (with D2 budget/git instrumentation), plus the D3 harness/transport research spike that decides Telegram bridge vs Codex/Claude native mobile surfaces.

## Boundaries Restated
Nothing here approves live Telegram automation, bot tokens, polling, webhooks, unattended runs, required gates, governance routing, runtime authority, default-mode promotion, Garmin/Hermes use, real personal data, public deployment, or V2 removal. Each gated item above requires its own named approval per existing repo conventions.
