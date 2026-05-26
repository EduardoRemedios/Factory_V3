# Premortem: Phase 4 Eval Expansion Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial Stage E premortem.

## Failure Scenarios
- PM1 Critical: Harness capability scores become overconfident or universal even though evidence is harness, model, repo, mission-profile, and tool-access specific. Mitigation: require profile metadata and forbid cross-harness generalization.
- PM2 Critical: Evals measure document compliance while missing real execution reliability. Mitigation: require scenarios for command execution, failed checks, halt behavior, reentry, evidence capture, and closeout quality.
- PM3 High: Negative fixtures become trigger-word synthetic cases that do not match real failures. Mitigation: label synthetic-only fixtures and plan real-run-derived negative cases.
- PM4 Critical: Phase 4 accidentally designs or implements Phase 5 governance routing. Mitigation: thresholds are advisory discussion only and cannot route work.
- PM5 Critical: Threshold language implies reduced governance, default mode, or V2 deprecation before evidence exists. Mitigation: every threshold section must state non-operational status and V2 fallback preservation.
- PM6 High: The Phase 3 missing natural halted, fallback, or clarification-heavy telemetry pilot is forgotten. Mitigation: make it an explicit evidence gap in Phase 4 plan and traceability.
- PM7 High: V2 fallback or non-deprecation language weakens while discussing reduced V2 decomposition. Mitigation: require V2 fallback language in the plan, template, and verification checks.
- PM8 Medium: False-positive and false-negative rollup shape is too vague for later decisions. Mitigation: plan explicit classification fields and human adjudication notes.
- PM9 Medium: Capability templates collect too much sensitive or irrelevant data. Mitigation: keep telemetry and profile payloads summary-only and avoid chain-of-thought, raw command output, secrets, source contents, and vendor-private cognition state.

## Planning Consequence
The Phase 4 execution pack must start from templates and fixture plans, then verify advisory-only language before adding any code.
