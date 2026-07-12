# Premortem - Mission Re-entry Proof Pack

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage E premortem.

## Failure Scenarios
1. The validator accepts stale repository state with `continue` because it checks shape but not semantic combinations.
   - Mitigation: direct scenario-specific semantic checks and isolated invalid fixture.
2. Recovery authority silently becomes permission to resume implementation broadly.
   - Mitigation: only `verify` is permitted after failed verification; require one action and authority basis.
3. Existing mission-control contracts fail because the new case list is treated as required.
   - Mitigation: absent list is a no-op and old direct fixture output is checked before/after.
4. Scenario inputs are described as operational proof of a real fresh session.
   - Mitigation: bounded-claim language in canon, trial plan, closeout, and boundary claims.
5. Expected-output regeneration hides historical drift.
   - Mitigation: save baseline, filter five new paths, compare old subset before installing expected output.
6. Four invalid fixtures produce multiple findings and obscure semantics.
   - Mitigation: mutate one condition per fixture and assert exact finding-ID set.
7. Canon updates imply profile promotion or runtime authority.
   - Mitigation: pointer-only updates, `NO PROMOTION YET` in promotion-sensitive paragraphs, advisory lint.
8. A generic scenario engine or dependency is introduced.
   - Mitigation: SIMPLE-CODE-GATE, direct helper near `_check_fixture_scenarios`, dependency/no-touch checks.

## Overall Judgment
The slice is low runtime risk but medium governance-integrity risk. Fixture-first implementation and historical subset comparison are mandatory.
