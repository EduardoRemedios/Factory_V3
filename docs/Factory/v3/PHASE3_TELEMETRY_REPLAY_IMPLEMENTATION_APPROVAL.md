# Factory v3 Phase 3 Telemetry Replay Implementation Approval

## Version
v0.1

## Change Log
- v0.1 (2026-05-26): Initial fixture-first implementation approval.

## Status
Approved for the next fixture-first advisory implementation step only.

This approval is research-only and non-enforcing. It does not approve real mission telemetry collection, required gates, CI wiring, `factoryctl` integration, runtime authority, proof, lease enforcement, governance routing, default-mode behavior, V3 promotion, or V2 build-support removal.

## Decision Metadata
- Decision: APPROVE_FIXTURE_FIRST_ADVISORY_REPLAY_IMPLEMENTATION
- Date: 2026-05-26
- Scope: `V3-OP-001` telemetry/replay fixtures and standalone advisory replay validator
- Human owner: Eduardo Remedios
- Required-gate integration approved: NO
- Real mission telemetry collection approved: NO
- Runtime authority approved: NO
- V3 default-mode promotion approved: NO
- V2 scaffolding removal approved: NO

## Approved Future Files
The next implementation step may touch only:

- `scripts/factory_v3_telemetry_replay_lint.py`
- `tests/fixtures/factory_v3_telemetry_replay/**`
- `docs/Factory/v3/PHASE3_TELEMETRY_REPLAY_IMPLEMENTATION_STATUS.md`
- `docs/Factory/v3/README.md`
- `docs/Factory/v3/ROADMAP_TO_FULL_VISION.md`
- `docs/ROADMAP.md`
- `CHANGELOG.md`
- `docs/CHANGELOG.md`
- a new V2 run pack under `docs/Factory/runs/`

Any additional file requires a new approval or an explicit scope update before implementation.

## Approved Fixture Corpus

### Valid Fixtures
- happy-path bounded code change,
- verification halt,
- pre-envelope fallback,
- stale reentry check,
- human clarification before execution.

### Invalid Fixtures
- non-monotonic sequence,
- command outside declared authority,
- file outside authorized scope,
- execution appears after a verification halt without a human decision,
- event after terminal closeout,
- excluded-data marker present.

Fixtures must use synthetic values. They must not contain secrets, full transcripts, chain-of-thought, real command logs, source file contents, or private vendor cognition state.

## Approved Advisory Validator Behavior
The future script may:

- read one JSONL file or a directory of JSONL fixtures,
- parse one event per line,
- emit deterministic JSON with `blocking_effect: none`,
- support `--json`,
- support `--expect` for deterministic fixture checks,
- report advisory statuses only:
  - `ADVISORY_PASS`,
  - `ADVISORY_WARN`,
  - `ADVISORY_FAIL_NON_BLOCKING`,
- check event sequence ordering,
- check mission and record identifier consistency when fixture metadata is present,
- check authority appears before command or file-change events,
- check commands against declared authority,
- check file paths against declared authority,
- check verification-halt sequence behavior,
- check terminal closeout ordering,
- check excluded-data marker absence.

The future script must not:

- execute commands,
- inspect git history,
- read source file contents,
- upload data,
- integrate with CI or `factoryctl`,
- create runtime authority or proof,
- block repository operations.

## Expected Output Shape
The future report should include:

- `report_id`,
- `status`,
- `blocking_effect`,
- `target`,
- `checked_logs`,
- `findings`,
- `warnings`,
- `generated_at`,
- `recommended_next_steps`.

`generated_at` should remain deterministic for fixture tests, using `not_recorded` unless a later pack approves timestamp behavior.

## Verification Commands For Future Implementation
- `python3 -m json.tool` on changed JSON fixture files.
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --json`
- `python3 scripts/factory_v3_telemetry_replay_lint.py --target tests/fixtures/factory_v3_telemetry_replay --expect tests/fixtures/factory_v3_telemetry_replay/expected/all.json --json`
- `python3 -m py_compile scripts/factory_v3_telemetry_replay_lint.py`
- `python3 scripts/factory_v3_advisory_lint.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --json`
- `python3 scripts/factory_v3_operational_readiness_eval.py --target docs/Factory/v3 --nl-pilot --json`
- `git diff --check`

## Non-Authority Rule
The validator output is evidence only. It does not replace the mission record, V2 run packs, human decisions, git history, or any project-owned source of truth.

## Stop Conditions For Future Implementation
Stop before implementation if the work requires:

- real mission telemetry capture,
- CI or required-gate integration,
- `factoryctl` integration,
- telemetry storage outside fixtures,
- external governance-kernel adapters,
- proof or lease enforcement,
- broader harness capability profiling,
- governance routing.

## Next Step
Implement the approved fixture-first advisory replay validator in a separate execution step.

That implementation must stay within the approved files and verification commands above.
