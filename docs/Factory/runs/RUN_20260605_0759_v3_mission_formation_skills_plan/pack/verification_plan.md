# Verification Plan - V3 Mission Formation Skills Plan

## Version
v0.1

## Change Log
- v0.1 (2026-06-05): Initial Stage F verification plan.

## Verification Strategy
This is a planning-only pack. Verification is primarily artifact review plus repository advisory checks.

## Required Checks
| ID | Tier | Check | Evidence |
| --- | --- | --- | --- |
| V0-A1 | V0 | Review future envelope for explicit no skill implementation in this run. | Envelope |
| V0-A2 | V0 | Review candidate-only and human Go language. | Intent; envelope |
| V0-A3 | V0 | Confirm SDK/MCP orchestration is deferred. | Intent; roadmap; envelope |
| V0-A4 | V0 | Confirm trial matrix includes more-discovery, V2/heavier-planning fallback, and bounded candidate V3 route. | Micro-sprints; traceability |
| V0-A5 | V0 | Confirm V2 fallback and non-deprecation language remain explicit. | Intent; risk register |
| V1-A6 | V1 | Run stage-lint for every stage. | Command output |
| V1-A7 | V1 | Run pack-lint after I2. | Command output |
| V1-A8 | V1 | Run V3 advisory lint after roadmap/direction edits. | Command output |

## Future Implementation Verification
The future implementation run should add checks that:
- both `SKILL.md` files exist and include required frontmatter,
- descriptions define trigger and non-trigger behavior,
- instructions prohibit code edits and execution authority,
- trial records exist for all three trial classes,
- V3 advisory lint passes.
