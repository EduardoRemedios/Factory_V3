# Factory V3 Agent Infrastructure Paper Review

Date: 2026-06-22

## Executive Summary

I reviewed the primary papers and major-lab artifacts surfaced by the scheduled research output. The strongest conclusion is narrow and practical: Factory V3 should not build a smarter worker loop next. It should build a loop admission and control contract that treats state, tool authority, evidence, monitoring, and safe-hold as first-class governed surfaces.

The highest-signal sources are:

1. Google DeepMind's AI Control Roadmap.
2. BLIND-ACT.
3. OSWorld-MCP.
4. MemoryAgentBench plus MemoryArena.
5. MAGE, as a design sketch for execution-state memory.
6. FeatureBench.
7. MARS.

Programming with Pixels and SCUBA are supporting evidence: they reinforce that structured APIs, shell/file tools, milestone evidence, demonstrations, and domain knowledge beat GUI-only autonomy for serious work.

## Source Triage

| Source | Reviewed artifact | Relevance | Factory V3 decision |
| --- | --- | ---: | --- |
| Google DeepMind AI Control Roadmap | [DeepMind blog](https://deepmind.google/blog/securing-the-future-of-ai-agents/) and [PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf) | 5 | Adopt control-plane vocabulary: detection, prevention, response, coverage, recall, time-to-response, async/sync intervention. |
| BLIND-ACT | [OpenReview](https://openreview.net/forum?id=9W4bPRsEIT) | 5 | Add explicit "act or ask?" gate and safe-hold terminal states for ambiguity, infeasibility, unsafe action, and missing context. |
| OSWorld-MCP | [OpenReview](https://openreview.net/forum?id=rceD6wwt4B) and [project](https://osworld-mcp.github.io) | 5 | Add tool-use evidence and tool-competence checks; listing a tool is not proof the worker can use it. |
| MemoryAgentBench | [OpenReview](https://openreview.net/forum?id=DT7JyQC3MR) | 5 | Define V3 memory competencies: retrieval, update/learning, long-range understanding, and forgetting/conflict handling. |
| MemoryArena | [arXiv](https://arxiv.org/abs/2602.16313) | 4 | Evaluate whether persisted mission state improves future execution, not just whether a fact can be recalled. |
| MAGE: Memory as Execution State Management | [arXiv](https://arxiv.org/abs/2606.06090) | 4 | Adapt the state-tree idea into V3 checkpoint/re-entry lineage; do not adopt the full architecture yet. |
| FeatureBench | [OpenReview](https://openreview.net/forum?id=41xrZ3uGuI) and [arXiv](https://arxiv.org/abs/2602.10975) | 4 | Feature work needs staged milestone proof and regression checks; benchmark strength on bug-fix tasks is not enough. |
| MARS | [arXiv](https://arxiv.org/abs/2602.02660) | 4 | Adapt budget-aware branch/attempt governance and cross-branch lesson handling; avoid implementing MCTS in V3 now. |
| Programming with Pixels | [OpenReview](https://openreview.net/forum?id=9N4Ps9Psfr) | 3 | Prefer typed file/shell/API tools for coding missions; GUI is a fallback or proof surface. |
| SCUBA | [OpenReview](https://openreview.net/forum?id=bkjKnO9s7T) | 3 | Enterprise workflows need milestone evaluators, sandboxing, and demonstrations; monitor for later external-tool missions. |
| Anthropic Trustworthy Agents in Practice | [Anthropic](https://www.anthropic.com/research/trustworthy-agents) | 4 | Use its model/harness/tools/environment trust boundary to shape V3 authority envelopes. |
| CEO-Bench | [arXiv](https://arxiv.org/abs/2606.18543) | 3 | Monitor for long-horizon mission-health evaluation; do not design around business-autonomy simulation yet. |

## Deep Reviews

### 1. Google DeepMind AI Control Roadmap

What it says: DeepMind frames agent safety as system-level control, not only model alignment. The roadmap treats some deployed agents as untrusted, borrows from cybersecurity, and centers automated monitoring, response, access control, least privilege, zero trust, behavior monitoring, and defense in depth. The blog version names three operational metrics: monitoring coverage, detection recall, and time-to-response.

Evidence:
- The roadmap defines AI control as system-level mitigation for large internal agent deployments, including automated monitoring/response, access controls, and environment hardening.
- It proposes four detection tiers and response tiers, plus a portfolio of 15 mitigations.
- It distinguishes asynchronous monitoring/response from synchronous monitoring/response. The latter matters for high-risk actions that must be blocked before execution.
- It explicitly discusses agent identities, separate permissions, human approval for sensitive permissions, and infrastructure to pause, terminate, or seal off agents and subagents.

Factory V3 implication:
- V3 should use a control-plane contract, not a generic loop-runner contract.
- Every governed loop should declare detection mode, prevention gates, response path, evidence coverage, reviewer/escalation owner, and time-to-response expectations.
- Safe-hold must be operational, not prose. V3 needs a machine-checkable halt/hold state that can stop execution, preserve evidence, and support re-entry.

Do not copy:
- Do not build DeepMind-scale threat modeling now.
- Do not assume V3 needs adversarial-agent controls before it has basic mission evidence controls.

### 2. BLIND-ACT

What it says: Computer-use agents often pursue a user goal when they should stop, clarify, refuse, or escalate. BLIND-ACT calls this blind goal-directedness. The benchmark has 90 tasks covering lack of contextual reasoning, assumptions under ambiguity, and contradictory or infeasible goals. The paper reports high blind-goal-directedness rates across frontier models and says prompting reduces but does not solve the problem.

Evidence:
- The OpenReview abstract reports 90 tasks, 93.75% judge-human agreement, and an 80.8% average BGD rate across nine frontier models.
- The paper identifies failure modes that map cleanly to V3: execution-first bias, thought-action disconnect, and request-primacy.
- It notes that BGD often appears early in a trajectory, typically within the first few steps.

Factory V3 implication:
- Add an explicit `act_or_ask_gate` to the loop contract before the worker acts.
- Add terminal states for `ambiguous`, `infeasible`, `unsafe`, `insufficient_context`, and `approval_required`.
- Require evidence that the worker checked whether it should act, not only how it acted.

Do not copy:
- Do not rely on LLM judges alone for safety-critical decisions.
- Do not treat a reflective prompt as sufficient mitigation.

### 3. OSWorld-MCP

What it says: MCP and tool access improve agent performance, but tool availability is not tool competence. OSWorld-MCP evaluates GUI operation, MCP tool invocation, and decision-making together. The benchmark includes 158 manually validated tools across seven common applications and reports that even strong models underuse tools.

Evidence:
- The OpenReview abstract reports that MCP tools improved OpenAI o3 from 8.3% to 17.6% at 15 steps and Claude 4 Sonnet from 38.9% to 45.0% at 50 steps.
- It reports that even the strongest model had only a 33.3% tool invocation rate.
- The paper defines metrics that are useful for V3: task accuracy, tool invocation rate, and average completion steps.
- It shows that making all 158 tools available can hurt performance due to oversized tool context.

Factory V3 implication:
- V3 loop admission should require `allowed_tools`, `expected_tool_classes`, and `tool_evidence`.
- Re-entry records should preserve actual tool calls, failures, wrong-tool events, and why tools were not used.
- V3 should prefer small, scoped tool sets over giant menus.

Do not copy:
- Do not make V3 a tool-selection optimizer.
- Do not count "tool connected" as evidence of execution capability.

### 4. MemoryAgentBench

What it says: Memory should be evaluated across multiple competencies, not reduced to retrieval. The paper defines accurate retrieval, test-time learning, long-range understanding, and selective forgetting as core competencies for memory agents. It finds that current memory agents, including RAG-style systems, fall short across the full set.

Evidence:
- The OpenReview abstract names the four competencies and says existing benchmarks do not cover all of them.
- The paper compares long-context agents, RAG agents, and agentic memory systems.
- It finds that RAG can help narrow retrieval but struggles with holistic understanding and continual update/forgetting.

Factory V3 implication:
- V3 memory should be mission state, not a vector store bolted onto chat history.
- The loop contract should specify memory write policy, update policy, contradiction handling, stale-state checks, deletion/forgetting policy, and provenance.
- V3 advisory lint should reject a re-entry plan that has no state source, no stale check, or no conflict handling.

Do not copy:
- Do not implement a general memory benchmark suite now.
- Do not make generic semantic retrieval the default mission memory primitive.

### 5. MemoryArena

What it says: Memory matters when it changes future action. MemoryArena evaluates multi-session Memory-Agent-Environment loops where later subtasks depend on earlier interactions. It covers web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning.

Evidence:
- The arXiv abstract says the benchmark uses explicitly interdependent subtasks where agents must distill earlier actions and feedback into memory for later tasks.
- It reports that agents with near-saturated long-context benchmark performance can perform poorly in this agentic setting.

Factory V3 implication:
- V3 should evaluate mission state by downstream usefulness: did the next worker re-enter correctly, avoid repeated mistakes, and preserve prior constraints?
- Add re-entry fixtures where a worker must use previous mission state to act correctly.

Do not copy:
- Do not build a MemoryArena-style gym yet.

### 6. MAGE: Memory as Execution State Management

What it says: MAGE argues that long-horizon memory should preserve execution-state integrity rather than retrieve semantically similar fragments. It uses a two-layer hierarchical state tree and four operations: Grow, Compress, Maintain, and Revise. Revise restores a target boundary and resumes on a new branch.

Evidence:
- The arXiv abstract reports a hierarchical state tree, active root-to-current path, sibling-branch hints, and Grow/Compress/Maintain/Revise operations.
- It reports task success improvements of 7.8 to 20.4 percentage points over baselines on MemoryArena, with 55.1% lower token consumption.

Factory V3 implication:
- Adapt the state-tree concept as V3 `checkpoint_lineage`, not as a full agent-memory engine.
- A mission record should distinguish active state, archived branches, invalidated branches, and re-entry boundary.
- Failed attempts should not disappear; they should be isolated as evidence and used carefully.

Do not copy:
- Do not put MAGE inside the worker loop now.
- Do not let workers freely revise protected mission state without Factory approval.

### 7. FeatureBench

What it says: Existing coding-agent benchmarks overstate real feature-development readiness. FeatureBench builds feature-level tasks using tests and dependency graphs, yielding 200 tasks and 3,825 executable environments from 24 repositories. It reports that a strong SWE-bench model succeeds on only 11.0% of FeatureBench tasks.

Evidence:
- The arXiv abstract and OpenReview page describe execution-based evaluation and task derivation from unit tests along dependency graphs.
- The paper emphasizes feature-level work spanning multiple commits and PRs, not narrow bug fixing.

Factory V3 implication:
- V3 should require staged evidence for feature missions: design checkpoint, implementation diff, tests, regression surface, and independent review.
- The mission record should distinguish "tests passed for touched path" from "feature verified end to end."
- V3 should not infer worker reliability from SWE-bench-style claims.

Do not copy:
- Do not build FeatureBench inside this repo now.

### 8. MARS

What it says: MARS treats automated AI research as cost-constrained search, not linear execution. It combines budget-aware MCTS, modular construction, and comparative reflective memory. The paper reports that 63% of utilized lessons came from cross-branch transfer.

Evidence:
- The arXiv abstract names budget-aware MCTS, modular construction, and comparative reflective memory as pillars.
- It frames MLE work as expensive and opaque, requiring cost-aware planning.
- It includes cost discussion and early-stopping/cost-control concerns.

Factory V3 implication:
- Add branch/attempt accounting to long-running missions: attempt id, cost/time budget, stop threshold, plateau rule, and promoted lessons.
- Cross-branch lessons should be quarantined until verified; a failed attempt can contain useful evidence but should not silently mutate the mission contract.

Do not copy:
- Do not implement MCTS for Factory V3.
- Do not turn V3 into a research-agent search engine.

### 9. Programming with Pixels

What it says: GUI-only coding agents are weak. The paper introduces an IDE-based benchmark and reports that pure visual interaction performs far worse than specialized coding agents. Adding two APIs, file editing and bash, raises performance substantially.

Evidence:
- The OpenReview abstract says pure visual agents underperform and file-editing plus bash APIs often bring them near specialized coding agents.
- The paper reports average accuracy of 22.9% for visual-only agents and 50.7% with file/bash APIs.

Factory V3 implication:
- For coding missions, Factory should prefer scoped shell/file APIs and repo-native verification over GUI-only interaction.
- GUI/browser evidence is useful for inspection and screenshots, not as the default execution substrate.

### 10. SCUBA

What it says: Enterprise SaaS computer-use remains hard. SCUBA evaluates Salesforce CRM workflows in sandbox environments with milestone metrics. It reports poor zero-shot results, improved but still imperfect demonstration-augmented performance, and the value of fine-grained milestone scoring.

Evidence:
- The OpenReview abstract reports 300 task instances from real user interviews, Salesforce sandboxes, milestone metrics, open-source agents below 5% zero-shot success, closed-source methods up to 39%, and demonstrations improving success to 50%.
- The paper emphasizes enterprise UI navigation, data manipulation, workflow automation, information retrieval, and troubleshooting.

Factory V3 implication:
- For future external-system missions, require sandbox, milestone evaluator, rollback/restore plan, and approval gates.
- Demonstrations can be treated as worker hints, not as authority.

## Cross-Paper Design Rules for Factory V3

1. V3 should govern whether a loop is allowed before it governs how the loop runs.
2. Memory is execution state, not generic recall.
3. Tool access requires competence evidence.
4. "Should act?" must be checked before "how to act?"
5. High-risk actions need synchronous prevention; low-risk reversible actions can use asynchronous review.
6. Feature delivery requires milestone proof, not final claims.
7. Branches, retries, and failed attempts are evidence objects.
8. GUI automation should be a fallback for coding and enterprise work unless the task is inherently visual.

## Recommended V3 Backlog Changes

### Ticket A: V3 Loop Contract With Control Profile

Problem: Current V3 research points to loop contracts, but the paper review shows the contract must also capture state, tool competence, and runtime control.

Proposed implementation:
- Add `V3_LOOP_CONTRACT_TEMPLATE.json` as advisory research artifact.
- Include sections for `mission`, `authority_envelope`, `state_policy`, `tool_policy`, `act_or_ask_gate`, `checkpoint_policy`, `verification_policy`, `control_profile`, `terminal_states`, and `reentry_protocol`.
- `control_profile` should include detection mode, prevention gates, response owner, escalation path, coverage expectation, recall/eval method, and time-to-response expectation.

Acceptance criteria:
- Template can represent a coding loop, review loop, scheduled loop, and memory/re-entry loop.
- Template has explicit terminal states for ambiguity, infeasibility, unsafe action, insufficient context, approval required, stale re-entry, and failed verification.
- Template references this paper review as evidence.

### Ticket B: Advisory Loop Contract Lint

Problem: A contract template without validation will become ceremonial.

Proposed implementation:
- Add `scripts/factory_v3_loop_contract_lint.py`.
- Reject missing authority envelope, missing state policy, missing tool policy, missing evidence policy, missing terminal states, or missing safe-hold behavior.
- Add deterministic fixtures for valid, missing-memory, missing-tool-authority, ambiguous-no-safe-hold, unsafe-no-approval, and stale-reentry cases.

Acceptance criteria:
- JSON output is stable.
- Invalid fixtures fail with specific reasons.
- No required gate wiring; advisory-only semantics are preserved.

### Ticket C: Memory/Re-entry State Fixtures

Problem: MemoryAgentBench, MemoryArena, and MAGE show that re-entry state must be tested through future action, not merely loaded.

Proposed implementation:
- Add fixtures for stale state, contradictory prior state, invalidated branch, missing source backlink, and re-entry from a safe checkpoint.
- Add docs explaining active state, archived branch, invalidated branch, and promoted lesson.

Acceptance criteria:
- Fixtures can be linted without runtime orchestration.
- Each fixture has expected pass/fail reasons.

### Ticket D: Tool-Use Evidence Schema

Problem: OSWorld-MCP shows that tool availability does not imply correct tool invocation.

Proposed implementation:
- Add advisory schema fields for allowed tools, expected tool classes, actual tool calls, tool failures, wrong-tool events, omitted-tool rationale, and tool-result evidence.
- Include a small example mission where shell/file tools are expected and GUI is explicitly fallback.

Acceptance criteria:
- Contract lint catches "tools allowed but no evidence policy."
- Contract lint catches oversized/unscoped tool authority.

### Ticket E: Blind-Action Safe-Hold Gate

Problem: BLIND-ACT shows agents often proceed under ambiguity, infeasibility, or safety risk.

Proposed implementation:
- Add a safe-hold checklist to the loop contract.
- Require workers to stop when objective, authority, data safety, external effect, or success criteria are materially ambiguous.
- Define safe-hold evidence: reason, last safe checkpoint, blocked action, human decision needed, and re-entry instructions.

Acceptance criteria:
- Ambiguous fixture fails if it proceeds without safe-hold.
- Safe-hold fixture passes when it preserves evidence and requests the right decision.

## What Factory V3 Should Build Next

Ticket A and Ticket B now have an initial advisory implementation:

- `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`
- `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`
- `scripts/factory_v3_loop_contract_lint.py`
- `tests/fixtures/factory_v3_loop_contract/`

Follow-up implementation: the fixture corpus now includes optional scenario checks for stale state, contradictory state, invalidated branch, safe checkpoint resume, wrong-tool selection, omitted-tool rationale, tool failure, blind-action safe-hold, and feature-work staged verification gaps. The terminal-state and safe-hold vocabulary is also documented outside JSON for human/worker use.

The next step is concrete mission-state and re-entry examples, plus a small promise-to-proof audit over V3's own loop-governance claims.

Do not build runtime orchestration yet. The paper review strengthens the case that V3 should first define the governance envelope workers must operate inside.
