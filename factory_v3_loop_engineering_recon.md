# Factory V3 Loop Engineering Recon

Date: 2026-06-22

## Executive summary

Loop engineering is not one technique. It is a family of patterns for repeatedly giving workers a bounded task, reading external state, verifying a result, recording evidence, and deciding whether to continue, stop, escalate, or resume.

Factory V3 should learn from this ecosystem, but it should not become a worker loop runner. The strongest design direction is:

- Factory V3 governs loop admission, authority, checkpoints, evidence, termination, interrupts, safe-hold, re-entry, and escalation.
- Workers run implementation loops, repo navigation, tactical fixes, local testing, and local memory updates.
- Factory V3 should express loop contracts as data and validators, not only as prose prompts.
- Loop output should be treated as evidence to adjudicate, not as authority to continue.
- Self-improving or learned loop behavior must be quarantined until reviewed and promoted.

Highest-value next build: a research-only **V3 Loop Contract** and advisory validator that can classify a proposed loop before execution. It should require objective, mutable surfaces, allowed worker, authority envelope, fixed checks, checkpoint cadence, stop states, safe-hold rules, re-entry rules, and evidence artifacts.

## Source inventory

| Source | What was inspected | Implementation depth | Factory V3 score |
| --- | --- | --- | --- |
| SantanderAI org | Profile and governance posture | Active org with multiple AI repos and explicit OSPO governance | 4 |
| SantanderAI/ralph | `ralph-loop.sh`, tests, `skills/ralph`, `skills/juez`, `skills/maestro`, README | Implemented Bash/PowerShell loop plus skills; tests cover only pre-agent validation and stop startup path | 5 |
| SantanderAI/ralph-vault-skill | `scripts/gv.py`, skill references, tests | Implemented stdlib CLI and skill package for progressive-disclosure repo memory | 5 |
| SantanderAI/mech-gov-framework | Governance regimes, hard gates, R2/R3 code, metrics, tests | Implemented Python framework with offline tests; R3 marked exploratory/stub | 5 |
| SantanderAI/autoguardrails | `ResearchLoop`, eval runner, judge, tests, README | Implemented guardrail policy-search harness with fixed evaluator and rollback | 5 |
| SantanderAI/gen-fraud-graph | Generator, typologies, verifier, tests | Implemented synthetic data generator and verifier; not an agent loop | 3 |
| SantanderAI/.github/GOVERNANCE.md | Org publication gates, roles, branch/token policy | Governance document, not code | 4 |
| Forward-Future/loop-library | Skill, operating rules, repo shell | Implemented skill/site shell; repo says production catalog database is source of truth | 4 |
| signals.forwardfuture.ai/loop-library | Homepage, learn page, agents page, `llms.txt`, `catalog.json`, `catalog.txt`, representative loop pages | Public production catalog: schema v2, updated 2026-06-21, 50 loops | 5 |
| GitHub `agent-loop` topic | Recently updated topic page | Noisy ecosystem sample, useful trend signal only | 2 |
| Addy Osmani loop engineering post | Five-piece loop framing | Conceptual but directly relevant to Factory/Codex/Claude split | 4 |
| snarktank/ralph | `ralph.sh`, `prompt.md`, `prd.json.example`, skill | Implemented minimal Ralph loop; much simpler than SantanderAI version | 3 |
| AI Hero Ralph guide | Setup article | Practical usage guide, no source code | 2 |
| Thomas Wiegold Ralph article | Pattern analysis and cautions | Useful synthesis and caveats, no primary implementation | 3 |

## Loop pattern taxonomy

| Pattern | Evidence | Worker-level or Factory-level | Relevance |
| --- | --- | --- | --- |
| Fresh-session loop | Ralph runs a new CLI session per iteration from a prompt file; snarktank does the same with Amp/Claude | Worker-level execution mechanic; Factory governs admission and re-entry | 5 |
| Stop-file / safe-hold loop | SantanderAI Ralph checks `stop.md` in root or `plan/` before each iteration; `juez` emits `stop.md` after hard cases | Factory-level stop semantics should be standardized | 5 |
| Completion-sigil loop | snarktank Ralph and AI Hero use `<promise>COMPLETE</promise>` to stop | Worker-level stop signal; Factory should not trust it alone | 3 |
| Evaluator loop | `juez` validates one block per invocation; autoguardrails freezes evaluator and judge prompt | Factory-level verification policy and evidence gate | 5 |
| Reviewer / maker split | Addy describes maker/checker subagents; Loop Library includes adversarial review and second-agent verification | Worker-level mechanics plus Factory-level verification independence | 5 |
| Worktree isolation loop | Addy and GitHub topic projects emphasize worktrees for parallel agents | Worker execution isolation; Factory should require declared isolation for parallel loops | 4 |
| Scheduled / heartbeat loop | Addy describes automations/heartbeats; topic page includes scheduled and menu-bar loops | Factory-level admission needed before scheduled authority | 4 |
| Sub-agent loop | SantanderAI Ralph `fase0` orchestrates subagents; Addy describes explorer/implementer/verifier | Worker-level orchestration; Factory tracks roles and evidence | 4 |
| Skill-based loop | SantanderAI `maestro` creates local skills; Loop Library itself is a skill | Worker memory and behavior; Factory must track provenance and quarantine learned skills | 5 |
| Repo-vault / memory loop | ralph-vault builds tiered docs, staleness checks, source backlinks | Factory-level re-entry evidence and mission-state loading pattern | 5 |
| Mechanical governance loop | mech-gov R2 hard gates, candidate freezing, ambiguity gate, metrics | Factory-level gate architecture | 5 |
| Guardrail-search loop | autoguardrails mutates only `policy.md` against fixed eval suite | Factory-level mutable-surface and fixed-evaluator contract | 5 |
| Fraud/simulation/evaluation loop | gen-fraud-graph injects known fraud rings and verifies them | Factory eval-fixture generation pattern | 3 |
| Promise-to-proof loop | Loop Library audits public/customer-facing claims against current evidence | Factory-level evidence policy and false-promise detection | 5 |
| Living context loop | Loop Library's Living Story carries open threads forward or marks them stale | Factory-level re-entry and continuity policy | 5 |
| Groundtruth audit loop | Loop Library's Groundtruth loop forces every audit area into proved/no issue/weak/N/A/blocked | Factory-level evidence table and no-silent-gap policy | 5 |
| Workflow-mining loop | Loop Library's Strip Miner mines repeated agent successes but requires contradiction review and fresh replay | Factory-level learned-skill/provenance promotion discipline | 5 |
| Recovery-proof loop | Loop Library validates real restores in isolated clean-room scenarios | Factory-level proof-over-claim pattern for operational readiness | 4 |
| Persistent follow-up loop | Loop Library's refund follow-up loop distinguishes pending progress from success | Factory-level terminal-state discipline for external workflows | 4 |
| Topic/noise loop | GitHub topic includes orchestration kits, second brains, system monitors, stop hooks | Monitor only; too noisy for direct adoption | 2 |

