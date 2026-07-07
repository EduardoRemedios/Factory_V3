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

SCHEMA_VERSION = "v0.1-mission-control-contract"
RECORD_TYPE = "factory_v3_mission_control_contract"

UNSAFE_APPROVAL_FLAGS = {
    "factory_v3_default_approved",
    "new_v3_profile_approved",
    "required_gate_integration_approved",
    "runtime_authority_approved",
    "scheduled_or_unattended_execution_approved",
    "governance_routing_approved",
}

REQUIRED_TOP_LEVEL_OBJECTS = {
    "record",
    "mission_envelope",
    "authority_envelope",
    "loop_admission",
    "checkpoint_policy",
    "next_action_gate",
    "verification_policy",
    "independent_verification",
    "evidence_policy",
    "interrupt_policy",
    "safe_hold_policy",
    "reentry_protocol",
    "worker_interface",
}

REQUIRED_TERMINAL_STATES = {
    "success",
    "no_op",
    "blocked",
    "approval_required",
    "failed_verification",
    "exhausted",
    "stagnated",
    "unsafe",
    "stale_reentry",
    "ambiguous",
    "infeasible",
    "insufficient_context",
}

NEXT_ACTION_CONFIDENCE = {"high", "medium", "low", "insufficient"}
NEXT_ACTION_RESULTS = {"continue", "verify", "ask", "safe_hold", "close", "halt"}
REQUIREMENT_STATUSES = {"PROVED", "WEAK", "MISSING", "CONTRADICTED"}
VERIFICATION_RESULTS = {"pass", "fail", "not_run", "blocked", "advisory_pass", "advisory_fail"}
LOOP_ADMISSION_ROUTES = {"admit", "reject", "safe_hold", "route_to_v2", "research_only"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run standalone advisory Factory V3 mission-control contract checks.",
    )
    parser.add_argument("--target", required=True, help="Mission-control contract JSON file or directory to scan.")
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
        contract = _load_contract(path, findings)
        if contract is None:
            continue
        findings.extend(_lint_contract(path, contract))

    findings.sort(key=lambda item: (item["id"], item["path"], item["message"]))
    warnings = [item for item in findings if item["severity"] == "advisory_high"]

    return {
        "blocking_effect": "none",
        "checked_contracts": [path.as_posix() for path in files],
        "findings": findings,
        "generated_at": "not_recorded",
        "recommended_next_steps": _recommended_next_steps(findings),
        "record_scope": "mission_control_contract_advisory",
        "report_id": "factory-v3-mission-control-contract-lint",
        "status": _status(findings),
        "target": target.as_posix(),
        "warnings": warnings,
    }


def format_text(report: dict[str, Any]) -> str:
    lines = [
        f"factory_v3_mission_control_contract_lint: {report['status']}",
        "blocking_effect=none",
        f"record_scope={report['record_scope']}",
        f"target={report['target']}",
        f"checked_contracts={len(report['checked_contracts'])} findings={len(report['findings'])}",
    ]
    if report["findings"]:
        lines.append("")
        lines.append("Findings:")
        for finding in report["findings"]:
            lines.append(f"- {finding['id']} [{finding['severity']}] {finding['path']}: {finding['message']}")
    lines.append("")
    lines.append("This report is advisory and non-blocking.")
    return "\n".join(lines)


