# V3 Mission Envelope: AMC v0.2 — Decision Tiers And Timestamped Budgets

## Status
DRAFT — PENDING SPONSOR APPROVAL. Optional `V3-OP-001` use; non-enforcing; based on Mission 012/013 POC evidence and sponsor doctrine recorded in `RAW_BRIEF_20260604_long_running_mission_path.md`.

## Profile
- Profile ID: `V3-OP-001`
- Profile name: Bounded Code Change (docs/templates scope)
- Factory v2 fallback retained: YES

## Objective
Update Adaptive Mission Control to v0.2 and its dependent templates (repository and standalone bootstrap copies) with two evidence-backed changes: (1) timestamped budget instrumentation replacing model-estimated minutes, and (2) the three-tier decision model that makes human interrupts the exception rather than the default.

## Success Criteria
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md` is v0.2 with a changelog entry and two new/updated sections:
  - Budget and timing discipline: checkpoints capture command-sourced timestamps (`date -u +%Y-%m-%dT%H:%M:%SZ`); durations are derived from timestamps or git commit times; model-estimated minutes must never be recorded as measurements (Mission 012/013 showed 6-9x inflation); tool-call counts are the preferred self-reported size metric; rate-limit window awareness states the sponsor's interim target of a ~4-hour run inside a ~5-hour plan window, with throttle/exhaustion producing a clean checkpoint-commit-halt and reentry instruction.
  - Decision tiers: Tier 1 Pre-Resolved Decisions (enumerated and answered by the sponsor in the envelope before execution); Tier 2 Resolve-and-Log (envelope-stated decision principles let the mission decide within authority and record the choice in a deferred-decisions log reviewed at closeout); Tier 3 Human Decision Interrupt (reserved for authority, safety/privacy, irreversibility, or envelope contradictions; mission continues parallel authorized work while pending where possible; blocked means checkpoint, commit, halt cleanly).
- `docs/Factory/v3/templates/V3_MISSION_ENVELOPE_TEMPLATE.md` gains optional `Pre-Resolved Decisions`, `Decision Principles (Tier 2)`, and `Deferred Decisions Log` sections.
- `docs/Factory/v3/templates/V3_MISSION_CHECKPOINT_TEMPLATE.md` Budget State carries: `checkpoint_recorded_at` (command-sourced UTC timestamp), elapsed-since-last-checkpoint derived from timestamps, tool-call count, qualitative context note, stop-threshold judgment, and a rate-limit window note.
- `docs/Factory/v3/templates/V3_MISSION_STATE_TEMPLATE.md` references the deferred-decisions log and last timestamp.
- `docs/Factory/v3/templates/V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json` gains optional fields `tier` (default `tier_3`) and `preresolution_check` (why Tier 1/2 could not answer this), remaining valid JSON.
- The standalone bootstrap copies under `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/` (canons/ADAPTIVE_MISSION_CONTROL.md, templates/V3_MISSION_CHECKPOINT_TEMPLATE.md, templates/V3_MISSION_STATE_TEMPLATE.md, templates/V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json, templates/V3_POC_MISSION_TEMPLATE.md) receive the same changes so future POC projects seed v0.2 behavior.
- Status docs record the change: `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, `docs/CHANGELOG.md`, and `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` (version bump + changelog line).
- This mission dogfoods the new rules: it authors a mission record plus a checkpoint file using the new timestamped Budget State format, and its own envelope carries the Pre-Resolved Decisions below.
- All edits remain research-only and non-enforcing: no promotion, no required gates, no profile creation, no Telegram approval, no default-mode language.

## Pre-Resolved Decisions (Tier 1)
- PRD-001 Timestamp format: ISO 8601 UTC via `date -u +%Y-%m-%dT%H:%M:%SZ`. Decided by sponsor doctrine 2026-06-04.
- PRD-002 Duration source of truth: timestamps/git commit times; checkpoint-estimated minutes are forbidden as measurements and may appear only as clearly labeled forecasts. Decided by sponsor doctrine 2026-06-04.
- PRD-003 Interrupt template change: add optional `tier` and `preresolution_check` fields rather than a breaking schema change; existing interrupt records remain valid. Decided at envelope authoring.
- PRD-004 Duration bands: retained as observational guardrails only; AMC v0.2 keeps the no-size-class principle and supersedes Mission 006-era size classes. Decided at envelope authoring.
- PRD-005 Rate-limit parameter: record "~4 hours inside a ~5-hour window" as the sponsor's current interim target, marked as a tunable operational parameter, not a constraint baked into validators. Decided by sponsor 2026-06-04.

## Decision Principles (Tier 2)
- Prefer the smallest wording change that carries the rule; preserve existing section ordering and tone.
- Where repo and bootstrap copies have drifted, make the bootstrap match the repo template after edits.
- Anything ambiguous about promotion/boundary language: copy the existing boundary phrasing style already used in the document being edited.
- Log all Tier 2 choices in the mission record notes for closeout review.