## SantanderAI findings

### SantanderAI organization

What it does: SantanderAI presents a public AI Lab open-source portfolio around small models, harness engineering, evolving agents, responsible AI, MLOps, and graph ML. The org profile lists Ralph, Ralph Vault, autoguardrails, gen-fraud-graph, llm_bridge, and mech-gov-framework as active projects. The org governance file defines roles, SLAs, six publication gates, repository protection, token policy, and amendment process.

Evidence:
- https://github.com/SantanderAI
- https://github.com/SantanderAI/.github/blob/main/profile/README.md
- https://github.com/SantanderAI/.github/blob/main/GOVERNANCE.md

Implementation depth: Governance document plus active repos. Not a runtime system.

Useful for Factory V3:
- Mission/loop admission should mirror publication gates: all required criteria pass before authority is granted.
- Named ownership and review roles map to sponsor, worker, verifier, and escalation owner.
- Token and programmatic-access policy maps to tool/connector authority envelopes.

Keep at worker level:
- None; this is governance posture, not worker mechanics.

Ignore:
- Corporate OSPO overhead that is too heavy for a solo developer.

Score: 4.

### SantanderAI/ralph

What it does: A configurable loop runner that executes a fresh AI CLI session per iteration from a prompt file. It supports Codex, Claude, Gemini, and Devin, reloads `.ralph/.env` before each iteration, checks `stop.md`, rotates logs, optionally enforces Linux systemd memory caps, and can ask the next agent to classify token/quota exhaustion and switch tools.

Evidence:
- https://github.com/SantanderAI/ralph
- `ralph-loop.sh`: `find_stop_file`, `run_tool`, `handle_token_exhaustion`, `resolve_config`, log writing in the iteration loop.
- `tests/ralph-loop.bats`: validates argument errors and startup `stop.md` behavior without launching agents.
- `skills/juez/SKILL.md` and `skills/juez/juzgar.md`: independent checkpoint reviewer, retry escalation, persistent evidence suite, stop-file on unresolved verification.
- `skills/maestro/SKILL.md`: local skill curator for durable repo knowledge.
- `skills/ralph/fase0.md`: decomposes a plan into task files and inserts effort and `juez` checkpoints.

Implementation depth: Implemented. The shell runner is real; the skill system is substantial. Test coverage is narrow for the shell runner and does not exercise actual agent execution.

Loop/governance/evaluation/memory pattern:
- Fresh-session loop.
- File-based stop/safe-hold.
- Per-iteration logs.
- Runtime config reload.
- Token-exhaustion worker rotation.
- Memory cap via systemd.
- Independent `juez` evaluator with retry, escalation, `stop.md`, and one-block-per-invocation rule.
- `maestro` local-skill learning loop.

Useful for Factory V3:
- `stop.md` is a practical safe-hold primitive, but Factory should formalize it as a structured halt/interrupt record.
- Re-reading config before each iteration is a simple runtime-control channel.
- One verifier checkpoint per block is better than broad end-of-mission self-attestation.
- Retry escalation and forced stop after repeated failed verification map well to mission-health and continuation judgment.
- The memory cap is a real runtime guardrail that Factory should record when available.

Should stay at worker level:
- CLI-specific flags, model selection, `codex exec`, Claude/Gemini/Devin invocation details.
- Local plan/task execution.
- Tactical retry/fix cycles.
- Local effort switching.
- Repo-local skill creation by `maestro`, unless promoted as authored knowledge.

Should be ignored or treated as risk:
- Default worker flags are intentionally permissive: Codex bypasses approvals/sandbox, Claude bypasses permissions, Gemini uses YOLO/skip-trust, Devin uses dangerous mode. Factory must not inherit those defaults as acceptable authority.
- Token-exhaustion agent switching is useful operationally but is not governance approval to change worker identity. Factory should record/approve worker switching separately.
- Learned skills can launder authority if used for verification or execution without review.

Score: 5.

### SantanderAI/ralph-vault-skill

What it does: A project-agnostic knowledge-vault skill for documenting one or more repos with tiered, progressive-disclosure docs. The deterministic `scripts/gv.py` CLI initializes vaults, registers repos, checks stale/missing docs, validates frontmatter/wikilinks/token budgets/no-source-code rules, and emits Ralph plan/task files for content generation. The skill explicitly separates deterministic CLI actions from content generation delegated to a Ralph loop.

Evidence:
- https://github.com/SantanderAI/ralph-vault-skill
- `SKILL.md`: hard rules for deterministic CLI vs loop-generated content, progressive disclosure, source backlinks, validation before done, one repo per iteration.
- `scripts/gv.py`: `cmd_validate`, `_affected_docs`, `_uncovered_files`, `_change_drift`, `cmd_plan`, `_write_task`, `cmd_mark_synced`.
- `references/validate.md`: frontmatter, wikilink, token budget, no-source-code, source backlink checks.
- `references/plan.md`: emits `plan/plan.md` and `plan/task/NN.md`, with diff scope and `[juez]` checkpoint.
- `tests/test_gv.py`: unit/integration tests for CLI, git helpers, staleness, config, validation, and planning.

Implementation depth: Implemented stdlib CLI and skill package with tests.

Loop/governance/evaluation/memory pattern:
- Repo-vault memory loop.
- Progressive disclosure.
- Source-backed provenance.
- Staleness and coverage signals.
- Plan generation for fresh-session loops.
- Validation gates around generated memory.

Useful for Factory V3:
- Re-entry should load from a bounded memory/evidence surface, not hidden agent memory.
- Mission state should have source backlinks, token budgets, stale markers, and validation.
- `source_globs`-style mapping is useful for knowing which evidence or docs need refresh after file changes.
- Deterministic CLI for lifecycle operations plus agent loop for content generation is the right separation.

Should stay at worker level:
- Deepwiki generation.
- Repo exploration and documentation writing.
- Stack-specific content prompts.

Should be ignored:
- Building a broad codebase wiki as a required Factory dependency. Factory needs mission evidence, not a universal repo encyclopedia.

Score: 5.

### SantanderAI/mech-gov-framework

What it does: A Python framework for comparing text-only governance (R1), mechanical governance (R2), and exploratory adaptive governance (R3) on synthetic high-stakes banking decisions. R2 applies pre-LLM hard gates, commit/reveal entropy, candidate expansion/freezing, argument-quality checks, ambiguity gates, and metrics. R3 adds bounded self-modification with invariants and drift budget, but the code says it is exploratory/stub and not a development priority.