def _lint_contract(path: Path, data: Any) -> list[dict[str, str]]:
    path_text = path.as_posix()
    if not isinstance(data, dict):
        return [_finding("V3-MC000", "advisory_critical", path_text, "mission-control contract root must be an object")]

    findings: list[dict[str, str]] = []
    for key in sorted(REQUIRED_TOP_LEVEL_OBJECTS):
        if not isinstance(data.get(key), dict):
            findings.append(_finding("V3-MC001", "advisory_critical", path_text, f"missing object: {key}"))

    terminal_states = data.get("terminal_states")
    if not isinstance(terminal_states, list):
        findings.append(_finding("V3-MC002", "advisory_critical", path_text, "terminal_states must be a list"))
    elif missing := sorted(REQUIRED_TERMINAL_STATES - _string_set(terminal_states)):
        findings.append(_finding("V3-MC003", "advisory_critical", path_text, f"terminal_states missing required states: {', '.join(missing)}"))

    record = data.get("record") if isinstance(data.get("record"), dict) else {}
    mission = data.get("mission_envelope") if isinstance(data.get("mission_envelope"), dict) else {}
    authority = data.get("authority_envelope") if isinstance(data.get("authority_envelope"), dict) else {}
    admission = data.get("loop_admission") if isinstance(data.get("loop_admission"), dict) else {}
    checkpoint = data.get("checkpoint_policy") if isinstance(data.get("checkpoint_policy"), dict) else {}
    next_action = data.get("next_action_gate") if isinstance(data.get("next_action_gate"), dict) else {}
    verification = data.get("verification_policy") if isinstance(data.get("verification_policy"), dict) else {}
    independent = data.get("independent_verification") if isinstance(data.get("independent_verification"), dict) else {}
    evidence = data.get("evidence_policy") if isinstance(data.get("evidence_policy"), dict) else {}
    interrupt = data.get("interrupt_policy") if isinstance(data.get("interrupt_policy"), dict) else {}
    safe_hold = data.get("safe_hold_policy") if isinstance(data.get("safe_hold_policy"), dict) else {}
    reentry = data.get("reentry_protocol") if isinstance(data.get("reentry_protocol"), dict) else {}
    worker = data.get("worker_interface") if isinstance(data.get("worker_interface"), dict) else {}

    findings.extend(_check_record(path_text, record))
    findings.extend(_check_mission(path_text, mission))
    findings.extend(_check_authority(path_text, authority))
    findings.extend(_check_loop_admission(path_text, admission))
    findings.extend(_check_checkpoint(path_text, checkpoint))
    findings.extend(_check_next_action(path_text, next_action))
    findings.extend(_check_verification(path_text, verification))
    findings.extend(_check_independent_verification(path_text, independent))
    findings.extend(_check_evidence(path_text, evidence))
    findings.extend(_check_interrupt(path_text, interrupt))
    findings.extend(_check_safe_hold(path_text, safe_hold))
    findings.extend(_check_reentry(path_text, reentry))
    findings.extend(_check_worker_interface(path_text, worker))
    findings.extend(_check_fixture_scenarios(path_text, data.get("fixture_scenarios")))
    return findings


