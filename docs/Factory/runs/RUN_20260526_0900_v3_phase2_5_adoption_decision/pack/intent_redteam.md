# Intent Red Team

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Red-team review of the Phase 2.5 adoption intent.

## Findings

| ID | Severity | Finding | Treatment |
|---|---|---|---|
| R1 | High | Optional shadow use could be misread as required-gate promotion. | Decision must say non-blocking and no required gates. |
| R2 | Medium | Backfilled records are weaker than records authored during missions. | Decision must name this residual risk. |
| R3 | Medium | Starting telemetry too soon could overbuild. | Decision must limit Phase 3 to planning until separately approved. |

## Verification Holes
- Need validator proof against `docs/Factory/v3/mission_records`.
- Need V3 advisory lint proof against the docs after edits.
