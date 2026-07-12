#!/usr/bin/env python3
"""Deterministic advisory state transitions for a serial Factory V3 mission.

The authored JSON state is authoritative. JSONL events are append-only audit
evidence. This module never runs worker or verification commands.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

from factory_v3_serial_mission_graph_lint import _lint_graph


STATE_SCHEMA_VERSION = "v0.1-serial-mission-state"
EVENT_SCHEMA_VERSION = "v0.1-serial-mission-transition-event"
STATE_RECORD_TYPE = "factory_v3_serial_mission_state"
EVENT_RECORD_TYPE = "factory_v3_serial_mission_transition_event"
EVIDENCE_STATUSES = {"PROVED", "WEAK", "MISSING", "CONTRADICTED"}
VERIFICATION_RESULTS = {"pass", "fail", "not_run", "blocked"}
CHILD_STATUSES = {"pending", "eligible", "active", "verification_pending", "completed", "safe_hold", "halted", "skipped"}
PARENT_STATUSES = {"planning", "active", "verification_pending", "completed", "safe_hold", "halted"}


class StateError(Exception):
    """A deterministic input or transition rejection."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def canonical_json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def graph_digest(graph: dict[str, Any]) -> str:
    encoded = json.dumps(graph, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def initialize_state(
    graph: dict[str, Any], graph_ref: str, repository_state_ref: str
) -> dict[str, Any]:
    findings = _lint_graph(Path(graph_ref), graph)
    if findings:
        raise StateError("invalid_graph", f"serial mission graph has {len(findings)} advisory finding(s)")
    parent = graph["parent_mission"]
    children = []
    for child in graph["children"]:
        children.append(
            {
                "child_id": child["child_id"],
                "dependencies": list(child["dependencies"]),
                "required": child["required"],
                "status": "pending",
                "start_authorized": False,
                "verification": {
                    "result": "not_run",
                    "evidence_status": "MISSING",
                    "evidence_refs": [],
                    "unresolved_gap": "Child verification has not run.",
                },
                "current_repository_state_ref": repository_state_ref,
            }
        )
    state = {
        "record": {
            "record_type": STATE_RECORD_TYPE,
            "schema_version": STATE_SCHEMA_VERSION,
            "status": "research_only_non_enforcing",
            "authored_state_is_authoritative": True,
            "derived_cursors_grant_authority": False,
            "session_memory_sufficient": False,
        },
        "mission_id": parent["mission_id"],
        "graph_ref": graph_ref,
        "graph_digest": graph_digest(graph),
        "revision": 0,
        "event_sequence": 1,
        "parent_status": "planning",
        "current_active_child": None,
        "last_safe_checkpoint": None,
        "open_decisions": [],
        "safe_hold_reason": None,
        "current_repository_state_ref": repository_state_ref,
        "children": children,
        "parent_verification": {
            "result": "not_run",
            "evidence_status": "MISSING",
            "evidence_refs": [],
            "unresolved_gap": "Parent verification has not run.",
        },
    }
    validate_state(state, graph)
    return state


def initial_event(
    state: dict[str, Any], actor_ref: str, timestamp: str, authority_basis: str
) -> dict[str, Any]:
    return {
        "record_type": EVENT_RECORD_TYPE,
        "schema_version": EVENT_SCHEMA_VERSION,
        "sequence": 1,
        "event_id": f"{state['mission_id']}:1",
        "mission_id": state["mission_id"],
        "child_id": None,
        "transition": "initialize",
        "actor_ref": actor_ref,
        "timestamp": timestamp,
        "authority_basis": authority_basis,
        "evidence_refs": [],
        "repository_state_ref": state["current_repository_state_ref"],
        "prior_state_revision": None,
        "resulting_state_revision": 0,
        "transition_data": {},
    }


def validate_state(state: Any, graph: dict[str, Any] | None = None) -> None:
    if not isinstance(state, dict):
        raise StateError("malformed_state", "state root must be an object")
    record = state.get("record")
    if not isinstance(record, dict) or record.get("record_type") != STATE_RECORD_TYPE or record.get("schema_version") != STATE_SCHEMA_VERSION:
        raise StateError("malformed_state", "state record type or schema version is invalid")
    required_record = {
        "status": "research_only_non_enforcing",
        "authored_state_is_authoritative": True,
        "derived_cursors_grant_authority": False,
        "session_memory_sufficient": False,
    }
    if any(record.get(key) != value for key, value in required_record.items()):
        raise StateError("unsafe_state", "state advisory/source-of-truth boundary flags are invalid")
    if not _text(state.get("mission_id")) or not _text(state.get("graph_ref")) or not _text(state.get("graph_digest")):
        raise StateError("malformed_state", "mission_id, graph_ref, and graph_digest are required")
    if not isinstance(state.get("revision"), int) or state["revision"] < 0:
        raise StateError("malformed_state", "revision must be a non-negative integer")
    if not isinstance(state.get("event_sequence"), int) or state["event_sequence"] < 1:
        raise StateError("malformed_state", "event_sequence must be a positive integer")
    if state.get("parent_status") not in PARENT_STATUSES:
        raise StateError("malformed_state", "parent_status is invalid")
    if not _text(state.get("current_repository_state_ref")):
        raise StateError("malformed_state", "current_repository_state_ref is required")
    if not isinstance(state.get("open_decisions"), list) or not all(_text(item) for item in state["open_decisions"]):
        raise StateError("malformed_state", "open_decisions must be a string list")
    children = state.get("children")
    if not isinstance(children, list) or not children:
        raise StateError("malformed_state", "children must be a non-empty list")
    ids: list[str] = []
    active: list[str] = []
    authorized: list[str] = []
    for child in children:
        if not isinstance(child, dict) or not _text(child.get("child_id")):
            raise StateError("malformed_state", "each child must have a child_id")
        child_id = child["child_id"]
        ids.append(child_id)
        if child.get("status") not in CHILD_STATUSES:
            raise StateError("malformed_state", f"child status is invalid: {child_id}")
        if (
            not isinstance(child.get("required"), bool)
            or not isinstance(child.get("dependencies"), list)
            or not all(_text(item) for item in child["dependencies"])
            or not _text(child.get("current_repository_state_ref"))
        ):
            raise StateError("malformed_state", f"child dependencies/required are invalid: {child_id}")
        if not isinstance(child.get("start_authorized"), bool):
            raise StateError("malformed_state", f"child start_authorized must be boolean: {child_id}")
        _validate_verification(child.get("verification"), f"child {child_id}")
        if child["status"] == "completed" and not (
            child["verification"]["result"] == "pass"
            and child["verification"]["evidence_status"] == "PROVED"
        ):
            raise StateError("state_contradiction", f"completed child lacks passing proved evidence: {child_id}")
        if child["status"] in {"active", "verification_pending", "safe_hold"}:
            active.append(child_id)
        if child["start_authorized"]:
            authorized.append(child_id)
    if len(ids) != len(set(ids)):
        raise StateError("malformed_state", "duplicate child IDs in authored state")
    if len(active) > 1 or len(authorized) > 1:
        raise StateError("serial_violation", "more than one child is active or start-authorized")
    current = state.get("current_active_child")
    expected_current = active[0] if active else None
    if current != expected_current:
        raise StateError("state_contradiction", "current_active_child does not match child statuses")
    if state["parent_status"] == "safe_hold" and not _text(state.get("safe_hold_reason")):
        raise StateError("state_contradiction", "safe_hold parent requires safe_hold_reason")
    if state["parent_status"] == "safe_hold" and current is not None and _child(state, current)["status"] != "safe_hold":
        raise StateError("state_contradiction", "safe_hold parent requires its current child to be safe_hold")
    _validate_verification(state.get("parent_verification"), "parent")
    if state["parent_status"] == "completed" and not (
        all(
            child["status"] == "completed"
            and child["verification"]["result"] == "pass"
            and child["verification"]["evidence_status"] == "PROVED"
            for child in children
            if child["required"]
        )
        and state["parent_verification"]["result"] == "pass"
        and state["parent_verification"]["evidence_status"] == "PROVED"
    ):
        raise StateError("state_contradiction", "completed parent lacks required child or parent proof")
    if graph is not None:
        _validate_graph_link(state, graph)


def _validate_verification(value: Any, label: str) -> None:
    if not isinstance(value, dict):
        raise StateError("malformed_state", f"{label} verification must be an object")
    if value.get("result") not in VERIFICATION_RESULTS or value.get("evidence_status") not in EVIDENCE_STATUSES:
        raise StateError("malformed_state", f"{label} verification result/evidence is invalid")
    refs = value.get("evidence_refs")
    if not isinstance(refs, list) or not all(_text(item) for item in refs):
        raise StateError("malformed_state", f"{label} evidence_refs must be a string list")
    if value["evidence_status"] == "PROVED" and not refs:
        raise StateError("evidence_missing", f"{label} PROVED evidence requires evidence_refs")
    if value["evidence_status"] != "PROVED" and not _text(value.get("unresolved_gap")):
        raise StateError("evidence_missing", f"{label} non-PROVED evidence requires unresolved_gap")


def _validate_graph_link(state: dict[str, Any], graph: dict[str, Any]) -> None:
    if state["graph_digest"] != graph_digest(graph):
        raise StateError("graph_changed", "graph digest does not match authored state")
    if state["mission_id"] != graph.get("parent_mission", {}).get("mission_id"):
        raise StateError("unknown_mission", "state mission ID does not match graph")
    graph_children = {child["child_id"]: child for child in graph.get("children", []) if isinstance(child, dict) and _text(child.get("child_id"))}
    state_children = {child["child_id"]: child for child in state["children"]}
    if set(graph_children) != set(state_children):
        raise StateError("unknown_child", "state child IDs do not match graph")
    for child_id, child in state_children.items():
        graph_child = graph_children[child_id]
        if child["dependencies"] != graph_child.get("dependencies") or child["required"] != graph_child.get("required"):
            raise StateError("graph_changed", f"authored child contract changed: {child_id}")


def validate_events(events: list[Any], state: dict[str, Any]) -> None:
    if not events:
        raise StateError("event_state_divergence", "event log is empty")
    previous_revision: int | None = None
    for index, event in enumerate(events, start=1):
        if not isinstance(event, dict):
            raise StateError("malformed_event", f"event {index} must be an object")
        if event.get("record_type") != EVENT_RECORD_TYPE or event.get("schema_version") != EVENT_SCHEMA_VERSION:
            raise StateError("malformed_event", f"event {index} record type or schema is invalid")
        if event.get("sequence") != index or event.get("event_id") != f"{state['mission_id']}:{index}":
            raise StateError("event_state_divergence", f"event sequence/linkage is invalid at {index}")
        if event.get("mission_id") != state["mission_id"]:
            raise StateError("unknown_mission", f"event {index} mission ID does not match state")
        if (
            not _text(event.get("transition"))
            or not _text(event.get("actor_ref"))
            or not _text(event.get("timestamp"))
            or not _text(event.get("authority_basis"))
            or not isinstance(event.get("evidence_refs"), list)
            or not all(_text(item) for item in event["evidence_refs"])
            or not _text(event.get("repository_state_ref"))
            or not isinstance(event.get("transition_data"), dict)
        ):
            raise StateError("malformed_event", f"event {index} required fields are invalid")
        prior = event.get("prior_state_revision")
        resulting = event.get("resulting_state_revision")
        if index == 1:
            if event.get("transition") != "initialize" or prior is not None or resulting != 0:
                raise StateError("event_state_divergence", "first event must initialize revision 0")
        elif prior != previous_revision or resulting != prior + 1:
            raise StateError("event_state_divergence", f"event revision linkage is invalid at {index}")
        previous_revision = resulting
    if len(events) != state["event_sequence"] or previous_revision != state["revision"]:
        raise StateError("event_state_divergence", "event log head does not match authored state revision/sequence")


def derive(state: dict[str, Any], graph: dict[str, Any]) -> dict[str, Any]:
    by_id = {child["child_id"]: child for child in state["children"]}
    eligible = []
    if state["parent_status"] not in {"safe_hold", "halted", "completed", "verification_pending"} and state["current_active_child"] is None:
        for child in state["children"]:
            if child["status"] in {"pending", "eligible"} and all(by_id[dep]["status"] == "completed" for dep in child["dependencies"]):
                eligible.append(child["child_id"])
    closeout = all(
        child["status"] == "completed"
        and child["verification"]["result"] == "pass"
        and child["verification"]["evidence_status"] == "PROVED"
        for child in state["children"]
        if child["required"]
    ) and state["parent_verification"]["result"] == "pass" and state["parent_verification"]["evidence_status"] == "PROVED"
    next_action: dict[str, Any]
    if state["parent_status"] == "completed":
        next_action = {"action": "none", "child_id": None, "reason": "parent mission is complete"}
    elif state["parent_status"] == "safe_hold":
        next_action = {"action": "resume_or_halt", "child_id": state["current_active_child"], "reason": state["safe_hold_reason"]}
    elif state["current_active_child"]:
        child = by_id[state["current_active_child"]]
        action = "record_verification" if child["status"] == "verification_pending" else "checkpoint_or_verification_pending"
        next_action = {"action": action, "child_id": child["child_id"], "reason": "bounded active child"}
    elif closeout:
        next_action = {"action": "close_parent", "child_id": None, "reason": "all closeout conditions pass"}
    elif all(child["status"] == "completed" for child in state["children"] if child["required"]):
        next_action = {"action": "record_parent_verification", "child_id": None, "reason": "required children are complete"}
    elif eligible:
        next_action = {"action": "activate_child", "child_id": eligible[0], "reason": "dependencies are complete; activation still requires authority basis"}
    else:
        next_action = {"action": "safe_hold", "child_id": None, "reason": "no eligible authorized transition"}
    return {
        "eligible_children": eligible,
        "one_safe_next_action": next_action,
        "parent_closeout_eligible": closeout,
        "derived_cursors_grant_authority": False,
        "session_memory_accepted": False,
    }


def apply_transition(
    state: dict[str, Any],
    graph: dict[str, Any],
    transition: str,
    *,
    expected_revision: int,
    actor_ref: str,
    timestamp: str,
    authority_basis: str,
    child_id: str | None = None,
    evidence_refs: list[str] | None = None,
    repository_state_ref: str | None = None,
    data: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_state(state, graph)
    if state["revision"] != expected_revision:
        raise StateError("stale_revision", f"expected revision {expected_revision}, found {state['revision']}")
    if not _text(actor_ref) or not _text(timestamp) or not _text(authority_basis):
        raise StateError("missing_authority", "actor_ref, timestamp, and authority_basis are required")
    if child_id is not None and child_id not in {child["child_id"] for child in state["children"]}:
        raise StateError("unknown_child", f"unknown child ID: {child_id}")
    refs = list(evidence_refs or [])
    if not all(_text(item) for item in refs):
        raise StateError("malformed_transition", "evidence_refs must contain non-empty strings")
    details = copy.deepcopy(data or {})
    new = copy.deepcopy(state)
    handler = TRANSITIONS.get(transition)
    if handler is None:
        raise StateError("unknown_transition", f"unknown transition: {transition}")
    handler(new, graph, child_id, refs, repository_state_ref, details)
    prior = state["revision"]
    new["revision"] = prior + 1
    new["event_sequence"] = state["event_sequence"] + 1
    if repository_state_ref is not None:
        if not _text(repository_state_ref):
            raise StateError("malformed_transition", "repository_state_ref must be non-empty")
        new["current_repository_state_ref"] = repository_state_ref
        if child_id is not None:
            _child(new, child_id)["current_repository_state_ref"] = repository_state_ref
    validate_state(new, graph)
    sequence = new["event_sequence"]
    event = {
        "record_type": EVENT_RECORD_TYPE,
        "schema_version": EVENT_SCHEMA_VERSION,
        "sequence": sequence,
        "event_id": f"{new['mission_id']}:{sequence}",
        "mission_id": new["mission_id"],
        "child_id": child_id,
        "transition": transition,
        "actor_ref": actor_ref,
        "timestamp": timestamp,
        "authority_basis": authority_basis,
        "evidence_refs": refs,
        "repository_state_ref": new["current_repository_state_ref"],
        "prior_state_revision": prior,
        "resulting_state_revision": new["revision"],
        "transition_data": details,
    }
    return new, event


def _activate(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    if child_id is None:
        raise StateError("unknown_child", "activate requires child_id")
    if state["parent_status"] in {"safe_hold", "halted", "completed", "verification_pending"} or state["current_active_child"] is not None:
        raise StateError("duplicate_activation", "parent cannot activate another child now")
    child = _child(state, child_id)
    if child["status"] not in {"pending", "eligible"}:
        raise StateError("invalid_transition", f"child {child_id} cannot activate from {child['status']}")
    by_id = {item["child_id"]: item for item in state["children"]}
    incomplete = [dep for dep in child["dependencies"] if by_id[dep]["status"] != "completed"]
    if incomplete:
        raise StateError("dependency_violation", f"incomplete dependencies: {', '.join(incomplete)}")
    for item in state["children"]:
        item["start_authorized"] = False
    child["status"] = "active"
    child["start_authorized"] = True
    state["current_active_child"] = child_id
    state["parent_status"] = "active"


def _checkpoint(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    checkpoint_id = data.get("checkpoint_id")
    if not _text(checkpoint_id) or not refs or not _text(repo):
        raise StateError("malformed_transition", "checkpoint requires checkpoint_id, evidence refs, and repository state ref")
    if child_id is not None and state["current_active_child"] != child_id:
        raise StateError("invalid_transition", "checkpoint child is not current active child")
    state["last_safe_checkpoint"] = {
        "checkpoint_id": checkpoint_id,
        "child_id": child_id,
        "evidence_refs": refs,
        "repository_state_ref": repo,
    }


def _verification_pending(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    child = _require_current(state, child_id, "active")
    child["status"] = "verification_pending"
    child["start_authorized"] = False
    child["verification"] = {
        "result": "not_run",
        "evidence_status": "MISSING",
        "evidence_refs": [],
        "unresolved_gap": "Verification is pending.",
    }
    state["parent_status"] = "verification_pending"


def _record_verification(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    child = _require_current(state, child_id, "verification_pending")
    result = data.get("result")
    evidence_status = data.get("evidence_status")
    gap = data.get("unresolved_gap", "")
    if result not in {"pass", "fail"} or evidence_status not in EVIDENCE_STATUSES:
        raise StateError("malformed_transition", "verification result/evidence status is invalid")
    if result == "pass" and (evidence_status != "PROVED" or not refs):
        raise StateError("evidence_missing", "passing verification requires PROVED evidence references")
    if evidence_status != "PROVED" and not _text(gap):
        raise StateError("evidence_missing", "non-PROVED verification requires unresolved_gap")
    child["verification"] = {"result": result, "evidence_status": evidence_status, "evidence_refs": refs, "unresolved_gap": gap}
    if result == "fail":
        child["status"] = "safe_hold"
        state["parent_status"] = "safe_hold"
        state["safe_hold_reason"] = data.get("safe_hold_reason") or "Child verification failed."
        decision = data.get("open_decision") or "Recovery requires explicit bounded authority."
        state["open_decisions"] = [decision]
    else:
        state["parent_status"] = "verification_pending"


def _complete_child(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    child = _require_current(state, child_id, "verification_pending")
    verification = child["verification"]
    if verification["result"] != "pass" or verification["evidence_status"] != "PROVED":
        raise StateError("verification_failed", "child completion requires passing verification and PROVED evidence")
    child["status"] = "completed"
    child["start_authorized"] = False
    state["current_active_child"] = None
    state["parent_status"] = "active"
    state["last_safe_checkpoint"] = {
        "checkpoint_id": data.get("checkpoint_id") or f"{child_id}-complete",
        "child_id": child_id,
        "evidence_refs": verification["evidence_refs"],
        "repository_state_ref": repo or state["current_repository_state_ref"],
    }


def _safe_hold(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    reason = data.get("reason")
    if not _text(reason):
        raise StateError("malformed_transition", "safe hold requires a reason")
    current = state["current_active_child"]
    if child_id is not None and current != child_id:
        raise StateError("invalid_transition", "safe-hold child is not current active child")
    if current is not None:
        child = _child(state, current)
        child["status"] = "safe_hold"
        child["start_authorized"] = False
    state["parent_status"] = "safe_hold"
    state["safe_hold_reason"] = reason
    decision = data.get("open_decision")
    state["open_decisions"] = [decision] if _text(decision) else []


def _resume(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    if state["parent_status"] != "safe_hold":
        raise StateError("invalid_transition", "resume requires parent safe_hold")
    if data.get("state_source") != "authored_state":
        raise StateError("session_memory_rejected", "resume state_source must be authored_state")
    if not _text(repo) or repo != state["current_repository_state_ref"]:
        raise StateError("stale_repository_state", "resume repository state does not match authored state")
    next_action = data.get("next_safe_action")
    if not _text(next_action):
        raise StateError("missing_next_action", "resume requires exactly one safe next action")
    current = state["current_active_child"]
    if current is not None:
        if child_id != current:
            raise StateError("invalid_transition", "resume child must match current active child")
        child = _child(state, current)
        if child["status"] != "safe_hold":
            raise StateError("state_contradiction", "resume child must be in safe_hold")
        child["status"] = "active"
        child["start_authorized"] = True
    elif child_id is not None:
        raise StateError("invalid_transition", "resume cannot name an inactive child")
    state["parent_status"] = "active"
    state["safe_hold_reason"] = None
    state["open_decisions"] = []


def _record_parent_verification(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    if child_id is not None:
        raise StateError("invalid_transition", "parent verification cannot name child_id")
    if state["current_active_child"] is not None or not all(child["status"] == "completed" for child in state["children"] if child["required"]):
        raise StateError("parent_closeout_too_early", "all required children must complete before parent verification")
    result = data.get("result")
    evidence_status = data.get("evidence_status")
    gap = data.get("unresolved_gap", "")
    if result not in {"pass", "fail"} or evidence_status not in EVIDENCE_STATUSES:
        raise StateError("malformed_transition", "parent verification result/evidence is invalid")
    if result == "pass" and (evidence_status != "PROVED" or not refs):
        raise StateError("evidence_missing", "passing parent verification requires PROVED evidence")
    if evidence_status != "PROVED" and not _text(gap):
        raise StateError("evidence_missing", "non-PROVED parent verification requires unresolved_gap")
    state["parent_verification"] = {"result": result, "evidence_status": evidence_status, "evidence_refs": refs, "unresolved_gap": gap}
    if result == "fail":
        state["parent_status"] = "safe_hold"
        state["safe_hold_reason"] = data.get("safe_hold_reason") or "Parent verification failed."
        state["open_decisions"] = [data.get("open_decision") or "Parent recovery requires explicit bounded authority."]
    else:
        state["parent_status"] = "verification_pending"


def _close_parent(state: dict[str, Any], graph: dict[str, Any], child_id: str | None, refs: list[str], repo: str | None, data: dict[str, Any]) -> None:
    if child_id is not None:
        raise StateError("invalid_transition", "close parent cannot name child_id")
    decision = derive(state, graph)
    if not decision["parent_closeout_eligible"]:
        raise StateError("parent_closeout_too_early", "parent closeout conditions are not satisfied")
    state["parent_status"] = "completed"
    state["current_active_child"] = None
    state["safe_hold_reason"] = None
    state["open_decisions"] = []


TRANSITIONS = {
    "activate_child": _activate,
    "checkpoint": _checkpoint,
    "mark_verification_pending": _verification_pending,
    "record_verification_result": _record_verification,
    "complete_child": _complete_child,
    "enter_safe_hold": _safe_hold,
    "resume": _resume,
    "record_parent_verification": _record_parent_verification,
    "close_parent": _close_parent,
}


def load_context(state_path: Path, events_path: Path, graph_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    state = _load_json(state_path, "state")
    graph = _load_json(graph_path, "graph")
    events = _load_jsonl(events_path)
    findings = _lint_graph(graph_path, graph)
    if findings:
        raise StateError("invalid_graph", f"serial mission graph has {len(findings)} advisory finding(s)")
    validate_state(state, graph)
    validate_events(events, state)
    return state, events, graph


def persist_transition(state_path: Path, events_path: Path, new_state: dict[str, Any], event: dict[str, Any]) -> None:
    # Cross-file atomicity is impossible here. Append+fsync first, then atomically
    # replace state. A crash between them is detected as event/state divergence.
    with events_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    _atomic_write_json(state_path, new_state)


def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(canonical_json(data))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def _load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StateError(f"malformed_{label}", f"could not load {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise StateError(f"malformed_{label}", f"{label} root must be an object")
    return value


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise StateError("malformed_event", f"could not load events: {exc}") from exc
    events = []
    for index, line in enumerate(lines, start=1):
        if not line.strip():
            raise StateError("malformed_event", f"blank event line at {index}")
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise StateError("malformed_event", f"invalid JSON event at line {index}: {exc}") from exc
    return events


def _child(state: dict[str, Any], child_id: str) -> dict[str, Any]:
    for child in state["children"]:
        if child["child_id"] == child_id:
            return child
    raise StateError("unknown_child", f"unknown child ID: {child_id}")


def _require_current(state: dict[str, Any], child_id: str | None, required_status: str) -> dict[str, Any]:
    if child_id is None or state["current_active_child"] != child_id:
        raise StateError("invalid_transition", "transition requires the current active child")
    child = _child(state, child_id)
    if child["status"] != required_status:
        raise StateError("invalid_transition", f"child {child_id} must be {required_status}, found {child['status']}")
    return child


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _add_common_mutation_args(parser: argparse.ArgumentParser, *, child: bool = False) -> None:
    parser.add_argument("--state", required=True)
    parser.add_argument("--events", required=True)
    parser.add_argument("--graph", required=True)
    parser.add_argument("--mission-id", required=True)
    if child:
        parser.add_argument("--child-id", required=True)
    parser.add_argument("--expected-revision", required=True, type=int)
    parser.add_argument("--actor-ref", required=True)
    parser.add_argument("--timestamp", required=True)
    parser.add_argument("--authority-basis", required=True)
    parser.add_argument("--evidence-ref", action="append", default=[])
    parser.add_argument("--repository-state-ref")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Factory V3 advisory deterministic serial mission-state kernel.")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--graph", required=True)
    init.add_argument("--state", required=True)
    init.add_argument("--events", required=True)
    init.add_argument("--repository-state-ref", required=True)
    init.add_argument("--actor-ref", required=True)
    init.add_argument("--timestamp", required=True)
    init.add_argument("--authority-basis", required=True)
    for name in ("status", "eligible"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--state", required=True)
        cmd.add_argument("--events", required=True)
        cmd.add_argument("--graph", required=True)
        cmd.add_argument("--mission-id")
    for name in ("activate", "verification-pending", "complete-child"):
        _add_common_mutation_args(sub.add_parser(name), child=True)
    checkpoint = sub.add_parser("checkpoint")
    _add_common_mutation_args(checkpoint)
    checkpoint.add_argument("--child-id")
    checkpoint.add_argument("--checkpoint-id", required=True)
    verify = sub.add_parser("record-verification")
    _add_common_mutation_args(verify, child=True)
    verify.add_argument("--result", choices=["pass", "fail"], required=True)
    verify.add_argument("--evidence-status", choices=sorted(EVIDENCE_STATUSES), required=True)
    verify.add_argument("--unresolved-gap", default="")
    verify.add_argument("--safe-hold-reason")
    verify.add_argument("--open-decision")
    hold = sub.add_parser("safe-hold")
    _add_common_mutation_args(hold)
    hold.add_argument("--child-id")
    hold.add_argument("--reason", required=True)
    hold.add_argument("--open-decision")
    resume = sub.add_parser("resume")
    _add_common_mutation_args(resume)
    resume.add_argument("--child-id")
    resume.add_argument("--state-source", required=True)
    resume.add_argument("--next-safe-action", required=True)
    parent_verify = sub.add_parser("record-parent-verification")
    _add_common_mutation_args(parent_verify)
    parent_verify.add_argument("--result", choices=["pass", "fail"], required=True)
    parent_verify.add_argument("--evidence-status", choices=sorted(EVIDENCE_STATUSES), required=True)
    parent_verify.add_argument("--unresolved-gap", default="")
    parent_verify.add_argument("--safe-hold-reason")
    parent_verify.add_argument("--open-decision")
    _add_common_mutation_args(sub.add_parser("close"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            state_path, events_path, graph_path = Path(args.state), Path(args.events), Path(args.graph)
            if state_path.exists() or events_path.exists():
                raise StateError("already_initialized", "state and event paths must not already exist")
            graph = _load_json(graph_path, "graph")
            state = initialize_state(graph, graph_path.as_posix(), args.repository_state_ref)
            event = initial_event(state, args.actor_ref, args.timestamp, args.authority_basis)
            events_path.parent.mkdir(parents=True, exist_ok=True)
            with events_path.open("x", encoding="utf-8") as handle:
                handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
            _atomic_write_json(state_path, state)
            output = _result("ok", args.command, state, graph, event)
        else:
            state_path, events_path, graph_path = Path(args.state), Path(args.events), Path(args.graph)
            state, events, graph = load_context(state_path, events_path, graph_path)
            _require_mission_id(state, getattr(args, "mission_id", None))
            if args.command in {"status", "eligible"}:
                output = _result("advisory_pass", args.command, state, graph, None)
            else:
                transition, data = _transition_request(args)
                new_state, event = apply_transition(
                    state,
                    graph,
                    transition,
                    expected_revision=args.expected_revision,
                    actor_ref=args.actor_ref,
                    timestamp=args.timestamp,
                    authority_basis=args.authority_basis,
                    child_id=getattr(args, "child_id", None),
                    evidence_refs=args.evidence_ref,
                    repository_state_ref=args.repository_state_ref,
                    data=data,
                )
                persist_transition(state_path, events_path, new_state, event)
                output = _result("ok", args.command, new_state, graph, event)
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    except StateError as exc:
        print(json.dumps({"blocking_effect": "mutation_rejected", "error": {"code": exc.code, "message": exc.message}, "status": "error"}, indent=2, sort_keys=True))
        return 2
    except OSError as exc:
        print(
            json.dumps(
                {
                    "blocking_effect": "persistence_failed_check_event_state_divergence",
                    "error": {"code": "persistence_error", "message": str(exc)},
                    "status": "error",
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 3


def _transition_request(args: argparse.Namespace) -> tuple[str, dict[str, Any]]:
    mapping = {
        "activate": "activate_child",
        "checkpoint": "checkpoint",
        "verification-pending": "mark_verification_pending",
        "record-verification": "record_verification_result",
        "complete-child": "complete_child",
        "safe-hold": "enter_safe_hold",
        "resume": "resume",
        "record-parent-verification": "record_parent_verification",
        "close": "close_parent",
    }
    keys = ("checkpoint_id", "result", "evidence_status", "unresolved_gap", "safe_hold_reason", "open_decision", "reason", "state_source", "next_safe_action")
    return mapping[args.command], {key: getattr(args, key) for key in keys if hasattr(args, key) and getattr(args, key) is not None}


def _require_mission_id(state: dict[str, Any], mission_id: str | None) -> None:
    if mission_id is not None and mission_id != state["mission_id"]:
        raise StateError("unknown_mission", f"unknown mission ID: {mission_id}")


def _result(status: str, command: str, state: dict[str, Any], graph: dict[str, Any], event: dict[str, Any] | None) -> dict[str, Any]:
    return {
        "blocking_effect": "none",
        "command": command,
        "derived": derive(state, graph),
        "event": event,
        "mission_id": state["mission_id"],
        "revision": state["revision"],
        "state": state,
        "status": status,
    }


if __name__ == "__main__":
    sys.exit(main())
