# V3-CODEX-DL-001 Execution Closeout

## Status

`READY`

Research-only, advisory, and non-enforcing code-only mission closeout.

The implementation matches the approved challenged contract. It generates
deterministic JSON text only and does not open a link, create or message a task,
start Codex, run a worker, use a clipboard, add a dependency, modify Same
Second, or introduce runtime-control power.

## Approval And Contract

- Sponsor approval: “Approve V3-CODEX-DL-001 for code-only implementation under
  the challenged contract.”
- Formation:
  `CODEX_DEEPLINK_ASSIST_FORMATION_20260716.md`
- Formation SHA-256:
  `357b6645799921a2a71ba112d1ab78266de42922a572b92e17a50f262514e5b1`
- Challenge:
  `CODEX_DEEPLINK_ASSIST_CHALLENGE_20260716.md`
- Challenge SHA-256:
  `bff5cdd08748f836ef48fc511ac9a183bfdb77fc2c7adf7795cc44e861979723`
- Repository `commit_before`:
  `5a271bc264eed4ddaa0b1aea0c3d813d5fe19d73`
- Repository `commit_after_at_mission_closeout`: unchanged at the same commit;
  the full attended pilot, discovery, formation, implementation, and closeout
  chain was honestly uncommitted at that observation. A later Factory
  integration commit does not rewrite this original closeout state.

## Implemented Files

- `scripts/factory_v3_codex_deeplink.py`
- `tests/test_factory_v3_codex_deeplink.py`
- `tests/fixtures/factory_v3_codex_deeplink/`
- `docs/Factory/v3/CODEX_DEEPLINK_ASSIST.md`
- this closeout artifact
- active canon references needed to record mission status

No unapproved package, abstraction, transport, product, or runtime file was
added.

## Contract Alignment

- Stdlib only: `argparse`, `hashlib`, `json`, `pathlib`, `sys`, `typing`, and
  `urllib.parse`.
- Prompt is file-only; inline and stdin prompt modes do not exist.
- Workspace must be absolute, existing, a directory, and strictly resolved.
- Prompt must be a regular file, non-empty UTF-8, NUL-free, and at most 8,192
  bytes; reading is bounded at 8,193 bytes.
- Pure encoder fixtures use a fixed synthetic absolute path; CLI path checks use
  temporary directories.
- Parameter order is `path`, then `prompt`; spaces encode as `%20`.
- JSON is sorted, indented, newline-terminated, and explicit about human Send
  and absent transport proof.
- Invalid inputs return deterministic JSON and exit `2`.
- No link opener, clipboard, GUI, browser, subprocess, network, socket, Codex
  CLI, SDK, MCP, scheduler, or background path exists.

## Verification

Focused original observation:

- `python3 -m unittest tests.test_factory_v3_codex_deeplink`
  - result: 8 tests passed
- `python3 -m py_compile scripts/factory_v3_codex_deeplink.py`
  - result: pass
- fixture JSON parsing
  - result: pass
- `git diff --check`
  - result: pass

Full replay observation:

- `python3 -m unittest discover -s tests`
  - result: 35 tests passed
- `bash scripts/knowledge_lint.sh`
  - result: pass; 56 checked files and 2 existing active pitfalls
- `./scripts/factoryctl context-index`
  - result: pass; 1,590 sources, 16,990 chunks, and 2,404 facts
- V3 docs advisory lint
  - result: `ADVISORY_PASS`, zero findings/warnings
- V3 operational-readiness evaluation
  - result: `ADVISORY_PASS`, zero findings/warnings
- opt-in natural-language pilot
  - result: four historical non-blocking findings in
    `LOOP_TERMINAL_STATES_AND_SAFE_HOLD.md` and
    `MISSION_CONTROL_CONTRACT.md`; no finding against the new helper artifacts
- mission-record docs lint
  - result: `ADVISORY_PASS`, zero findings/warnings
- telemetry, loop-contract, mission-control, and serial-graph validators with
  pinned expected outputs
  - result: all exact expectation comparisons passed
- serial mission-state template status
  - result: `advisory_pass`
- `python3 -m py_compile scripts/factory_v3_*.py`
  - result: pass
- helper fixture JSON parsing
  - result: pass
- static forbidden-effect token scan over the helper source
  - result: pass
- `git diff --check`
  - result: pass
- Same Second no-touch check
  - result: clean at
    `20554125a422f0fc0afeadf18948b4c8e649a732`

## Provenance And Independence

The same Codex task implemented the helper, authored the focused tests, and ran
verification. This is not independent builder/verifier separation. Pinned
fixtures and full-suite replay provide deterministic separation only.

No live desktop or fresh-worker actor participated. No link was generated for a
real workspace, opened, or sent.

## FP/FN And Authoring Observations

- The challenge caught a likely cross-machine fixture false negative before
  implementation: pinning `Path.resolve()` from the checkout would have embedded
  a user-specific path. The repaired pure-encoder fixture uses a fixed synthetic
  absolute path while CLI tests cover real resolution.
- Static forbidden-token checks are useful negative evidence but cannot prove
  the absence of every possible external-effect mechanism. Manual source review
  and the deliberately small import set narrow that gap.
- Deterministic fixtures cannot detect installed-desktop rejection, composer
  transformation, URL logging, or user edits because no live probe is approved.

## Residual Risks

- The generated URL contains the complete prompt and is unsuitable for secrets.
- The 8,192-byte policy is not live compatibility evidence.
- A path can change after generation and before a human opens the link.
- The input digest does not prove composer or sent text.
- The desktop may reject or transform a syntactically correct link.
- Same-actor verification limits remain.

## Next Gate

The next decision is separate formation/challenge of an attended,
synthetic-data-only live-link trial. It must name the exact workspace, prompt,
observation method, no-tool/no-write worker boundary, and safe-hold rules.

This implementation does not authorize that trial, opening a link, creating a
task, worker execution, CLI repair, SDK/MCP use, dependencies, credentials,
Same Second changes, push, merge, deployment, or adapter implementation.
