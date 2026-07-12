# Verification Plan - Recall Sync And Endurance Canon

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage F verification design.

## Strategy
Use focused contract tests first, full repository regressions second, V3 advisory language checks third, and manual source/canon review last. Any failed required command halts execution.

## Required Checks
| ID | Tier | Constraint | Check | Expected evidence |
| --- | --- | --- | --- | --- |
| V2-001 | V2 | C-001 | `python3 -m unittest tests.test_context_recall_repair` | All repair-path cases pass |
| V3-002 | V3 | C-001, M-003 | `python3 -m unittest discover -s tests` | Full suite exits 0 |
| V3-003 | V3 | C-001, H-005 | `bash scripts/knowledge_lint.sh` | `knowledge_lint: PASS` |
| V1-004 | V1 | C-001 | Compile modified Python entry points | No syntax errors |
| V2-005 | V2 | M-002 | Mission-record fixture expected output | Deterministic PASS |
| V2-006 | V2 | M-002 | Telemetry replay fixture expected output | Deterministic PASS |
| V2-007 | V2 | M-002 | Loop-contract fixture expected output | Deterministic PASS |
| V2-008 | V2 | M-002 | Mission-control-contract fixture expected output | Deterministic PASS |
| V1-009 | V1 | C-002, H-002, H-003 | V3 advisory lint and operational-readiness evals, including NL pilot | Non-blocking classifications remain within existing accepted posture |
| V1-010 | V1 | H-001 | Compare modified sync hunks to upstream commit `06646d7` | Only direct-source repair behavior transferred |
| V0-011 | V0 | H-002, H-003 | Manual endurance-language review | No duration/call/waypoint floor or proof overclaim remains in active canon |
| V0-012 | V0 | H-004 | Changed-path review | No prior run evidence or human adjudication record changed |
| V1-013 | V1 | H-005 | Search current status and next-gate sections | Completed work no longer appears as active next work |
| V1-014 | V1 | M-001 | `git diff --check` | No whitespace errors |

## Verification Order
1. Apply and test the V2 build-support sync with V2-001 through V3-003 and V1-004.
2. Halt before V3 canon edits if any first-slice check fails.
3. Apply canon reconciliation.
4. Run all checks V2-001 through V1-014.
5. Independent verifier reviews source transfer, changed paths, active status agreement, and no-promotion wording.

## Manual Review Questions
- Does every successful mission stop when objective and verification are complete?
- Is an early successful finish distinct from evidence about unobserved endurance capacity?
- Are quality, authority, checkpoint, re-entry, and evidence continuity the evaluated dimensions?
- Does `V3-OP-003` remain unapproved?
- Did any prior run record or decision artifact change?

## Failure Handling
Do not weaken validators, alter expected outputs without explained behavior change, or broaden scope to make verification pass. Halt, record the failing check, and request human direction if the failure cannot be fixed within the locked envelope.
