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

SCHEMA_VERSION = "v0.1-loop-contract"
RECORD_TYPE = "factory_v3_loop_contract"

UNSAFE_APPROVAL_FLAGS = {
    "factory_v3_default_approved",
    "new_v3_profile_approved",
    "required_gate_integration_approved",
    "runtime_authority_approved",
    "scheduled_or_unattended_execution_approved",
}

REQUIRED_TOP_LEVEL_OBJECTS = {
    "record",
    "mission",
    "authority_envelope",
    "state_policy",
    "tool_policy",
    "act_or_ask_gate",
    "control_profile",
    "checkpoint_policy",
    "verification_policy",
    "evidence_policy",
    "reentry_protocol",
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

ACT_OR_ASK_TERMINALS = {
    "ambiguous",
    "infeasible",
    "unsafe",
    "insufficient_context",
    "approval_required",
}

APPROVED_DETECTION_MODES = {"none", "asynchronous", "synchronous", "hybrid"}
MEMORY_SCENARIO_TYPES = {"stale_state", "contradictory_state", "invalidated_branch", "safe_checkpoint_resume"}
TOOL_SCENARIO_TYPES = {"wrong_tool_selection", "omitted_tool", "tool_failure", "valid_tool_use"}
ACT_OR_ASK_SCENARIO_TYPES = {"ambiguous_goal", "infeasible_goal", "unsafe_action", "insufficient_context", "approval_required"}
FEATURE_SCENARIO_TYPES = {"feature_staged_verification", "regression_gap", "claim_to_proof_gap"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run standalone advisory Factory V3 loop-contract checks.",
    )
    parser.add_argument("--target", required=True, help="Loop-contract JSON file or directory to scan.")
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
        "record_scope": "loop_contract_advisory",
        "report_id": "factory-v3-loop-contract-lint",
        "status": _status(findings),
        "target": target.as_posix(),
        "warnings": warnings,
    }


