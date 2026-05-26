# Intent Red Team: Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage B red-team review.

## Iteration
- Iteration: 1 of max 2

## Findings

### F1 - Critical - Thresholds can imply routing authority
- Why it matters: Phase 4 needs threshold discussion, but autonomous, light, standard, and heavy labels belong to Phase 5 routing. If written operationally, the pack could imply governance reduction before evidence exists.
- Fix recommendation: require every threshold reference to be marked advisory, non-operational, harness/profile-specific, and not usable for routing without a later approved Phase 5 run.

### F2 - Critical - Harness scoring can become universal
- Why it matters: Capability profiles for Codex, Claude Code, Cursor, and future harnesses can be misread as general model capability rather than observed behavior in a specific harness, profile, repo, command set, and interruption condition.
- Fix recommendation: make capability profile fields bind score to harness, model when known, tool access, repo profile, mission profile, verification commands, and evidence date.

### F3 - High - Document compliance can hide execution unreliability
- Why it matters: Existing evals can catch V3 promotion drift, but Phase 4 must measure whether a harness actually runs checks, halts, recovers, and records evidence.
- Fix recommendation: require future fixture expansion to include execution-reliability scenarios and real-run result corpus planning, not only doc wording checks.

### F4 - High - Negative fixtures may be too synthetic
- Why it matters: Synthetic fixtures are useful but can train the validator around trigger phrases rather than realistic failure modes.
- Fix recommendation: require a fixture expansion plan with real-run-derived negative cases when available and a label for synthetic-only coverage.

### F5 - High - Phase 3 negative telemetry gap can be lost
- Why it matters: No natural halted, fallback, or clarification-heavy telemetry pilot exists. Omitting this gap would overstate evidence quality.
- Fix recommendation: put the gap in intent, premortem, verification, traceability, and future Phase 4 plan acceptance criteria.

### F6 - Medium - V2 fallback language can weaken
- Why it matters: Phase 4 is about possible future reduced decomposition, which can accidentally read as V2 replacement.
- Fix recommendation: state that V2 remains supported and fallback until explicit later release evidence approves otherwise.

## Verification Holes
- The pack must include checks for advisory-only threshold language.
- The pack must include no-touch verification that no Phase 4 implementation files are created in this run.

## Blocking Findings
- None after recommended hardening.
