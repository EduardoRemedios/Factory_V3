# Mission Formation Direction

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial strategic note on discovery, challenge, mission formation, and long-running autonomous execution.

## Status
Strategic direction and research roadmap context only. This document does not make Factory V3 the default mode, approve a new operational profile, approve non-coding execution missions, deprecate Factory V2, wire V3 into required gates, or grant runtime authority.

## Purpose
Record a key V3 product direction:

```text
The quality of the mission determines the quality of the autonomy.
```

Long-running autonomous work is only useful when the mission is clear enough to execute safely. For overnight or multi-hour Codex runs, the highest leverage work may happen before implementation: discovery, problem framing, assumption testing, option comparison, and objective clarification.

Traditional consulting and software discovery reduce uncertainty before a team commits to a build. Factory V3 should preserve that value instead of collapsing too quickly from an idea into execution.

## Core Thesis
Factory V3 should evolve from a coding-governance process toward a broader system for:

```text
AI-assisted mission formation and governed autonomous mission execution.
```

Coding remains the first proving ground because it has strong evidence surfaces: diffs, commands, tests, commits, failures, and closeout records. But the deeper product value is the ability to turn vague intent into a high-quality mission contract before any autonomous worker receives execution authority.

## Directional Flow
The target flow should be closer to:

```text
Idea
  -> Discovery Mission
  -> Challenge Mission
  -> Mission Contract
  -> Execution Mission
  -> Closeout / Learning
```

not:

```text
Idea
  -> Execution
```

Each step should have a different authority level.

## Discovery Mission
A Discovery Mission is a non-executing mission formation activity.

It may:
- ask Socratic questions,
- clarify the actual problem,
- identify stakeholders and constraints,
- expose hidden assumptions,
- compare solution paths,
- research relevant context where authorized,
- estimate value, cost, risk, and uncertainty,
- identify unknowns and decision points,
- recommend whether execution is ready.

It must not:
- make code changes,
- create production effects,
- grant itself execution authority,
- treat conversation as approval authority,
- promote a mission into execution without human approval.

The output should be a structured artifact, not just a chat transcript.

## Challenge Mission
A Challenge Mission is a non-executing red-team pass over the discovery output.

It should ask:
- Is the real problem different from the stated problem?
- Is the proposed build larger than necessary?
- Are there cheaper or safer paths?
- Which assumptions are weak or unsupported?
- Which risks would invalidate the mission?
- What would cause an overnight run to fail or halt?
- Are the success criteria observable?
- Are the authority boundaries explicit?

The Challenge Mission should reduce false confidence before execution begins.

## Mission Contract
The Mission Contract converts discovery output into executable authority only after human approval.

It should include:
- problem statement,
- desired outcome,
- non-goals,
- assumptions,
- unknowns,
- rejected paths,
- chosen path,
- success criteria,
- authority boundaries,
- budget and checkpoint rules,
- allowed tools and commands,
- dependency policy,
- verification requirements,
- halt and fallback rules,
- human decision interrupt rules,
- reentry instructions.

For code-changing work, the Mission Contract may become a V3 mission envelope. For broader strategy or non-coding work, it remains roadmap vision until separate profile evidence and approval exist.

## Autonomy Preparation
Discovery is not only requirements gathering. It is autonomy preparation.

A good discovery phase should pre-resolve common decisions and define when the worker must interrupt later. The goal is not to ask every possible question before execution. The goal is to ask enough high-value questions to avoid predictable failure and preserve human control over material decisions.

Useful Discovery Mission outputs include:
- assumption ledger,
- open-question register,
- decision log,
- option matrix,
- risk register,
- evidence plan,
- pre-resolved decision list,
- execution-readiness assessment,
- draft mission envelope.

## Research Implications
Future V3 research should consider a non-operational mission-formation profile family, for example:

```text
V3-DISC-001 - Discovery / Mission Formation
V3-CHAL-001 - Challenge / Assumption Test
V3-EXEC-*   - Governed Execution Profiles
```

These names are directional only. They do not approve new profiles.

Before any mission-formation profile is promoted, V3 should collect evidence that the profile:
- reduces ambiguity before execution,
- improves mission envelope quality,
- avoids performative questioning without convergence,
- records assumptions and human decisions replayably,
- preserves V2 fallback for broad or high-risk work,
- does not blur conversation, evidence, and approval authority.

## Boundary
This document is strategic context only.

It does not change the current approved optional operational profile:

```text
V3-OP-001 Bounded Code Change
```

Discovery, challenge, strategy, market, acquisition, build-versus-buy, and non-coding mission formation remain roadmap direction until separately evidenced and approved.