def format_text(report: dict[str, Any]) -> str:
    lines = [
        f"factory_v3_loop_contract_lint: {report['status']}",
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
        return [_finding("V3-LC000", "advisory_critical", path_text, "loop contract root must be an object")]

    findings: list[dict[str, str]] = []
    for key in sorted(REQUIRED_TOP_LEVEL_OBJECTS):
        if not isinstance(data.get(key), dict):
            findings.append(_finding("V3-LC001", "advisory_critical", path_text, f"missing object: {key}"))

    terminal_states = data.get("terminal_states")
    if not isinstance(terminal_states, list):
        findings.append(_finding("V3-LC002", "advisory_critical", path_text, "terminal_states must be a list"))
    elif missing := sorted(REQUIRED_TERMINAL_STATES - _string_set(terminal_states)):
        findings.append(_finding("V3-LC003", "advisory_critical", path_text, f"terminal_states missing required states: {', '.join(missing)}"))

    if findings and any(item["id"] == "V3-LC001" for item in findings):
        # Continue with present sections only so malformed fixtures get specific secondary findings.
        pass

    record = data.get("record") if isinstance(data.get("record"), dict) else {}
    mission = data.get("mission") if isinstance(data.get("mission"), dict) else {}
    authority = data.get("authority_envelope") if isinstance(data.get("authority_envelope"), dict) else {}
    state_policy = data.get("state_policy") if isinstance(data.get("state_policy"), dict) else {}
    tool_policy = data.get("tool_policy") if isinstance(data.get("tool_policy"), dict) else {}
    act_or_ask = data.get("act_or_ask_gate") if isinstance(data.get("act_or_ask_gate"), dict) else {}
    control = data.get("control_profile") if isinstance(data.get("control_profile"), dict) else {}
    checkpoint = data.get("checkpoint_policy") if isinstance(data.get("checkpoint_policy"), dict) else {}
    verification = data.get("verification_policy") if isinstance(data.get("verification_policy"), dict) else {}
    evidence = data.get("evidence_policy") if isinstance(data.get("evidence_policy"), dict) else {}
    reentry = data.get("reentry_protocol") if isinstance(data.get("reentry_protocol"), dict) else {}

    findings.extend(_check_record(path_text, record))
    findings.extend(_check_mission(path_text, mission))
    findings.extend(_check_authority(path_text, authority))
    findings.extend(_check_state_policy(path_text, state_policy))
    findings.extend(_check_tool_policy(path_text, tool_policy))
    findings.extend(_check_act_or_ask(path_text, act_or_ask))
    findings.extend(_check_control_profile(path_text, control))
    findings.extend(_check_checkpoint_policy(path_text, checkpoint))
    findings.extend(_check_verification_policy(path_text, verification))
    findings.extend(_check_evidence_policy(path_text, evidence))
    findings.extend(_check_reentry_protocol(path_text, reentry))
    findings.extend(_check_fixture_scenarios(path_text, data.get("fixture_scenarios")))
    return findings


def _check_record(path: str, record: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if record.get("record_type") != RECORD_TYPE:
        findings.append(_finding("V3-LC010", "advisory_critical", path, f"record.record_type must be {RECORD_TYPE}"))
    if record.get("schema_version") != SCHEMA_VERSION:
        findings.append(_finding("V3-LC011", "advisory_critical", path, f"record.schema_version must be {SCHEMA_VERSION}"))
    if record.get("status") != "research_only_non_enforcing":
        findings.append(_finding("V3-LC012", "advisory_critical", path, "record.status must be research_only_non_enforcing"))
    if not _nonempty_string(record.get("contract_id")):
        findings.append(_finding("V3-LC013", "advisory_high", path, "record.contract_id is missing"))
    approval_scope = record.get("approval_scope")
    if not isinstance(approval_scope, dict):
        findings.append(_finding("V3-LC014", "advisory_critical", path, "record.approval_scope must be an object"))
        return findings
    for flag in sorted(UNSAFE_APPROVAL_FLAGS):
        if approval_scope.get(flag) is not False:
            findings.append(_finding("V3-LC015", "advisory_critical", path, f"unsafe approval flag must be false: {flag}"))
    if approval_scope.get("factory_v2_fallback_retained") is not True:
        findings.append(_finding("V3-LC016", "advisory_critical", path, "factory_v2_fallback_retained must be true"))
    return findings


def _check_mission(path: str, mission: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not _nonempty_string(mission.get("objective")):
        findings.append(_finding("V3-LC020", "advisory_critical", path, "mission.objective is missing"))
    if not _nonempty_string(mission.get("loop_type")):
        findings.append(_finding("V3-LC021", "advisory_high", path, "mission.loop_type is missing"))
    if not _nonempty_string(mission.get("admission_rationale")):
        findings.append(_finding("V3-LC022", "advisory_critical", path, "mission.admission_rationale is missing"))
    return findings


def _check_authority(path: str, authority: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("authorized_files", "forbidden_scope", "allowed_commands", "approval_required_for"):
        if not isinstance(authority.get(key), list) or not authority.get(key):
            findings.append(_finding("V3-LC030", "advisory_critical", path, f"authority_envelope.{key} must be a non-empty list"))
    for key in ("authorized_files",):
        for file_path in _invalid_safe_paths(authority.get(key)):
            findings.append(_finding("V3-LC031", "advisory_critical", path, f"authority_envelope.{key} contains unsafe path: {file_path}"))
    if authority.get("external_effects_allowed") is not False:
        findings.append(_finding("V3-LC032", "advisory_critical", path, "authority_envelope.external_effects_allowed must be false for advisory loop contracts"))
    return findings


def _check_state_policy(path: str, state: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(state.get("state_sources"), list) or not state.get("state_sources"):
        findings.append(_finding("V3-LC040", "advisory_critical", path, "state_policy.state_sources must be a non-empty list"))
    for key in ("write_policy", "contradiction_handling", "deletion_forgetting_policy"):
        if not _nonempty_string(state.get(key)):
            findings.append(_finding("V3-LC041", "advisory_critical", path, f"state_policy.{key} is missing"))
    for key in ("stale_state_check_required", "checkpoint_lineage_required"):
        if state.get(key) is not True:
            findings.append(_finding("V3-LC042", "advisory_critical", path, f"state_policy.{key} must be true"))
    if not isinstance(state.get("reentry_read_order"), list) or not state.get("reentry_read_order"):
        findings.append(_finding("V3-LC043", "advisory_critical", path, "state_policy.reentry_read_order must be a non-empty list"))
    return findings


def _check_tool_policy(path: str, tools: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    allowed_tools = tools.get("allowed_tools")
    if not isinstance(allowed_tools, list) or not allowed_tools:
        findings.append(_finding("V3-LC050", "advisory_critical", path, "tool_policy.allowed_tools must be a non-empty list"))
    else:
        for index, tool in enumerate(allowed_tools, start=1):
            tool_path = f"{path}:tool_policy.allowed_tools[{index}]"
            if not isinstance(tool, dict):
                findings.append(_finding("V3-LC051", "advisory_critical", tool_path, "allowed tool must be an object"))
                continue
            for key in ("name", "class", "authority_scope"):
                if not _nonempty_string(tool.get(key)):
                    findings.append(_finding("V3-LC052", "advisory_critical", tool_path, f"allowed tool missing {key}"))
    if not isinstance(tools.get("expected_tool_classes"), list) or not tools.get("expected_tool_classes"):
        findings.append(_finding("V3-LC053", "advisory_critical", path, "tool_policy.expected_tool_classes must be a non-empty list"))
    if tools.get("tool_call_evidence_required") is not True:
        findings.append(_finding("V3-LC054", "advisory_critical", path, "tool_policy.tool_call_evidence_required must be true"))
    if tools.get("omitted_tool_rationale_required") is not True:
        findings.append(_finding("V3-LC055", "advisory_critical", path, "tool_policy.omitted_tool_rationale_required must be true"))
    if tools.get("oversized_tool_menu_allowed") is not False:
        findings.append(_finding("V3-LC056", "advisory_critical", path, "tool_policy.oversized_tool_menu_allowed must be false"))
    if not _nonempty_string(tools.get("tool_failure_behavior")):
        findings.append(_finding("V3-LC057", "advisory_critical", path, "tool_policy.tool_failure_behavior is missing"))
    return findings


def _check_act_or_ask(path: str, gate: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if gate.get("required") is not True:
        findings.append(_finding("V3-LC060", "advisory_critical", path, "act_or_ask_gate.required must be true"))
    if gate.get("checked_before_action") is not True:
        findings.append(_finding("V3-LC061", "advisory_critical", path, "act_or_ask_gate.checked_before_action must be true"))
    halt_conditions = _string_set(gate.get("halt_conditions"))
    if missing := sorted(ACT_OR_ASK_TERMINALS - halt_conditions):
        findings.append(_finding("V3-LC062", "advisory_critical", path, f"act_or_ask_gate.halt_conditions missing: {', '.join(missing)}"))
    safe_hold = _string_set(gate.get("safe_hold_evidence_required"))
    required_safe_hold = {"reason", "blocked_action", "last_safe_checkpoint", "human_decision_needed", "reentry_instructions"}
    if missing := sorted(required_safe_hold - safe_hold):
        findings.append(_finding("V3-LC063", "advisory_critical", path, f"act_or_ask_gate.safe_hold_evidence_required missing: {', '.join(missing)}"))
    return findings


def _check_control_profile(path: str, control: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if control.get("detection_mode") not in APPROVED_DETECTION_MODES:
        findings.append(_finding("V3-LC070", "advisory_critical", path, "control_profile.detection_mode is invalid"))
    for key in ("prevention_gates", "escalation_path", "synchronous_required_for"):
        if not isinstance(control.get(key), list) or not control.get(key):
            findings.append(_finding("V3-LC071", "advisory_critical", path, f"control_profile.{key} must be a non-empty list"))
    for key in ("response_owner", "coverage_expectation", "recall_eval_method", "time_to_response_expectation"):
        if not _nonempty_string(control.get(key)):
            findings.append(_finding("V3-LC072", "advisory_critical", path, f"control_profile.{key} is missing"))
    return findings


def _check_checkpoint_policy(path: str, checkpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not _nonempty_string(checkpoint.get("cadence")):
        findings.append(_finding("V3-LC080", "advisory_high", path, "checkpoint_policy.cadence is missing"))
    if not isinstance(checkpoint.get("required_fields"), list) or not checkpoint.get("required_fields"):
        findings.append(_finding("V3-LC081", "advisory_critical", path, "checkpoint_policy.required_fields must be a non-empty list"))
    return findings


def _check_verification_policy(path: str, verification: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(verification.get("required_evidence"), list) or not verification.get("required_evidence"):
        findings.append(_finding("V3-LC090", "advisory_critical", path, "verification_policy.required_evidence must be a non-empty list"))
    if not isinstance(verification.get("independent_review_required"), bool):
        findings.append(_finding("V3-LC091", "advisory_critical", path, "verification_policy.independent_review_required must be boolean"))
    if not isinstance(verification.get("verification_commands"), list):
        findings.append(_finding("V3-LC092", "advisory_critical", path, "verification_policy.verification_commands must be a list"))
    return findings


def _check_evidence_policy(path: str, evidence: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(evidence.get("required_artifacts"), list) or not evidence.get("required_artifacts"):
        findings.append(_finding("V3-LC100", "advisory_critical", path, "evidence_policy.required_artifacts must be a non-empty list"))
    if evidence.get("claim_to_proof_required") is not True:
        findings.append(_finding("V3-LC101", "advisory_critical", path, "evidence_policy.claim_to_proof_required must be true"))
    return findings


def _check_reentry_protocol(path: str, reentry: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(reentry.get("state_read_order"), list) or not reentry.get("state_read_order"):
        findings.append(_finding("V3-LC110", "advisory_critical", path, "reentry_protocol.state_read_order must be a non-empty list"))
    for key in ("stale_check_required", "protected_surface_check_required", "last_safe_checkpoint_required"):
        if reentry.get(key) is not True:
            findings.append(_finding("V3-LC111", "advisory_critical", path, f"reentry_protocol.{key} must be true"))
    if not _nonempty_string(reentry.get("worker_reentry_instruction")):
        findings.append(_finding("V3-LC112", "advisory_critical", path, "reentry_protocol.worker_reentry_instruction is missing"))
    return findings


def _check_fixture_scenarios(path: str, scenarios: Any) -> list[dict[str, str]]:
    if scenarios is None:
        return []
    if not isinstance(scenarios, dict):
        return [_finding("V3-LC120", "advisory_critical", path, "fixture_scenarios must be an object when present")]

    findings: list[dict[str, str]] = []
    findings.extend(_check_memory_scenarios(path, scenarios.get("memory_reentry_cases")))
    findings.extend(_check_tool_scenarios(path, scenarios.get("tool_use_cases")))
    findings.extend(_check_act_or_ask_scenarios(path, scenarios.get("act_or_ask_cases")))
    findings.extend(_check_feature_scenarios(path, scenarios.get("feature_work_cases")))
    return findings


def _check_memory_scenarios(path: str, cases: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if cases is None:
        return findings
    if not isinstance(cases, list):
        return [_finding("V3-LC121", "advisory_critical", path, "fixture_scenarios.memory_reentry_cases must be a list")]
    for index, case in enumerate(cases, start=1):
        case_path = f"{path}:fixture_scenarios.memory_reentry_cases[{index}]"
        if not isinstance(case, dict):
            findings.append(_finding("V3-LC122", "advisory_critical", case_path, "memory reentry case must be an object"))
            continue
        scenario_type = case.get("scenario_type")
        terminal_state = case.get("expected_terminal_state")
        if scenario_type not in MEMORY_SCENARIO_TYPES:
            findings.append(_finding("V3-LC123", "advisory_critical", case_path, "memory reentry case scenario_type is invalid"))
        if terminal_state not in REQUIRED_TERMINAL_STATES:
            findings.append(_finding("V3-LC124", "advisory_critical", case_path, "memory reentry case expected_terminal_state is invalid"))
        if not isinstance(case.get("state_evidence_required"), list) or not case.get("state_evidence_required"):
            findings.append(_finding("V3-LC125", "advisory_critical", case_path, "memory reentry case state_evidence_required must be a non-empty list"))
        if not isinstance(case.get("safe_hold_required"), bool):
            findings.append(_finding("V3-LC126", "advisory_critical", case_path, "memory reentry case safe_hold_required must be boolean"))
        if not isinstance(case.get("reentry_allowed"), bool):
            findings.append(_finding("V3-LC127", "advisory_critical", case_path, "memory reentry case reentry_allowed must be boolean"))
        if scenario_type in {"stale_state", "contradictory_state", "invalidated_branch"}:
            if case.get("safe_hold_required") is not True:
                findings.append(_finding("V3-LC128", "advisory_critical", case_path, "risky memory reentry cases must require safe-hold"))
            if case.get("reentry_allowed") is not False:
                findings.append(_finding("V3-LC129", "advisory_critical", case_path, "risky memory reentry cases must not allow direct re-entry"))
        if scenario_type == "safe_checkpoint_resume" and case.get("reentry_allowed") is not True:
            findings.append(_finding("V3-LC130", "advisory_critical", case_path, "safe checkpoint resume case must allow re-entry"))
    return findings


def _check_tool_scenarios(path: str, cases: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if cases is None:
        return findings
    if not isinstance(cases, list):
        return [_finding("V3-LC131", "advisory_critical", path, "fixture_scenarios.tool_use_cases must be a list")]
    for index, case in enumerate(cases, start=1):
        case_path = f"{path}:fixture_scenarios.tool_use_cases[{index}]"
        if not isinstance(case, dict):
            findings.append(_finding("V3-LC132", "advisory_critical", case_path, "tool use case must be an object"))
            continue
        scenario_type = case.get("scenario_type")
        terminal_state = case.get("expected_terminal_state")
        if scenario_type not in TOOL_SCENARIO_TYPES:
            findings.append(_finding("V3-LC133", "advisory_critical", case_path, "tool use case scenario_type is invalid"))
        if terminal_state not in REQUIRED_TERMINAL_STATES:
            findings.append(_finding("V3-LC134", "advisory_critical", case_path, "tool use case expected_terminal_state is invalid"))
        if not isinstance(case.get("tool_evidence_required"), list) or not case.get("tool_evidence_required"):
            findings.append(_finding("V3-LC135", "advisory_critical", case_path, "tool use case tool_evidence_required must be a non-empty list"))
        if not isinstance(case.get("safe_hold_required"), bool):
            findings.append(_finding("V3-LC136", "advisory_critical", case_path, "tool use case safe_hold_required must be boolean"))
        if scenario_type == "omitted_tool" and case.get("omitted_tool_rationale_required") is not True:
            findings.append(_finding("V3-LC137", "advisory_critical", case_path, "omitted-tool cases must require omitted-tool rationale"))
        if scenario_type in {"wrong_tool_selection", "tool_failure"} and case.get("safe_hold_required") is not True:
            findings.append(_finding("V3-LC138", "advisory_critical", case_path, "wrong-tool and tool-failure cases must require safe-hold"))
    return findings


def _check_act_or_ask_scenarios(path: str, cases: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if cases is None:
        return findings
    if not isinstance(cases, list):
        return [_finding("V3-LC141", "advisory_critical", path, "fixture_scenarios.act_or_ask_cases must be a list")]
    for index, case in enumerate(cases, start=1):
        case_path = f"{path}:fixture_scenarios.act_or_ask_cases[{index}]"
        if not isinstance(case, dict):
            findings.append(_finding("V3-LC142", "advisory_critical", case_path, "act-or-ask case must be an object"))
            continue
        scenario_type = case.get("scenario_type")
        terminal_state = case.get("expected_terminal_state")
        if scenario_type not in ACT_OR_ASK_SCENARIO_TYPES:
            findings.append(_finding("V3-LC143", "advisory_critical", case_path, "act-or-ask case scenario_type is invalid"))
        if terminal_state not in ACT_OR_ASK_TERMINALS:
            findings.append(_finding("V3-LC144", "advisory_critical", case_path, "act-or-ask case expected_terminal_state must be an act/ask halt condition"))
        if case.get("checked_before_action") is not True:
            findings.append(_finding("V3-LC145", "advisory_critical", case_path, "act-or-ask case must be checked before action"))
        if case.get("safe_hold_required") is not True:
            findings.append(_finding("V3-LC146", "advisory_critical", case_path, "act-or-ask case must require safe-hold"))
    return findings


def _check_feature_scenarios(path: str, cases: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if cases is None:
        return findings
    if not isinstance(cases, list):
        return [_finding("V3-LC151", "advisory_critical", path, "fixture_scenarios.feature_work_cases must be a list")]
    for index, case in enumerate(cases, start=1):
        case_path = f"{path}:fixture_scenarios.feature_work_cases[{index}]"
        if not isinstance(case, dict):
            findings.append(_finding("V3-LC152", "advisory_critical", case_path, "feature work case must be an object"))
            continue
        scenario_type = case.get("scenario_type")
        if scenario_type not in FEATURE_SCENARIO_TYPES:
            findings.append(_finding("V3-LC153", "advisory_critical", case_path, "feature work case scenario_type is invalid"))
        if not isinstance(case.get("required_stages"), list) or not case.get("required_stages"):
            findings.append(_finding("V3-LC154", "advisory_critical", case_path, "feature work case required_stages must be a non-empty list"))
        if case.get("regression_evidence_required") is not True:
            findings.append(_finding("V3-LC155", "advisory_critical", case_path, "feature work case regression_evidence_required must be true"))
        if case.get("claim_to_proof_required") is not True:
            findings.append(_finding("V3-LC156", "advisory_critical", case_path, "feature work case claim_to_proof_required must be true"))
        if scenario_type == "feature_staged_verification" and case.get("independent_review_required") is not True:
            findings.append(_finding("V3-LC157", "advisory_critical", case_path, "feature staged-verification cases must require independent review"))
    return findings


def _status(findings: list[dict[str, str]]) -> str:
    if not findings:
        return ADVISORY_PASS
    if any(finding["severity"] == "advisory_critical" for finding in findings):
        return ADVISORY_FAIL_NON_BLOCKING
    return ADVISORY_WARN


def _recommended_next_steps(findings: list[dict[str, str]]) -> list[str]:
    if not findings:
        return ["No loop-contract findings. Keep loop contracts advisory until a promotion pack approves otherwise."]
    return [
        "Review loop-contract findings manually; this report is advisory and non-blocking.",
        "Fix missing authority, state, tool, act-or-ask, control, evidence, or re-entry fields before using the contract as mission guidance.",
        "Do not wire loop-contract checks into required gates without explicit Factory governance approval.",
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
        findings.append(_finding("V3-LC000", "advisory_critical", path.as_posix(), f"could not load JSON: {exc}"))
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
            "factory_v3_loop_contract_lint fixture mismatch",
            "Expected:",
            json.dumps(expected, indent=2, sort_keys=True),
            "Actual:",
            json.dumps(actual, indent=2, sort_keys=True),
        ]
    )


if __name__ == "__main__":
    sys.exit(main())
