# Ladder Design Review Round 2 — Review And Adopted Path (HDI-RUNG2-007)

## Status
Research-only and non-enforcing design review and sponsor-decision record, mandated by the third rung-2 duration failure (`HDI-RUNG2-006`) and executed under mission `LADDER_DESIGN_REVIEW2_20260611`. The sponsor's path direction arrived in-thread together with the GO, so this document both reviews and records the adopted path. It approves no rung execution: the attempt-4 envelope requires its own scope-sufficiency derivation, pre-flight with browser-availability verification, and explicit sponsor Go.

## Record
- Decision ID: `HDI-RUNG2-007`
- Recording mission: `LADDER_DESIGN_REVIEW2_20260611`
- Decision tier: 3 (rung-class path after repeated duration failures is a sponsor roadmap decision; named open in `HDI-RUNG2-006`)
- Raised at: 2026-06-11, at the `HDI-RUNG2-006` recording-mission closeout in the Claude Code session thread (options presented: Option A-final, Option B, hybrid)
- Answered at: 2026-06-11, in-thread, together with the GO for this review
- Transport: in-session thread (sponsor attending); no notification surface used

## Verbatim Sponsor Answer
"GO and then lets try option A and based on what we see we could do another one using the hybrid approach, we might learn something"

## Decision
**Option A-final adopted**: rung-2 attempt 4 at roughly 2x Mission 023's deliverable scope (~27 build waypoints) with browser tooling enabled and verified at pre-flight. **The hybrid is the named contingent follow-on either way**: based on what attempt 4 shows, a subsequent duration mission may be drafted as a rung-3-class contract (mission-formation skill + challenge-skill red-team, the `V3-ANCHOR-005` trial), explicitly for learning value. Option B (demoting wall-clock to an observation) is not adopted but remains available to the sponsor at any future review.

## Three-Point Calibration Evidence

| Quantity | Mission 021 | Mission 022 | Mission 023 | Verdict |
| --- | --- | --- | --- | --- |
| Observed calls | 150 | 160 | ~333 | scope-driven |
| Active duration | 24m11s | 40m06s | 54m03s | rising with scope, still under floor |
| Working throughput | ~6.2 calls/min | ~5.7-6.2 calls/min | ~6.2 calls/min | CALIBRATED (stable) |
| Build waypoints | ~4 | 5 | 16 | — |
| Total calls per build waypoint | — | ~32 | ~21 | NON-STATIONARY (falls as the codebase matures) |
| Governance share | ~56% | ~56% | ~50% | amortizes slowly with scale |
| Mechanics criteria | 7/8 | 8/8 | clean | improving |
| Browser QA | n/a | real (found a defect) | unavailable (harness) | duration-relevant harness state |

## Diagnosis (Round 2)
Round 1's diagnosis (envelope-design failure, fix by bottom-up sizing) was half right: throughput was successfully calibrated, but the per-waypoint cost coefficient is non-stationary — each mission leaves the codebase with more reusable patterns, so the next mission's deliverables get cheaper. Duration-by-scope therefore chases a receding target. Two additional facts from Mission 023 change the round-2 arithmetic:

1. **Missing browser workload** (sponsor-named, `HDI-RUNG2-006` F2): browser QA was unavailable in the session, removing genuine verification work that in Mission 022 had found a real defect. Restoring it adds honest calls and minutes; the sponsor confirms the plugin can be enabled at Codex session start, so pre-flight availability verification becomes a Go-blocking check.
2. **Governance amortizes**: the governance ratio fell from ~1.29:1 to ~0.98:1 at 3.5x scope, so added scope converts to duration at close to its objective cost — larger scope is a more honest duration lever than it was at small scale.

## Adopted Attempt-4 Class (applied to `DURATION_LADDER_PLAN.md` v0.9)
Recalibrated coefficients (source: Mission 023 actuals, replacing the Mission 021/022-derived values per the sizing rule's own update requirement): ~21 total calls per build waypoint; ~50% governance share; ~6.2 calls/min working throughput; ~16.5 calls per evidence artifact.

- Scope: ~27 build waypoints (roughly 2x Mission 023's 16), of which ~3 are dedicated browser-QA waypoints restoring the missing workload; ~31-34 waypoints total.
- Bottom-up forecast: 27 x ~21 ≈ 567 build calls, plus discovery 25-45, decision/pause 25-45, verification 60-100, closeout 40-70 → **forecast band ~700-1050 calls ≈ 113-170 minutes** at calibrated throughput.
- Budget floor 540 and wall-clock band 90-180 min unchanged as criteria; stop threshold 1300 (sits above the 180-min ceiling of ~1116 calls, margin noted as thinner than round 1's 20% target — acceptable because the stop threshold is a safety rail, not a target).
- Pre-flight additions (Go-blocking): browser-tool availability verified and recorded as harness state alongside model identity and speed/effort entry; transport delivery test as before.
- Honest risk statement: if the per-waypoint coefficient falls again (to ~15), attempt 4 lands near ~560 calls ≈ 90 minutes — at the floor, not comfortably above it. A further fall below that compresses attempt 4 despite everything; in that case the contingent hybrid below is the named next move, not a fifth scope inflation.

## Named Contingent Follow-On: The Hybrid
Per the sponsor's direction, after attempt 4 closes (pass or fail), the lane may run a duration mission drafted as a **rung-3-class contract**: scope formed with the mission-formation skill, red-teamed with the challenge skill (both non-executing — the named `V3-ANCHOR-005` live trial), natural interrupts, 200-300 min band. If attempt 4 passes, this is simply rung 3 proceeding. If attempt 4 compresses again, the hybrid absorbs the duration burden into the rung-3 contract and the rung-2 wall-clock criterion is re-presented to the sponsor for an Option B decision with four calibration points. Either way it requires its own envelope and explicit sponsor Go; nothing here approves it.

## Consequences
- `DURATION_LADDER_PLAN.md` v0.9 carries the attempt-4 class and recalibrated coefficients (this mission); failure handling unchanged.
- The attempt-4 envelope (POC Mission 024) is the next named gate: drafted with the scope-sufficiency derivation shown, browser pre-flight verification, interrupt field set v2, one live phone interrupt, one deliberate pause/reentry; then sponsor Go.
- Rung 3 remains locked; pre-written pack criteria unamended; assessment stays `NO PROMOTION YET`.

## Evidence Pointers
- `../rung2/RUNG2_ADJUDICATION_HDI_RUNG2_002.md`; `../rung2/RUNG2_RERUN_ADJUDICATION_HDI_RUNG2_004.md`; `../rung2/RUNG2_ATTEMPT3_ADJUDICATION_HDI_RUNG2_006.md` (including the F1 calibration verdict and F2 browser finding).
- `LADDER_DESIGN_REVIEW_20260611.md` and `LADDER_DESIGN_ADOPTION_HDI_RUNG2_005.md` (round 1).
- POC repo: Mission 021/022/023 closeouts and records (commits `a5c2c9a`..`63a0a99`, `e043b37`..`9d0c463`, `a301cb3`..`28e06b6`).
