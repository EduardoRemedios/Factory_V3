# V3 Standalone Bootstrap Manifest

## Version
v0.1

## Status
Research-only and non-enforcing. This manifest does not approve POC execution, V3 default use, required gates, public deployment, or V2 removal.

## Package Root
`docs/Factory/v3/standalone_bootstrap/package/.factory-v3/`

## Files
| Path | Purpose |
| --- | --- |
| `README.md` | Target-project operating guide. |
| `canons/POC_VISION.md` | Product and operational proof vision. |
| `canons/POC_CONSTRAINTS.md` | Scope, authority, data, deployment, and dependency constraints. |
| `canons/POC_VERIFICATION.md` | Project verification plan and evidence expectations. |
| `canons/DEPENDENCY_RESEARCH.md` | Garmin and Hermes research decision record. |
| `canons/ADAPTIVE_MISSION_CONTROL.md` | Checkpoint, human-interrupt, plan-delta, and reentry rules for larger missions. |
| `missions/MISSION_001_START_HERE.md` | First V3-only mission envelope template. |
| `templates/V3_POC_MISSION_TEMPLATE.md` | Reusable mission template for later missions. |
| `templates/V3_POC_CLOSEOUT_TEMPLATE.md` | Closeout template for V3-only POC missions. |
| `templates/V3_POC_MISSION_RECORD_TEMPLATE.json` | Structured mission record template. |
| `templates/V3_HUMAN_DECISION_INTERRUPT_TEMPLATE.json` | Structured human decision interrupt record. |
| `templates/V3_MISSION_CHECKPOINT_TEMPLATE.md` | Checkpoint template for longer missions. |
| `templates/V3_MISSION_STATE_TEMPLATE.md` | Authored mission-state template for reentry. |
| `templates/V3_MISSION_PLAN_DELTA_TEMPLATE.md` | Plan-delta template for human-approved mission changes. |
| `evals/V3_POC_EVAL_RUBRIC.md` | Pass/fail rubric for the operational POC. |
| `evals/V3_POC_EVAL_RECORD_TEMPLATE.json` | Structured eval result template. |

## Standalone Boundary
The package is intentionally independent from Factory V2. It has no dependency on:
- `factoryctl`,
- V2 stage-lint,
- V2 pack-lint,
- V2 planning stages,
- V2 fallback execution.

## Current Limitations
- Evals are rubric-based and structured-record based; they are not yet automated gates.
- The first target deployment remains private/internal until a POC brief names the exact target.
- Garmin and Hermes are research inputs only until separately approved.
