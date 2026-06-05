# Intent Red Team - V3 Mission Formation Skills Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial Stage B adversarial review.

## Iteration
Iteration: 1 of max 2

## Findings

### F1 - Critical - Skill output could be mistaken for approval authority
Why it matters: A mission contract produced by a skill may look executable even when no human Go exists.

Fix recommendation: Require every skill and trial output to label itself candidate-only and require separate human approval before execution.

### F2 - High - One combined skill may hide challenge discipline
Why it matters: If discovery and challenge live in one workflow, Codex may under-red-team its own recommended path.

Fix recommendation: Start with two skills unless implementation evidence proves one skill gives cleaner behavior.

### F3 - High - SDK orchestration could creep into the skill implementation run
Why it matters: Programmatic worker orchestration is a separate research direction and would expand authority, dependencies, and risk.

Fix recommendation: Block SDK/MCP implementation in this pack and require a later spike after skill trials.

### F4 - High - Trials could be happy-path only
Why it matters: A skill that only handles bounded execution candidates will not prove discovery or fallback value.

Fix recommendation: Require three trial classes: more-discovery, V2/heavier-planning fallback, and bounded candidate V3 envelope.

### F5 - Medium - Skill descriptions may trigger too broadly
Why it matters: Implicit skill invocation could interfere with ordinary bounded tasks.

Fix recommendation: Define precise trigger and non-trigger language, and consider disabling implicit invocation later only if trials show over-triggering.

## Verification Holes
- Need evidence that the future skill refuses to edit code.
- Need evidence that the future skill preserves V2 fallback.
- Need evidence that candidate envelopes include assumptions, unknowns, risks, and human decisions.
