# Codex SDK And MCP Orchestration Direction

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial strategic note on using Codex SDK, Codex MCP, and Agents SDK as possible orchestration surfaces for Factory V3 and Harmony.

## Status
Strategic direction and research roadmap context only. This document does not make Factory V3 the default mode, approve a new operational profile, approve unattended execution, approve production actions, wire V3 into required gates, or grant runtime authority.

## Purpose
Record a second important V3 product direction:

```text
Codex should be treated as a programmable software-engineering worker, not as the whole governance brain.
```

The Codex SDK and Codex MCP surfaces suggest a useful architecture for Factory V3 and Harmony:

```text
Harmony / Factory = mission authority, routing, evidence, policy
Codex            = code-changing worker runtime
Agents SDK / MCP = orchestration substrate
Skills           = reusable worker behavior
Mission records  = replayable governance evidence
```

This is a strategic signal, not current operating authority.

## Source Signals
The official Codex SDK documentation describes programmatic control over Codex, including starting and resuming threads and using sandbox presets such as read-only, workspace-write, and full-access.

The official Codex with Agents SDK guide describes running Codex as an MCP server, exposing tools to start and continue Codex sessions, and orchestrating Codex inside multi-agent workflows with handoffs, guardrails, and traces.

These surfaces align with the V3 direction toward governed autonomous execution, but they do not replace Factory governance.

## Architectural Interpretation
Factory V3 should not treat Codex as the source of mission authority.

Instead:
- Factory or Harmony creates the mission envelope.
- Factory or Harmony defines constraints, allowed tools, sandbox, budget, verification, and halt rules.
- Codex executes only within the granted mission authority.
- Factory or Harmony validates evidence and decides whether to continue, interrupt, halt, or escalate.

This preserves the V3 distinction between:
- conversation,
- evidence,
- human approval,
- execution authority.

## Candidate Workflow
A future research workflow could look like:

```text
Discovery Skill
  -> Challenge Skill
  -> Candidate Mission Contract
  -> Human Approval
  -> Factory/Harmony Orchestrator
  -> Codex Worker Runtime
  -> Verification Agent
  -> Governance Review
  -> Closeout / Learning
```

For Harmony-style systems, this may later support:
- integration adapter generation,
- feed/API sandbox work,
- test generation and repair,
- evidence-pack creation,
- PR preparation,
- review and verification passes.

## Research Spike
The first useful spike should be small and non-operational.

Recommended sequence:

1. Design the mission-formation and challenge skills.
2. Trial those skills manually.
3. Create a Codex SDK or Codex MCP orchestration research spike.
4. Run read-only discovery/challenge trials first.
5. Record thread IDs, prompts, outputs, sandbox modes, decisions, and closeout evidence.
6. Only after evidence exists, consider a controlled workspace-write execution trial under an explicit mission envelope.

## Required Boundaries
Any SDK/MCP orchestration work must preserve:
- no runtime authority,
- no default execution,
- no production actions,
- no hidden replacement for V3 governance,
- no credential or deployment authority without separate approval,
- no use of Codex worker output as approval authority,
- no treatment of orchestration traces as a substitute for mission records.

Codex is a worker. Factory remains the authority layer.

## Evidence To Collect
Before SDK/MCP orchestration becomes recommended V3 tooling, collect:
- setup and dependency friction,
- sandbox behavior evidence,
- thread resume behavior,
- trace/evidence completeness,
- human interrupt behavior,
- failure and halt behavior,
- comparison with manual Codex app execution,
- false confidence or runaway orchestration risks,
- whether the workflow improves mission replayability.

## Boundary
This document does not change the current approved optional operational profile:

```text
V3-OP-001 Bounded Code Change
```

Codex SDK, Codex MCP, Agents SDK orchestration, multi-agent workflow execution, and Harmony-driven worker orchestration remain research direction until separately planned, trialed, evidenced, and approved.