Evidence:
- https://github.com/SantanderAI/mech-gov-framework
- `src/mech_gov/governance/r1_text_only.py`: text-only policy prompt and LLM parsing.
- `src/mech_gov/governance/r2_mechanical.py`: hard gates -> entropy commit -> CEFL -> I6Q -> ambiguity gate -> reveal.
- `src/mech_gov/governance/primitives/hard_gates.py`: ordered gates with forced decisions.
- `src/mech_gov/governance/primitives/cefl.py`: candidate expansion/freezing and mechanical score selection.
- `src/mech_gov/governance/r3_adaptive.py`: invariants and drift budget for modification proposals.
- `tests/test_hard_gates.py`, `tests/test_regimes_deep.py`: offline tests for gates and regimes.

Implementation depth: Implemented with tests. R3 is explicitly exploratory/stub.

Loop/governance/evaluation/memory pattern:
- Mechanical gates beat text-only policy.
- Candidate freezing prevents the model from moving the target after output.
- Ambiguity gates force defer/escalate when inputs are insufficient.
- Drift budgets and invariants constrain self-modification.
- Governance metrics quantify deferral and framing behavior.

Useful for Factory V3:
- V3 should prefer mechanical mission/loop gates over prompt-only governance.
- Pre-worker hard gates should reject/route loops before a worker starts.
- Post-worker ambiguity and verification gates should override worker "done."
- Self-modifying skills, validators, or mission rules need invariants and drift budget.
- Metrics should track escalation quality, deferral quality, and false completion.

Should stay at worker level:
- Domain-specific banking decision rules.
- LLM candidate generation for business decisions.

Should be ignored:
- Direct adoption of banking metrics as-is. The pattern matters, not the domain.

Score: 5.

### SantanderAI/autoguardrails

What it does: A small autoresearch-style guardrail loop. It searches over one mutable file, `policy.md`, against a fixed `eval_suite.jsonl`, fixed `judge_prompt.md`, fixed harness, acceptance rule, runtime budget, and append-only `results.tsv`. `ResearchLoop` records a baseline, snapshots the protected surface, rejects candidates if fixed files changed, evaluates candidates repeatedly, accepts only ASR improvements with benign-pass floor, and restores the previous accepted policy on rejection.

Evidence:
- https://github.com/SantanderAI/autoguardrails
- `README.md`: mutable surface, fixed suite/judge/harness, ASR metric, benign-pass floor, runtime budget.
- `autoguardrails/loop.py`: `run_baseline`, `run_candidate`, `decide_candidate`, `write_protected_manifest`, `assert_protected_surface_unchanged`.
- `autoguardrails/eval_runner.py`: fixed suite loading, wall-clock budget, repeated stability checks.
- `autoguardrails/judge.py`: frozen heuristic or OpenAI-compatible judge.
- `tests/test_loop.py`: acceptance when policy improves, rejection when protected surface drifts.

Implementation depth: Implemented and tested.

Loop/governance/evaluation/memory pattern:
- Mutable-surface minimization.
- Fixed evaluator and frozen judge.
- Baseline before candidates.
- Stability check via repeated runs.
- Protected-surface manifest.
- Automatic rollback on failed candidate.
- Append-only result log.

Useful for Factory V3:
- A Factory loop contract should name the mutable surface and protected surface.
- Every loop should have a baseline or prior evidence state before it optimizes.
- Changing evaluator/verification mid-loop should either halt or open a new lineage.
- Failed candidate rollback should be explicit in mission authority.
- `blocked`, `discarded`, and `unstable` are terminal states, not success.

Should stay at worker level:
- Searching over policy text.
- Running the target model and judge.

Should be ignored:
- ASR/benign-pass metrics outside safety-policy loops.

Score: 5.

### SantanderAI/gen-fraud-graph

What it does: Generates synthetic financial transaction graphs with accounts, transactions, and injected fraud rings. It has a CLI, multiprocessing generation, CSV/Neptune output, embedding providers, and a verifier that checks fraud-case cycles are backed by real transaction edges.

Evidence:
- https://github.com/SantanderAI/gen-fraud-graph
- `src/gen_fraud_graph/generator.py`: three-phase generation pipeline.
- `src/gen_fraud_graph/typologies.py`: fraud-ring injection.
- `src/gen_fraud_graph/verify.py`: checks injected cycles exist in generated transaction edges.
- `tests/test_generator.py`: full pipeline and verification tests.

Implementation depth: Implemented data generator and verifier. Not an agent-loop system.

Loop/governance/evaluation/memory pattern:
- Synthetic fixture generation with known injected structures.
- Verification against ground-truth patterns.
- Resume/skip support for large generation.

Useful for Factory V3:
- Build synthetic mission-history fixtures with known injected defects: missing authority, stale re-entry, false completion, unsafe tool use, bad safe-hold, verifier drift.
- Use verifiers to test whether V3 advisory validators detect known injected failures.

Should stay at worker level:
- Fraud graph generation and ML/data tasks.

Should be ignored:
- Financial-graph domain specifics.

Score: 3.

### SantanderAI/.github/GOVERNANCE.md

What it does: Defines open-source governance roles, SLAs, six publication gates, repository protection baseline, programmatic access policy, and amendment process.

Evidence:
- https://github.com/SantanderAI/.github/blob/main/GOVERNANCE.md

Implementation depth: Governance document, not executable.

Loop/governance/evaluation/memory pattern:
- Gate-based admission.
- Named owners and escalation roles.
- Required checks before release.
- Programmatic access minimization.
- Audit cadence.

Useful for Factory V3:
- Mission and loop admission should be gate-based.
- Programmatic tool/connector access should be explicit, minimal, and time-bounded.
- Escalation owner and review owner should be named in nontrivial loop contracts.

Should stay at worker level:
- None.

Should be ignored:
- Corporate publication SLAs and process overhead.

Score: 4.

## Broader loop ecosystem findings

### Scheduled research addendum: measurable agent infrastructure

The attached scheduled research report is not another loop catalog. Its main claim is that the current frontier is measurable agent infrastructure: memory benchmarks, long-horizon simulations, MCP/tool-use evaluation, computer-use safety, and formal control-plane research. That reinforces Factory V3's direction: govern loops through state, authority, evidence, monitoring, and escalation, not through better worker prompts alone.

Follow-up review: I reviewed the primary papers and major-lab artifacts in `factory_v3_agent_infrastructure_paper_review.md`. The practical change is that the next V3 loop contract should be a state/tool/control contract, not merely a prompt/loop template.

High-signal sources from the report:

