# Intent Red Team - Recall Sync And Endurance Canon

## Version
v0.1

## Change Log
- v0.1 (2026-07-12): Stage B review, iteration 1 of 2.

Iteration: 1 of max 2

## Findings

### High H1 - Combined slices could contaminate ownership boundaries
- Why it matters: V2 validator behavior and V3 promotion-sensitive wording have different owners and failure modes.
- Recommended fix: enforce separate micro-sprints and require the V2 sync to pass before any V3 canon edit begins.

### High H2 - Correcting the duration floor could accidentally weaken the capability criterion
- Why it matters: removing a four-hour pass floor must not become an unsupported claim that four-hour endurance is already proven.
- Recommended fix: distinguish mission PASS from endurance-evidence coverage and retain `NO PROMOTION YET` until quality continuity near the upper envelope is evidenced and approved.

### High H3 - Blind upstream copying could import unrelated starter-kit changes
- Why it matters: upstream files have evolved independently after the repository split.
- Recommended fix: transfer only behavior attributable to commit `06646d7`; manually preserve local V2 build-support and V3-boundary language.

### High H4 - Repair validation could accept ceremonial evidence
- Why it matters: a token repair section without existing local files, source summaries, or materiality closure would weaken Stage A.
- Recommended fix: require focused tests for unrepaired weak, valid repair, missing source, outside-repo source, and material unresolved refs; run the full suite.

### Medium M1 - Historical ladder reports may be rewritten as though prior adjudications never occurred
- Why it matters: historical failures are evidence about earlier criteria and must remain auditable.
- Recommended fix: update active summaries and add explicit reinterpretation notes; do not alter immutable run evidence or prior human decision records.

### Medium M2 - “Four hours” remains underspecified
- Why it matters: elapsed time alone does not measure continuity quality.
- Recommended fix: define evidence dimensions including requirement coverage, late-run verification quality, objective/scope drift, checkpoint integrity, stale-state handling, and safe stop behavior.

### Medium M3 - Current next-step cleanup could expand into broad editorial refactoring
- Why it matters: the canon is large and repeated; broad rewriting increases contradiction risk.
- Recommended fix: limit edits to active status, current queue, current assessment, remaining gates, version pointers, and changelog entries directly affected by this run.

## Agent Failure Modes
- Treat a valid shorter mission as failed because it did not consume enough time or calls.
- Continue work after success to manufacture duration evidence.
- Claim upper-envelope endurance from shorter runs alone.
- Accept a handwritten weak recall repair without direct-source validation.
- Replace local files wholesale and erase V3 repository-specific boundary wording.

## Verification Holes To Close
- Exact upstream commit attribution for transferred behavior.
- Negative test for a direct source outside the repository.
- Search-based review for remaining active “duration floor,” “must run four hours,” and completed-work-as-next-gate wording.
- Independent comparison between early-run and late-run quality criteria in active canon.

## Verdict
CONDITIONAL PASS to Stage C after H1-H4 are bound into acceptance criteria, sequencing, and verification.
