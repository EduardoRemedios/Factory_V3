# Micro-Sprints: V3 Operational POC Decision Prep

## Version
v0.3

## Change Log
- v0.3 (2026-06-03): Added Hermes Agent surface research spike.
- v0.2 (2026-06-03): Added V3-only POC execution path and Garmin research spike.
- v0.1 (2026-06-03): Initial Stage H micro-sprints.

## MS-01: Garmin Connect/API Research Spike
- Objective: Determine the practical Garmin data path for a private health and fitness POC.
- Inputs: Official Garmin Connect Developer Program docs, official Health/API docs, public GitHub repositories, relevant open-source project docs, and current access/terms signals.
- Outputs: Research note classifying official API, manual export/import, unofficial open-source clients, and synthetic-only options.
- Exit criteria: Recommended first POC data path is named with risks, terms/access constraints, credential handling implications, and fallback option.
- Stop condition: No credentials, API calls, or integration implementation during the spike unless separately approved.

## MS-02: Hermes Agent Surface Research Spike
- Objective: Determine whether Hermes Agent can provide useful research comparison, optional harness leverage, or should remain out of scope for the first POC.
- Inputs: Hermes public docs, GitHub repository, desktop page, installation docs, architecture/security docs if reviewed, and V3 standalone-readiness constraints.
- Outputs: Research note classifying CLI/TUI, desktop, gateway/messaging, memory, skills, MCP, scheduling, subagents, browser/search tooling, voice, and sandbox/terminal backends.
- Exit criteria: Recommendation states whether Hermes is out of scope, research-only, optional harness candidate, or later integration candidate, with authority, memory, credential, model-routing, unattended automation, and sandbox implications.
- Stop condition: No Hermes installation, configuration, credential grant, execution, memory adoption, MCP wiring, scheduled automation, subagent use, or sandbox/backend use during the spike unless separately approved.

## MS-03: POC Brief Lock
- Objective: Convert the health and fitness concept into a bounded POC brief.
- Inputs: Sponsor feature priorities, MS-01 research result, MS-02 research result, deployment preference, data-source decision, and V3-only readiness criterion.
- Outputs: Approved POC brief with feature scope, data scope, deployment target, test expectations, and success criteria.
- Exit criteria: Sponsor approves exact POC scope.
- Stop condition: No build starts before brief approval.

## MS-04: Standalone V3 Gap Analysis
- Objective: Identify what V3-native capabilities must exist to run the POC without V2 help.
- Inputs: Current V3 docs, mission-record design, operational profile, advisory evals, and POC brief.
- Outputs: Gap list separating ready V3 capabilities from missing V3-native planning, execution, verification, closeout, recovery, and documentation behavior.
- Exit criteria: Every V2 behavior normally used by the sponsor has a V3-native equivalent, an explicit V3-only workaround, or a no-go label.
- Stop condition: Any required V2 dependency blocks POC readiness evidence.

## MS-05: V3-Only POC Execution Plan
- Objective: Prepare a POC execution plan governed by V3 only.
- Inputs: Approved brief, MS-01 research result, MS-02 research result, MS-04 gap analysis.
- Outputs: V3-only execution plan with commands, files, verification, deployment target, evidence capture, and stop conditions.
- Exit criteria: Sponsor approves the V3-only execution plan.
- Stop condition: Any V2 command or artifact is required for execution.

## MS-06: V3-Only POC Build
- Objective: Design, build, test, and deploy the private POC application using V3 only.
- Inputs: Approved V3-only execution plan.
- Outputs: Application, tests, deployment evidence, mission record, and readiness evidence.
- Exit criteria: POC passes its approved tests and deployment target without V2 help.
- Stop condition: If V3 cannot continue without V2, stop and record the standalone gap.

## MS-07: Operational Readiness Decision
- Objective: Decide whether V3 is ready for the named operational scope.
- Inputs: POC evidence, V3-only execution record, Garmin/data evidence, Hermes evidence if separately approved, test results, deployment evidence, and unresolved gaps.
- Outputs: Decision record: no-go, continue research, POC-only readiness, or broader readiness candidate.
- Exit criteria: Sponsor receives a clear readiness recommendation with evidence and remaining risks.
- Stop condition: Do not generalize from named POC readiness to default production readiness without separate evidence.