| Source | Factory V3 relevance | Design implication |
| --- | --- | --- |
| MARS | Cost-aware reflective search and cross-branch learning for long-horizon research agents | Future long-running V3 profiles need budget-aware branch/attempt governance, not only linear checkpoints |
| MemoryAgentBench | Tests retrieval, test-time learning, long-range understanding, and selective forgetting | V3 memory/re-entry must define write, update, deletion, contradiction, and provenance rules |
| MemoryArena | Evaluates memory coupled to future action across sessions | V3 should test whether mission state improves later execution, not only whether it is recalled |
| MAGE | Treats memory as hierarchical execution state instead of semantic RAG | V3 mission state should be a structured state tree or checkpoint path, not a bag of retrieved notes |
| OSWorld-MCP | Measures MCP tool invocation quality; tool availability does not imply tool competence | V3 should record allowed tools, actual tool-selection evidence, failures, and tool-use competence |
| SCUBA | Enterprise SaaS tasks remain hard even for strong agents | V3 must gate enterprise/customer workflows and prefer milestone evidence over final claims |
| Programming with Pixels | GUI-only software work is weak; structured file/shell APIs help | V3 should prefer typed/shell/file tools with scoped authority; GUI is fallback/proof surface |
| FeatureBench | Complex feature development is much harder than bug-fix benchmarks | V3 should require staged feature evidence, not treat coding benchmark strength as mission readiness |
| BLIND-ACT | Computer-use agents keep acting under ambiguity, infeasibility, or risk | V3 needs explicit "should act?" checks and safe-hold before ambiguous/consequential actions |
| CEO-Bench | Long-horizon business control remains unreliable | V3 should keep financial/resource decisions behind hard limits and human review |
| DeepMind AI Control Roadmap | Runtime monitoring, prevention, response, and escalation for advanced agents | V3 should frame itself as a control plane: detection, prevention, response, audit, and escalation |
| Anthropic Trustworthy Agents | Trust depends on model, harness, tools, environment, transparency, privacy, and human control | V3's authority envelope must include tool/environment boundaries and human override |

Factory-specific interpretation:

- Memory is execution state, not generic retrieval. Factory should own mission-state schemas, checkpoint lineage, stale-state detection, contradiction handling, and deletion/forgetting policy.
- Tool use must be evaluated. A future loop contract should not only list tools; it should record expected tool use, actual tool calls, failures, and whether the worker chose appropriate tools.
- "Act or ask?" is a first-class gate. BLIND-ACT aligns directly with V3 safe-hold and human decision interrupt semantics.
- Control-plane vocabulary should be explicit: prevention gates before execution, detection during execution, response after anomalies, and replayable audit evidence.
- Long-horizon missions need branch/attempt accounting and budget-aware continuation, not only chronological logs.

Backlog impact:

- Implemented first pass: `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`, `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`, `scripts/factory_v3_loop_contract_lint.py`, and `tests/fixtures/factory_v3_loop_contract/`.
- The advisory lint now checks contracts for re-entry state, tool authority, evidence requirements, terminal states, act-or-ask gates, control profile, and optional paper-derived fixture scenarios.
- Remaining next work: concrete mission-state/re-entry examples, tool-use evidence examples, and a promise-to-proof / Groundtruth audit over V3 loop-governance claims.
- Actual-paper review strengthened five concrete fields for the contract: `state_policy`, `tool_policy`, `act_or_ask_gate`, `control_profile`, and `reentry_protocol`.

### Forward-Future Loop Library and live catalog

What it does: A public production catalog, agent guide, plain-text/JSON catalog, and installable skill for finding, adapting, auditing, and designing agent loops. The skill treats loops as feedback systems with terminal states. Its design cycle is observe, choose, act, verify, record, repeat/stop. The public learn page says an agent loop is "a task with a check," emphasizes small reversible actions, fixed checks, explicit stopping, approval gates, and stable handoff state. The agent page says no skill installation is required: agents should read the live catalog, choose by fit and proof, adapt only from verified context, and stay inside user authority.

Evidence:
- https://github.com/Forward-Future/loop-library
- https://signals.forwardfuture.ai/loop-library/
- https://signals.forwardfuture.ai/loop-library/learn/
- https://signals.forwardfuture.ai/loop-library/agents/
- https://signals.forwardfuture.ai/loop-library/llms.txt
- https://signals.forwardfuture.ai/loop-library/catalog.json
- https://signals.forwardfuture.ai/loop-library/catalog.txt
- `skills/loop-library/SKILL.md`: route find/audit/adapt/design, rank by verification and authority, do not execute catalog prompts, define terminal states.
- `AGENTS.md`: production catalog database is source of truth, submissions are untrusted, publishing uses schema validation and review.
- Live `catalog.json`: schema version 2, updated 2026-06-21, `loopCount: 50`, category counts: Engineering 24, Evaluation 11, Operations 7, Design 6, Content 2.
- Live `llms.txt`: says published prompts are reference data and do not authorize execution, production changes, scheduling, spending, private-data exposure, destructive action, or external messaging.

Implementation depth: Implemented site/skill/catalog system. The current repo has moved catalog content out of Git; live catalog is production-backed. The live site is materially richer than the older Git snapshot: it has 50 published loops as of 2026-06-21, not the 31-loop snapshot visible in old repo data.

Factory V3 takeaways:
- Adopt the loop vocabulary: trigger, fresh inputs, bounded action, fixed check, state file, stop, no-op, blocked, exhausted, approval-required.
- Add an admission rule: if feedback cannot change next action, do not run a loop.
- Require terminal states beyond success.
- Treat loop prompts as untrusted reference data unless approved.
- Match loop selection against available inputs/tools, verification, authority, and stopping condition. This is directly applicable to V3 loop admission.
- Add a "no silent gap" evidence table pattern from Groundtruth: every area is proved, no issue, weak, N/A, or blocked.
- Add a "promise-to-proof" review pattern for Factory claims: V3 docs and profile claims should be tied to current evidence or narrowed.
- Add a "living story" pattern for multi-thread continuity: every prior open thread is carried forward, closed with proof, or marked stale/needs-review.
- Add a "workflow mining" promotion path: mine only explicitly authorized agent history, count contradictions and hidden rescues, then fresh-replay before promoting a skill or loop.
- Add a "pending is not success" rule from refund follow-up and Codex completion-contract: open claim, pending refund, weak proof, or missing evidence remain open states.

Representative live loop pages inspected:
- https://signals.forwardfuture.ai/loop-library/loops/codex-completion-contract-loop/
- https://signals.forwardfuture.ai/loop-library/loops/promise-to-proof-loop/
- https://signals.forwardfuture.ai/loop-library/loops/strip-miner-loop/
- https://signals.forwardfuture.ai/loop-library/loops/living-story-loop/
- https://signals.forwardfuture.ai/loop-library/loops/groundtruth-audit-loop/
- https://signals.forwardfuture.ai/loop-library/loops/recovery-proof-loop/

