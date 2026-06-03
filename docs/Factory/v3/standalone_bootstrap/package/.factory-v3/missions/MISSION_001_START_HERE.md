# Mission 001: Start Here

## Mission Status
DRAFT. Research-only and non-enforcing. Do not execute until every placeholder is resolved and a separate POC mission is approved.

## Profile
- Profile ID: `V3-POC-STANDALONE`
- Profile status: POC proof profile, not general production approval.
- V3-only: YES
- V2 allowed: NO

## Objective
Define the first bounded POC mission.

Replace this with one concrete objective:

```text
<one bounded app-design, scaffolding, implementation, verification, or deployment objective>
```

## Success Criteria
-

## Authorized Files And Directories
-

## Forbidden Scope
- Factory V2 usage.
- Public deployment.
- Production infrastructure unless explicitly approved.
- Garmin integration before dependency research approval.
- Hermes use before dependency research approval.
- Credentials or secrets in prompts, files, logs, or evidence.
- Broad architecture changes outside this mission.

## Allowed Commands
-

## Dependency Policy
- New dependencies allowed: NO by default.
- If YES, name the dependency, approval, install command, rollback plan, and verification.

## Verification
Commands and expected evidence:
-

## Halt Rules
Stop if:
- V2 is needed,
- objective or scope is ambiguous,
- authorized files are insufficient,
- an unapproved dependency is needed,
- verification fails,
- deployment scope expands,
- credentials or private data would be exposed.

## Reentry Rules
- Resume only from this mission, current repo state, and the latest closeout.
- If a derived summary conflicts with files on disk, trust files on disk.

## Closeout Required
Use:

```text
.factory-v3/templates/V3_POC_CLOSEOUT_TEMPLATE.md
```

## Mission Record Required
Use:

```text
.factory-v3/templates/V3_POC_MISSION_RECORD_TEMPLATE.json
```
