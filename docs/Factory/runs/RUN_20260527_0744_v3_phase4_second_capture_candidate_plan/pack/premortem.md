# Premortem: Phase 4 Second Capture Candidate Plan

## Version
v0.1

## Change Log
- v0.1 (2026-05-27): Initial Stage E premortem.

## Failure Scenarios
- PM1 Critical: Candidate planning is mistaken for execution approval. Mitigation: block execution until explicit Go.
- PM2 Critical: Capture artifacts are created before the mission runs. Mitigation: future envelope names them only after approval.
- PM3 High: Docs-only work yields weak execution-reliability signal. Mitigation: require command and verification evidence in summary.
- PM4 High: `NO_TELEMETRY` is treated as closing telemetry gap. Mitigation: state gap remains open.
- PM5 Medium: Candidate drifts beyond `V3-OP-001`. Mitigation: stop on broad scope, dependencies, infrastructure, auth, payment, compliance, deployment, or runtime concerns.
- PM6 Medium: FP/FN adjudication is skipped. Mitigation: require human classification in future result summary.
- PM7 High: Future index wording implies routing threshold or promotion evidence. Mitigation: apply scratchpad FP-002 and run the NL pilot before closeout.
