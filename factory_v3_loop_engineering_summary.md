# Factory V3 Loop Engineering Summary

Date: 2026-06-22

## Top 5 findings

1. Loop engineering is moving from "prompt the agent" to "design a feedback system that prompts workers." Factory V3 should own the governance layer above that system, not the worker loop itself.
2. The strongest reusable pattern is a loop contract: bounded objective, one mutable surface, protected surfaces, fixed checks, explicit terminal states, evidence, safe-hold, and re-entry.
3. SantanderAI Ralph is a real implementation, but its default worker execution is deliberately permissive. Factory should learn from its stop/config/log/checkpoint mechanics while rejecting permissive flags as default authority.
4. SantanderAI mech-gov and autoguardrails show the most important governance lesson: prompts are not enough. Use mechanical gates, frozen evaluators, protected-surface manifests, rollback, and explicit metrics.
5. The live Loop Library is now a serious source, not just a prompt list: schema v2, 50 loops as of 2026-06-21, agent-facing instructions, and newer loops for promise-to-proof, Groundtruth audits, Living Story continuity, Strip Miner workflow mining, Recovery Proof, and Codex completion contracts.

The full recon includes a 50-loop live-catalog crosswalk with Factory interpretation and relevance score for each Loop Library entry.

I also reviewed the primary papers/artifacts surfaced by the scheduled research output in `factory_v3_agent_infrastructure_paper_review.md`. That review made the next step sharper: V3's first loop artifact should govern state, tools, act/ask decisions, and control-plane response, not just loop prompts.

Implementation note: the initial advisory loop contract template, terminal-state/safe-hold vocabulary, and lint fixture corpus now exist at `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`, `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`, `scripts/factory_v3_loop_contract_lint.py`, and `tests/fixtures/factory_v3_loop_contract/`. The fixture corpus includes richer paper-derived scenarios for memory/re-entry, tool use, blind-action safe-hold, and feature-work verification gaps.

## Top 3 SantanderAI takeaways

1. `ralph` proves fresh-session loops need external continuity: plan files, task files, logs, stop files, config reload, and reviewer checkpoints. Factory should govern that continuity as mission state and safe-hold evidence.
2. `ralph-vault-skill` shows how to keep long-running agents from loading the world: progressive disclosure, source backlinks, token budgets, staleness checks, and deterministic validation.
3. `mech-gov-framework` plus `autoguardrails` show the Factory-grade pattern: hard gates before model work, fixed evaluators, protected surfaces, candidate rollback, and drift/invariant controls for anything self-modifying.

## Top 3 loop-engineering takeaways

1. Use a loop only when feedback changes the next action. Otherwise use a one-shot task.
2. Split maker and checker for any nontrivial or unattended work. Worker self-reported completion is a signal, not proof.
3. Treat loop catalogs and prompts as untrusted reference data. Selection must match outcome, inputs/tools, verification, authority, and stopping condition; execution still requires Factory/user authority.

## Top 5 backlog items

1. Add mission re-entry evidence tiers with stale/protected-surface checks.
2. Add concrete mission-state examples that show active state, archived branch, invalidated branch, and promoted lesson.
3. Add a tool-use evidence example that shows expected tool classes, actual tool calls, omitted-tool rationale, and tool failure behavior.
4. Add a small promise-to-proof / Groundtruth audit pass over V3's own loop-governance claims.
5. Monitor SantanderAI and Loop Library-style sources for changes to loop governance, memory, tool-use, and evaluation patterns.

## Recommendation

Yes: Factory V3 should continuously monitor SantanderAI and Loop Library-style projects.

But the monitoring rule should be strict: extract patterns, not dependencies. SantanderAI is currently high-signal for implemented loop mechanics, memory, governance gates, and eval harnesses. Loop Library is high-signal for public loop vocabulary, terminal-state discipline, evidence tables, workflow-mining criteria, and agent-facing authority boundaries. GitHub `agent-loop` topics are useful only as trend radar.

What Factory V3 should build next: add concrete mission-state/re-entry examples and evidence tiers, then run a small promise-to-proof / Groundtruth audit over V3's own loop-governance claims. Runtime orchestration and scheduled loop execution should still wait.