## Eligible-Work Rationale
Bounded docs/templates change with deterministic verification, no runtime behavior, no dependencies, and clear file authority — squarely inside optional `V3-OP-001`. Executing it under V3 governance also adds home-repository V3 evidence.

## Non-Goals
- No validator code changes (the versioned mission-record validator is a separate mission).
- No new profiles (`V3-OP-003` remains a candidate only), no promotion, no required gates, no enforcement, no routing, no telemetry mandates.
- No live Telegram/Channels/bridge work of any kind.
- No POC repo edits in this mission.
- No V2 doc changes beyond the named status docs.

## Authorized Scope
Files and directories:
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md`
- `docs/Factory/v3/templates/V3_MISSION_ENVELOPE_TEMPLATE.md`
- `docs/Factory/v3/templates/V3_MISSION_CHECKPOINT_TEMPLATE.md`
- `docs/Factory/v3/templates/V3_MISSION_STATE_TEMPLATE.md`
- `docs/Factory/v3/templates/V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json`
- `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/canons/ADAPTIVE_MISSION_CONTROL.md`
- `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/templates/V3_MISSION_CHECKPOINT_TEMPLATE.md`
- `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/templates/V3_MISSION_STATE_TEMPLATE.md`
- `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/templates/V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json`
- `docs/Factory/v3/standalone_bootstrap/package/.factory-v3/templates/V3_POC_MISSION_TEMPLATE.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/missions/MISSION_V3OP001_20260604_AMC_V02_DECISION_TIERS_AND_TIMESTAMPS.md` (this envelope: status updates only)
- `docs/Factory/v3/mission_records/MR_20260604_007_amc_v02_update.json`
- `docs/Factory/v3/mission_records/MR_20260604_007_amc_v02_checkpoints.md`
- `docs/Factory/v3/mission_records/README.md` (index row only)

## Forbidden Scope
Files, directories, systems, or concerns:
- `scripts/` (no validator or tooling changes), `tests/`, `tools/`, `.agents/`, `AGENTS.md`.
- Factory V2 process docs under `docs/Factory/` other than the named status docs.
- The POC repository.
- Any promotion, enforcement, gate, routing, runtime-authority, Telegram, or V2-removal language.

## Allowed Commands
- Read/search/status: `pwd`, `ls`, `find`, `sed`, `rg`, `git status --short --branch`, `git diff --stat`, `git log --oneline -n <N>`.
- Timestamps: `date -u +%Y-%m-%dT%H:%M:%SZ`.
- Git (scoped): `git add <authorized paths only>`, `git commit -m "AMC v0.2 checkpoint <NNN>: <summary>"` and final `git commit -m "AMC v0.2: decision tiers and timestamped budgets"`. No push, pull, branch, merge, rebase, tag, reset, checkout, remote, or init.
- Verification: `bash scripts/knowledge_lint.sh`; `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`; `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json`; `python3 -m json.tool` on edited JSON templates and the new mission record; `diff` between repo templates and bootstrap copies for the synced files.

## Dependency Policy
- New dependencies allowed: NO
- If YES, human approval path: not applicable.

## Verification
Commands and expected evidence:
- `bash scripts/knowledge_lint.sh` passes.
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json` reports zero findings/warnings.
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json` reports `ADVISORY_PASS`.
- `python3 scripts/factory_v3_mission_record_lint.py --target docs/Factory/v3/mission_records --json` remains advisory-clean for the new record (note: the validator predates the versioned-schema mission; record findings honestly if the shape triggers advisory notes).
- `python3 -m json.tool` passes on `V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json` (both copies) and the new mission record.
- `diff` confirms each synced bootstrap file matches its repo counterpart where the envelope requires parity.
- AMC version reads v0.2 with changelog; ROADMAP_TO_FULL_VISION bumps with changelog line.
- The mission's own checkpoint file demonstrates the new timestamped Budget State format.

## Halt Rules
Stop if:
- any edit would require files outside authorized scope,
- any change would alter validator behavior or create enforcement,
- promotion/boundary language cannot be preserved with confidence (Tier 3 interrupt to sponsor),
- verification fails and the fix implies scope expansion,
- git authority beyond the scoped add/commit set appears necessary.

## Interruption And Reentry
- Resume only from authored artifacts (this envelope, the checkpoint file, the mission record) and current repository state.
- Halt if derived state conflicts with authored artifacts.

## V2 Fallback Triggers
Fallback to Factory v2 if:
- objective ambiguity remains after Tier 1/2 resolution,
- scope expands beyond the named files,
- verification fails irrecoverably within authority,
- human sponsor requests V2.

## SIMPLE-CODE-GATE Expectations
- Smallest clear change carrying the two rules.
- No doc bloat, no speculative sections, no new abstractions.
- No silent weakening of research-only/non-enforcing language.
