# Factory V3 Loop Contract Fixtures

These fixtures exercise the research-only advisory loop-contract validator:

```bash
python3 scripts/factory_v3_loop_contract_lint.py --target tests/fixtures/factory_v3_loop_contract --json
```

The validator emits `blocking_effect: none` and is not wired into `factoryctl`, CI, merge preflight, or required Factory gates.

Fixture intent:

- `valid_loop_contract.json` covers the minimum complete advisory loop contract.
- `valid_rich_scenarios.json` covers paper-derived scenario fixtures for memory/re-entry, tool use, act-or-ask, and feature-work verification.
- `invalid/missing_state_policy.json` covers missing memory/state governance.
- `invalid/missing_tool_authority.json` covers missing tool-use authority and evidence.
- `invalid/ambiguous_no_safe_hold.json` covers BLIND-ACT-style act/ask and safe-hold gaps.
- `invalid/unsafe_approval_scope.json` covers accidental approval or runtime-authority laundering.
- `invalid/stale_reentry_gap.json` covers missing stale-reentry safeguards.
- `invalid/missing_terminal_states.json` covers incomplete terminal-state vocabulary.
- `invalid/stale_memory_allows_reentry.json` covers stale memory that incorrectly allows direct re-entry.
- `invalid/contradictory_memory_missing_evidence.json` covers contradictory state without source evidence.
- `invalid/invalidated_branch_no_safe_hold.json` covers invalidated branch state without safe-hold.
- `invalid/wrong_tool_no_evidence.json` covers wrong-tool selection without tool evidence.
- `invalid/omitted_tool_no_rationale.json` covers omitted-tool cases without rationale.
- `invalid/tool_failure_no_safe_hold.json` covers tool failure without safe-hold.
- `invalid/blind_action_not_checked.json` covers a BLIND-ACT-style scenario that was not checked before action.
- `invalid/feature_work_no_staged_evidence.json` covers feature-work verification without staged proof, regression evidence, claim-to-proof, or independent review.
