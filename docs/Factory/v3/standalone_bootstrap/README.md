# V3 Standalone Bootstrap

## Version
v0.1

## Change Log
- v0.1 (2026-06-03): Initial standalone bootstrap package for a clean V3-only POC project.

## Status
Research-to-operational bootstrap candidate. This package does not make V3 the default, approve public deployment, approve new required gates, deprecate V2 in this repository, or authorize the POC application build by itself.

## Purpose
Provide a copyable V3-only seed package for a clean POC project.

The target proof is:

```text
Use V3 with Codex to design, build, test, and privately deploy an application without Factory V2 help.
```

## Package
Copy this directory into a new project:

```text
docs/Factory/v3/standalone_bootstrap/package/.factory-v3/
```

Target layout after copy:

```text
<poc-project>/.factory-v3/
```

## Operating Rule
The POC passes only if the new project can use this V3-only package to plan, build, test, and privately deploy the app without V2 stage, pack, lint, recovery, fallback, or validation machinery.

If V3 cannot continue without V2, stop and record a standalone gap. Do not use V2 to rescue the POC while still claiming V3 operational readiness.

## Intended First Use
The current candidate POC is an internal/private personal health and fitness tracker for the sponsor.

Before building the app:
- lock the POC vision,
- lock the POC constraints,
- lock the POC verification plan,
- complete Garmin Connect/API research,
- complete Hermes Agent surface research if it may influence tooling,
- create the first V3 mission from the starting mission template,
- define checkpoint, human decision interrupt, mission-state, and plan-delta rules for any larger mission,
- define the eval record that will judge whether V3 passed the POC.

## Not Included
This package intentionally does not include:
- V2 Factory stage, pack, or lint machinery,
- public deployment authority,
- Garmin credentials or implementation,
- Hermes installation or configuration,
- runtime authority, proof, leases, telemetry enforcement, or governance routing.
