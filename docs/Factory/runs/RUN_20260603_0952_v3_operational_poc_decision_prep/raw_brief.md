# Raw Brief: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent docs and non-desktop surfaces to the research scope.
- v0.2 (2026-06-03): Added user clarification that the POC application build must use V3 only, with no V2 help path; added Garmin Connect/API research spike.
- v0.1 (2026-06-03): Initial operational-readiness decision-prep brief.

## User Direction
The sponsor defines V3 operations as using V3 with Codex to design, build, test, and deploy an application in the same operational sense that V2 is used today.

The sponsor is considering a personal health and fitness tracking application as the first operational proof. The app would be internal/private, not publicly deployed. Synthetic data may be used to accelerate design and build. The sponsor wants a research spike to understand Garmin Connect data options, official Garmin API access, and relevant public open-source approaches before the POC brief is locked.

Critical clarification: the POC application build must use V3 only. V2 may be used as temporary build-support scaffolding for this repository planning step while V3 is still maturing, but V2 must not help design, build, test, or deploy the POC application. Any POC evidence that depends on V2 for normal operation cannot support a V3 operational-readiness claim.

The sponsor also wants to consider Hermes Agent. The research scope should evaluate Hermes broadly, not only the desktop app: CLI/TUI, desktop, gateway/messaging surfaces, memory, skills, MCP, scheduling, subagents, browser/search tooling, and sandbox/terminal backends.

## Planning Objective
Create a Factory-controlled planning pack that prepares the decision path for a V3-only operational POC without executing the POC.

The pack must:
- Define the readiness question for V3 operational use with Codex.
- Treat standalone V3 operation as a hard criterion.
- Separate the current planning pack from any future POC build.
- Define a Garmin Connect/API research spike before POC implementation planning.
- Define a Hermes Agent surface research spike before any tooling dependency decision.
- Keep internal/private deployment and synthetic-data acceleration within scope.
- Avoid approving public deployment, production credentials, infrastructure changes, or external integrations before separate approval.

## Explicit Non-Goals
- Do not build the health and fitness POC in this run.
- Do not use V2 to help build, test, or deploy the future POC application.
- Do not claim V3 is production/default ready.
- Do not deprecate or remove V2 scaffolding.
- Do not wire V3 advisory validators into required gates.
- Do not introduce runtime authority, proof, lease enforcement, governance routing, telemetry enforcement, production-action mediation, or external governance-kernel adapters.
- Do not commit to an official or unofficial Garmin integration path before the research spike.
- Do not install, configure, or use Hermes before the research spike and explicit approval.

## Required Output
A planning-only pack with intent, risks, traceability, verification, micro-sprints, and envelope artifacts that are ready for review and can be used to decide the next approved step.