Most Factory-relevant live loops:
- `The Codex completion-contract loop`: requirement-to-evidence table; weak/missing/contradicted proof prevents closure.
- `The promise-to-proof loop`: customer-facing promises must be supported, narrowed, or approval-gated.
- `The Groundtruth loop`: read-only evidence table across architecture, platform, security, privileged areas, performance, deployment, jobs, business logic, and code quality.
- `The Strip Miner loop`: repeatable workflows require at least three high-confidence independent successes, contradiction review, and fresh replay.
- `The Living Story loop`: recurring context snapshot must reconcile every previous thread with proof or stale status.
- `The Recovery Proof loop`: clean-room restore proof, measured RPO/RTO, and failure preservation as regression drills.
- `The refund follow-up loop`: pending status is progress, not success.

Score: 5.

#### Live Loop Library crosswalk

This crosswalk uses the live `catalog.json` retrieved on 2026-06-22. The score is Factory V3 relevance, not loop quality. "Gate" means the loop contains production, external, scheduled, destructive, privacy, or runtime implications that Factory should explicitly bound before any worker executes it.

| # | Loop | Factory interpretation | Score |
| --- | --- | --- | --- |
| 001 | The docs sweep | Adapt as bounded worker verification loop for documentation drift. | 4 |
| 002 | The architecture satisfaction loop | Adapt; requires objective architecture target and no-progress stop to avoid subjective churn. | 4 |
| 003 | The sub-50 ms page-load loop | Adapt; strong fixed-benchmark and environment-recording pattern. | 4 |
| 004 | The production error sweep | Gate; production telemetry and fixes require explicit authority and data handling. | 3 |
| 005 | The 100% test coverage loop | Adapt; useful only when coverage command and exclusions are trusted. | 4 |
| 006 | The SEO/GEO visibility loop | Adapt; good repeatable benchmark pattern, but external search evidence is variable. | 4 |
| 007 | The logging coverage loop | Adapt; useful evidence policy for observability without sensitive data leakage. | 4 |
| 008 | The nightly changelog loop | Gate; scheduled cadence and release claims need authority, but terminal no-change state is useful. | 3 |
| 009 | The quality streak loop | Adopt as verification pattern: consecutive successes plus regression capture. | 4 |
| 010 | The full product evaluation loop | Adapt for POC evals; gate any production-like data or destructive action. | 4 |
| 011 | The test-suite speed loop | Adapt as worker-level optimization with fixed timing/coverage baseline. | 4 |
| 012 | The repository cleanup loop | Gate destructive git cleanup; adapt inventory/recovery evidence pattern. | 3 |
| 013 | The stale-safe batch release loop | Gate; release authority remains outside current V3 approval. | 3 |
| 014 | The production data cleanup loop | Gate; production data and classifier changes are out of scope without separate authority. | 2 |
| 015 | The post-release baseline loop | Gate release context; adapt baseline-recording pattern. | 3 |
| 016 | The ticket-to-PR-ready loop | Adopt for `V3-OP-001`-style bounded code changes. | 5 |
| 017 | The customer AI deployment loop | Gate; customer process, rollout, monitoring, and ROI claims exceed current V3 scope. | 2 |
| 018 | The product update podcast loop | Gate; external publication and Jellypod/MCP use require explicit approval. | 2 |
| 019 | The Clodex adversarial-review loop | Adapt maker/checker and iteration-cap pattern; do not inherit tool-specific workflow. | 4 |
| 020 | The Loop Harness verification loop | Adapt second-agent verification and isolated worktree pattern; unattended scheduling remains gated. | 4 |
| 021 | The Boeing 747 benchmark | Conceptually useful fixed-view visual eval pattern; not central to Factory governance. | 3 |
| 022 | War Loops: frontend reconstruction | Worker/design pattern; Factory relevance is authorization and capture/proof boundaries. | 3 |
| 023 | The self-improving champion loop | Adopt as eval-lineage pattern: holdouts, must-pass checks, budget, no overfitting. | 5 |
| 024 | The devil's-advocate loop | Adopt for challenge missions and design objection logs. | 5 |
| 025 | The fresh-clone loop | Adopt for bootstrap/onboarding proof and disposable-environment evidence. | 5 |
| 026 | The Infinite Clickbait thumbnail loop | Monitor/tactical; useful rubric/accuracy discipline but not core Factory governance. | 2 |
| 027 | The autonomy-loop builder-reviewer loop | Adapt builder/reviewer, red-before/green-after proof, and protected-path parking. | 4 |
| 028 | The Codex completion-contract loop | Adopt directly as Factory completion-evidence model. | 5 |
| 029 | The Revolve versioned-experiment loop | Adapt for versioned experiment lineage and rollback. | 4 |
| 030 | The five-minute repository maintainer loop | Gate; heartbeat orchestration and multi-repo delegation need runtime authority. | 3 |
| 031 | The recent-feedback sweep | Adapt for failure-pattern audits from user corrections. | 4 |
| 032 | The promise-to-proof loop | Adopt for Factory's own claims and profile-readiness evidence reviews. | 5 |
| 033 | The propagation compliance loop | Adapt where code changes must propagate across docs/examples/tests; gate external compliance claims. | 4 |
| 034 | The multi-LLM convergence loop | Adapt cautiously for independent review; avoid consensus-as-proof fallacy. | 4 |
| 035 | The Goal Forge loop | Adapt for turning vague goals into bounded contracts, if it preserves Factory authority. | 4 |
| 036 | The UI/UX Score Loop | Worker/design eval pattern; Factory relevance is fixed rubric and evidence capture. | 3 |
| 037 | The cold-load trimmer loop | Worker optimization loop; adapt only with stable benchmark and rollback. | 3 |
| 038 | The pixel-safe CSS trim loop | Worker/design loop; useful fixed visual-regression proof pattern. | 3 |
| 039 | The easy onboarding loop | Adopt for onboarding/friction evals and solo-developer operator-friction measurement. | 4 |
| 040 | The accessibility repair loop | Adapt as bounded remediation loop with objective accessibility checks. | 4 |
| 041 | The housekeeper loop | Gate destructive cleanup; adapt stale/no-op/owner evidence pattern. | 3 |
| 042 | The Axelrod subagent arena loop | Conceptually useful for subagent evals; monitor before adopting. | 3 |
| 043 | The prepare-a-new-project loop | Adapt for V3 standalone bootstrap readiness. | 4 |
| 044 | The test stabilizer loop | Adapt for flaky-test evidence and retry discipline. | 4 |
| 045 | The artifact-to-skill loop | Adopt with skill provenance quarantine and fresh second-case validation. | 5 |
| 046 | The Strip Miner loop | Adopt as learned-loop promotion policy: repeated proof, contradiction review, fresh replay. | 5 |
| 047 | The Living Story loop | Adopt/adapt for mission re-entry and cross-thread continuity, with privacy boundaries. | 5 |
| 048 | The Groundtruth loop | Adopt as no-silent-gap, evidence-table audit pattern for V3 readiness. | 5 |
| 049 | The Recovery Proof loop | Adapt as operational-readiness proof-over-claim pattern; actual restores are gated. | 4 |
| 050 | The refund follow-up loop | Conceptually useful: pending progress is not success; external messaging/claims are gated. | 3 |

