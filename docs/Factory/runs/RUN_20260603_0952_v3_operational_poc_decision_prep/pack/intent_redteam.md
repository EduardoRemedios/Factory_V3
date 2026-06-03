# Intent Red Team: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface risks.
- v0.2 (2026-06-03): Added V3-only POC build and Garmin research spike risks.
- v0.1 (2026-06-03): Initial Stage B red team.

## Findings
| ID | Severity | Concern | Impact | Required Mitigation | Status |
| --- | --- | --- | --- | --- | --- |
| RT-001 | Critical | Current V2-governed planning could be confused with approval to use V2 during the POC build. | Invalid readiness evidence. | State that V2 is allowed only for current repository planning, while the POC build must use V3 only. | Addressed in intent v0.2. |
| RT-002 | Critical | A future POC could be treated as V3-ready even if V3 cannot run standalone. | False operational-readiness claim. | Add V2 dependency as a hard no-go and stop condition. | Addressed in intent v0.2. |
| RT-003 | High | Garmin integration could be chosen before access, terms, credential, and reliability risks are understood. | POC could stall or adopt brittle integration. | Require a research spike before POC implementation planning. | Addressed in intent v0.2. |
| RT-004 | High | "Internal only" could be mistaken as approval for unmanaged real personal data or public exposure. | Data handling and deployment ambiguity. | Keep public deployment blocked; require explicit approval for real data source, storage, retention, and access handling. | Addressed in intent v0.2. |
| RT-005 | Medium | Synthetic data could mask integration complexity. | POC may prove UI only, not data ingestion. | Require the POC plan to label synthetic-only evidence separately from Garmin-backed evidence. | Addressed in micro-sprints v0.2. |
| RT-006 | Medium | Research spike could become implementation. | Scope creep. | Forbid Garmin credentials, calls, app scaffolding, or deployment in this planning run. | Addressed in intent v0.2. |
| RT-007 | High | Hermes could be used as a hidden agent authority while claiming V3-only readiness. | Invalid operational proof. | Research Hermes surfaces separately and forbid Hermes execution before explicit approval. | Addressed in intent v0.3. |

## Residual Risk
- Official Garmin access may be unavailable, delayed, or unsuitable for a personal internal POC.
- Unofficial open-source clients may work technically but carry terms, reliability, credential, and maintenance risks.
- The first POC may need to start with synthetic or manual-export data while Garmin integration remains a later milestone.
- Hermes may be useful for comparison, memory, subagent, MCP, scheduling, or sandbox research, but using it during the first POC could obscure whether V3 operated standalone.

## Conclusion
Intent is acceptable for planning if the V3-only POC build requirement remains explicit across the envelope, micro-sprints, and verification plan.
