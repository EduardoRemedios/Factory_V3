# Factory V3 Mission-Control Contract

## Version
v0.9

## Change Log
- v0.9 (2026-07-13): Recorded Trial 001's 19/23 fail-closed result. The kernel preserved safe hold and prevented product work; the next separate gate is a repaired Trial 002 with explicit ordinary-artifact fields and split critical/completeness scoring.
- v0.8 (2026-07-12): Recorded the three-sample evidence-integrity review decision `KEEP_OPTIONAL_NO_SCHEMA_CHANGE`. The next separate decision is the live fresh-worker artifact-sufficiency trial; this adds no field promotion, validator change, worker orchestration, or runtime authority.
- v0.7 (2026-07-12): Recorded the approved deterministic serial mission-state kernel and third natural optional evidence-integrity record. The next decision is the separate three-sample friction/FP-FN review, then fresh-worker and attended serial-epic gates; no worker orchestration or runtime authority was added.
- v0.6 (2026-07-12): Added optional advisory re-entry decision cases for clean continuation, stale repository state, changed authority, failed verification without recovery authority, and one bounded recovery verification action. These are deterministic semantic examples, not live fresh-session proof or runtime behavior.
- v0.5 (2026-07-12): Implemented the narrow optional mission-record evidence-integrity shape for observation provenance, verifier provenance, per-artifact visual evidence, bounded boundary claims, and completed-record commit consistency. All support remains advisory, backward-compatible, and non-blocking; endurance/exposure fields remain deferred.
- v0.4 (2026-07-12): Reordered advisory backlog work so Mission 026 claim-to-proof evidence informs optional mission-record fields; removed completed template/fixture work from the active next-step sequence.
- v0.3 (2026-07-07): Added the initial advisory mission-control contract template, standalone advisory lint, and deterministic fixtures for next-action authorization, requirement-to-evidence status, independent verification, restartable handoff, unsafe approval flags, and session-memory-only re-entry.
- v0.2 (2026-07-07): Added loop-library-derived governance primitives to the advisory roadmap backlog: next-action authorization, requirement-to-evidence status, independent verification, restartable handoff, loop auditability, direct-source audit, mission formation, and claim-to-proof mapping. This is primitive absorption, not named loop adoption.
- v0.1 (2026-07-02): Initial research-only contract distilled from loop-engineering reconnaissance, Factory V3 loop-governance artifacts, and POC Mission 026 evidence.

## Status
Research-only and non-enforcing.

This document does not approve a new V3 profile, make Factory V3 the default, wire required gates, add runtime authority, start loop orchestration, schedule background work, approve real data, approve live integrations, approve deployment, or remove Factory V2 build-support scaffolding.

## Purpose
Define what Factory V3 should own as the mission-control layer above AI workers.

The core lesson from loop engineering and POC Mission 026 is:

```text
Factory V3 should not merely run loops. Factory V3 should govern loops.
```

Workers should continue to own tactical execution. Factory V3 should own the contract, boundaries, checkpoints, interrupts, verification policy, evidence policy, re-entry rules, and closeout proof.

## Source Evidence
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md`
- `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`
- `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`
- `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_EXECUTION_ENVELOPE_20260702.md`
- `docs/Factory/v3/ladder/rung3/RUNG3_OPTION_A_POST_RUN_EVIDENCE_REVIEW_20260702.md`
- POC repo `/Users/eduardodosremedios/V3_POC_App_Creation`, commit `404a32a`
- POC Mission 026 closeout: `.factory-v3/evidence/MISSION_026_CLOSEOUT.md`
- POC Mission 026 record: `.factory-v3/evidence/MISSION_026_RECORD.json`
- POC Mission 026 audit summary: `.factory-v3/evidence/MISSION_026_AUDIT_SUMMARY.json`
- Repo-root `factory_v3_loop_engineering_recon.md`
- Repo-root `factory_v3_loop_engineering_summary.md`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/next-action-confidence-check/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/loop-harness-verification-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/codex-completion-contract-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/restartable-handoff-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/loop-auditor-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/groundtruth-audit-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/goal-forge-loop/`
- Loop-library source: `https://signals.forwardfuture.com/loop-library/loops/promise-to-proof-loop/`

## Ownership Split