Factory should not import this catalog as a dependency. It should maintain a small watchlist/crosswalk, then promote only specific patterns into repo-authored V3 guidance after review.

### Addy Osmani: Loop Engineering

What it does: Conceptual article framing loop engineering as designing the system that prompts agents. It identifies automations, worktrees, skills, plugins/connectors, sub-agents, and state as the core pieces. It emphasizes maker/checker separation, state outside the conversation, verification responsibility, and the risk of cognitive surrender.

Evidence:
- https://addyosmani.com/blog/loop-engineering/

Implementation depth: Conceptual.

Factory V3 takeaways:
- Factory V3 is the "floor above harness engineering": governance and mission control above worker/harness mechanics.
- Human review bandwidth remains the bottleneck; Factory should manage review queue and escalation, not pretend review disappears.
- State file is the spine of the loop; Factory should own durable mission state and evidence.
- Subagent verification should be explicit and cost-aware.

Score: 4.

### GitHub `agent-loop` topic

What it shows: A noisy but useful snapshot of emerging repos. The topic page listed 76 public repos matching `agent-loop` on 2026-06-22, spanning TypeScript, Python, Shell, and other languages. Recent entries include human-on-loop Codex control planes, orchestrator-worker-reviewer harnesses, gated delivery pipelines, worktree loop kits, menu-bar system loops, stop-hook engines, and evidence-anchored audit loops.

Evidence:
- https://github.com/topics/agent-loop?o=desc&s=updated

Implementation depth: Mixed and unverified from the topic page alone.

Factory V3 takeaways:
- Monitor the category, but do not import patterns without code review.
- The market vocabulary is drifting toward human-on-loop, recoverable workflow loops, worktree isolation, reviewer separation, and stop hooks.

Score: 2.

### snarktank/ralph

What it does: Minimal Ralph implementation with `ralph.sh`, PRD JSON, progress file, branch archival, one user story per iteration, completion sigil, and Amp/Claude execution. The prompt instructs the agent to read `prd.json` and `progress.txt`, select the highest-priority failing story, implement one story, run checks, commit, update PRD/progress, update AGENTS.md with reusable learnings, and emit `<promise>COMPLETE</promise>` when all stories pass.

Evidence:
- https://github.com/snarktank/ralph
- `ralph.sh`: loops Amp or Claude, checks completion sigil, archives prior runs.
- `prompt.md`: one-story iteration rules, progress report, AGENTS.md update, quality checks, browser verification for frontend.
- `prd.json.example`: structured stories with acceptance criteria and `passes`.
- `skills/ralph/SKILL.md`: PRD-to-Ralph JSON conversion and story sizing.

Implementation depth: Implemented but simple.

Factory V3 takeaways:
- One item per iteration is a strong worker-level reliability pattern.
- PRD entries with verifiable acceptance criteria map to mission-contract task blocks.
- Completion sigils are convenient but must be verified independently.

Score: 3.

### Optional Ralph guides

AI Hero's Ralph guide emphasizes first running a human-in-the-loop loop, using a PRD/progress file, one task per run, iteration caps, completion sigil, and sandboxing through Docker. Thomas Wiegold's article emphasizes fresh context, one task per iteration, file-system memory, structured commits/logs, when Ralph is appropriate, sandboxing, circuit breakers, and not using resume/continue when fresh context is the point.

Evidence:
- https://www.aihero.dev/getting-started-with-ralph
- https://thomas-wiegold.com/blog/ralph-loop-how-recursive-ai-agents-work/

Factory V3 takeaways:
- Start with attended/manual loop trials before scheduled loops.
- Require explicit circuit breakers: iteration, time, token/cost, repeated-failure, and stuck thresholds.
- If output is not machine-verifiable, wire a judge or keep human approval.

Scores: AI Hero 2, Thomas Wiegold 3.

## Worker-level vs Factory V3-level split

### Worker-level patterns

Factory should allow workers to own these, subject to authority:

- Running Codex, Claude Code, Gemini, Devin, Amp, or other local CLIs.
- Local repo navigation and search.
- Implementation and tactical reasoning.
- Test/fix loops inside an approved scope.
- Worktree setup and local branch mechanics, when authorized.
- Updating local progress files and task checkboxes.
- Local learned memory proposals.
- Creating local evidence artifacts requested by the mission.
- Running evaluator subagents, when the mission contract permits them.
- Tool/model switching for quota or capability, only when pre-authorized or escalated.

### Factory V3-level patterns

Factory should own these:

- Mission contract and objective.
- Authority envelope: files, commands, tools, network, git, external systems, credentials, deployment.
- Loop admission: whether a proposed loop is suitable at all.
- Mutable/protected surface declaration.
- Worker identity and permitted worker switching.
- Checkpoint policy and cadence.
- Verification policy and independent reviewer requirements.
- Evidence policy: required logs, command output, diffs, tests, screenshots, artifacts, commit IDs.
- Safe-hold/interrupt semantics.
- Stop states: success, no-op, blocked, approval-required, failed-verification, exhausted, stagnated, unsafe, stale-reentry.
- Re-entry protocol: what state must be read, what stale checks must pass, and what prior evidence is binding.
- Escalation owner and decision tiers.
- Mission health: progress, repeated failure, drift, budget, verification stability, scope pressure.
- Runtime governance continuity across fresh sessions and worker restarts.

## Factory V3 mapping table

