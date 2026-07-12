# Factory V3 Loop Terminal States And Safe-Hold

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Added the advisory re-entry decision matrix and bounded recovery rule used by deterministic mission-control fixtures. Fixture inputs do not prove a live fresh-session handoff.
- v0.1 (2026-06-22): Initial research-only vocabulary for loop terminal states, safe-hold evidence, and loop-contract fixture alignment.

## Status
Research-only advisory canon.

This document does not approve a new V3 profile, make Factory V3 the default, authorize scheduled or unattended execution, create runtime authority, or wire loop-contract checks into required gates.

## Purpose
Define a shared vocabulary for Factory V3 loop governance before runtime orchestration exists.

Factory V3 should govern loops by deciding when they may start, when they must stop, what evidence they must preserve, and how a later worker may safely re-enter. Workers still own tactical implementation, local repo navigation, test/fix cycles, and tool execution inside a mission envelope.

## Source Evidence
This vocabulary is derived from:

- `factory_v3_loop_engineering_recon.md`
- `factory_v3_agent_infrastructure_paper_review.md`
- `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`
- `tests/fixtures/factory_v3_loop_contract/`

Paper and ecosystem sources behind the vocabulary include BLIND-ACT for act-or-ask failure modes, OSWorld-MCP for tool-use evidence, MemoryAgentBench/MemoryArena/MAGE for state and re-entry, FeatureBench for staged feature verification, DeepMind's AI Control Roadmap for detection/prevention/response language, and Loop Library terminal-state discipline.

## Terminal States

| State | Meaning | Factory V3 handling |
| --- | --- | --- |
| `success` | The loop met its objective and required evidence is present. | Close only after verification and claim-to-proof evidence are recorded. |
| `no_op` | The loop found no authorized or necessary action. | Close with evidence explaining why no action was needed. |
| `blocked` | The loop cannot proceed without missing authority, missing input, unavailable tool, or external condition. | Safe-hold unless the block is purely informational and no further worker action is possible. |
| `approval_required` | A human decision is required before the next material action. | Safe-hold and ask for the smallest decision that unblocks the loop. |
| `failed_verification` | A required check failed or evidence contradicted the completion claim. | Halt or safe-hold; do not continue implementation unless a recovery scope is separately authorized. |
| `exhausted` | Retry, budget, time, or attempt limits were reached. | Stop and preserve attempt evidence; do not silently extend the loop. |
| `stagnated` | Repeated iterations are not improving the result or changing the next action. | Stop or escalate; no-loop admission should be reconsidered. |
| `unsafe` | The next action may be unsafe, destructive, externally consequential, privacy-sensitive, or outside approved authority. | Safe-hold before action. |
| `stale_reentry` | Authored state, checkpoint lineage, repo state, or prior evidence is stale. | Safe-hold; direct worker re-entry is not allowed. |
| `ambiguous` | Objective, authority, success criteria, data boundary, or user intent is materially unclear. | Safe-hold before action. |
| `infeasible` | The requested goal cannot be completed under current authority, tools, environment, or constraints. | Safe-hold or close blocked; do not improvise around constraints. |
| `insufficient_context` | The worker lacks enough current evidence to choose a safe next action. | Safe-hold and request the missing context or route to heavier planning. |

## Safe-Hold

Safe-hold is a structured pause before further material action. It is not a failure by itself.

Factory V3 should use safe-hold when a loop reaches a state where continuing would require guessing, expanding authority, acting under stale state, ignoring failed verification, using a broader tool than approved, or taking an external or destructive action without explicit approval.

Safe-hold must preserve:

- `reason`: the terminal or near-terminal condition that triggered the pause.
- `blocked_action`: the action that must not proceed yet.
- `last_safe_checkpoint`: the latest checkpoint or state boundary that remains valid.
- `evidence_summary`: current evidence, failed checks, contradictory state, or missing proof.
- `human_decision_needed`: the smallest concrete decision needed from the sponsor.
- `reentry_instructions`: what a future worker must read before resuming.

## Act-Or-Ask Gate

Before a consequential action, the worker should answer whether it should act at all.

The loop must safe-hold instead of acting when any of these are true:

- the objective is ambiguous,
- the goal appears infeasible,
- the action is unsafe or externally consequential,
- required context is missing,
- approval is required by the authority envelope,
- current state contradicts authored mission state,
- verification failed and recovery was not separately authorized.

This is the BLIND-ACT lesson in V3 terms: prompting the worker to be careful is not enough; the mission-control layer needs explicit halt states and evidence requirements.

## Re-Entry Rules

A worker may re-enter only from authored state and current repository evidence.

Direct re-entry is not allowed when:

- state is stale,
- branches or attempts were invalidated,
- current repo state contradicts prior mission state,
- last safe checkpoint is missing,
- protected-surface status is unknown,
- tool failures are unresolved,
- verification status is failed or missing.

Valid re-entry requires:

- the loop contract,
- mission envelope or equivalent authority,
- latest valid checkpoint,
- mission state,
- verification evidence,
- open human decisions,
- stale-state and protected-surface checks.

### Re-entry Decision Matrix

| Observed condition | Gate result | Terminal state | Material action allowed |
| --- | --- | --- | --- |
| Repository and authority match; verification is current and passing | `continue` | `success` | One action named by the current authority basis |
| Repository state differs from the last safe checkpoint | `safe_hold` | `stale_reentry` | No implementation; preserve evidence and reconcile state |
| Authority envelope differs from the last safe checkpoint | `safe_hold` | `approval_required` | No implementation; obtain explicit authority decision |
| Verification failed and recovery authority is absent | `safe_hold` or `halt` | `failed_verification` | No recovery or implementation action |
| Verification failed and one bounded recovery check is explicitly authorized | `verify` | `failed_verification` until verification passes | Only the named recovery or verification action |

Deterministic fixtures can test this matrix, but they do not establish that a real worker started in a fresh session, lacked prior memory, or reconstructed state correctly. Those claims require live trial evidence.

## Tool-Use Evidence

Tool access is not tool competence. A loop contract should preserve enough evidence to show whether the worker selected and used tools appropriately.

For material tool use, record:

- expected tool class,
- allowed tool name and authority scope,
- actual tool call or command label,
- result or failure output,
- wrong-tool event if applicable,
- omitted-tool rationale when a relevant allowed tool was not used,
- safe-hold or retry decision after failure.

## Feature-Work Evidence

Feature-oriented loops need staged proof. A final "done" claim is too weak.

For feature work, require evidence for:

- design checkpoint,
- implementation diff or artifact summary,
- focused tests,
- regression or no-touch checks,
- claim-to-proof mapping,
- independent review when risk or blast radius warrants it.

This is the FeatureBench lesson in V3 terms: real feature work is harder than narrow bug-fix benchmarks and should not close on self-reported completion.

## Validator Alignment

The advisory loop-contract validator checks the JSON contract and fixture scenarios:

```bash
python3 scripts/factory_v3_loop_contract_lint.py --target tests/fixtures/factory_v3_loop_contract --expect tests/fixtures/factory_v3_loop_contract/expected/all.json --json
```

The validator emits `blocking_effect: none`. It is not wired into `factoryctl`, CI, merge preflight, `knowledge_lint.sh`, `stage-lint`, `pack-lint`, mission lint, or any required Factory gate.

## Next Use

Use this vocabulary when drafting future loop contracts, safe-hold records, mission-state examples, and re-entry fixtures. Do not treat this document as approval for runtime orchestration, scheduled loops, background workers, or reduced governance.
