# Fixture Inventory - Advisory Record Shape

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage G fixture plan.

| Path | Expected purpose |
| --- | --- |
| `fixture_evidence_integrity_optional.json` | Rich valid completed record with original/replay observations, deterministic-only verifier, hash-match/visual-fail evidence, and bounded change-range claim |
| `invalid/evidence_observation_supersedes_original.json` | MR081 |
| `invalid/verifier_same_actor_claims_independent.json` | MR082 |
| `invalid/boundary_proved_without_limit.json` | MR084 |
| `invalid/completed_with_placeholder_commit.json` | MR085 |

MR083 is covered by validator shape assertions and the rich valid fixture; no sixth product fixture is authorized. If implementation cannot cover malformed visual structure without a sixth fixture, halt for scope review rather than silently expanding.