| Concern | Factory V3 mission-control owns | Worker owns |
| --- | --- | --- |
| Mission intent | Objective, success criteria, non-goals, sponsor approval source | Tactical interpretation inside the envelope |
| Authority | Authorized files, commands, tools, dependency policy, external-effect limits | Staying inside the granted authority while executing |
| Loop admission | Whether a loop is allowed, should route to V2, should safe-hold, or should be rejected | No self-admission outside the envelope |
| Checkpoints | Required cadence, required fields, mission-health signals, state persistence | Emitting accurate checkpoint evidence |
| Next action | Authorization to continue, stop, safe-hold, ask, verify, or close | Proposing the next tactical action without self-authorizing expanded scope |
| Verification | Verification policy, required tiers, no-touch checks, evidence freshness expectations | Running checks and preserving outputs |
| Independent verification | Builder/verifier separation policy and acceptance criteria | Serving as builder or verifier only inside the assigned role |
| Interrupts | Decision tiers, approval gates, timeout behavior, safe-hold semantics | Asking only when Tier 1 or Tier 2 cannot resolve safely |
| Re-entry | Read order, stale-state checks, last-safe-checkpoint rule | Resuming only from authored state and current repo evidence |
| Evidence | Requirement-to-evidence status, claim-to-proof requirements, audit summary, closeout record, proof gaps | Producing command, diff, screenshot, test, and artifact evidence |
| Escalation | Terminal-state vocabulary, halt/fallback rules, recovery authorization | Halting when the contract says halt |
| Product implementation | Boundary and review policy | Coding, local navigation, tactical reasoning, test/fix cycles |

## Contract Lifecycle

1. Mission formation:
   - convert intent into an explicit candidate contract;
   - classify whether the work is V3-eligible, V2/heavy-planning, research-only, blocked, or no-go;
   - name unresolved decisions before execution.

2. Loop admission:
   - admit only if objective, authority, tools, verification, evidence, and stop rules are explicit;
   - reject or safe-hold when authority is missing, state is stale, verification is undefined, or external effects are implied.

3. Worker dispatch:
   - give the worker a bounded envelope, allowed commands, verification plan, checkpoint rules, and re-entry instructions;
   - preserve Factory as the authority layer and the worker as the execution layer.

4. Checkpoint cycle:
   - record objective progress, authority status, files touched, commands run, verification status, mission-health signals, open risks, and next action;
   - checkpoint before risky transitions, before/after interrupts, before pause/re-entry, and after verification milestones.

5. Approval and escalation:
   - use Tier 1 pre-resolved decisions where the envelope already answers the question;
   - use Tier 2 resolve-and-log for implementation choices that do not expand authority or weaken boundaries;
   - use Tier 3 human decision interrupts for missing authority, safety/privacy boundaries, dependencies, deployment, failed-verification recovery, contradiction, or irreversible action.

6. Safe-hold or halt:
   - safe-hold before any action that would require guessing, expanding authority, ignoring failed verification, acting on stale state, or creating external effects;
   - halt when continuation would be unsafe, infeasible, unauthorized, or unverifiable.

7. Closeout:
   - prove claims with evidence, not completion prose;
   - record verification, residual risks, FP/FN observations where applicable, and whether evidence transfers to Factory V3 design.

## Required Contract Fields

| Field group | Minimum content |
| --- | --- |
| `mission_envelope` | objective, success criteria, non-goals, sponsor approval source, execution mode |
| `authority_envelope` | authorized paths, forbidden paths, allowed commands, allowed tools, dependency policy, git policy, external-effect policy |
| `loop_admission` | admission rationale, route, rejection/safe-hold conditions, V2 fallback trigger |
| `checkpoint_policy` | cadence, required fields, mission-health signals, budget state, commit/checkpoint relationship |
| `next_action_gate` | proposed next action, authority basis, confidence, required verification before continuing, stop/ask/safe-hold trigger |
| `verification_policy` | required commands, verification tiers, no-touch checks, browser/external proof if needed, failure handling |
| `independent_verification` | builder actor, verifier actor, acceptance criteria, verification result, unresolved gaps, conflict handling |
| `evidence_policy` | required artifacts, requirement-to-evidence status, claim-to-proof mapping, screenshots or logs where relevant, JSON parse rules for records |
| `interrupt_policy` | decision tiers, approval gates, timeout behavior, answer interpretation, plan-delta rule |
| `safe_hold_policy` | safe-hold reasons, blocked action, last safe checkpoint, human decision needed, re-entry instructions |
| `reentry_protocol` | read order, stale-state checks, protected-surface checks, current repo-state verification, one safe next action |
| `terminal_states` | success, no-op, blocked, approval-required, failed-verification, exhausted, stagnated, unsafe, stale-reentry, ambiguous, infeasible, insufficient-context |
| `worker_interface` | worker role, allowed tactical autonomy, evidence emission obligations, prohibited self-authorization |

## Advisory Template And Fixture Status

Initial advisory coverage now exists:

- `docs/Factory/v3/templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`
- `scripts/factory_v3_mission_control_contract_lint.py`
- `tests/fixtures/factory_v3_mission_control_contract/`

Use the standalone advisory validator:

```bash
python3 scripts/factory_v3_mission_control_contract_lint.py --target tests/fixtures/factory_v3_mission_control_contract --expect tests/fixtures/factory_v3_mission_control_contract/expected/all.json --json
```

The validator emits `blocking_effect: none`. It is not wired into `factoryctl`, CI, merge preflight, `knowledge_lint.sh`, `stage-lint`, `pack-lint`, mission lint, or any required Factory gate.

## Re-entry Decision Cases

The optional `fixture_scenarios.reentry_cases` list makes the re-entry policy falsifiable without creating a runtime state model. `reentry_protocol` remains reusable policy; each re-entry case is an observed or synthetic decision input used only for advisory evaluation.

Controlled case types:

| Scenario type | Required decision |
| --- | --- |
| `clean_fresh_session_reentry` | `continue` only when repository and authority state match, verification is current and passing, and one safe next action has an explicit authority basis |
| `stale_repository_state` | `safe_hold` with terminal state `stale_reentry` |
| `changed_authority_envelope` | `safe_hold` with terminal state `approval_required` |
| `failed_verification_without_recovery_authority` | `safe_hold` or `halt` with terminal state `failed_verification` |
| `failed_verification_with_bounded_recovery` | `verify` for one bounded action with an explicit authority basis; prior verification remains failed until that action actually passes |

Each case records whether it represents a fresh session, but that value is a scenario input, not proof that a live fresh-session or cross-harness handoff occurred. Operational proof still requires the separately governed fresh-worker trial and source artifacts. Session memory is never sufficient authority or evidence.

The case list is optional. Existing mission-control contracts without it remain valid. The advisory validator checks supplied cases for malformed or contradictory decisions and retains `blocking_effect: none`.

## Loop-Library Primitive Absorption

Factory V3 should absorb the shared primitives from high-quality loop patterns, not add a catalog of named loops to the runtime.

| Source pattern | Absorb into Factory V3 | Do not absorb |
| --- | --- | --- |
| Next-Action Confidence Check | `next_action_gate`: continue/ask/safe-hold/verify/close authorization after each meaningful checkpoint | Worker self-authorization to continue outside the mission envelope |
| Loop Harness Verification Loop | Builder/verifier role separation, acceptance criteria, independent verification result, unresolved-gap recording | Scheduled harnesses, unattended execution, or automatic shipping |
| Codex Completion-Contract Loop | Requirement-to-evidence status before closeout: `PROVED`, `WEAK`, `MISSING`, `CONTRADICTED` | Treating completion prose as evidence |
| Restartable Handoff Loop | `restartable_handoff`: last safe checkpoint, stale-state checks, read order, one safe next action | Session memory as sufficient re-entry proof |
| Loop Auditor Loop | Later audit of Factory's own reusable loop-governance primitives for purpose, evidence, budget, kill conditions, and fitness | A loop registry or governance router before primitives have evidence |
| Groundtruth Loop | Direct-source audit and health-inspection pattern for repo claims and context recall repair | Generic repo scoring without source-backed claims |
| Goal Forge Loop | Mission-formation support for converting vague intent into measurable mission specs | Runtime execution authority from a formed goal alone |
| Promise-to-Proof Loop | Passive claim-to-proof audits over roadmap, profile, and closeout claims | Product or governance claims that outrun proof |

## Mission 026 Transfer Lessons

POC Mission 026 contributes design evidence, not profile promotion.

Directly transferable patterns:
- Worker outputs should expose their evidence posture. Mission 026 added recommendation `evidence_review` metadata with status, counts, uncertainty, follow-up state, and review actions.
- Report-like outputs should expose coherence and review state. Mission 026 added `coherence_summary` and `review_queue`.
- Approval rehearsal should be visible and non-mutating before real authority exists. Mission 026 exposed synthetic approval rehearsal state with no live delivery.
- Future-surface rehearsals should list disabled capabilities. Mission 026 exposed fixture-only future surfaces with credentials, scheduler, background sync, webhooks, and live delivery disabled.
- Browser QA can discover governance-surface defects. Mission 026 found mobile overflow in the workbench and fixed it before closeout.
- Repeatable mission QA and closeout verifier scripts make proof cheaper to replay.

Non-transferable or insufficient:
- The POC app's personal-performance domain does not approve real health data use.
- Synthetic Garmin-shaped or manual-import fixtures do not approve live Garmin.
- Approval rehearsal does not approve live Telegram, scheduler, ambient runtime, or delivery.
- Mission 026 does not by itself satisfy `V3-OP-003` duration-ladder promotion, natural negative-case, or FP/FN review requirements.