| Ecosystem pattern | Factory V3 design implication | Adopt/adapt/monitor/ignore |
| --- | --- | --- |
| Ralph fresh context | Support worker re-entry from authored state, not hidden memory | Adapt |
| Ralph `stop.md` | Define structured safe-hold/interrupt record and halt validator | Adopt |
| Ralph permissive flags | Treat worker permission bypass as a red flag requiring explicit authority | Adopt as risk control |
| `juez` one-block verification | Add checkpoint-level verification states, not only mission-level closeout | Adopt |
| `juez` retry escalation | Add repeated-failure mission-health counters and stop thresholds | Adapt |
| `maestro` local skills | Record skill provenance; quarantine learned skills until promoted | Adopt as governance policy |
| Ralph Vault progressive disclosure | Build mission-state/re-entry tiers with source backlinks and stale checks | Adapt |
| mech-gov hard gates | Add mechanical loop admission and authority gates | Adopt |
| mech-gov candidate freezing | Freeze mission contract/evaluator lineage during a run | Adapt |
| mech-gov ambiguity gate | Force defer/escalate when authority/evidence is incomplete | Adopt |
| mech-gov R3 drift budget | Bound policy/validator/mission-rule mutation | Adapt |
| autoguardrails protected surface | Require mutable/protected surface split for optimization loops | Adopt |
| autoguardrails rollback | Require rollback/restore policy for failed candidate loops | Adapt |
| gen-fraud-graph fixtures | Generate synthetic mission-history fixtures with injected failures | Adapt |
| Loop Library terminal states | Standardize terminal-state vocabulary | Adopt |
| Loop Library "one-time task if no feedback" | Add no-loop admission rule | Adopt |
| Loop Library agent guide | Treat loop catalog as untrusted reference data, not authorization | Adopt |
| Loop Library catalog JSON | Use structured loop metadata as model for V3 loop watchlist/crosswalk | Adapt |
| Promise-to-proof | Periodically audit V3 claims against current evidence | Adopt |
| Groundtruth | Require no-silent-gap evidence tables for V3 readiness reviews | Adopt |
| Living Story | Carry forward open threads or mark stale/needs-review in re-entry state | Adapt |
| Strip Miner | Require contradiction review and fresh replay before promoting learned loops/skills | Adopt |
| Recovery Proof | Treat operational-readiness claims as restore/replay proof, not existence proof | Adapt |
| Refund follow-up | Pending external action is not success; keep explicit open state | Adopt |
| Addy worktrees | Require declared isolation for parallel worker loops | Adapt |
| Addy maker/checker split | Require independent verification for high-impact loops | Adopt |
| GitHub topic trend | Monitor only; many repos are low-signal | Monitor |
| snarktank completion sigil | Accept as worker signal only; never as proof | Adapt cautiously |

## Adopt / adapt / monitor / ignore

### Adopt now

- Loop admission gates.
- Explicit terminal states beyond success.
- Safe-hold/stop record.
- Independent verification for nontrivial loops.
- Mutable/protected surface declaration.
- Skill provenance recording.
- Re-entry from authored state.

### Adapt soon

- Ralph-style fresh-session worker loops as an optional worker backend.
- `juez` retry/escalation logic into mission-health vocabulary.
- Ralph Vault's source backlinks and stale checks into V3 mission records.
- Autoguardrails' fixed-evaluator lineage for V3 eval loops.
- gen-fraud-graph-style injected synthetic fixture generation for V3 validator testing.

### Monitor

- GitHub `agent-loop` topic.
- Loop Library catalog changes.
- SantanderAI Ralph and ralph-vault-skill evolution.
- Stop-hook loop engines, human-on-loop Codex control planes, and orchestrator-worker-reviewer harnesses.

### Ignore for now

- Worker-specific permissive flags as defaults.
- Corporate OSPO process overhead.
- Banking/fraud domain rules.
- Broad deepwiki generation as required Factory infrastructure.
- Self-modifying governance without explicit human approval and drift/invariant controls.

## Pattern scores

| Pattern | Score | Reason |
| --- | --- | --- |
| Loop admission contract | 5 | Directly fills Factory's authority boundary before execution |
| Safe-hold / interrupt record | 5 | Core to long-running mission control |
| Checkpoint-level verification | 5 | Prevents false mission completion |
| Re-entry state and stale checks | 5 | Fresh-session loops require durable continuity |
| Mutable/protected surface split | 5 | Prevents evaluator or scope drift during optimization loops |
| Mechanical hard gates | 5 | Converts governance from prompt-only to enforceable data |
| Independent reviewer split | 5 | Necessary when worker output should not self-certify |
| Skill provenance quarantine | 5 | Prevents learned skills from laundering authority |
| Worktree isolation | 4 | Important for parallel execution; lower-level than Factory |
| Scheduled heartbeat | 4 | Important but unapproved until runtime authority matures |
| Token-exhaustion worker rotation | 3 | Operationally useful; dangerous if it changes worker identity silently |
| Completion sigil | 3 | Useful as a worker hint, insufficient as proof |
| Synthetic fraud graph pattern | 3 | Useful as fixture-generation analogy, not directly loop governance |
| Topic trend watching | 2 | Monitor only |

## Backlog tickets

### Ticket 1: Add V3 Loop Contract template

Problem: Factory V3 currently has mission envelopes and mission records, but no explicit shape for admitting or governing a loop as a first-class execution pattern. The scheduled research adds that this contract must cover memory/state and tool/control-plane behavior, not just loop prompts.

Status: First advisory pass implemented on 2026-06-22. Remaining work is concrete mission-state/re-entry examples and audits, not runtime orchestration.

Proposed implementation:
- Add a research-only `V3_LOOP_CONTRACT_TEMPLATE.json` with objective, trigger, worker, mutable surface, protected surface, allowed actions, forbidden actions, checks, checkpoint cadence, terminal states, safe-hold rules, re-entry rules, evidence artifacts, escalation owner, and approval requirements.
- Include memory/state fields: state source, write policy, stale-state check, contradiction handling, deletion/forgetting policy, and re-entry read order.
- Include tool/control fields: allowed tools, expected tool classes, tool-call evidence, tool failure behavior, and "act or ask" ambiguity gate.
- Add a companion Markdown explanation under V3 docs.

Acceptance criteria:
- Template includes all Factory-owned loop governance fields.
- Template explicitly separates worker mechanics from Factory authority.
- Template marks scheduled/unattended execution as unapproved unless separately authorized.
- Docs cite Ralph, ralph-vault, mech-gov, autoguardrails, Loop Library, and the scheduled-research memory/tool/control sources as research inputs.

