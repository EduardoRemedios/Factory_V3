# Sprint Envelope: V3 Operational POC Decision Prep

## Version
v0.4

## Change Log
- v0.4 (2026-06-03): Expanded Hermes research from desktop-specific to all relevant Agent surfaces.
- v0.3 (2026-06-03): Added initial Hermes tooling research branch.
- v0.2 (2026-06-03): Added V3-only POC build requirement and Garmin research spike.
- v0.1 (2026-06-03): Initial Stage I envelope.

## Sprint Metadata
- RUN_ID: `RUN_20260603_0952_v3_operational_poc_decision_prep`
- Sprint ID: `SPRINT_20260603_0952_V3_OPERATIONAL_POC_DECISION_PREP`
- Execution Mode: `PLANNING_ONLY`

## Objective
Prepare the next decision point for V3 operational readiness: a future private POC application built, tested, and deployed with V3 only.

## Readiness Question
Can Factory V3, with Codex, standalone and without V2 assistance, design, build, test, and deploy a private application in the same operational sense that V2 is used today?

## Candidate Operational Proof
- Application concept: personal health and fitness tracker.
- Deployment posture: internal/private only; no public deployment.
- Data posture: synthetic data allowed for acceleration; real personal data handling requires later explicit approval.
- Garmin posture: research spike required before choosing official API, open-source client, manual export/import, or deferred integration.
- Hermes posture: research spike may evaluate whether Hermes Agent surfaces can provide useful open-source local-agent leverage, but Hermes is not approved as a POC dependency or V3 substitute.

## Critical Boundary
The future POC build must use V3 only. V2 must not help design, build, test, deploy, govern, lint, stage, pack, recover, or validate the POC application. Any V2 dependency during POC execution is a readiness no-go.

## Current Planning Boundary
This pack may use existing V2 Factory planning scaffolding because V3 is still under development. That does not authorize V2 use in the future POC build.

## Source Context
- `README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/PROMOTION_CRITERIA.md`
- Official Garmin Connect Developer Program / Health API public docs.
- Public GitHub/open-source Garmin client landscape.
- Hermes Agent public docs, desktop page, and GitHub repository.

## File-Touch Budget
Authorized for this planning run:
- Canon documentation updates that clarify the next operational-readiness decision.
- This run directory under `docs/Factory/runs/RUN_20260603_0952_v3_operational_poc_decision_prep/`.
- No application source code.
- No Garmin credentials or API calls.
- No Hermes install, configuration, or execution.
- No deployment or infrastructure files.

## Decision Levels for Future Review
| Level | Meaning |
| --- | --- |
| `NO_GO_CONTINUE_RESEARCH` | V3-only operational use is not ready; continue research or capability buildout. |
| `POC_BRIEF_READY` | The private POC brief is clear enough for V3-only planning. |
| `V3_ONLY_POC_PLAN_READY` | The POC can be planned with V3 only, but execution is not yet approved. |
| `STANDALONE_GAP_REMAINS` | A required operational behavior still depends on V2 or is missing in V3. |
| `V3_ONLY_POC_EXECUTION_APPROVED` | Sponsor separately approves building the POC with V3 only. |
| `NAMED_POC_READINESS_CANDIDATE` | POC evidence may support readiness for the named scope only. |

## Research Spike Requirements
### Garmin
- Compare official Garmin Connect Developer Program / Health API options with open-source alternatives.
- Identify access, licensing, auth, credential, reliability, maintenance, terms, and data-shape implications.
- Recommend the first POC data path: synthetic-only, manual import/export, official API, unofficial client, or deferred Garmin integration.

### Hermes Agent Surfaces
- Confirm current license, supported operating systems, installation model, repository maturity, and available surfaces.
- Evaluate whether CLI/TUI, desktop, gateway/messaging, persistent memory, skills, MCP, scheduling, delegated subagents, web/browser tooling, voice, and sandbox/terminal backends could help V3 operations.
- Identify risks around extra agent authority, memory boundaries, credentials, model routing, unattended automation, and overlap with Codex.
- Decide whether Hermes is useful as a research comparison, optional harness, or out-of-scope for the first POC.

## Acceptance Criteria
- The pack explicitly forbids V2 use in the future POC build.
- The pack includes Garmin and Hermes research spikes before any dependency decision.
- The pack keeps the POC private/internal and blocks public deployment.
- The pack permits synthetic data while preventing overclaiming against Garmin-backed integration evidence.
- The pack does not claim V3 default production readiness or V2 deprecation.
- Stage lint, pack lint, and V3 advisory evaluations pass.

## Stop Conditions
- Any future POC plan depends on V2.
- Any future POC plan treats Hermes as a V3 replacement rather than a separately evaluated optional tool.
- Garmin credentials, API calls, or app integration are attempted before research and explicit approval.
- Hermes is installed, configured, granted credentials, or used to execute work before research and explicit approval.
- Public deployment, production infrastructure, or external governance authority is introduced.
- V3 advisory validators are made required gates.
- V2 deprecation or removal is implied.
