from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import factory_v3_serial_mission_state as kernel  # noqa: E402


GRAPH_PATH = REPO_ROOT / "tests/fixtures/factory_v3_serial_mission_graph/valid_serial_graph.json"
EXPECTED_PATH = REPO_ROOT / "tests/fixtures/factory_v3_serial_mission_state/expected/lifecycle_summary.json"


class SerialMissionStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        self.state = kernel.initialize_state(self.graph, GRAPH_PATH.relative_to(REPO_ROOT).as_posix(), "git:fixture-head")
        self.events = [kernel.initial_event(self.state, "builder", "2026-07-12T00:00:00Z", "approved fixture mission")]
        self.tick = 1

    def transition(self, name: str, child_id: str | None = None, refs: list[str] | None = None, repo: str | None = None, **data: object) -> None:
        new, event = kernel.apply_transition(
            self.state,
            self.graph,
            name,
            expected_revision=self.state["revision"],
            actor_ref="builder",
            timestamp=f"2026-07-12T00:00:{self.tick:02d}Z",
            authority_basis="approved fixture mission",
            child_id=child_id,
            evidence_refs=refs,
            repository_state_ref=repo,
            data=data,
        )
        self.tick += 1
        self.state = new
        self.events.append(event)

    def activate(self, child_id: str) -> None:
        self.transition("activate_child", child_id)

    def pass_child(self, child_id: str) -> None:
        self.transition("mark_verification_pending", child_id)
        self.transition("record_verification_result", child_id, [f"evidence/{child_id}.json"], result="pass", evidence_status="PROVED", unresolved_gap="")
        self.transition("complete_child", child_id, repo="git:fixture-head")

    def complete_all(self) -> None:
        for child_id in ("feature-a", "feature-b", "feature-c"):
            self.activate(child_id)
            self.pass_child(child_id)

    def test_clean_three_child_serial_lifecycle_matches_pinned_summary(self) -> None:
        self.activate("feature-a")
        self.transition("checkpoint", "feature-a", ["evidence/cp-a.json"], "git:fixture-head", checkpoint_id="CP-A")
        self.pass_child("feature-a")
        for child_id in ("feature-b", "feature-c"):
            self.activate(child_id)
            self.pass_child(child_id)
        self.transition("record_parent_verification", refs=["evidence/parent.json"], result="pass", evidence_status="PROVED", unresolved_gap="")
        self.transition("close_parent")
        derived = kernel.derive(self.state, self.graph)
        summary = {
            "eligible_children": derived["eligible_children"],
            "event_sequence": self.state["event_sequence"],
            "one_safe_next_action": derived["one_safe_next_action"],
            "parent_closeout_eligible": derived["parent_closeout_eligible"],
            "parent_status": self.state["parent_status"],
            "revision": self.state["revision"],
            "statuses": {child["child_id"]: child["status"] for child in self.state["children"]},
        }
        self.assertEqual(summary, json.loads(EXPECTED_PATH.read_text(encoding="utf-8")))
        kernel.validate_events(self.events, self.state)

    def test_dependency_order_is_enforced(self) -> None:
        before = copy.deepcopy(self.state)
        with self.assertRaisesRegex(kernel.StateError, "incomplete dependencies"):
            self.activate("feature-b")
        self.assertEqual(self.state, before)

    def test_duplicate_activation_is_rejected(self) -> None:
        self.activate("feature-a")
        with self.assertRaises(kernel.StateError) as caught:
            self.activate("feature-b")
        self.assertEqual(caught.exception.code, "duplicate_activation")

    def test_multiple_start_authorizations_are_malformed(self) -> None:
        self.state["children"][0]["start_authorized"] = True
        self.state["children"][1]["start_authorized"] = True
        with self.assertRaises(kernel.StateError) as caught:
            kernel.validate_state(self.state, self.graph)
        self.assertEqual(caught.exception.code, "serial_violation")

    def test_stale_expected_revision_does_not_mutate(self) -> None:
        before = copy.deepcopy(self.state)
        with self.assertRaises(kernel.StateError) as caught:
            kernel.apply_transition(self.state, self.graph, "activate_child", expected_revision=9, actor_ref="builder", timestamp="2026-07-12T00:00:01Z", authority_basis="approval", child_id="feature-a")
        self.assertEqual(caught.exception.code, "stale_revision")
        self.assertEqual(self.state, before)

    def test_unknown_mission_child_and_changed_graph_are_rejected(self) -> None:
        before = copy.deepcopy(self.state)
        with self.assertRaises(kernel.StateError) as caught:
            kernel.apply_transition(self.state, self.graph, "activate_child", expected_revision=0, actor_ref="builder", timestamp="2026-07-12T00:00:01Z", authority_basis="approval", child_id="unknown")
        self.assertEqual(caught.exception.code, "unknown_child")
        changed = copy.deepcopy(self.graph)
        changed["children"][0]["authority"]["authorized_paths"] = ["outside/authority"]
        with self.assertRaises(kernel.StateError):
            kernel.validate_state(self.state, changed)
        self.assertEqual(self.state, before)

    def test_failed_verification_enters_safe_hold_and_cannot_complete(self) -> None:
        self.activate("feature-a")
        self.transition("mark_verification_pending", "feature-a")
        self.transition("record_verification_result", "feature-a", ["evidence/fail.txt"], result="fail", evidence_status="CONTRADICTED", unresolved_gap="Tests failed.")
        self.assertEqual(self.state["parent_status"], "safe_hold")
        before = copy.deepcopy(self.state)
        with self.assertRaises(kernel.StateError):
            self.transition("complete_child", "feature-a")
        self.assertEqual(self.state, before)

    def test_explicit_safe_hold_and_bounded_resume(self) -> None:
        self.activate("feature-a")
        self.transition("enter_safe_hold", "feature-a", reason="Repository review needed.", open_decision="Confirm current state.")
        self.transition("resume", "feature-a", repo="git:fixture-head", state_source="authored_state", next_safe_action="Checkpoint feature-a.")
        self.assertEqual(self.state["parent_status"], "active")
        self.assertEqual(self.state["children"][0]["status"], "active")

    def test_session_memory_only_resume_is_rejected_without_mutation(self) -> None:
        self.activate("feature-a")
        self.transition("enter_safe_hold", "feature-a", reason="Pause.")
        before = copy.deepcopy(self.state)
        with self.assertRaises(kernel.StateError) as caught:
            self.transition("resume", "feature-a", repo="git:fixture-head", state_source="session_memory", next_safe_action="Continue.")
        self.assertEqual(caught.exception.code, "session_memory_rejected")
        self.assertEqual(self.state, before)

    def test_parent_closeout_too_early_is_rejected(self) -> None:
        before = copy.deepcopy(self.state)
        with self.assertRaises(kernel.StateError) as caught:
            self.transition("close_parent")
        self.assertEqual(caught.exception.code, "parent_closeout_too_early")
        self.assertEqual(self.state, before)

    def test_parent_closeout_after_evidence_passes(self) -> None:
        self.complete_all()
        self.transition("record_parent_verification", refs=["evidence/parent.json"], result="pass", evidence_status="PROVED", unresolved_gap="")
        self.transition("close_parent")
        self.assertTrue(kernel.derive(self.state, self.graph)["parent_closeout_eligible"])
        self.assertEqual(self.state["parent_status"], "completed")

    def test_event_state_revision_divergence_is_rejected(self) -> None:
        self.activate("feature-a")
        divergent = copy.deepcopy(self.events)
        divergent[-1]["resulting_state_revision"] = 8
        with self.assertRaises(kernel.StateError) as caught:
            kernel.validate_events(divergent, self.state)
        self.assertEqual(caught.exception.code, "event_state_divergence")

    def test_malformed_state_and_event_are_rejected(self) -> None:
        malformed = copy.deepcopy(self.state)
        del malformed["revision"]
        with self.assertRaises(kernel.StateError):
            kernel.validate_state(malformed, self.graph)
        with self.assertRaises(kernel.StateError):
            kernel.validate_events([{"bad": True}], self.state)

    def test_status_derivation_is_deterministic(self) -> None:
        first = kernel.derive(self.state, self.graph)
        second = kernel.derive(copy.deepcopy(self.state), copy.deepcopy(self.graph))
        self.assertEqual(first, second)
        self.assertEqual(first["eligible_children"], ["feature-a"])
        self.assertFalse(first["derived_cursors_grant_authority"])

    def test_cli_rejection_does_not_change_state_or_events(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            graph_path = temp / "graph.json"
            state_path = temp / "state.json"
            events_path = temp / "events.jsonl"
            graph_path.write_text(json.dumps(self.graph), encoding="utf-8")
            base = [sys.executable, str(SCRIPTS_DIR / "factory_v3_serial_mission_state.py")]
            init = subprocess.run(base + ["init", "--graph", str(graph_path), "--state", str(state_path), "--events", str(events_path), "--repository-state-ref", "git:fixture-head", "--actor-ref", "builder", "--timestamp", "2026-07-12T00:00:00Z", "--authority-basis", "approval"], check=False, capture_output=True, text=True)
            self.assertEqual(init.returncode, 0, init.stderr)
            state_before = state_path.read_bytes()
            events_before = events_path.read_bytes()
            rejected = subprocess.run(base + ["activate", "--graph", str(graph_path), "--state", str(state_path), "--events", str(events_path), "--mission-id", "EPIC-FIXTURE-001", "--child-id", "feature-b", "--expected-revision", "0", "--actor-ref", "builder", "--timestamp", "2026-07-12T00:00:01Z", "--authority-basis", "approval"], check=False, capture_output=True, text=True)
            self.assertEqual(rejected.returncode, 2)
            self.assertEqual(state_path.read_bytes(), state_before)
            self.assertEqual(events_path.read_bytes(), events_before)


if __name__ == "__main__":
    unittest.main()
