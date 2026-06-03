# Intent Lock Report: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Locked Hermes Agent research deferral.
- v0.2 (2026-06-03): Locked V3-only POC build requirement and Garmin spike deferral.
- v0.1 (2026-06-03): Initial Stage D lock report.

## Locked Intent
The pack is locked as a planning-only decision-prep run for a future V3-only operational POC application.

## Locked Readiness Question
Can Factory V3, with Codex, standalone and without V2 assistance, design, build, test, and deploy a private application?

## Locked POC Candidate
- Private personal health and fitness tracker.
- Internal/private deployment only.
- Synthetic data allowed for acceleration.
- Garmin Connect/API integration deferred to research and later approval.
- Hermes Agent surfaces deferred to research and later approval.

## Locked Hard Stops
- Stop if any future POC execution plan uses V2 to design, build, test, deploy, govern, lint, stage, pack, recover, or validate the app.
- Stop if V3 standalone gaps are converted into a readiness claim.
- Stop if Garmin credentials, API calls, or integration implementation are introduced before the research spike and explicit approval.
- Stop if Hermes is installed, configured, granted credentials, used for execution, or treated as a V3 substitute before the research spike and explicit approval.
- Stop if public deployment, production infrastructure, or external governance authority is introduced.

## Bounded Deferrals
| ID | Deferral | Bound |
| --- | --- | --- |
| DEF-001 | Exact health/fitness POC feature scope. | Must be resolved in a later POC brief before implementation. |
| DEF-002 | Garmin data path. | Must be resolved through a research spike before implementation. |
| DEF-003 | Hermes Agent surface fit. | Must be resolved through a research spike before any tooling dependency decision. |
| DEF-004 | V3 standalone proof mechanics. | Must be resolved through a gap analysis before POC execution can support readiness. |
| DEF-005 | Real personal data handling. | Must be explicitly approved before use. |
| DEF-006 | Deployment target. | Must be explicitly approved; current default is local/private only. |

## Lock Outcome
PASS for planning. No POC execution is authorized.
