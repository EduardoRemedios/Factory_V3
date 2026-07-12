# Verification Cases

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Initial verification case set.

## Direct-Source Recall Cases
- Unrepaired generated `WEAK` report: reject.
- Valid local direct-source repair with summaries and no material unresolved refs: accept.
- Missing local source: reject.
- Source outside repository: reject.
- Material unresolved refs remain: reject.
- Strong generated report without repair: preserve existing acceptance.

## Endurance Canon Cases
- Mission completes in two hours with all requirements proved: mission PASS; upper-envelope coverage remains partial.
- Mission naturally runs close to four hours with stable objective, authority, checkpoints, verification, and evidence: candidate endurance evidence, not automatic promotion.
- Mission continues after all success criteria pass solely to reach a duration or call target: reject as padding.
- Late-run verification or evidence quality declines: safe-hold, halt, or ask according to the envelope; do not normalize the drift.
- Historical run failed under an earlier pre-written duration criterion: preserve the record and explain the current interpretation in active canon.