Likely files/modules:
- `docs/Factory/v3/templates/V3_LOOP_CONTRACT_TEMPLATE.json`
- `docs/Factory/v3/LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md`
- `scripts/factory_v3_loop_contract_lint.py`
- `tests/fixtures/factory_v3_loop_contract/`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`

Suggested agent/sub-agent:
- Main Codex for docs/template.
- Challenge subagent to check authority leakage.

Evidence/source:
- SantanderAI Ralph `stop.md` and `.ralph/.env` reload.
- autoguardrails mutable/protected surface.
- Loop Library terminal states.

Score: 5.

### Ticket 2: Build advisory loop-contract lint

Problem: A loop contract without validation becomes another prose artifact.

Proposed implementation:
- Add `scripts/factory_v3_loop_contract_lint.py`.
- Validate required fields, terminal-state coverage, no unbounded loop, explicit mutable/protected surface, verification command/evidence presence, approval boundary, and no scheduled/runtime authority unless marked research-only/no-execution.
- Emit `blocking_effect: none`.

Acceptance criteria:
- Valid, invalid, and edge-case fixtures exist.
- Lint rejects missing stop states, missing verification, missing authority, and contradictory approval fields.
- Output is deterministic JSON.
- Not wired into required gates.

Likely files/modules:
- `scripts/factory_v3_loop_contract_lint.py`
- `tests/fixtures/factory_v3_loop_contract/`
- `docs/Factory/v3/LOOP_GOVERNANCE_CONTRACT.md`

Suggested agent/sub-agent:
- Main Codex implementation.
- Verification subagent for fixture review.

Evidence/source:
- mech-gov hard gates.
- autoguardrails protected manifest.
- ralph-vault `gv.py validate`.

Score: 5.

### Ticket 3: Add safe-hold and terminal-state vocabulary for loops

Problem: V3 has halt/fallback/interrupt language, but loop ecosystems use many stop states: success, no-op, blocked, approval-required, exhausted, stagnated, unsafe, repeated-failure, stale-reentry.

Proposed implementation:
- Add a research-only loop terminal-state section to mission-health or a new loop governance note.
- Define required fields for safe-hold records: reason, current worker, last evidence, pending decision, timeout behavior, re-entry instruction, allowed next action.
- Map Ralph `stop.md` to a structured V3 safe-hold record.

Acceptance criteria:
- States are mutually distinct.
- Completion sigils are classified as worker-reported signals, not proof.
- Repeated-failure and no-response safe-hold behavior are explicitly covered.

Likely files/modules:
- `docs/Factory/v3/MISSION_HEALTH_VOCABULARY.md`
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md`
- `docs/Factory/v3/templates/`

Suggested agent/sub-agent:
- Main Codex docs.
- Challenge subagent for ambiguity and false-success cases.

Evidence/source:
- SantanderAI `juez` retry/stop semantics.
- Loop Library terminal-state guidance.
- Thomas Wiegold circuit-breaker guidance.

Score: 5.

### Ticket 4: Add mission re-entry evidence tiers

Problem: Fresh-session loops rely on external state. Factory V3 needs a disciplined, bounded re-entry surface that avoids both hidden memory and broad context dumps.

Proposed implementation:
- Define a V3 mission-state tier model: mission envelope, latest checkpoint, open interrupts, touched files, command evidence, verification status, stale checks, and optional repo-memory references.
- Add stale-reentry checks analogous to ralph-vault source backlinks/source_globs.

Acceptance criteria:
- Re-entry instructions identify exactly what must be read.
- Stale commit or changed protected surface forces safe-hold or new plan delta.
- No hidden worker memory is trusted.

Likely files/modules:
- `docs/Factory/v3/ADAPTIVE_MISSION_CONTROL.md`
- `docs/Factory/v3/MISSION_RECORD_DESIGN_V0.md`
- `docs/Factory/v3/templates/V3_MISSION_STATE_TEMPLATE.md`

Suggested agent/sub-agent:
- Main Codex docs/template.
- Verifier subagent to test against existing stale-reentry evidence.

Evidence/source:
- Ralph fresh sessions.
- ralph-vault progressive disclosure and staleness.
- Factory POC stale-reentry evidence already in project state.

Score: 5.

### Ticket 5: Add loop-health advisory metrics

Problem: Long-running loops need continuation judgment beyond pass/fail.

Proposed implementation:
- Add advisory metrics: repeated rejection count, no-progress iterations, verification instability, evaluator drift, protected-surface drift, budget burn, authority pressure, worker-switch count, human-interrupt count, and stale-reentry risk.
- Start as vocabulary and fixture fields, not gates.

Acceptance criteria:
- Metrics are observable from mission records/checkpoints.
- Metrics do not authorize default routing or runtime control.
- At least three synthetic examples show healthy, degraded, and halt-required loop states.

Likely files/modules:
- `docs/Factory/v3/MISSION_HEALTH_VOCABULARY.md`
- `docs/Factory/v3/PHASE4_EVAL_EXPANSION_PLAN.md`
- `tests/fixtures/factory_v3_loop_contract/`

Suggested agent/sub-agent:
- Main Codex docs.
- Data/eval subagent for fixture design.

Evidence/source:
- mech-gov governance metrics.
- autoguardrails stability and acceptance logs.
- SantanderAI `juez` retry counters.

Score: 5.

### Ticket 6: Add loop-source watchlist and quarterly recon cadence

Problem: Loop-engineering primitives are changing quickly, but importing every repo creates churn and authority confusion.

Proposed implementation:
- Add a small watchlist file listing SantanderAI Ralph/Ralph Vault/mech-gov/autoguardrails, Forward-Future Loop Library, and selected `agent-loop` topic categories.
- Review manually on a fixed cadence or before a V3 profile promotion decision.

Acceptance criteria:
- Watchlist records source, why watched, last reviewed date, and what would trigger Factory action.
- Watchlist is explicitly non-authoritative and non-enforcing.

Likely files/modules:
- `docs/Factory/v3/LOOP_ENGINEERING_WATCHLIST.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`

Suggested agent/sub-agent:
- Research subagent for future read-only scans.

Evidence/source:
- SantanderAI org activity.
- Loop Library production catalog updates.
- GitHub `agent-loop` topic velocity.

Score: 4.

### Ticket 7: Generate synthetic loop failure fixtures

Problem: V3 validators need known-answer loop histories to test false negatives and false positives.

Proposed implementation:
- Create fixture records that inject known defects: missing safe-hold, worker switch without authority, verifier changed mid-run, completion sigil without verification, stale re-entry, protected-surface drift, repeated failed verification without escalation.

Acceptance criteria:
- Each fixture has expected advisory findings.
- Fixtures are deterministic and do not rely on live tools.
- At least one fixture is a clean negative/control.

Likely files/modules:
- `tests/fixtures/factory_v3_loop_contract/`
- `tests/fixtures/factory_v3_mission_record/`
- `scripts/factory_v3_loop_contract_lint.py`

Suggested agent/sub-agent:
- Main Codex for fixtures.
- Verification subagent for expected output review.

Evidence/source:
- gen-fraud-graph's inject-and-verify pattern.
- Current Factory V3 mission-record fixture strategy.

Score: 4.

## Practical recommendation

Factory V3 should monitor SantanderAI and Loop Library continuously, but with a narrow intake rule:

- Monitor SantanderAI Ralph/Ralph Vault/mech-gov/autoguardrails as high-signal sources for loop execution, memory, governance, and evaluation.
- Monitor Loop Library as a public vocabulary/catalog source.
- Monitor GitHub `agent-loop` topic only as a trend sensor.
- Do not install or depend on external loop tooling directly in Factory V3 until a specific pattern passes Factory-style mission formation, challenge, advisory lint, and human approval.

The next Factory V3 build should be a research-only loop contract plus advisory lint and fixtures. That gives Factory a way to govern loops before it tries to run or orchestrate them.
