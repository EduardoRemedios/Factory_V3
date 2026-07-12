# Risk Register - Mission Re-entry Proof Pack

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Stale or changed-authority case is allowed to continue | Semantic cross-field checks | Isolated MC151/MC152 fixtures |
| R-002 | Critical | Failed verification gains broad recovery authority | Permit only `verify` plus one bounded action/basis | MC153 fixture and rich valid recovery case |
| R-003 | High | Existing contracts become invalid | Optional list absence is no-op | Existing valid fixture exact baseline |
| R-004 | High | Fixture claims operational fresh-session proof | Bound `fresh_session` as scenario input | Canon/closeout static review |
| R-005 | High | Expected refresh hides old drift | Filter new paths and compare baseline | Old-subset JSON comparison |
| R-006 | High | Invalid fixture has unrelated findings | One mutation per invalid file | Exact per-file ID assertion |
| R-007 | High | Runtime/gate/promotion scope leaks into canon or code | Exact paths and no-touch searches | Advisory/readiness lints and diff audit |
| R-008 | Medium | New generic abstraction adds complexity | Direct helper, no dependency | Code review and dependency diff |
| R-009 | Medium | One closeout sample overstates FP/FN evidence | Label one-sample observation and residual uncertainty | Closeout review |
| R-010 | Medium | Visual evidence is added despite no visual surface | Omit visual evidence as not relevant | Mission-record closeout parse/review |
