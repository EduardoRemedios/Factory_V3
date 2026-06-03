# Intent Synthesis: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface research synthesis.
- v0.2 (2026-06-03): Synthesized V3-only POC build and Garmin spike clarifications.
- v0.1 (2026-06-03): Initial Stage C synthesis.

## Synthesis
The planning pack should prepare a decision path, not execute the application. The central readiness claim under test is whether V3 can be used with Codex, standalone, to design, build, test, and deploy a private application.

The current POC concept is a personal health and fitness tracker. The app is internal/private and may use synthetic data to accelerate design and build. Garmin Connect data integration is desirable, but it must be researched before implementation because the official program and unofficial open-source paths have different access, terms, reliability, and credential implications. Hermes Agent is also worth researching across its CLI/TUI, desktop, gateway, memory, skills, MCP, scheduling, subagent, tooling, and sandbox surfaces, but only as separately evaluated leverage.

## Resolved Constraints
- Current planning may use V2 build-support scaffolding.
- Future POC application work must use V3 only.
- V2 must not be used as a fallback, helper, gate, linter, packer, recovery path, or operational validator for the POC build.
- V3 operational readiness cannot be claimed if the named POC scope depends on V2.
- Garmin integration is deferred to a research spike and later explicit approval.
- Hermes use is deferred to a research spike and later explicit approval.
- Internal/private use does not authorize public deployment, production infrastructure, credentials, or unmanaged real-data handling.

## Planning Decision
Proceed with a planning-only envelope that defines:
- a V3-only operational POC readiness question,
- a Garmin Connect/API research spike,
- a Hermes Agent surface research spike,
- a POC brief lock step,
- a standalone V3 gap analysis,
- and explicit stop conditions before any app build.
