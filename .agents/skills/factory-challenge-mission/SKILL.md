---
name: factory-challenge-mission
description: Use to red-team a Factory V3 discovery output, candidate mission contract, long-running build plan, overnight Codex plan, or mission envelope before execution. Finds weak assumptions, missing authority, over-scoping, verification gaps, fallback triggers, and human-decision risks. Do not use to implement changes.
---

# Factory Challenge Mission

## Status
Non-executing Factory V3 challenge skill. This skill reviews and hardens mission-formation output; it does not grant execution authority or approve implementation.

## Core Rule
Challenge reduces false confidence before autonomy begins.

Do not edit files, run implementation commands, create production effects, or treat a PASS as human approval.

## Source Context
When working in this repository, align with:
- `docs/Factory/v3/MISSION_FORMATION_DIRECTION.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md` Phase 4.5
- `docs/Factory/v3/CODEX_SDK_ORCHESTRATION_DIRECTION.md` for SDK/MCP boundaries

Load these only when repository-grounded V3 context is needed.

## Trigger
Use this skill when the user asks to:
- challenge a mission plan,
- red-team a discovery output,
- review a candidate mission envelope,
- find what is missing before a long-running build,
- decide whether a mission is ready for V3 execution,
- compare mission contract quality before and after discovery.

Do not use this skill when:
- the user only wants normal code review of an implemented diff,
- there is no mission/discovery/plan output to challenge,
- the task is already under an approved execution envelope and the user asks to implement.

## Review Workflow
1. Identify the proposed mission and claimed route.
2. Check whether the plan is executable, candidate-only, or should route to V2/heavier planning.
3. Attack the problem framing: is the stated problem the real problem?
4. Attack assumptions: which assumptions are unsupported, risky, or decision-changing?
5. Attack scope: is the mission too broad, under-bounded, or missing forbidden scope?
6. Attack authority: are files, commands, tools, credentials, deployment, dependencies, and human approvals explicit?
7. Attack verification: are success criteria observable and checks runnable?
8. Attack long-running behavior: what happens on failed verification, context exhaustion, stale state, rate limits, missing human answer, or partial completion?
9. Recommend `PASS`, `CONDITIONAL PASS`, `MORE DISCOVERY`, or `V2_OR_HEAVY_PLANNING`.

## Finding Severity
- Critical: would allow execution without authority, unsafe scope, production action, credential misuse, or failed-verification continuation.
- High: would likely cause overnight failure, bad route selection, weak verification, or major rework.
- Medium: degrades clarity, reviewability, or trial quality.
- Low: polish or wording issue.

## Output Shape
Use concise headings:

```text
Challenge Result
Verdict
Critical Findings
High Findings
Medium/Low Findings
Assumptions To Resolve
Authority Gaps
Verification Gaps
Fallback Triggers
Recommended Repairs
Execution Readiness
```

## Guardrails
- A clean challenge result is not approval to execute.
- Do not invent missing authority to make the mission pass.
- Prefer conservative routing when payment, authentication, compliance, deployment, credentials, infrastructure, runtime authority, production data, or regulated actions appear.
- Preserve V2 fallback and non-deprecation language.
- Treat Codex SDK/MCP orchestration as a separate research spike unless explicitly approved.
