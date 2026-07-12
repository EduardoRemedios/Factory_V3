# Risk Register - Advisory Record Shape Implementation

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E risk register.

| ID | Risk | Severity | Control | Evidence |
| --- | --- | --- | --- | --- |
| R-001 | Old records regress | Critical | Optional absence no-op; representative expected checks | V3-001/V3-002 |
| R-002 | Validator gains enforcement | Critical | `blocking_effect: none`; no wiring | V1-009/V3-012 |
| R-003 | Second mission-state source | Critical | Reference-only fields; design boundary | V1-004 |
| R-004 | Replay supersedes original | High | MR081 and invalid fixture | V2-005 |
| R-005 | Same actor claims independence | High | MR082 and invalid fixture | V2-006 |
| R-006 | Visual identity conflated with correctness | High | rich valid fixture; MR083 shape-only | V2-007 |
| R-007 | Boundary claim overstates proof | High | MR084 and invalid fixture | V2-008 |
| R-008 | Commit placeholder accepted as final | High | MR085; preserve `not_recorded` | V2-009 |
| R-009 | Scope/canon churn | High | exact 18-file budget | V1-010 |
| R-010 | Privacy/vendor IDs retained | Medium | coarse refs only | V1-011 |

## Residual Risk
Fresh-record authoring friction remains unmeasured and must be reviewed after optional shadow use.
