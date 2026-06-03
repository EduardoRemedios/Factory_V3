# Intent: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface research scope beyond desktop.
- v0.2 (2026-06-03): Added sponsor clarification that the future POC build must use V3 only; added Garmin research spike.
- v0.1 (2026-06-03): Initial Stage A intent.

## Purpose
Prepare the decision path for judging whether Factory V3 can be used operationally with Codex to design, build, test, and deploy an application.

## Goal
Create a planning-only decision-prep pack for a future V3-only POC application, currently expected to be a private personal health and fitness tracker.

## Operational Definition
V3 operations means using V3 with Codex to design, build, test, and deploy an application in the same practical sense that V2 is used today.

## Hard Standalone Criterion
The future POC application build must use V3 only. V2 must not help design, build, test, deploy, govern, lint, stage, pack, recover, or validate the POC application. Current repository planning may still be governed by V2 because V3 is still maturing, but POC execution evidence that depends on V2 for normal operation cannot support V3 operational readiness.

## Candidate POC Concept
- Application: private personal health and fitness tracker.
- Initial deployment posture: internal/private only; no public deployment.
- Data posture: synthetic data is allowed to accelerate design and build; later real personal data use requires explicit approval of source, storage, retention, and access handling.
- Garmin posture: research first. No Garmin integration path is approved until the spike compares official Garmin Connect Developer Program options with relevant open-source approaches.
- Hermes posture: research first. No Hermes Agent surface, backend, memory, skill, MCP server, automation, or subagent path is approved until a spike evaluates fit and boundaries.

## Garmin Research Spike Scope
The research spike must answer:
- What official Garmin Connect Developer Program and Health/API options are available for the target use case.
- Whether official access is practical for an internal personal POC.
- Which public GitHub projects or open-source clients are relevant.
- Whether any candidate open-source approach is unofficial, reverse engineered, brittle, rate-limited, credential-sensitive, or likely to violate terms.
- What minimum viable data path should be used for the first V3-only POC: synthetic data, manual export/import, official API, unofficial client, or deferred Garmin integration.

## Hermes Agent Surface Research Spike Scope
The research spike must answer:
- Which Hermes surfaces are relevant: CLI/TUI, desktop, gateway/messaging, dashboard, memory, skills, MCP, scheduling, subagents, web/browser tooling, voice, or sandbox/terminal backends.
- Whether Hermes can provide useful research comparison or optional harness leverage without becoming a V3 substitute.
- What authority, memory, credentials, model routing, unattended automation, and sandbox boundaries would be required.
- Whether Hermes should be out of scope for the first POC, used only for research comparison, or separately approved as an optional harness after the V3-only readiness question is preserved.

## Requirements
- R1 [SOURCE: user direction] V3 operations means using V3 with Codex for app design, build, test, and deployment.
- R2 [SOURCE: user direction] The POC application build must use V3 only, with no V2 help path.
- R3 [SOURCE: user direction] The current POC candidate is a private personal health and fitness tracker.
- R4 [SOURCE: user direction] The app is internal/private, not public.
- R5 [SOURCE: user direction] Synthetic data may be used to accelerate design and build.
- R6 [SOURCE: user direction] Garmin Connect/API and public GitHub approaches require a research spike.
- R7 [SOURCE: user direction and Hermes public docs] Hermes Agent should be considered across non-desktop and desktop surfaces before any tooling dependency decision.
- R8 [SOURCE: `PROMOTION_CRITERIA.md`] Standalone V3 operation is a required promotion input and V2 dependency is a hard no-go.
- R9 [SOURCE: `ROADMAP_TO_FULL_VISION.md`] The next move is operational-readiness decision prep, not default production promotion.
- R10 [SOURCE: Garmin public documentation] Official Garmin Connect Developer Program/Health API options exist but must be evaluated for access, licensing, and practical POC fit.

## Boundaries
- This run is `PLANNING_ONLY`.
- No POC code, app scaffolding, Garmin credentials, Garmin API calls, Hermes install/configuration/use, deployment, or infrastructure changes are authorized.
- No public deployment is authorized.
- No production-readiness claim is authorized.
- No V2 deprecation or removal is authorized.
- No V3 advisory validator is promoted into a required gate.
- No runtime authority, proof, lease, telemetry enforcement, governance routing, production-action mediation, or infrastructure authority is authorized.

## Acceptance Criteria
- The pack states the V3-only POC build requirement as a hard stop condition.
- The pack includes a Garmin research spike before POC implementation planning.
- The pack includes a Hermes Agent surface research spike before any tooling dependency decision.
- The pack defines internal/private deployment and synthetic-data acceleration boundaries.
- The pack separates current V2-governed planning from future V3-only POC execution.
- Stage lint, pack lint, and V3 advisory evals pass.
