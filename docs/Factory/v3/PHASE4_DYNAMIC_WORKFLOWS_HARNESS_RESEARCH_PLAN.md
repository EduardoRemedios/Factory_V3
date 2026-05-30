# Factory V3 Phase 4 Dynamic Workflows Harness Research Plan

## Version
v0.3

## Change Log
- v0.3 (2026-05-30): Reclassified Codex from anticipation-only to official-docs source signal for subagent workflows and experimental CSV fanout, while still marking local Factory evidence as absent.
- v0.2 (2026-05-30): Generalized from Claude-only research to the dynamic/parallel workflow harness class, with Codex tracked as an anticipated sibling profile without shipped-capability claims.
- v0.1 (2026-05-30): Initial research-only plan for evaluating Claude Code dynamic workflows as a future Factory V3 harness capability profile.

## Status
Research-only and non-enforcing.

This document does not authorize live mission execution, governance routing, reduced governance, required gates, CI wiring, telemetry completeness checks, runtime authority, proof, lease enforcement, default-mode behavior, V3 profile promotion, Factory V2 build-support removal, or routine use of dynamic workflows.

Factory V3 is not promoted by this document. V3 remains optional/advisory except for the already approved optional profile `V3-OP-001 Bounded Code Change`, and Factory V2 remains supported and available as fallback.

## Source Signals
This plan tracks dynamic/parallel workflow harnesses as a capability class, not as a Claude-specific branch.

Anthropic announced Claude Code dynamic workflows on 2026-05-28:

```text
https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
```

The announcement describes a Claude Code capability that can dynamically plan work, fan subtasks out across parallel subagents, check or refute results, coordinate a single answer, persist progress, and resume long-running jobs.

OpenAI Codex docs also describe source signals in this class:

```text
https://developers.openai.com/codex/learn/best-practices#organize-long-running-work-with-session-controls
https://developers.openai.com/codex/subagents#process-csv-batches-with-subagents-experimental
```

Those docs describe Codex subagent workflows for bounded offload from a main thread and an experimental CSV-batch fanout pattern that spawns worker subagents, waits for the batch, and exports combined results.

Factory has not locally observed or validated any dynamic/parallel workflow harness capability in this repository. Treat Claude and Codex as external source signals only until local Factory V3 evidence exists.

## Factory Interpretation
Dynamic/parallel workflows are a potential executor capability under Factory governance.

They do not replace:
- mission envelopes,
- authority leases,
- token or cost budgets,
- allowed command and file boundaries,
- verification requirements,
- halt and fallback rules,
- evidence and closeout records,
- Factory V2 fallback.

The expected Factory value is harness capability evidence: whether a parallel, long-running coding harness can preserve scope discipline, verification quality, interruption recovery, and replayable evidence for selected bounded work.

## Research Objective
Prepare a conservative Phase 4 evaluation path for dynamic/parallel workflow harnesses without changing Factory operating authority.

The first useful question is not whether dynamic workflows can do large work. The first useful question is whether Factory can inspect and replay enough evidence from a dynamic workflow to trust it for a narrow, separately approved `V3-OP-001` evidence mission.

## Candidate Harness Profiles
Initial Claude profile:

```text
docs/Factory/v3/harness_profiles/HP_20260530_001_claude_code_dynamic_workflows_research.md
```

Initial Codex profile:

```text
docs/Factory/v3/harness_profiles/HP_20260530_002_codex_subagent_workflows_research.md
```

Evidence band:

```text
insufficient_evidence
```

Reason:
- Claude dynamic workflows are externally announced and Codex subagent workflows are described in official OpenAI docs,
- no local Factory V3 mission has used either capability class,
- no local dynamic-workflow command, diff, verification, interruption, or closeout evidence exists,
- vendor-internal planner or subagent cognition state must not be treated as Factory evidence.

## Minimum Evidence Before Any Local Candidate
A future dynamic-workflow candidate must be separately planned and approved before execution.

Required before starting:
- a named mission profile, normally `V3-OP-001` only if the task is still bounded,
- explicit authorized files or directories,
- explicit forbidden files or directories,
- allowed command families,
- dependency policy,
- human approval points,
- token or cost budget if exposed by the harness,
- stop conditions for scope expansion, verification failure, missing evidence, or unclear subagent output,
- V2 fallback triggers.

Dynamic/parallel workflows must not be used as a shortcut around Factory V2 for broad migrations, repo-wide audits, security reviews, infrastructure work, deployment, authentication, payment, compliance, runtime-kernel, proof, or lease-enforcement work.

## Evidence Capture Requirements
If a future candidate is approved, preserve only reviewable execution evidence:
- prompt and mission envelope summary,
- generated orchestration script names or summaries if exposed and safe to record,
- subtask list or work partition summary if exposed and safe to record,
- files touched,
- commands attempted,
- verification results,
- failed-check handling,
- human decisions,
- interruption or resume behavior,
- final closeout and residual risks.

Do not capture:
- chain-of-thought,
- vendor-private cognition state,
- raw full transcripts,
- raw command-output dumps,
- secrets,
- source file contents outside normal diffs,
- external proof artifacts outside the repository boundary.

## Evaluation Questions
Use the Phase 4 dimensions from `PHASE4_EVAL_EXPANSION_PLAN.md`.

| Dimension | Dynamic-workflow Question |
| --- | --- |
| Harness capability | Can Factory see enough of the workflow plan, subtask boundaries, and verification results to review the mission? |
| Execution reliability | Does the workflow finish the bounded objective without losing planned checks or closeout discipline? |
| Scope discipline | Do parallel subagents stay inside authorized files, commands, dependencies, and forbidden scope? |
| Verification quality | Are findings and implementation results independently checked before closeout? |
| Interruption recovery | If the run pauses or resumes, does it continue from source artifacts and recorded state rather than stale derived context? |
| Evidence quality | Can a later reviewer reconstruct objective, authority, file touches, commands, verification, decisions, and gaps? |
| False-positive behavior | Do refutation or review agents over-report issues that human review rejects? |
| False-negative behavior | Do parallel agents miss scope or verification defects that Factory checks later catch? |

## Candidate Shapes
Prefer low-risk candidates that naturally test evidence quality before implementation ambition:
- docs-only clarification-heavy candidate where canonical source selection is ambiguous,
- bounded fixture-maintenance candidate with deterministic expected-output checks,
- review-only dead-code or cleanup opportunity scan that produces findings but no edits,
- small bounded code change with named files and existing tests.

Do not use dynamic/parallel workflows for the first local candidate if the request is broad, security-critical, migration-sized, or requires new authority semantics.

## Relationship To Existing Phase 4 Gap
The Phase 3 natural halted/fallback/clarification-heavy evidence gap remains open.

Dynamic/parallel workflows may become a useful way to observe clarification, failed verification, interruption, or evidence-quality behavior, but only if a future separately approved candidate naturally produces that signal. Do not manufacture ambiguity, failure, or fallback to close the gap.

## Verification For This Planning Artifact
Run:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json
python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json
git diff --check
```

Manual review:
- confirm this plan remains research-only,
- confirm the dynamic-workflow harness profiles are marked `insufficient_evidence`,
- confirm no router, enforcement, required gate, telemetry completeness, runtime authority, proof, lease, default-mode, or V2-removal language was introduced,
- confirm Factory V2 fallback remains explicit.

## Next Step
Do not execute a dynamic/parallel workflow from this plan alone.

The next eligible step is a separate Factory V2-governed candidate-selection run or a narrowly authorized `V3-OP-001` intake that decides whether a specific dynamic-workflow trial is bounded enough to proceed.
