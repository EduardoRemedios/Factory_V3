# Intent Red Team

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Red-team review for real telemetry capture planning.

## Iteration
Iteration: 1 of max 2

## Findings

| Severity | Finding | Resolution |
|---|---|---|
| High | Plan could be read as approval to start logging immediately. | State no real telemetry is collected and future pilot needs a separate execution run. |
| High | Storage path could normalize telemetry as required evidence. | Label future logs optional shadow evidence only. |
| High | Real logs could over-collect sensitive data. | Add explicit excluded-data and redaction review rules. |
| Medium | First pilots could be too broad. | Limit to 3 small `V3-OP-001` missions. |

## Exit Criteria
PASS
