# Risk Register: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface risks.
- v0.2 (2026-06-03): Added V3-only POC and Garmin research risks.
- v0.1 (2026-06-03): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification |
| --- | --- | --- | --- | --- |
| RISK-001 | Critical | Future POC uses V2 assistance. | Treat any V2 build/test/deploy/governance dependency as a hard no-go. | Verification plan checks V3-only stop condition. |
| RISK-002 | Critical | Standalone V3 gaps are ignored. | Require a standalone gap analysis before POC execution readiness. | Micro-sprint MS-03. |
| RISK-003 | High | Garmin official API access is unavailable or unsuitable. | Research official access, terms, program fit, and evaluation environment before implementation. | Micro-sprint MS-01. |
| RISK-004 | High | Unofficial Garmin clients expose credentials or violate terms. | Research open-source options and classify terms, auth, maintenance, and reliability risk. | Micro-sprint MS-01. |
| RISK-005 | High | Hermes Agent surfaces introduce extra authority, memory, credentials, or unattended automation. | Research CLI/TUI, desktop, gateway, memory, skills, MCP, scheduling, subagents, and backends before use. | Micro-sprint MS-02. |
| RISK-006 | High | POC starts before exact feature/data/deployment brief is approved. | Require brief lock before implementation planning. | Micro-sprint MS-03. |
| RISK-007 | Medium | Synthetic data evidence is overclaimed. | Separate synthetic-data proof from Garmin-backed proof. | Traceability matrix and verification plan. |
| RISK-008 | Medium | Internal/private app expands into public deployment. | Keep public deployment out of scope until explicit approval. | Envelope stop conditions. |
| RISK-009 | Medium | V3 advisory validators are promoted into required gates. | Preserve advisory-only semantics. | V3 advisory lint and manual review. |
| RISK-010 | Medium | V2 removal is implied by standalone POC planning. | Keep V2 deprecation outside scope. | Canon and envelope review. |
