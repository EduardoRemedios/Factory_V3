# Factory V3 Mission-Control Contract

## Version
v0.1

## Change Log
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

## Ownership Split

| Concern | Factory V3 mission-control owns | Worker owns |
| --- | --- | --- |
| Mission intent | Objective, success criteria, non-goals, sponsor approval source | Tactical interpretation inside the envelope |
| Authority | Authorized files, commands, tools, dependency policy, external-effect limits | Staying inside the granted authority while executing |
| Loop admission | Whether a loop is allowed, should route to V2, should safe-hold, or should be rejected | No self-admission outside the envelope |
| Checkpoints | Required cadence, required fields, mission-health signals, state persistence | Emitting accurate checkpoint evidence |
| Verification | Verification policy, required tiers, no-touch checks, evidence freshness expectations | Running checks and preserving outputs |
| Interrupts | Decision tiers, approval gates, timeout behavior, safe-hold semantics | Asking only when Tier 1 or Tier 2 cannot resolve safely |
| Re-entry | Read order, stale-state checks, last-safe-checkpoint rule | Resuming only from authored state and current repo evidence |
| Evidence | Claim-to-proof requirements, audit summary, closeout record, proof gaps | Producing command, diff, screenshot, test, and artifact evidence |
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
| `verification_policy` | required commands, verification tiers, no-touch checks, browser/external proof if needed, failure handling |
| `evidence_policy` | required artifacts, claim-to-proof mapping, screenshots or logs where relevant, JSON parse rules for records |
| `interrupt_policy` | decision tiers, approval gates, timeout behavior, answer interpretation, plan-delta rule |
| `safe_hold_policy` | safe-hold reasons, blocked action, last safe checkpoint, human decision needed, re-entry instructions |
| `reentry_protocol` | read order, stale-state checks, protected-surface checks, current repo-state verification |
| `terminal_states` | success, no-op, blocked, approval-required, failed-verification, exhausted, stagnated, unsafe, stale-reentry, ambiguous, infeasible, insufficient-context |
| `worker_interface` | worker role, allowed tactical autonomy, evidence emission obligations, prohibited self-authorization |

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
   - Create `templates/V3_MISSION_CONTROL_CONTRACT_TEMPLATE.json`.
   - Acceptance: covers mission envelope, authority envelope, loop admission, checkpoints, interrupts, safe-hold, re-entry, evidence, verification, and worker interface.

2. Mission-record schema candidate:
   - Add advisory fields for `mission_control`, `loop_admission`, `safe_hold_events`, `worker_reentry`, and `claim_to_proof`.
   - Acceptance: existing records remain valid; new fields are optional and advisory.

3. Advisory fixtures:
   - Add deterministic fixtures for admitted mission, rejected mission, safe-hold, stale re-entry, failed verification, and worker self-authorization attempt.
   - Acceptance: fixture expected outputs are stable and non-blocking.

4. Claim-to-proof audit:
   - Run a docs-only audit over Mission 026 claims and map each claim to evidence path, command, screenshot, record, or unresolved gap.
   - Acceptance: no claim relies only on narrative closeout text when artifact proof exists.

5. Worker handoff protocol:
   - Define the minimum handoff from Factory to Codex/Claude/sub-agent worker.
   - Acceptance: handoff states what the worker may decide tactically and what it may not self-authorize.

6. Post-run adjudication pack:
   - Produce a short `NO PROMOTION YET` adjudication over Mission 026 against `V3_OP_003_DECISION_PACK.md`.
   - Acceptance: clearly separates useful design evidence from missing promotion evidence.

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
Implement the design backlog in advisory order:

1. template,
2. fixtures,
3. passive claim-to-proof audit,
4. optional validator support,
5. then only later consider read-only Codex SDK/MCP orchestration discovery.

Do not start runtime orchestration or scheduled execution from this document.
