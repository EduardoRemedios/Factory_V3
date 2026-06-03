# POC Constraints

## Version
v0.1

## Status
Research-only and non-enforcing until a separate POC mission is approved.

## V3-Only Constraint
Factory V2 must not be used to design, build, test, deploy, govern, lint, recover, or validate this POC.

If V3 cannot proceed without V2, stop and record:
- the missing V3 capability,
- the blocked mission,
- the evidence that proves the gap,
- the recommended V3 improvement.

## Deployment Constraint
Deployment is private/internal only unless a later mission explicitly approves a target and scope.

No public deployment is approved by this file.

## Data Constraint
Allowed by default:
- synthetic data,
- local mock data,
- local manually entered data.

Requires separate approval:
- real personal health/fitness data,
- Garmin Connect data,
- credentials,
- tokens,
- third-party integrations,
- cloud-hosted storage.

## Garmin Constraint
Garmin Connect/API work is research-only until `DEPENDENCY_RESEARCH.md` records an approved path.

Research must compare:
- official Garmin Connect Developer Program / Health API,
- manual export/import,
- relevant open-source clients,
- synthetic-only or deferred integration.

## Hermes Constraint
Hermes Agent work is research-only until `DEPENDENCY_RESEARCH.md` records an approved path.

Research must evaluate relevant surfaces:
- CLI/TUI,
- desktop,
- gateway/messaging,
- dashboard,
- memory,
- skills,
- MCP,
- scheduling,
- subagents,
- browser/search tooling,
- voice,
- sandbox or terminal backends.

Hermes must not become a hidden substitute for V3 standalone operation.

## Dependency Constraint
No new dependency is allowed unless the active mission names:
- package name,
- purpose,
- risk,
- install command,
- rollback plan,
- verification command,
- human approval.

## Evidence Constraint
Every mission must produce:
- mission envelope,
- files changed,
- commands run,
- verification result,
- halt/fallback review,
- closeout,
- mission record.
