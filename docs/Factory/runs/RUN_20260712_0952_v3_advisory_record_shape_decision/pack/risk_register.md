# Risk Register - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E risk register.

| ID | Risk | Severity | Control | Verification hook |
| --- | --- | --- | --- | --- |
| R-001 | Optional additions become mandatory | Critical | Missing objects produce no finding | Existing valid fixture outputs unchanged |
| R-002 | Record replaces authored mission state | Critical | Evidence refs only; explicit source-of-truth rule | Static review and fixture assertions |
| R-003 | Validator gains blocking authority | Critical | Preserve `blocking_effect: none`; no CI/factoryctl wiring | Advisory lint output check |
| R-004 | Verification independence overstated | High | Explicit actor/session relationship and independence enum | Same-actor fixture must not report independent |
| R-005 | Hash identity conflated with visual correctness | High | Separate verdict fields per artifact | Hash-match/visual-fail fixture |
| R-006 | Boundary absence claim outruns evidence | High | Proof scope plus limit required when claim supplied | Change-range claim fixture |
| R-007 | Replay overwrites original result | High | Observation source kind and `supersedes_original: false` | Original/replay coexistence fixture |
| R-008 | Commit state duplicated or contradictory | High | Keep existing `commit_after`; semantic checks only | Placeholder completed-record fixture |
| R-009 | Profile-specific endurance fields bloat base record | High | Defer until natural evidence | Scope review |
| R-010 | Personal/vendor session data retained | Medium | Coarse refs; no raw IDs/transcripts | Fixture content scan |

## Residual Risk
Authoring burden is not yet measured in real records. Later implementation should remain shadow-only until at least two fresh records test usability.
