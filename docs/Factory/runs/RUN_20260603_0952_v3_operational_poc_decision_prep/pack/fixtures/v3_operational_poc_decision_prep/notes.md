# Fixture Notes: V3 Operational POC Decision Prep

## Version
v0.4

## Change Log
- v0.4 (2026-06-03): Expanded Hermes evidence classes beyond desktop.
- v0.3 (2026-06-03): Added Hermes research branch.
- v0.2 (2026-06-03): Added V3-only POC and Garmin research notes.
- v0.1 (2026-06-03): Initial notes.

## Purpose
This directory records planning notes only. It contains no app fixture, Garmin fixture, Hermes fixture, credentials, deployment artifact, or executable POC material.

## Future Evidence Classes
| Class | Meaning |
| --- | --- |
| `synthetic_data_only` | POC uses generated or mocked health/fitness data and cannot prove Garmin ingestion. |
| `manual_import` | POC ingests user-provided export files without live Garmin API access. |
| `official_garmin_api` | POC uses an approved official Garmin API path. |
| `unofficial_garmin_client` | POC uses an open-source/unofficial client after explicit risk acceptance. |
| `garmin_deferred` | POC intentionally defers Garmin integration. |
| `hermes_research_only` | Hermes Agent surfaces are evaluated as tooling context but not used in POC execution. |
| `hermes_optional_harness` | Hermes is separately approved as an optional harness or comparison tool, with surfaces and authority labeled. |
| `v3_only_execution` | POC design/build/test/deploy evidence uses V3 only. |
| `v2_dependency_no_go` | A required V2 dependency blocks operational-readiness evidence. |

## Notes
- No evidence class is assigned by this planning run.
- Future POC evidence must record whether V3 operated standalone.
