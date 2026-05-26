# Risk Register

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Risk register for Phase 3 telemetry/replay planning.

| ID | Severity | Risk | Mitigation | Verification Hook |
|---|---|---|---|---|
| R1 | High | Scope creep from planning into implementation. | State no implementation approval in plan and roadmap. | V3 advisory lint and manual diff review. |
| R2 | High | Over-collection of private data. | Excluded-data and data-minimization sections are required. | Plan review checklist. |
| R3 | High | Telemetry creates a second source of truth. | Replay derives from mission record plus log; mission record remains shadow advisory. | Source-of-truth rule in plan. |
| R4 | Medium | Replay checks imply enforcement. | Label checks future advisory-only until separately approved. | Operational-readiness eval and wording review. |
| R5 | Medium | Future fixture corpus becomes too large. | Limit initial fixture categories. | Traceability matrix. |