def _check_record(path: str, record: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if record.get("record_type") != RECORD_TYPE:
        findings.append(_finding("V3-MC010", "advisory_critical", path, f"record.record_type must be {RECORD_TYPE}"))
    if record.get("schema_version") != SCHEMA_VERSION:
        findings.append(_finding("V3-MC011", "advisory_critical", path, f"record.schema_version must be {SCHEMA_VERSION}"))
    if record.get("status") != "research_only_non_enforcing":
        findings.append(_finding("V3-MC012", "advisory_critical", path, "record.status must be research_only_non_enforcing"))
    if not _nonempty_string(record.get("contract_id")):
        findings.append(_finding("V3-MC013", "advisory_high", path, "record.contract_id is missing"))
    approval_scope = record.get("approval_scope")
    if not isinstance(approval_scope, dict):
        findings.append(_finding("V3-MC014", "advisory_critical", path, "record.approval_scope must be an object"))
        return findings
    for flag in sorted(UNSAFE_APPROVAL_FLAGS):
        if approval_scope.get(flag) is not False:
            findings.append(_finding("V3-MC015", "advisory_critical", path, f"unsafe approval flag must be false: {flag}"))
    if approval_scope.get("factory_v2_fallback_retained") is not True:
        findings.append(_finding("V3-MC016", "advisory_critical", path, "factory_v2_fallback_retained must be true"))
    return findings


def _check_mission(path: str, mission: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("objective", "sponsor_approval_source", "execution_mode"):
        if not _nonempty_string(mission.get(key)):
            findings.append(_finding("V3-MC020", "advisory_critical", path, f"mission_envelope.{key} is missing"))
    for key in ("success_criteria", "non_goals"):
        if not isinstance(mission.get(key), list) or not mission.get(key):
            findings.append(_finding("V3-MC021", "advisory_critical", path, f"mission_envelope.{key} must be a non-empty list"))
    return findings


def _check_authority(path: str, authority: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("authorized_paths", "forbidden_paths", "allowed_commands", "approval_gates"):
        if not isinstance(authority.get(key), list) or not authority.get(key):
            findings.append(_finding("V3-MC030", "advisory_critical", path, f"authority_envelope.{key} must be a non-empty list"))
    for key in ("authorized_paths",):
        for file_path in _invalid_safe_paths(authority.get(key)):
            findings.append(_finding("V3-MC031", "advisory_critical", path, f"authority_envelope.{key} contains unsafe path: {file_path}"))
    if authority.get("external_effects_allowed") is not False:
        findings.append(_finding("V3-MC032", "advisory_critical", path, "authority_envelope.external_effects_allowed must be false for advisory contracts"))
    return findings


def _check_loop_admission(path: str, admission: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if admission.get("route") not in LOOP_ADMISSION_ROUTES:
        findings.append(_finding("V3-MC040", "advisory_critical", path, "loop_admission.route is invalid"))
    if not _nonempty_string(admission.get("admission_rationale")):
        findings.append(_finding("V3-MC041", "advisory_critical", path, "loop_admission.admission_rationale is missing"))
    for key in ("rejection_conditions", "safe_hold_conditions"):
        if not isinstance(admission.get(key), list) or not admission.get(key):
            findings.append(_finding("V3-MC042", "advisory_critical", path, f"loop_admission.{key} must be a non-empty list"))
    return findings


def _check_checkpoint(path: str, checkpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not _nonempty_string(checkpoint.get("cadence")):
        findings.append(_finding("V3-MC050", "advisory_high", path, "checkpoint_policy.cadence is missing"))
    required_fields = _string_set(checkpoint.get("required_fields"))
    minimum = {"objective_status", "authority_status", "verification_status", "next_action_gate", "open_decisions"}
    if missing := sorted(minimum - required_fields):
        findings.append(_finding("V3-MC051", "advisory_critical", path, f"checkpoint_policy.required_fields missing: {', '.join(missing)}"))
    return findings


def _check_next_action(path: str, next_action: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("proposed_next_action", "authority_basis"):
        if not _nonempty_string(next_action.get(key)):
            findings.append(_finding("V3-MC060", "advisory_critical", path, f"next_action_gate.{key} is missing"))
    if next_action.get("confidence") not in NEXT_ACTION_CONFIDENCE:
        findings.append(_finding("V3-MC061", "advisory_critical", path, "next_action_gate.confidence is invalid"))
    if next_action.get("gate_result") not in NEXT_ACTION_RESULTS:
        findings.append(_finding("V3-MC062", "advisory_critical", path, "next_action_gate.gate_result is invalid"))
    if not isinstance(next_action.get("authorized_to_continue"), bool):
        findings.append(_finding("V3-MC063", "advisory_critical", path, "next_action_gate.authorized_to_continue must be boolean"))
    if next_action.get("gate_result") == "continue" and next_action.get("authorized_to_continue") is not True:
        findings.append(_finding("V3-MC064", "advisory_critical", path, "continue gate requires authorized_to_continue=true"))
    if next_action.get("confidence") == "insufficient" and next_action.get("gate_result") not in {"ask", "safe_hold", "halt"}:
        findings.append(_finding("V3-MC065", "advisory_critical", path, "insufficient confidence must ask, safe-hold, or halt"))
    if not isinstance(next_action.get("stop_or_safe_hold_triggers"), list) or not next_action.get("stop_or_safe_hold_triggers"):
        findings.append(_finding("V3-MC066", "advisory_critical", path, "next_action_gate.stop_or_safe_hold_triggers must be a non-empty list"))
    return findings


def _check_verification(path: str, verification: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("required_commands", "verification_tiers", "failure_handling"):
        if not isinstance(verification.get(key), list) or not verification.get(key):
            findings.append(_finding("V3-MC070", "advisory_critical", path, f"verification_policy.{key} must be a non-empty list"))
    return findings


def _check_independent_verification(path: str, verification: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    builder = verification.get("builder_actor")
    verifier = verification.get("verifier_actor")
    if not _nonempty_string(builder):
        findings.append(_finding("V3-MC080", "advisory_critical", path, "independent_verification.builder_actor is missing"))
    if not _nonempty_string(verifier):
        findings.append(_finding("V3-MC081", "advisory_critical", path, "independent_verification.verifier_actor is missing"))
    if _nonempty_string(builder) and builder == verifier:
        findings.append(_finding("V3-MC082", "advisory_critical", path, "builder_actor and verifier_actor must be different"))
    if not isinstance(verification.get("acceptance_criteria"), list) or not verification.get("acceptance_criteria"):
        findings.append(_finding("V3-MC083", "advisory_critical", path, "independent_verification.acceptance_criteria must be a non-empty list"))
    if verification.get("verification_result") not in VERIFICATION_RESULTS:
        findings.append(_finding("V3-MC084", "advisory_critical", path, "independent_verification.verification_result is invalid"))
    if not isinstance(verification.get("unresolved_gaps"), list):
        findings.append(_finding("V3-MC085", "advisory_critical", path, "independent_verification.unresolved_gaps must be a list"))
    return findings


def _check_evidence(path: str, evidence: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if evidence.get("claim_to_proof_required") is not True:
        findings.append(_finding("V3-MC090", "advisory_critical", path, "evidence_policy.claim_to_proof_required must be true"))
    if not isinstance(evidence.get("required_artifacts"), list) or not evidence.get("required_artifacts"):
        findings.append(_finding("V3-MC091", "advisory_critical", path, "evidence_policy.required_artifacts must be a non-empty list"))
    requirements = evidence.get("requirement_to_evidence")
    if not isinstance(requirements, list) or not requirements:
        findings.append(_finding("V3-MC092", "advisory_critical", path, "evidence_policy.requirement_to_evidence must be a non-empty list"))
        return findings
    for index, item in enumerate(requirements, start=1):
        item_path = f"{path}:evidence_policy.requirement_to_evidence[{index}]"
        if not isinstance(item, dict):
            findings.append(_finding("V3-MC093", "advisory_critical", item_path, "requirement evidence item must be an object"))
            continue
        status = item.get("status")
        if not _nonempty_string(item.get("requirement")):
            findings.append(_finding("V3-MC094", "advisory_critical", item_path, "requirement is missing"))
        if status not in REQUIREMENT_STATUSES:
            findings.append(_finding("V3-MC095", "advisory_critical", item_path, "requirement status is invalid"))
        if status == "PROVED" and (not isinstance(item.get("evidence_refs"), list) or not item.get("evidence_refs")):
            findings.append(_finding("V3-MC096", "advisory_critical", item_path, "PROVED requirements must include evidence_refs"))
        if status in {"WEAK", "MISSING", "CONTRADICTED"} and not _nonempty_string(item.get("unresolved_gap")):
            findings.append(_finding("V3-MC097", "advisory_critical", item_path, f"{status} requirements must include unresolved_gap"))
    return findings


def _check_interrupt(path: str, interrupt: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(interrupt.get("decision_tiers"), list) or not interrupt.get("decision_tiers"):
        findings.append(_finding("V3-MC100", "advisory_critical", path, "interrupt_policy.decision_tiers must be a non-empty list"))
    if not isinstance(interrupt.get("approval_gates"), list) or not interrupt.get("approval_gates"):
        findings.append(_finding("V3-MC101", "advisory_critical", path, "interrupt_policy.approval_gates must be a non-empty list"))
    if not _nonempty_string(interrupt.get("timeout_behavior")):
        findings.append(_finding("V3-MC102", "advisory_critical", path, "interrupt_policy.timeout_behavior is missing"))
    return findings


def _check_safe_hold(path: str, safe_hold: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if safe_hold.get("required_for_missing_authority") is not True:
        findings.append(_finding("V3-MC110", "advisory_critical", path, "safe_hold_policy.required_for_missing_authority must be true"))
    if not isinstance(safe_hold.get("safe_hold_reasons"), list) or not safe_hold.get("safe_hold_reasons"):
        findings.append(_finding("V3-MC111", "advisory_critical", path, "safe_hold_policy.safe_hold_reasons must be a non-empty list"))
    required_fields = _string_set(safe_hold.get("required_fields"))
    minimum = {"reason", "blocked_action", "last_safe_checkpoint", "human_decision_needed", "reentry_instructions"}
    if missing := sorted(minimum - required_fields):
        findings.append(_finding("V3-MC112", "advisory_critical", path, f"safe_hold_policy.required_fields missing: {', '.join(missing)}"))
    return findings


def _check_reentry(path: str, reentry: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("read_order", "stale_state_checks"):
        if not isinstance(reentry.get(key), list) or not reentry.get(key):
            findings.append(_finding("V3-MC120", "advisory_critical", path, f"reentry_protocol.{key} must be a non-empty list"))
    for key in ("last_safe_checkpoint", "one_safe_next_action"):
        if not _nonempty_string(reentry.get(key)):
            findings.append(_finding("V3-MC121", "advisory_critical", path, f"reentry_protocol.{key} is missing"))
    if reentry.get("session_memory_sufficient") is not False:
        findings.append(_finding("V3-MC122", "advisory_critical", path, "reentry_protocol.session_memory_sufficient must be false"))
    return findings


def _check_worker_interface(path: str, worker: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not _nonempty_string(worker.get("worker_role")):
        findings.append(_finding("V3-MC130", "advisory_critical", path, "worker_interface.worker_role is missing"))
    for key in ("allowed_tactical_autonomy", "prohibited_self_authorization", "evidence_obligations"):
        if not isinstance(worker.get(key), list) or not worker.get(key):
            findings.append(_finding("V3-MC131", "advisory_critical", path, f"worker_interface.{key} must be a non-empty list"))
    return findings


def _check_fixture_scenarios(path: str, scenarios: Any) -> list[dict[str, str]]:
    if scenarios is None:
        return []
    if not isinstance(scenarios, dict):
        return [_finding("V3-MC140", "advisory_critical", path, "fixture_scenarios must be an object when present")]
    findings: list[dict[str, str]] = []
    cases = scenarios.get("mission_control_cases")
    if cases is None:
        return findings
    if not isinstance(cases, list):
        return [_finding("V3-MC141", "advisory_critical", path, "fixture_scenarios.mission_control_cases must be a list")]
    for index, case in enumerate(cases, start=1):
        case_path = f"{path}:fixture_scenarios.mission_control_cases[{index}]"
        if not isinstance(case, dict):
            findings.append(_finding("V3-MC142", "advisory_critical", case_path, "mission-control case must be an object"))
            continue
        if not _nonempty_string(case.get("scenario_type")):
            findings.append(_finding("V3-MC143", "advisory_critical", case_path, "mission-control case scenario_type is missing"))
        if case.get("expected_gate_result") not in NEXT_ACTION_RESULTS:
            findings.append(_finding("V3-MC144", "advisory_critical", case_path, "mission-control case expected_gate_result is invalid"))
        if case.get("expected_terminal_state") not in REQUIRED_TERMINAL_STATES:
            findings.append(_finding("V3-MC145", "advisory_critical", case_path, "mission-control case expected_terminal_state is invalid"))
        if not isinstance(case.get("required_evidence"), list) or not case.get("required_evidence"):
            findings.append(_finding("V3-MC146", "advisory_critical", case_path, "mission-control case required_evidence must be a non-empty list"))
        if case.get("expected_gate_result") in {"ask", "safe_hold", "halt"} and case.get("safe_hold_or_interrupt_required") is not True:
            findings.append(_finding("V3-MC147", "advisory_critical", case_path, "ask/safe-hold/halt cases must require safe-hold or interrupt"))
    return findings


def _status(findings: list[dict[str, str]]) -> str:
    if not findings:
        return ADVISORY_PASS
    if any(finding["severity"] == "advisory_critical" for finding in findings):
        return ADVISORY_FAIL_NON_BLOCKING
    return ADVISORY_WARN


def _recommended_next_steps(findings: list[dict[str, str]]) -> list[str]:
    if not findings:
        return ["No mission-control contract findings. Keep contracts advisory until a promotion pack approves otherwise."]
    return [
        "Review mission-control contract findings manually; this report is advisory and non-blocking.",
        "Fix missing authority, next-action, evidence, verifier, safe-hold, or re-entry fields before using the contract as mission guidance.",
        "Do not wire mission-control checks into required gates without explicit Factory governance approval.",
    ]


def _json_files(target: Path) -> list[Path]:
    if not target.exists():
        raise SystemExit(f"target does not exist: {target}")
    if target.is_file():
        return [target]
    return sorted(path for path in target.rglob("*.json") if path.is_file() and "expected" not in path.parts)


def _load_contract(path: Path, findings: list[dict[str, str]]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        findings.append(_finding("V3-MC000", "advisory_critical", path.as_posix(), f"could not load JSON: {exc}"))
        return None


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"failed to load expected JSON {path}: {exc}") from exc


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str) and item}


def _invalid_safe_paths(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    invalid: list[str] = []
    for item in value:
        if not isinstance(item, str):
            invalid.append(str(item))
            continue
        path = item.strip()
        if not path or path.startswith("~") or "\\" in path:
            invalid.append(item)
            continue
        parts = PurePosixPath(path).parts
        if not parts or any(part in {"", ".", ".."} for part in parts):
            invalid.append(item)
    return invalid


def _finding(check_id: str, severity: str, path: str, message: str) -> dict[str, str]:
    return {
        "id": check_id,
        "message": message,
        "path": path,
        "severity": severity,
    }


def _format_diff(expected: Any, actual: Any) -> str:
    return "\n".join(
        [
            "factory_v3_mission_control_contract_lint fixture mismatch",
            "Expected:",
            json.dumps(expected, indent=2, sort_keys=True),
            "Actual:",
            json.dumps(actual, indent=2, sort_keys=True),
        ]
    )


if __name__ == "__main__":
    sys.exit(main())