## Design Backlog

1. Mission-control contract template:
   - Status: initial advisory implementation exists at `templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`.
   - Acceptance: covers mission envelope, authority envelope, loop admission, next-action gate, checkpoints, interrupts, safe-hold, re-entry, evidence, independent verification, and worker interface.

2. Mission-record schema candidate:
   - Status: the first narrow advisory implementation exists in `MISSION_RECORD_DESIGN_V0.md`, `templates/V3_MISSION_RECORD_TEMPLATE.json`, and `scripts/factory_v3_mission_record_lint.py` for verification observations, verifier provenance, per-artifact visual evidence, bounded boundary claims, and completed-record `commit_after` consistency.
   - Acceptance: existing records remain valid; new fields are optional and advisory; visual failure remains valid evidence rather than a malformed-record finding; endurance/exposure fields remain deferred pending natural evidence.

3. Advisory fixtures:
   - Status: initial deterministic fixtures exist under `tests/fixtures/factory_v3_mission_control_contract/`.
   - Add or extend deterministic fixtures for admitted mission, rejected mission, next-action not authorized, safe-hold, stale re-entry, failed verification, weak evidence, contradicted evidence, builder/verifier conflict, and worker self-authorization attempt.
   - Acceptance: fixture expected outputs are stable and non-blocking.

4. Claim-to-proof audit:
   - Run a docs-only audit over Mission 026 claims and map each claim to evidence path, command, screenshot, record, or unresolved gap.
   - Acceptance: no claim relies only on narrative closeout text when artifact proof exists.

5. Worker handoff protocol:
   - Define the minimum handoff from Factory to Codex/Claude/sub-agent worker.
   - Acceptance: handoff states what the worker may decide tactically, what it may not self-authorize, the last safe checkpoint, stale-state checks, and one safe next action.

6. Post-run adjudication pack:
   - Produce a short `NO PROMOTION YET` adjudication over Mission 026 against `V3_OP_003_DECISION_PACK.md`.
   - Acceptance: clearly separates useful design evidence from missing promotion evidence.

7. Loop auditability backlog:
   - Define later, after advisory templates and fixtures exist, how Factory reviews its own reusable loop-governance primitives for purpose, evidence, budget, kill conditions, and retirement criteria.
   - Acceptance: records KEEP/PIVOT/RETIRE/KILL-style audit outcomes without creating routing authority or required gates.

8. Serial mission graph:
   - Status: initial research-only implementation exists in `SERIAL_MISSION_GRAPH_CONTRACT.md`, `templates/V3_SERIAL_MISSION_GRAPH_TEMPLATE.json`, `scripts/factory_v3_serial_mission_graph_lint.py`, and `tests/fixtures/factory_v3_serial_mission_graph/`.
   - Acceptance: a parent authority ceiling bounds every child; dependencies are acyclic; no more than one child is active; completed children have passing verification and proved evidence; parent completion requires all required children plus parent verification.
   - Status: the separately approved deterministic authored-state kernel now exists in `SERIAL_MISSION_STATE_KERNEL.md`, `scripts/factory_v3_serial_mission_state.py`, templates, fixtures, and focused tests.
   - Evidence review: `EVIDENCE_INTEGRITY_THREE_SAMPLE_REVIEW_20260712.md` records `KEEP_OPTIONAL_NO_SCHEMA_CHANGE`.
   - Live observation: `V3-FW-TRIAL-001` matched 19 of 23 fields and failed closed before product work; see `LIVE_FRESH_WORKER_TRIAL_001_REVIEW_20260713.md`.
   - Next gate: a separately approved repaired Trial 002, then an attended serial-epic pilot only on sufficient evidence, without worker dispatch.

## Non-Goals
- No loop runner.
- No scheduler.
- No background worker.
- No runtime authority service.
- No required-gate integration.
- No governance routing.
- No production proof ledger.
- No replacement for Factory V2 build-support until explicitly approved.

## Next Recommended Step
Continue the design backlog in evidence-first advisory order:

1. separately approve and run a repaired Trial 002 using a new mission, explicit ordinary-artifact fields, and one safe next action; Trial 001 is closed at fail-closed safe hold,
2. only after sufficient fresh-worker evidence, run one attended serial-epic pilot with bounded child verification and parent integration verification,
3. collect natural negative-case and upper-envelope continuity evidence only through useful separately approved work,
4. then only later consider read-only Codex SDK/MCP orchestration discovery.

Do not start runtime orchestration or scheduled execution from this document.
