#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ADVISORY_PASS = "ADVISORY_PASS"
ADVISORY_WARN = "ADVISORY_WARN"
ADVISORY_FAIL_NON_BLOCKING = "ADVISORY_FAIL_NON_BLOCKING"

SCHEMA_VERSION = "v0.1-serial-mission-graph"
RECORD_TYPE = "factory_v3_serial_mission_graph"

UNSAFE_APPROVAL_FLAGS = {
    "concurrent_execution_approved",
    "factory_v3_default_approved",
    "governance_routing_approved",
    "new_v3_profile_approved",
    "required_gate_integration_approved",
    "runtime_authority_approved",
    "scheduled_or_unattended_execution_approved",
    "worker_dispatch_approved",
}

CHILD_STATUSES = {
    "pending",
    "eligible",
    "active",
    "verification_pending",
    "completed",
    "blocked",
    "safe_hold",
    "halted",
    "skipped",
}
ACTIVE_CHILD_STATUSES = {"active", "verification_pending"}
DEPENDENCY_READY_STATUSES = {"eligible", "active", "verification_pending", "completed"}
GATE_RESULTS = {"wait", "continue", "verify", "ask", "safe_hold", "halt", "close"}
EVIDENCE_STATUSES = {"PROVED", "WEAK", "MISSING", "CONTRADICTED"}
VERIFICATION_RESULTS = {"pass", "fail", "not_run", "blocked"}
PARENT_STATUSES = {"planning", "active", "verification_pending", "completed", "blocked", "safe_hold", "halted"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run standalone advisory Factory V3 serial mission-graph checks.",
    )
    parser.add_argument("--target", required=True, help="Serial mission-graph JSON file or directory to scan.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--expect", help="Optional expected JSON file for fixture checks.")
    args = parser.parse_args()

    report = lint_target(Path(args.target))
    if args.expect:
        expected = _load_json(Path(args.expect))
        if report != expected:
            print(_format_diff(expected, report), file=sys.stderr)
            return 1

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(format_text(report))
    return 0


def lint_target(target: Path) -> dict[str, Any]:
    files = _json_files(target)
    findings: list[dict[str, str]] = []

    for path in files:
        graph = _load_graph(path, findings)
        if graph is not None:
            findings.extend(_lint_graph(path, graph))

    findings.sort(key=lambda item: (item["id"], item["path"], item["message"]))
    warnings = [item for item in findings if item["severity"] == "advisory_high"]
    return {
        "blocking_effect": "none",
        "checked_graphs": [path.as_posix() for path in files],
        "findings": findings,
        "generated_at": "not_recorded",
        "recommended_next_steps": _recommended_next_steps(findings),
        "record_scope": "serial_mission_graph_advisory",
        "report_id": "factory-v3-serial-mission-graph-lint",
        "status": _status(findings),
        "target": target.as_posix(),
        "warnings": warnings,
    }


def format_text(report: dict[str, Any]) -> str:
    lines = [
        f"factory_v3_serial_mission_graph_lint: {report['status']}",
        "blocking_effect=none",
        f"record_scope={report['record_scope']}",
        f"target={report['target']}",
        f"checked_graphs={len(report['checked_graphs'])} findings={len(report['findings'])}",
    ]
    if report["findings"]:
        lines.extend(["", "Findings:"])
        lines.extend(
            f"- {item['id']} [{item['severity']}] {item['path']}: {item['message']}"
            for item in report["findings"]
        )
    lines.extend(["", "This report is advisory and non-blocking."])
    return "\n".join(lines)


def _lint_graph(path: Path, data: Any) -> list[dict[str, str]]:
    path_text = path.as_posix()
    if not isinstance(data, dict):
        return [_finding("V3-SG000", "advisory_critical", path_text, "serial mission-graph root must be an object")]

    findings: list[dict[str, str]] = []
    for key in ("record", "parent_mission", "authority_ceiling", "graph_policy", "state_policy", "parent_closeout"):
        if not isinstance(data.get(key), dict):
            findings.append(_finding("V3-SG001", "advisory_critical", path_text, f"missing object: {key}"))

    record = data.get("record") if isinstance(data.get("record"), dict) else {}
    parent = data.get("parent_mission") if isinstance(data.get("parent_mission"), dict) else {}
    authority = data.get("authority_ceiling") if isinstance(data.get("authority_ceiling"), dict) else {}
    policy = data.get("graph_policy") if isinstance(data.get("graph_policy"), dict) else {}
    state = data.get("state_policy") if isinstance(data.get("state_policy"), dict) else {}
    closeout = data.get("parent_closeout") if isinstance(data.get("parent_closeout"), dict) else {}
    children = data.get("children")

    findings.extend(_check_record(path_text, record))
    findings.extend(_check_parent(path_text, parent))
    findings.extend(_check_authority(path_text, authority))
    findings.extend(_check_policy(path_text, policy))
    findings.extend(_check_state_policy(path_text, state))

    if not isinstance(children, list) or len(children) < 2:
        findings.append(_finding("V3-SG060", "advisory_critical", path_text, "children must contain at least two feature missions"))
        children = []
    findings.extend(_check_children(path_text, children, authority))
    findings.extend(_check_parent_closeout(path_text, closeout, children, parent.get("status")))
    return findings


