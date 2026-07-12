# Sprint Envelope - Recall Sync And Endurance Canon

## Version
v0.2

## Change Log
- v0.2 (2026-07-12): Stage I hardening pins source reads to the upstream commit snapshot, protects the separate upstream worktree, and requires full planned verification beyond the manifest subset.
- v0.1 (2026-07-12): Stage H execution envelope.

## Sprint Identity
- Sprint ID: `SPRINT_20260712_0927_V3_RECALL_SYNC_ENDURANCE_CANON`
- Run ID: `RUN_20260712_0927_v3_recall_sync_endurance_canon`
- Execution mode: `EXECUTION_ENABLED`
- Execution status: awaiting Stage I2 PASS and explicit post-pack human Go

## Objective
Synchronize the bounded direct-source Stage A recall repair from `factory-starter-kit` commit `06646d7`, then reconcile active V3 canon so Factory is expected to preserve quality and governance for missions naturally lasting up to roughly four hours without requiring missions to consume four hours.

## Authorized Files
V2 build-support slice:
- `docs/Factory/ORCHESTRATION.md`
- `docs/Factory/Spec/STAGE_CONTRACTS.md`
- `docs/Factory/templates/CONTEXT_RECALL_REPORT_TEMPLATE.md`
- `scripts/factory_pack_lint.py`
- `scripts/factory_stage_lint.py`
- `scripts/knowledge_lint.sh`
- `tests/test_context_recall_repair.py`

V3 active-canon candidate set:
- `README.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/Factory/v3/ANCHOR_REGISTRY.md`
- `docs/Factory/v3/MISSION_CONTROL_CONTRACT.md`
- `docs/Factory/v3/V3_OP_003_DECISION_PACK.md`
- `docs/Factory/v3/DURATION_LADDER_PLAN.md`
- `docs/Factory/v3/CANDIDATE_PROFILE_V3_OP_003_LONG_RUNNING_REMOTE_INTERRUPT.md`
- `docs/Factory/v3/ladder/LADDER_STATUS.md`
- `docs/Factory/v3/ladder/rung3/README.md`

Run planning and later execution-closeout evidence under this run root is authorized. Touch only candidate canon files with directly affected active text or necessary version/change-log updates.

## File-Touch Budget
| Micro-sprint | Maximum product files |
| --- | ---: |
| MS-00 | 0 |
| MS-01 | 3 |
| MS-02 | 4 |
| MS-03 | 0 |
| MS-04 | 13 |
| MS-05 | 0 additional |
| Total unique product files | 20 |

Planning and closeout artifacts under this run root are excluded from the product-file budget. Any product file outside the authorized list is blocking scope expansion.

## Authorized Commands
- Read-only `git`, `rg`, `sed`, `diff`, `find`, and file-inspection commands.
- `python3 -m unittest tests.test_context_recall_repair`
- `python3 -m unittest discover -s tests`
- `bash scripts/knowledge_lint.sh`
- `python3 -m py_compile scripts/factory_pack_lint.py scripts/factory_stage_lint.py scripts/factory_context_index.py scripts/factoryctl`
- Canonical V3 advisory validator commands listed in `AGENTS.md` and `verification_plan.md`.
- `git diff --check`
- `./scripts/factoryctl context-index`
- Stage, pack, mission-record, loop-contract, telemetry-replay, and mission-control advisory checks already present in the repository.

No dependency installation, network write, external messaging, deployment, credential use, destructive command, commit, or push is authorized by this envelope.

## Implementation Constraints
- Apply SIMPLE-CODE-GATE v2: smallest clear change, no speculative abstraction, no dependency addition, no silent failure, no broad validator refactor.
- Transfer only direct-source repair behavior attributable to upstream commit `06646d7`.
- Read authoritative upstream content with commit-pinned `git show` or `git diff` against `06646d7`; do not treat the mutable upstream working tree as source authority.
- Do not modify, clean, stage, or otherwise alter the separate `factory-starter-kit` working tree or its unrelated untracked files.
- Preserve local V2 build-support wording and V3 repository boundaries.
- Complete and verify MS-01 through MS-03 before editing any V3 canon candidate.
- A mission ends when objective and verification are complete; do not add work, time, calls, waypoints, tests, files, or scope to create endurance evidence.
- A shorter mission may PASS while leaving the unobserved upper endurance envelope insufficiently evidenced.
- Do not claim four-hour capability is proven by this documentation repair.
- Preserve `V3-OP-003` at `NO PROMOTION YET` and retain every current exclusion.
- Do not edit prior run evidence or prior human decision/adjudication records.

## Independent Verification
- Builder and verifier roles must be distinguishable in closeout evidence, even if both are performed sequentially by Codex.
- Verifier rereads the locked intent, changed paths, upstream source commit, and final canon without relying only on builder prose.
- Requirement status should be reported as `PROVED`, `WEAK`, `MISSING`, or `CONTRADICTED` for AC1 through AC13.

## Required Verification
Use `verification_plan.md`, `traceability_matrix.md`, and `verification_manifest.yaml`. All manifest commands and every additional required check in `verification_plan.md` must pass. Manual V0 checks for source fidelity, no historical rewrites, no padding incentives, active-status agreement, and no promotion overclaim are required before closeout.

## Halt And Fallback Rules
Halt and ask if:
- upstream source behavior cannot be isolated from unrelated changes;
- user changes overlap an authorized target in a way that makes intent ambiguous;
- a required verification command fails outside a clearly bounded repair;
- validator compatibility requires unrelated refactoring;
- canon correction would weaken an approval boundary or imply proven endurance;
- any unauthorized file, dependency, external effect, runtime authority, routing, required gate, telemetry enforcement, or profile promotion appears necessary.

Factory V2 remains the governing fallback. Do not continue from stale or contradictory source state.

## Completion Conditions
- All AC1-AC13 are evidenced.
- Both micro-sprint gates pass in order.
- All required commands and manual reviews pass.
- Active canon agrees on current status and next work.
- Residual upper-envelope evidence gap is explicit.
- No unauthorized paths or effects occurred.
- Execution closeout is prepared for human review.
