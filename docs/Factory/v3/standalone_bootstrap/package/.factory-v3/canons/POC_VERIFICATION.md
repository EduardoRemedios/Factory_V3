# POC Verification

## Version
v0.1

## Status
Research-only and non-enforcing until a separate POC mission is approved.

## Verification Goal
Prove both:
- the application works for the approved private POC scope,
- V3 operated standalone during the lifecycle.

## Required Verification Classes
| Class | Required Evidence |
| --- | --- |
| V3-only compliance | No Factory V2 stage, pack, lint, fallback, recovery, or validation was used. |
| Scope discipline | Every edit maps to an approved mission. |
| App behavior | The app meets the mission success criteria. |
| Test quality | Tests or checks run and results are recorded. |
| Deployment | Private/internal deployment target works if deployment is in scope. |
| Evidence replay | Mission records and closeouts are enough to reconstruct what happened. |
| Halt behavior | Failures stop work until a human decision or a new mission. |
| Dependency discipline | Garmin, Hermes, or other dependencies are approved before use. |

## Default Verification Commands
Fill these after the app stack is chosen:

```bash
# lint

# typecheck

# test

# build

# local/private deployment smoke check
```

## Evidence Rules
- Summarize command output; do not paste secrets or private tokens.
- Record failed checks honestly.
- Do not continue after failed verification unless a new mission explicitly authorizes the recovery path.
- Label synthetic-only evidence separately from Garmin-backed evidence.
- Label Hermes-assisted evidence separately if Hermes is later approved.
