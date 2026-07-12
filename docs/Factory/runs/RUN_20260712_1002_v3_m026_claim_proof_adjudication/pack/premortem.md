# Premortem - Mission 026 Claim Audit

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E premortem.

## Failure Scenarios
1. Replay passes and is misreported as preserved original output. Mitigation: separate source summary from replay result in every claim row.
2. Self-attested boundary flags become proof. Mitigation: require diff/code/test corroboration or grade `WEAK`.
3. Same-worker QA is called independent verification. Mitigation: record actor-independence limitation explicitly.
4. Screenshot hashes match but UI claims are never inspected. Mitigation: hash plus visual review on desktop and mobile.
5. POC source is modified during replay. Mitigation: clone to a unique `/tmp` path and never run write commands in source POC.
6. Stale `commit_after` is overlooked. Mitigation: mandatory contradiction claim and FN review item.
7. Mission PASS is confused with four-hour proof. Mitigation: separate observed exposure from upper-envelope coverage in audit and adjudication.
8. Positive evidence wording implies promotion. Mitigation: same-paragraph `NO PROMOTION YET` review and advisory evals.
9. Existing uncommitted Factory changes are accidentally reversed. Mitigation: changed-path review against the approved cumulative working-tree baseline.

## Stop Conditions
- Exact commit unavailable.
- Replay requires dependency installation or POC source mutation.
- Screenshot identity cannot be established.
- A material claim cannot be graded without inventing evidence.
- Active-canon update would exceed the nine-file budget or weaken boundaries.