def _check_record(path: str, record: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if record.get("record_type") != RECORD_TYPE:
        findings.append(_finding("V3-SG010", "advisory_critical", path, f"record.record_type must be {RECORD_TYPE}"))
    if record.get("schema_version") != SCHEMA_VERSION:
        findings.append(_finding("V3-SG011", "advisory_critical", path, f"record.schema_version must be {SCHEMA_VERSION}"))
    if record.get("status") != "research_only_non_enforcing":
        findings.append(_finding("V3-SG012", "advisory_critical", path, "record.status must be research_only_non_enforcing"))
    if not _nonempty_string(record.get("graph_id")):
        findings.append(_finding("V3-SG013", "advisory_high", path, "record.graph_id is missing"))
    approval = record.get("approval_scope")
    if not isinstance(approval, dict):
        return findings + [_finding("V3-SG014", "advisory_critical", path, "record.approval_scope must be an object")]
    for flag in sorted(UNSAFE_APPROVAL_FLAGS):
        if approval.get(flag) is not False:
            findings.append(_finding("V3-SG015", "advisory_critical", path, f"unsafe approval flag must be false: {flag}"))
    if approval.get("factory_v2_fallback_retained") is not True:
        findings.append(_finding("V3-SG016", "advisory_critical", path, "factory_v2_fallback_retained must be true"))
    return findings


def _check_parent(path: str, parent: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("mission_id", "objective", "sponsor_approval_source"):
        if not _nonempty_string(parent.get(key)):
            findings.append(_finding("V3-SG020", "advisory_critical", path, f"parent_mission.{key} is missing"))
    for key in ("success_criteria", "non_goals"):
        if not _string_list(parent.get(key)):
            findings.append(_finding("V3-SG021", "advisory_critical", path, f"parent_mission.{key} must be a non-empty string list"))
    if parent.get("status") not in PARENT_STATUSES:
        findings.append(_finding("V3-SG022", "advisory_critical", path, "parent_mission.status is invalid"))
    return findings


def _check_authority(path: str, authority: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("authorized_paths", "forbidden_paths", "allowed_commands", "approval_gates"):
        if not _string_list(authority.get(key)):
            findings.append(_finding("V3-SG030", "advisory_critical", path, f"authority_ceiling.{key} must be a non-empty string list"))
    for item in _invalid_safe_paths(authority.get("authorized_paths")):
        findings.append(_finding("V3-SG031", "advisory_critical", path, f"authority_ceiling.authorized_paths contains unsafe path: {item}"))
    if authority.get("external_effects_allowed") is not False:
        findings.append(_finding("V3-SG032", "advisory_critical", path, "authority_ceiling.external_effects_allowed must be false"))
    return findings


def _check_policy(path: str, policy: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    expected = {
        "execution_mode": "serial",
        "max_active_children": 1,
        "dependency_policy": "all_dependencies_completed",
        "cycle_policy": "reject",
        "failure_policy": "safe_hold_parent",
        "child_authority_must_be_subset": True,
        "scope_expansion_requires_human": True,
    }
    for key, value in expected.items():
        if policy.get(key) != value:
            findings.append(_finding("V3-SG040", "advisory_critical", path, f"graph_policy.{key} must be {value!r}"))
    return findings


def _check_state_policy(path: str, state: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if state.get("authored_state_is_source_of_truth") is not True:
        findings.append(_finding("V3-SG050", "advisory_critical", path, "authored mission state must remain the source of truth"))
    if state.get("eligibility_cursor_is_derived") is not True:
        findings.append(_finding("V3-SG051", "advisory_critical", path, "eligibility cursor must be derived"))
    if state.get("session_memory_sufficient") is not False:
        findings.append(_finding("V3-SG052", "advisory_critical", path, "session_memory_sufficient must be false"))
    for key in ("authored_state_ref", "event_log_ref", "checkpoint_ref"):
        if not _nonempty_string(state.get(key)):
            findings.append(_finding("V3-SG053", "advisory_critical", path, f"state_policy.{key} is missing"))
    return findings


def _check_children(path: str, children: list[Any], authority: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    child_by_id: dict[str, dict[str, Any]] = {}
    duplicate_ids: set[str] = set()

    for index, raw_child in enumerate(children, start=1):
        child_path = f"{path}:children[{index}]"
        if not isinstance(raw_child, dict):
            findings.append(_finding("V3-SG061", "advisory_critical", child_path, "child must be an object"))
            continue
        child_id = raw_child.get("child_id")
        if not _nonempty_string(child_id):
            findings.append(_finding("V3-SG062", "advisory_critical", child_path, "child_id is missing"))
            continue
        if child_id in child_by_id:
            duplicate_ids.add(child_id)
        child_by_id[child_id] = raw_child
        findings.extend(_check_child_shape(child_path, raw_child, authority))

    for child_id in sorted(duplicate_ids):
        findings.append(_finding("V3-SG063", "advisory_critical", path, f"duplicate child_id: {child_id}"))

    known_ids = set(child_by_id)
    dependencies: dict[str, list[str]] = {}
    for child_id, child in child_by_id.items():
        child_path = f"{path}:children[{child_id}]"
        deps = child.get("dependencies") if isinstance(child.get("dependencies"), list) else []
        string_deps = [item for item in deps if isinstance(item, str)]
        dependencies[child_id] = string_deps
        for dependency in string_deps:
            if dependency == child_id:
                findings.append(_finding("V3-SG070", "advisory_critical", child_path, "child cannot depend on itself"))
            elif dependency not in known_ids:
                findings.append(_finding("V3-SG071", "advisory_critical", child_path, f"unknown dependency: {dependency}"))

    if _has_cycle(dependencies):
        findings.append(_finding("V3-SG072", "advisory_critical", path, "child dependency graph contains a cycle"))

    active_ids = sorted(
        child_id for child_id, child in child_by_id.items() if child.get("status") in ACTIVE_CHILD_STATUSES
    )
    if len(active_ids) > 1:
        findings.append(_finding("V3-SG073", "advisory_critical", path, f"serial graph has multiple active children: {', '.join(active_ids)}"))

    authorized_start_ids = sorted(
        child_id
        for child_id, child in child_by_id.items()
        if isinstance(child.get("continuation_gate"), dict)
        and child["continuation_gate"].get("authorized_to_start") is True
    )
    if len(authorized_start_ids) > 1:
        findings.append(_finding("V3-SG077", "advisory_critical", path, f"serial graph authorizes multiple child starts: {', '.join(authorized_start_ids)}"))

    for child_id, child in child_by_id.items():
        child_path = f"{path}:children[{child_id}]"
        incomplete = [dep for dep in dependencies.get(child_id, []) if child_by_id.get(dep, {}).get("status") != "completed"]
        if child.get("status") in DEPENDENCY_READY_STATUSES and incomplete:
            findings.append(_finding("V3-SG074", "advisory_critical", child_path, f"child is ready before dependencies complete: {', '.join(sorted(incomplete))}"))
        gate = child.get("continuation_gate") if isinstance(child.get("continuation_gate"), dict) else {}
        if gate.get("authorized_to_start") is True and incomplete:
            findings.append(_finding("V3-SG075", "advisory_critical", child_path, "child start is authorized before dependencies complete"))
        if gate.get("gate_result") == "continue" and gate.get("authorized_to_start") is not True:
            findings.append(_finding("V3-SG076", "advisory_critical", child_path, "continue gate requires authorized_to_start=true"))
    return findings


def _check_child_shape(path: str, child: dict[str, Any], parent_authority: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("objective", "worker_actor"):
        if not _nonempty_string(child.get(key)):
            findings.append(_finding("V3-SG080", "advisory_critical", path, f"child.{key} is missing"))
    if child.get("status") not in CHILD_STATUSES:
        findings.append(_finding("V3-SG081", "advisory_critical", path, "child.status is invalid"))
    if not isinstance(child.get("required"), bool):
        findings.append(_finding("V3-SG088", "advisory_critical", path, "child.required must be boolean"))
    if not isinstance(child.get("dependencies"), list) or not all(isinstance(item, str) for item in child.get("dependencies", [])):
        findings.append(_finding("V3-SG082", "advisory_critical", path, "child.dependencies must be a string list"))
    if not _string_list(child.get("success_criteria")):
        findings.append(_finding("V3-SG083", "advisory_critical", path, "child.success_criteria must be a non-empty string list"))

    authority = child.get("authority") if isinstance(child.get("authority"), dict) else {}
    for key in ("authorized_paths", "forbidden_paths", "allowed_commands"):
        if not _string_list(authority.get(key)):
            findings.append(_finding("V3-SG084", "advisory_critical", path, f"child.authority.{key} must be a non-empty string list"))
    parent_paths = parent_authority.get("authorized_paths") if isinstance(parent_authority.get("authorized_paths"), list) else []
    for child_path in authority.get("authorized_paths", []) if isinstance(authority.get("authorized_paths"), list) else []:
        if isinstance(child_path, str) and not _path_within_any(child_path, parent_paths):
            findings.append(_finding("V3-SG085", "advisory_critical", path, f"child path exceeds parent authority ceiling: {child_path}"))
    parent_commands = set(parent_authority.get("allowed_commands", [])) if isinstance(parent_authority.get("allowed_commands"), list) else set()
    for command in authority.get("allowed_commands", []) if isinstance(authority.get("allowed_commands"), list) else []:
        if command not in parent_commands:
            findings.append(_finding("V3-SG086", "advisory_critical", path, f"child command exceeds parent authority ceiling: {command}"))
    if authority.get("external_effects_allowed") is not False:
        findings.append(_finding("V3-SG087", "advisory_critical", path, "child external_effects_allowed must be false"))

    verification = child.get("verification") if isinstance(child.get("verification"), dict) else {}
    if not _string_list(verification.get("required_commands")):
        findings.append(_finding("V3-SG090", "advisory_critical", path, "child.verification.required_commands must be a non-empty string list"))
    child_commands = set(authority.get("allowed_commands", [])) if isinstance(authority.get("allowed_commands"), list) else set()
    for command in verification.get("required_commands", []) if isinstance(verification.get("required_commands"), list) else []:
        if command not in child_commands:
            findings.append(_finding("V3-SG094", "advisory_critical", path, f"verification command exceeds child authority: {command}"))
    if verification.get("result") not in VERIFICATION_RESULTS:
        findings.append(_finding("V3-SG091", "advisory_critical", path, "child.verification.result is invalid"))
    verifier = verification.get("verifier_actor")
    if not _nonempty_string(verifier):
        findings.append(_finding("V3-SG092", "advisory_critical", path, "child.verification.verifier_actor is missing"))
    elif verifier == child.get("worker_actor"):
        findings.append(_finding("V3-SG093", "advisory_critical", path, "worker_actor and verifier_actor must be different"))

    evidence = child.get("evidence") if isinstance(child.get("evidence"), dict) else {}
    status = evidence.get("status")
    if status not in EVIDENCE_STATUSES:
        findings.append(_finding("V3-SG100", "advisory_critical", path, "child.evidence.status is invalid"))
    if status == "PROVED" and not _string_list(evidence.get("evidence_refs")):
        findings.append(_finding("V3-SG101", "advisory_critical", path, "PROVED child evidence requires evidence_refs"))
    if status in {"WEAK", "MISSING", "CONTRADICTED"} and not _nonempty_string(evidence.get("unresolved_gap")):
        findings.append(_finding("V3-SG102", "advisory_critical", path, f"{status} child evidence requires unresolved_gap"))

    gate = child.get("continuation_gate") if isinstance(child.get("continuation_gate"), dict) else {}
    if gate.get("gate_result") not in GATE_RESULTS:
        findings.append(_finding("V3-SG110", "advisory_critical", path, "child.continuation_gate.gate_result is invalid"))
    if not isinstance(gate.get("authorized_to_start"), bool):
        findings.append(_finding("V3-SG111", "advisory_critical", path, "child.continuation_gate.authorized_to_start must be boolean"))
    if not _nonempty_string(gate.get("authority_basis")):
        findings.append(_finding("V3-SG112", "advisory_critical", path, "child.continuation_gate.authority_basis is missing"))
    if child.get("status") == "active" and not (
        gate.get("gate_result") == "continue" and gate.get("authorized_to_start") is True
    ):
        findings.append(_finding("V3-SG113", "advisory_critical", path, "active child requires an authorized continue gate"))
    if child.get("status") == "verification_pending" and not (
        gate.get("gate_result") == "verify" and gate.get("authorized_to_start") is False
    ):
        findings.append(_finding("V3-SG114", "advisory_critical", path, "verification-pending child requires a non-starting verify gate"))

    if child.get("status") == "completed":
        if verification.get("result") != "pass":
            findings.append(_finding("V3-SG120", "advisory_critical", path, "completed child requires passing verification"))
        if status != "PROVED":
            findings.append(_finding("V3-SG121", "advisory_critical", path, "completed child requires PROVED evidence"))
        if gate.get("gate_result") != "close" or gate.get("authorized_to_start") is not False:
            findings.append(_finding("V3-SG122", "advisory_critical", path, "completed child requires a non-starting close gate"))
    return findings


def _check_parent_closeout(
    path: str,
    closeout: dict[str, Any],
    children: list[Any],
    parent_status: Any,
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if closeout.get("require_all_required_children_complete") is not True:
        findings.append(_finding("V3-SG130", "advisory_critical", path, "parent_closeout.require_all_required_children_complete must be true"))
    if closeout.get("parent_verification_required") is not True:
        findings.append(_finding("V3-SG131", "advisory_critical", path, "parent_closeout.parent_verification_required must be true"))
    if closeout.get("claim_to_proof_required") is not True:
        findings.append(_finding("V3-SG132", "advisory_critical", path, "parent_closeout.claim_to_proof_required must be true"))
    result = closeout.get("parent_verification_result")
    if result not in VERIFICATION_RESULTS:
        findings.append(_finding("V3-SG133", "advisory_critical", path, "parent_closeout.parent_verification_result is invalid"))
    if parent_status == "completed":
        incomplete = [
            child.get("child_id", "<missing>")
            for child in children
            if isinstance(child, dict) and child.get("required", True) and child.get("status") != "completed"
        ]
        if incomplete:
            findings.append(_finding("V3-SG135", "advisory_critical", path, f"parent completed before required children: {', '.join(sorted(incomplete))}"))
        if result != "pass":
            findings.append(_finding("V3-SG136", "advisory_critical", path, "completed parent requires passing parent verification"))
    return findings


def _has_cycle(dependencies: dict[str, list[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dependency in dependencies.get(node, []):
            if dependency in dependencies and visit(dependency):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in dependencies)


def _path_within_any(child: str, parent_paths: list[Any]) -> bool:
    if child in _invalid_safe_paths([child]):
        return False
    child_parts = PurePosixPath(child).parts
    for parent in parent_paths:
        if not isinstance(parent, str) or parent in _invalid_safe_paths([parent]):
            continue
        parent_parts = PurePosixPath(parent).parts
        if child_parts[: len(parent_parts)] == parent_parts:
            return True
    return False


def _invalid_safe_paths(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    invalid: list[str] = []
    for item in value:
        if not isinstance(item, str):
            invalid.append(str(item))
            continue
        path = item.strip()
        if not path or path.startswith(("/", "~")) or "\\" in path:
            invalid.append(item)
            continue
        parts = PurePosixPath(path).parts
        if not parts or any(part in {"", ".", ".."} for part in parts):
            invalid.append(item)
    return invalid


def _status(findings: list[dict[str, str]]) -> str:
    if not findings:
        return ADVISORY_PASS
    if any(item["severity"] == "advisory_critical" for item in findings):
        return ADVISORY_FAIL_NON_BLOCKING
    return ADVISORY_WARN


def _recommended_next_steps(findings: list[dict[str, str]]) -> list[str]:
    if not findings:
        return ["No serial mission-graph findings. Keep the graph advisory until a promotion pack approves otherwise."]
    return [
        "Review serial mission-graph findings manually; this report is advisory and non-blocking.",
        "Repair dependency, authority, verification, evidence, or completion contradictions before using the graph as mission guidance.",
        "Do not dispatch workers or wire graph checks into required gates without separate approval.",
    ]


def _json_files(target: Path) -> list[Path]:
    if not target.exists():
        raise SystemExit(f"target does not exist: {target}")
    if target.is_file():
        return [target]
    return sorted(path for path in target.rglob("*.json") if path.is_file() and "expected" not in path.parts)


def _load_graph(path: Path, findings: list[dict[str, str]]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        findings.append(_finding("V3-SG000", "advisory_critical", path.as_posix(), f"could not load JSON: {exc}"))
        return None


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"failed to load expected JSON {path}: {exc}") from exc


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_nonempty_string(item) for item in value)


def _finding(check_id: str, severity: str, path: str, message: str) -> dict[str, str]:
    return {"id": check_id, "message": message, "path": path, "severity": severity}


def _format_diff(expected: Any, actual: Any) -> str:
    return "\n".join(
        [
            "factory_v3_serial_mission_graph_lint fixture mismatch",
            "Expected:",
            json.dumps(expected, indent=2, sort_keys=True),
            "Actual:",
            json.dumps(actual, indent=2, sort_keys=True),
        ]
    )


if __name__ == "__main__":
    sys.exit(main())
