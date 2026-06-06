#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ADVISORY_PASS = "ADVISORY_PASS"
ADVISORY_WARN = "ADVISORY_WARN"
ADVISORY_FAIL_NON_BLOCKING = "ADVISORY_FAIL_NON_BLOCKING"

DECISION_STATES = {"pre_envelope_fallback", "completed_with_v3", "halted", "blocked"}
ENVELOPE_MODES = {"not_created_pre_envelope_fallback", "thread_local", "file_artifact"}
VERIFICATION_RESULTS = {"pass", "fail", "not_run", "not_applicable"}
REVIEW_RESULTS = {"pass", "fail", "not_applicable"}
KERNEL_VALUES = {"yes", "no", "unknown"}
SCHEMA_FACTORY_V3_SHADOW = "factory_v3_shadow_v0_1"
SCHEMA_POC_STANDALONE = "poc_standalone_v0_1"
SCHEMA_POC_STANDALONE_AMC = "poc_standalone_v0_1_amc"
SCHEMA_POC_STANDALONE_FLAT = "poc_standalone_flat_v0_1"
SCHEMA_POC_LEGACY_FLAT = "poc_legacy_flat"
SCHEMA_UNKNOWN = "unknown"
POC_PROFILE_ID = "V3-POC-STANDALONE"
POC_RECORD_TYPE = "factory_v3_poc_mission_record"
POC_SCHEMA_VERSION = "v0.1-poc-standalone"
SHADOW_SCHEMA_VERSION = "v0.1-shadow"
POC_DECISION_STATES = {"draft", "completed_with_v3", "halted", "blocked", "standalone_gap"}
POC_DEPLOYMENT_TARGETS = {"private_internal", "local_only", "not_applicable", "other"}
POC_DATA_MODES = {
    "synthetic",
    "manual_local",
    "garmin_official",
    "garmin_unofficial",
    "mixed",
    "not_applicable",
}
POC_REVIEW_RESULTS = {"pass", "fail", "not_reviewed"}
POC_DEPENDENCY_MODES = {
    "garmin": {"not_used", "research_only", "official_api", "manual_import", "unofficial_client", "deferred"},
    "hermes": {"not_used", "research_only", "optional_harness", "integration_candidate"},
}

UNSAFE_APPROVAL_FLAGS = {
    "factory_v3_default_approved",
    "new_v3_profile_approved",
    "required_gate_integration_approved",
    "runtime_authority_approved",
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run standalone advisory Factory v3 mission-record checks.",
    )
    parser.add_argument("--target", required=True, help="Mission-record JSON file or directory to scan.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--expect", help="Optional expected JSON file for fixture checks.")
    parser.add_argument(
        "--record-files-only",
        action="store_true",
        help="When scanning a directory, only include likely mission-record JSON files.",
    )
    parser.add_argument(
        "--replay-evidence",
        action="store_true",
        help="Run passive, non-executing evidence replay checks against mission-record claims.",
    )
    parser.add_argument(
        "--evidence-root",
        help="Optional repository root used to resolve relative evidence paths during replay.",
    )
    args = parser.parse_args()

    report = lint_target(
        Path(args.target),
        replay_evidence=args.replay_evidence,
        evidence_root=Path(args.evidence_root) if args.evidence_root else None,
        record_files_only=args.record_files_only,
    )

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


def lint_target(
    target: Path,
    replay_evidence: bool = False,
    evidence_root: Path | None = None,
    record_files_only: bool = False,
) -> dict[str, Any]:
    files = _json_files(target, record_files_only=record_files_only)
    findings: list[dict[str, str]] = []
    schema_versions: dict[str, str] = {}
    replay_summary = _new_replay_summary(evidence_root, record_files_only) if replay_evidence else None

    for path in files:
        record = _load_record(path, findings)
        if record is None:
            continue
        schema_id = _schema_id(record)
        schema_versions[path.as_posix()] = schema_id
        findings.extend(_lint_record(path, record, schema_id))
        if replay_summary is not None and schema_id != SCHEMA_UNKNOWN:
            replay = _replay_record_evidence(path, record, schema_id, evidence_root)
            findings.extend(replay["findings"])
            _merge_replay_summary(replay_summary, replay)

    findings.sort(key=lambda item: (item["id"], item["path"], item["message"]))
    warnings = [item for item in findings if item["severity"] == "advisory_high"]

    report = {
        "blocking_effect": "none",
        "checked_records": [path.as_posix() for path in files],
        "checked_schema_versions": schema_versions,
        "findings": findings,
        "generated_at": "not_recorded",
        "recommended_next_steps": _recommended_next_steps(findings),
        "record_scope": "shadow_advisory",
        "report_id": "factory-v3-mission-record-lint",
        "status": _status(findings),
        "target": target.as_posix(),
        "warnings": warnings,
    }
    if replay_summary is not None:
        replay_findings = [item for item in findings if item["id"].startswith("V3-MR2")]
        replay_summary["claims_warned"] = replay_summary["claims_checked"] - replay_summary["claims_passed"]
        replay_summary["findings_count"] = len(replay_findings)
        replay_summary["status"] = _status(replay_findings)
        report["evidence_replay"] = replay_summary
    return report


def format_text(report: dict[str, Any]) -> str:
    lines = [
        f"factory_v3_mission_record_lint: {report['status']}",
        "blocking_effect=none",
        f"record_scope={report['record_scope']}",
        f"target={report['target']}",
        f"checked_records={len(report['checked_records'])} findings={len(report['findings'])}",
    ]
    if report["findings"]:
        lines.append("")
        lines.append("Findings:")
        for finding in report["findings"]:
            lines.append(f"- {finding['id']} [{finding['severity']}] {finding['path']}: {finding['message']}")
    lines.append("")
    lines.append("This report is advisory and non-blocking.")
    return "\n".join(lines)


def _lint_record(path: Path, data: Any, schema_id: str) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    path_text = path.as_posix()

    if not isinstance(data, dict):
        return [_finding("V3-MR000", "advisory_critical", path_text, "mission record root must be an object")]

    if schema_id == SCHEMA_POC_STANDALONE:
        return _lint_poc_standalone_record(path_text, data, require_amc=False)
    if schema_id == SCHEMA_POC_STANDALONE_AMC:
        return _lint_poc_standalone_record(path_text, data, require_amc=True)
    if schema_id == SCHEMA_POC_STANDALONE_FLAT:
        return _lint_poc_standalone_flat_record(path_text, data)
    if schema_id == SCHEMA_POC_LEGACY_FLAT:
        return _lint_poc_legacy_flat_record(path_text, data)
    if schema_id == SCHEMA_UNKNOWN:
        return [_finding("V3-MR090", "advisory_critical", path_text, "unsupported or missing mission-record schema version")]

    record = data.get("record")
    mission = data.get("mission")
    authority = data.get("authority")
    execution = data.get("execution")
    reviews = data.get("reviews")

    for name, value in (
        ("record", record),
        ("mission", mission),
        ("authority", authority),
        ("execution", execution),
        ("reviews", reviews),
    ):
        if not isinstance(value, dict):
            findings.append(_finding("V3-MR001", "advisory_critical", path_text, f"missing object: {name}"))

    if not all(isinstance(value, dict) for value in (record, mission, authority, execution, reviews)):
        return findings

    if "schema_version" in record and record.get("schema_version") != SHADOW_SCHEMA_VERSION:
        findings.append(_finding("V3-MR006", "advisory_high", path_text, f"unexpected Factory V3 shadow schema_version: {record.get('schema_version')}"))
    decision_state = record.get("decision_state")
    if decision_state not in DECISION_STATES:
        findings.append(_finding("V3-MR002", "advisory_critical", path_text, "record.decision_state is invalid or missing"))
    if record.get("record_type") != "factory_v3_mission_record":
        findings.append(_finding("V3-MR003", "advisory_critical", path_text, "record.record_type must be factory_v3_mission_record"))
    if record.get("profile_id") != "V3-OP-001":
        findings.append(_finding("V3-MR004", "advisory_critical", path_text, "record.profile_id must stay within V3-OP-001"))
    if record.get("status") != "research_only_non_enforcing":
        findings.append(_finding("V3-MR005", "advisory_critical", path_text, "record.status must be research_only_non_enforcing"))

    findings.extend(_check_approval_scope(path_text, record.get("approval_scope")))
    findings.extend(_check_mission(path_text, mission))
    findings.extend(_check_authority(path_text, authority, decision_state))
    findings.extend(_check_execution(path_text, authority, execution, decision_state))
    findings.extend(_check_reviews(path_text, reviews))
    findings.extend(_check_state_consistency(path_text, mission, authority, execution, decision_state))
    return findings


def _schema_id(data: Any) -> str:
    if not isinstance(data, dict):
        return SCHEMA_UNKNOWN
    record = data.get("record")
    if isinstance(record, dict):
        schema_version = record.get("schema_version")
        record_type = record.get("record_type")
        if record_type == "factory_v3_mission_record":
            return SCHEMA_FACTORY_V3_SHADOW
        if schema_version == POC_SCHEMA_VERSION and record_type == POC_RECORD_TYPE:
            return SCHEMA_POC_STANDALONE_AMC if isinstance(data.get("adaptive_mission_control"), dict) else SCHEMA_POC_STANDALONE
        return SCHEMA_UNKNOWN
    if data.get("schema_version") == POC_SCHEMA_VERSION:
        return SCHEMA_POC_STANDALONE_FLAT if "mission_id" in data else SCHEMA_UNKNOWN
    if {"mission_id", "status", "v3_only", "authorized_paths", "commands_run"}.issubset(data.keys()):
        return SCHEMA_POC_LEGACY_FLAT
    return SCHEMA_UNKNOWN


def _lint_poc_standalone_record(path: str, data: dict[str, Any], require_amc: bool) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    record = data.get("record")
    mission = data.get("mission")
    authority = data.get("authority")
    execution = data.get("execution")
    reviews = data.get("reviews")

    for name, value in (
        ("record", record),
        ("mission", mission),
        ("authority", authority),
        ("execution", execution),
        ("reviews", reviews),
    ):
        if not isinstance(value, dict):
            findings.append(_finding("V3-MR101", "advisory_critical", path, f"POC record missing object: {name}"))
    if not all(isinstance(value, dict) for value in (record, mission, authority, execution, reviews)):
        return findings

    decision_state = record.get("decision_state")
    if record.get("schema_version") != POC_SCHEMA_VERSION:
        findings.append(_finding("V3-MR102", "advisory_critical", path, "POC record.schema_version must be v0.1-poc-standalone"))
    if record.get("record_type") != POC_RECORD_TYPE:
        findings.append(_finding("V3-MR103", "advisory_critical", path, "POC record.record_type must be factory_v3_poc_mission_record"))
    if record.get("profile_id") != POC_PROFILE_ID:
        findings.append(_finding("V3-MR104", "advisory_critical", path, "POC record.profile_id must be V3-POC-STANDALONE"))
    if decision_state not in POC_DECISION_STATES:
        findings.append(_finding("V3-MR105", "advisory_critical", path, "POC record.decision_state is invalid or missing"))
    if record.get("v3_only") is not True:
        findings.append(_finding("V3-MR106", "advisory_critical", path, "POC record.v3_only must be true"))
    if record.get("factory_v2_used") is not False:
        findings.append(_finding("V3-MR107", "advisory_critical", path, "POC record.factory_v2_used must be false"))

    findings.extend(_check_poc_mission(path, mission))
    findings.extend(_check_poc_authority(path, authority, decision_state))
    findings.extend(_check_poc_execution(path, authority, execution, decision_state))
    findings.extend(_check_poc_reviews(path, reviews))

    amc = data.get("adaptive_mission_control")
    if require_amc:
        findings.extend(_check_poc_adaptive_mission_control(path, amc))
    elif amc is not None and not isinstance(amc, dict):
        findings.append(_finding("V3-MR130", "advisory_critical", path, "adaptive_mission_control must be an object when present"))

    dependency_evidence = data.get("dependency_evidence")
    if dependency_evidence is not None:
        findings.extend(_check_poc_dependency_evidence(path, dependency_evidence))
    return findings


def _check_poc_mission(path: str, mission: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("repository", "objective", "coding_harness"):
        if not _nonempty_string(mission.get(key)):
            findings.append(_finding("V3-MR111", "advisory_critical", path, f"POC mission.{key} is missing"))
    if mission.get("deployment_target") not in POC_DEPLOYMENT_TARGETS:
        findings.append(_finding("V3-MR112", "advisory_critical", path, "POC mission.deployment_target is invalid or missing"))
    if mission.get("data_mode") not in POC_DATA_MODES:
        findings.append(_finding("V3-MR113", "advisory_critical", path, "POC mission.data_mode is invalid or missing"))
    return findings


def _check_poc_authority(path: str, authority: dict[str, Any], decision_state: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    authorized_files = authority.get("authorized_files")
    forbidden_scope = authority.get("forbidden_scope")
    allowed_commands = authority.get("allowed_commands")
    approved_dependencies = authority.get("approved_dependencies")

    if not isinstance(authorized_files, list):
        findings.append(_finding("V3-MR114", "advisory_critical", path, "POC authority.authorized_files must be a list"))
    elif decision_state in {"completed_with_v3", "halted"} and not authorized_files:
        findings.append(_finding("V3-MR115", "advisory_critical", path, "executed POC records must include authorized files"))
    if isinstance(authorized_files, list):
        for file_path in _invalid_safe_paths(authorized_files):
            findings.append(_finding("V3-MR116", "advisory_critical", path, f"POC authorized file path is unsafe: {file_path}"))
    if not isinstance(forbidden_scope, list):
        findings.append(_finding("V3-MR117", "advisory_critical", path, "POC authority.forbidden_scope must be a list"))
    if not isinstance(allowed_commands, list):
        findings.append(_finding("V3-MR118", "advisory_critical", path, "POC authority.allowed_commands must be a list"))
    elif decision_state in {"completed_with_v3", "halted"} and not allowed_commands:
        findings.append(_finding("V3-MR119", "advisory_critical", path, "executed POC records must include allowed commands"))
    if not _nonempty_string(authority.get("dependency_policy")):
        findings.append(_finding("V3-MR120", "advisory_critical", path, "POC authority.dependency_policy is missing"))
    if not isinstance(approved_dependencies, list):
        findings.append(_finding("V3-MR121", "advisory_critical", path, "POC authority.approved_dependencies must be a list"))
    return findings


def _check_poc_execution(
    path: str,
    authority: dict[str, Any],
    execution: dict[str, Any],
    decision_state: Any,
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    files_changed = execution.get("files_changed")
    commands_run = execution.get("commands_run")
    if not isinstance(files_changed, list):
        findings.append(_finding("V3-MR122", "advisory_critical", path, "POC execution.files_changed must be a list"))
    else:
        for file_path in _invalid_safe_paths(files_changed):
            findings.append(_finding("V3-MR123", "advisory_critical", path, f"POC changed file path is unsafe: {file_path}"))
    if not isinstance(commands_run, list):
        findings.append(_finding("V3-MR124", "advisory_critical", path, "POC execution.commands_run must be a list"))

    verification = execution.get("verification")
    if not isinstance(verification, dict):
        findings.append(_finding("V3-MR125", "advisory_critical", path, "POC execution.verification must be an object"))
    else:
        result = verification.get("result")
        if not isinstance(verification.get("commands"), list):
            findings.append(_finding("V3-MR126", "advisory_critical", path, "POC execution.verification.commands must be a list"))
        if result not in VERIFICATION_RESULTS:
            findings.append(_finding("V3-MR127", "advisory_critical", path, "POC execution.verification.result is invalid or missing"))
        if decision_state == "completed_with_v3" and result != "pass":
            findings.append(_finding("V3-MR128", "advisory_critical", path, "completed POC records must have passing verification"))

    findings.extend(_check_reasoned_boolean(path, execution.get("halt"), "halt", "V3-MR129"))
    standalone_gap = execution.get("standalone_gap")
    if isinstance(standalone_gap, dict):
        if not isinstance(standalone_gap.get("found"), bool):
            findings.append(_finding("V3-MR131", "advisory_critical", path, "POC execution.standalone_gap.found must be boolean"))
    elif standalone_gap is not None:
        findings.append(_finding("V3-MR131", "advisory_critical", path, "POC execution.standalone_gap must be an object when present"))

    if isinstance(files_changed, list) and decision_state == "blocked" and files_changed:
        findings.append(_finding("V3-MR132", "advisory_critical", path, "blocked POC records must not report changed files"))
    if isinstance(files_changed, list):
        authorized_files = authority.get("authorized_files")
        if isinstance(authorized_files, list) and authorized_files:
            unauthorized = sorted(str(item) for item in files_changed if not _path_is_authorized_by_patterns(str(item), authorized_files))
            for file_path in unauthorized:
                findings.append(_finding("V3-MR133", "advisory_critical", path, f"POC changed file is outside authorized_files: {file_path}"))
    return findings


def _check_poc_adaptive_mission_control(path: str, amc: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(amc, dict):
        return [_finding("V3-MR130", "advisory_critical", path, "adaptive_mission_control must be an object")]
    for key in ("checkpoints", "human_decision_interrupts", "plan_deltas", "verification_side_effects"):
        if not isinstance(amc.get(key), list):
            findings.append(_finding("V3-MR134", "advisory_critical", path, f"adaptive_mission_control.{key} must be a list"))
    if not _nonempty_string(amc.get("mission_state_reference")) and not _nonempty_string(amc.get("mission_state_file")):
        findings.append(_finding("V3-MR135", "advisory_critical", path, "adaptive_mission_control must reference mission state"))
    git = amc.get("git")
    if git is not None:
        if not isinstance(git, dict):
            findings.append(_finding("V3-MR136", "advisory_critical", path, "adaptive_mission_control.git must be an object when present"))
        elif "allowed" in git and not isinstance(git.get("allowed"), bool):
            findings.append(_finding("V3-MR137", "advisory_critical", path, "adaptive_mission_control.git.allowed must be boolean"))
    return findings


def _check_poc_reviews(path: str, reviews: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("scope_discipline", "verification_quality", "evidence_replay"):
        if reviews.get(key) not in POC_REVIEW_RESULTS:
            findings.append(_finding("V3-MR138", "advisory_critical", path, f"POC reviews.{key} is invalid or missing"))
    notes = reviews.get("operator_friction_notes")
    if notes is not None and not isinstance(notes, list):
        findings.append(_finding("V3-MR139", "advisory_critical", path, "POC reviews.operator_friction_notes must be a list when present"))
    return findings


def _check_poc_dependency_evidence(path: str, value: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(value, dict):
        return [_finding("V3-MR140", "advisory_critical", path, "dependency_evidence must be an object")]
    for key, modes in POC_DEPENDENCY_MODES.items():
        evidence = value.get(key)
        if evidence is None:
            continue
        if not isinstance(evidence, dict):
            findings.append(_finding("V3-MR141", "advisory_critical", path, f"dependency_evidence.{key} must be an object"))
        elif evidence.get("mode") not in modes:
            findings.append(_finding("V3-MR142", "advisory_critical", path, f"dependency_evidence.{key}.mode is invalid or missing"))
    return findings


def _lint_poc_standalone_flat_record(path: str, data: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if data.get("schema_version") != POC_SCHEMA_VERSION:
        findings.append(_finding("V3-MR160", "advisory_critical", path, "flat POC schema_version must be v0.1-poc-standalone"))
    if data.get("profile_id") != POC_PROFILE_ID:
        findings.append(_finding("V3-MR161", "advisory_critical", path, "flat POC profile_id must be V3-POC-STANDALONE"))
    if not _nonempty_string(data.get("mission_id")):
        findings.append(_finding("V3-MR162", "advisory_critical", path, "flat POC mission_id is missing"))
    if data.get("v3_only") is not True:
        findings.append(_finding("V3-MR163", "advisory_critical", path, "flat POC v3_only must be true"))
    if data.get("factory_v2_used") is not False:
        findings.append(_finding("V3-MR164", "advisory_critical", path, "flat POC factory_v2_used must be false"))
    if data.get("real_data_used") is not False:
        findings.append(_finding("V3-MR165", "advisory_critical", path, "flat POC real_data_used must be false unless separately approved"))

    decision = data.get("decision")
    if decision not in {"COMPLETE", "HALTED", "BLOCKED", "STANDALONE_GAP", "DRAFT"}:
        findings.append(_finding("V3-MR166", "advisory_critical", path, "flat POC decision is invalid or missing"))
    if decision == "COMPLETE" and data.get("objective_completed") is not True:
        findings.append(_finding("V3-MR167", "advisory_critical", path, "complete flat POC records must mark objective_completed true"))

    verification = data.get("verification")
    if not isinstance(verification, dict) or not verification:
        findings.append(_finding("V3-MR168", "advisory_critical", path, "flat POC verification must be a non-empty object"))
    elif decision == "COMPLETE" and not _has_passing_verification_value(verification):
        findings.append(_finding("V3-MR169", "advisory_critical", path, "complete flat POC records must include passing verification evidence"))

    interrupts = data.get("interrupts")
    if interrupts is not None and not isinstance(interrupts, list):
        findings.append(_finding("V3-MR170", "advisory_critical", path, "flat POC interrupts must be a list when present"))
    checkpoint_commits = data.get("checkpoint_commits")
    if checkpoint_commits is not None and not isinstance(checkpoint_commits, list):
        findings.append(_finding("V3-MR171", "advisory_critical", path, "flat POC checkpoint_commits must be a list when present"))

    amc = data.get("adaptive_mission_control")
    if amc is not None:
        findings.extend(_check_poc_flat_adaptive_mission_control(path, amc))
    return findings


def _check_poc_flat_adaptive_mission_control(path: str, amc: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(amc, dict):
        return [_finding("V3-MR172", "advisory_critical", path, "flat POC adaptive_mission_control must be an object")]
    if amc.get("checkpoints_required") is True:
        checkpoints_recorded = amc.get("checkpoints_recorded")
        if not isinstance(checkpoints_recorded, int) or checkpoints_recorded <= 0:
            findings.append(_finding("V3-MR173", "advisory_critical", path, "flat POC adaptive_mission_control.checkpoints_recorded must be positive when checkpoints are required"))
    if not _nonempty_string(amc.get("mission_state_file")) and not _nonempty_string(amc.get("mission_state_reference")):
        findings.append(_finding("V3-MR174", "advisory_critical", path, "flat POC adaptive_mission_control must reference mission state"))
    required_interrupts = amc.get("human_decision_interrupts_required")
    applied_interrupts = amc.get("human_decision_interrupts_applied")
    if required_interrupts is not None and not isinstance(required_interrupts, list):
        findings.append(_finding("V3-MR175", "advisory_critical", path, "flat POC adaptive_mission_control.human_decision_interrupts_required must be a list when present"))
    if applied_interrupts is not None and not isinstance(applied_interrupts, list):
        findings.append(_finding("V3-MR176", "advisory_critical", path, "flat POC adaptive_mission_control.human_decision_interrupts_applied must be a list when present"))
    if isinstance(required_interrupts, list) and required_interrupts:
        if not isinstance(applied_interrupts, list):
            findings.append(_finding("V3-MR177", "advisory_critical", path, "flat POC adaptive_mission_control must record applied required interrupts"))
        else:
            missing = sorted(str(item) for item in required_interrupts if item not in applied_interrupts)
            for interrupt in missing:
                findings.append(_finding("V3-MR178", "advisory_critical", path, f"flat POC required interrupt was not applied: {interrupt}"))
    for key in ("halt_rules_triggered", "plan_deltas_applied"):
        if key in amc and not isinstance(amc.get(key), list):
            findings.append(_finding("V3-MR179", "advisory_critical", path, f"flat POC adaptive_mission_control.{key} must be a list"))
    return findings


def _lint_poc_legacy_flat_record(path: str, data: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = [
        _finding(
            "V3-MR150",
            "advisory_high",
            path,
            "legacy flat POC mission record should be migrated to v0.1-poc-standalone nested shape",
        )
    ]
    if data.get("v3_only") is not True:
        findings.append(_finding("V3-MR151", "advisory_critical", path, "legacy POC record.v3_only must be true"))
    if data.get("real_data_used") is not False:
        findings.append(_finding("V3-MR152", "advisory_critical", path, "legacy POC record.real_data_used must be false unless separately approved"))
    for key in ("mission_id", "status", "workspace"):
        if not _nonempty_string(data.get(key)):
            findings.append(_finding("V3-MR153", "advisory_critical", path, f"legacy POC record.{key} is missing"))
    authorized_paths = data.get("authorized_paths")
    commands_run = data.get("commands_run")
    if not isinstance(authorized_paths, list) or not authorized_paths:
        findings.append(_finding("V3-MR154", "advisory_critical", path, "legacy POC record.authorized_paths must be a non-empty list"))
    elif any(path_value for path_value in _invalid_safe_paths(authorized_paths) if not str(path_value).startswith("fixtures/")):
        for file_path in _invalid_safe_paths(authorized_paths):
            findings.append(_finding("V3-MR155", "advisory_critical", path, f"legacy POC authorized path is unsafe: {file_path}"))
    if not isinstance(commands_run, list) or not commands_run:
        findings.append(_finding("V3-MR156", "advisory_critical", path, "legacy POC record.commands_run must be a non-empty list"))
    verification_results = data.get("verification_results")
    if not isinstance(verification_results, dict) or not verification_results:
        findings.append(_finding("V3-MR157", "advisory_critical", path, "legacy POC record.verification_results must be a non-empty object"))
    elif not any(str(value).lower().startswith("pass") for value in verification_results.values()):
        findings.append(_finding("V3-MR158", "advisory_critical", path, "legacy POC record must include passing verification evidence"))
    return findings


def _check_approval_scope(path: str, approval_scope: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(approval_scope, dict):
        return [_finding("V3-MR020", "advisory_critical", path, "record.approval_scope must be an object")]

    for flag in sorted(UNSAFE_APPROVAL_FLAGS):
        if approval_scope.get(flag) is not False:
            findings.append(_finding("V3-MR021", "advisory_critical", path, f"unsafe approval flag must be false: {flag}"))
    if approval_scope.get("factory_v2_fallback_retained") is not True:
        findings.append(_finding("V3-MR022", "advisory_critical", path, "factory_v2_fallback_retained must be true"))
    return findings


def _check_mission(path: str, mission: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not _nonempty_string(mission.get("repository")):
        findings.append(_finding("V3-MR030", "advisory_high", path, "mission.repository is missing"))
    if not _nonempty_string(mission.get("objective")):
        findings.append(_finding("V3-MR031", "advisory_critical", path, "mission.objective is missing"))
    if mission.get("separate_governance_kernel_present") not in KERNEL_VALUES:
        findings.append(_finding("V3-MR032", "advisory_critical", path, "separate_governance_kernel_present is invalid"))

    envelope = mission.get("envelope")
    if not isinstance(envelope, dict):
        return findings + [_finding("V3-MR033", "advisory_critical", path, "mission.envelope must be an object")]

    mode = envelope.get("mode")
    reference = envelope.get("reference")
    if mode not in ENVELOPE_MODES:
        findings.append(_finding("V3-MR034", "advisory_critical", path, "mission.envelope.mode is invalid"))
    if mode in {"thread_local", "file_artifact"} and not _meaningful_reference(reference):
        findings.append(_finding("V3-MR035", "advisory_critical", path, "thread-local or file envelope must include a reference"))
    if mode == "not_created_pre_envelope_fallback" and not _nonempty_string(envelope.get("not_created_reason")):
        findings.append(_finding("V3-MR036", "advisory_critical", path, "pre-envelope fallback must include not_created_reason"))
    return findings


def _check_authority(path: str, authority: dict[str, Any], decision_state: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    authorized_files = authority.get("authorized_files")
    allowed_commands = authority.get("allowed_commands")
    fallback_triggers = authority.get("fallback_triggers")

    if not isinstance(authorized_files, list):
        findings.append(_finding("V3-MR040", "advisory_critical", path, "authority.authorized_files must be a list"))
    elif decision_state in {"completed_with_v3", "halted"} and not authorized_files:
        findings.append(_finding("V3-MR041", "advisory_critical", path, "executed V3 records must include authorized files"))
    if isinstance(authorized_files, list):
        for file_path in _invalid_safe_paths(authorized_files):
            findings.append(_finding("V3-MR046", "advisory_critical", path, f"authorized file path is unsafe: {file_path}"))

    if not isinstance(allowed_commands, list):
        findings.append(_finding("V3-MR042", "advisory_critical", path, "authority.allowed_commands must be a list"))
    elif decision_state in {"completed_with_v3", "halted"} and not allowed_commands:
        findings.append(_finding("V3-MR043", "advisory_critical", path, "executed V3 records must include allowed commands"))

    if authority.get("v2_fallback_required") is not True:
        findings.append(_finding("V3-MR044", "advisory_critical", path, "authority.v2_fallback_required must be true"))
    if not isinstance(fallback_triggers, list):
        findings.append(_finding("V3-MR045", "advisory_critical", path, "authority.fallback_triggers must be a list"))
    return findings


def _check_execution(
    path: str,
    authority: dict[str, Any],
    execution: dict[str, Any],
    decision_state: Any,
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    files_changed = execution.get("files_changed")
    if not isinstance(files_changed, list):
        findings.append(_finding("V3-MR050", "advisory_critical", path, "execution.files_changed must be a list"))
    else:
        for file_path in _invalid_safe_paths(files_changed):
            findings.append(_finding("V3-MR059", "advisory_critical", path, f"changed file path is unsafe: {file_path}"))

    verification = execution.get("verification")
    if not isinstance(verification, dict):
        findings.append(_finding("V3-MR051", "advisory_critical", path, "execution.verification must be an object"))
    else:
        commands = verification.get("commands")
        result = verification.get("result")
        if not isinstance(commands, list):
            findings.append(_finding("V3-MR052", "advisory_critical", path, "execution.verification.commands must be a list"))
        if result not in VERIFICATION_RESULTS:
            findings.append(_finding("V3-MR053", "advisory_critical", path, "execution.verification.result is invalid or missing"))
        if decision_state == "completed_with_v3" and result != "pass":
            findings.append(_finding("V3-MR054", "advisory_critical", path, "completed V3 records must have passing verification"))
        if decision_state == "pre_envelope_fallback" and result == "pass" and files_changed:
            findings.append(_finding("V3-MR055", "advisory_critical", path, "pre-envelope fallback cannot report changed files with passing verification"))

    halt = execution.get("halt")
    fallback = execution.get("fallback")
    findings.extend(_check_reasoned_boolean(path, halt, "halt", "V3-MR056"))
    findings.extend(_check_reasoned_boolean(path, fallback, "fallback", "V3-MR057"))

    if isinstance(files_changed, list):
        authorized_files = authority.get("authorized_files")
        if isinstance(authorized_files, list) and authorized_files:
            unauthorized = sorted(str(item) for item in files_changed if item not in authorized_files)
            for file_path in unauthorized:
                findings.append(_finding("V3-MR058", "advisory_critical", path, f"changed file is outside authorized_files: {file_path}"))
    return findings


def _check_reviews(path: str, reviews: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for key in ("simple_code_gate", "fallback_halt_review"):
        review = reviews.get(key)
        if not isinstance(review, dict):
            findings.append(_finding("V3-MR060", "advisory_critical", path, f"reviews.{key} must be an object"))
            continue
        if review.get("result") not in REVIEW_RESULTS:
            findings.append(_finding("V3-MR061", "advisory_critical", path, f"reviews.{key}.result is invalid or missing"))
    return findings


def _check_state_consistency(
    path: str,
    mission: dict[str, Any],
    authority: dict[str, Any],
    execution: dict[str, Any],
    decision_state: Any,
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    envelope = mission.get("envelope") if isinstance(mission.get("envelope"), dict) else {}
    verification = execution.get("verification") if isinstance(execution.get("verification"), dict) else {}
    halt = execution.get("halt") if isinstance(execution.get("halt"), dict) else {}
    fallback = execution.get("fallback") if isinstance(execution.get("fallback"), dict) else {}

    if decision_state == "pre_envelope_fallback":
        if envelope.get("mode") != "not_created_pre_envelope_fallback":
            findings.append(_finding("V3-MR070", "advisory_critical", path, "pre-envelope fallback must use not_created_pre_envelope_fallback envelope mode"))
        if fallback.get("used") is not True:
            findings.append(_finding("V3-MR071", "advisory_critical", path, "pre-envelope fallback records must mark fallback.used true"))

    if decision_state == "completed_with_v3":
        if fallback.get("used") is True:
            findings.append(_finding("V3-MR072", "advisory_critical", path, "completed V3 records must not mark fallback.used true"))
        if halt.get("halted") is True:
            findings.append(_finding("V3-MR073", "advisory_critical", path, "completed V3 records must not mark halt.halted true"))
        if not verification.get("commands") and not authority.get("allowed_commands"):
            findings.append(_finding("V3-MR074", "advisory_critical", path, "completed V3 records must record verification command evidence"))

    if decision_state == "halted":
        if halt.get("halted") is not True:
            findings.append(_finding("V3-MR075", "advisory_critical", path, "halted records must mark halt.halted true"))
        if verification.get("result") == "pass":
            findings.append(_finding("V3-MR076", "advisory_critical", path, "halted records must not report passing verification"))

    if decision_state == "blocked":
        if execution.get("files_changed"):
            findings.append(_finding("V3-MR077", "advisory_critical", path, "blocked records must not report changed files"))
        if verification.get("result") == "pass":
            findings.append(_finding("V3-MR078", "advisory_critical", path, "blocked records must not report passing verification"))
        if fallback.get("used") is not True:
            findings.append(_finding("V3-MR079", "advisory_critical", path, "blocked records must mark fallback.used true"))
        if halt.get("halted") is True:
            findings.append(_finding("V3-MR080", "advisory_critical", path, "blocked records must not mark halt.halted true"))
    return findings


def _check_reasoned_boolean(path: str, value: Any, name: str, check_id: str) -> list[dict[str, str]]:
    if not isinstance(value, dict):
        return [_finding(check_id, "advisory_critical", path, f"execution.{name} must be an object")]
    key = "halted" if name == "halt" else "used"
    if not isinstance(value.get(key), bool):
        return [_finding(check_id, "advisory_critical", path, f"execution.{name}.{key} must be boolean")]
    reason_codes = value.get("reason_codes")
    if not isinstance(reason_codes, list):
        return [_finding(check_id, "advisory_critical", path, f"execution.{name}.reason_codes must be a list")]
    if value.get(key) and not reason_codes:
        return [_finding(check_id, "advisory_critical", path, f"execution.{name} is true but reason_codes is empty")]
    return []


def _replay_record_evidence(
    path: Path,
    data: dict[str, Any],
    schema_id: str,
    configured_root: Path | None,
) -> dict[str, Any]:
    root = configured_root or _infer_evidence_root(path)
    root = root.resolve()
    path_text = path.as_posix()
    findings: list[dict[str, str]] = []
    checked_claims = 0
    passed_claims = 0

    if not root.exists():
        return {
            "claims_checked": 1,
            "claims_passed": 0,
            "evidence_root": root.as_posix(),
            "findings": [
                _finding("V3-MR201", "advisory_high", path_text, f"evidence replay root does not exist: {root.as_posix()}")
            ],
            "records_replayed": [path_text],
        }

    claims = _evidence_claims(path, data, schema_id)
    related_text = _related_evidence_text(path, claims["mission_token"])

    def check(condition: bool, check_id: str, message: str) -> None:
        nonlocal checked_claims, passed_claims
        checked_claims += 1
        if condition:
            passed_claims += 1
        else:
            findings.append(_finding(check_id, "advisory_high", path_text, message))

    for ref in sorted(claims["file_refs"]):
        resolved = _resolve_evidence_ref(root, ref)
        if resolved is None:
            continue
        if _contains_glob(ref):
            matches = _glob_evidence_ref(root, ref)
            check(bool(matches), "V3-MR202", f"evidence replay glob matched no files: {ref}")
            continue
        exists = resolved.exists()
        check(exists, "V3-MR203", f"evidence replay referenced file is missing: {ref}")
        if exists and resolved.suffix == ".json":
            try:
                json.loads(resolved.read_text(encoding="utf-8"))
                passed_claims += 1
            except (OSError, json.JSONDecodeError) as exc:
                findings.append(_finding("V3-MR204", "advisory_high", path_text, f"evidence replay JSON reference does not parse: {ref}: {exc}"))
            checked_claims += 1

    for checkpoint in sorted(claims["checkpoint_refs"]):
        check(
            _text_mentions_label(related_text, checkpoint),
            "V3-MR205",
            f"evidence replay checkpoint reference was not found in related evidence: {checkpoint}",
        )

    for interrupt_id in sorted(claims["interrupt_ids"]):
        interrupt_file = _interrupt_file_for_id(claims["mission_token"], interrupt_id)
        if interrupt_file:
            resolved = _resolve_evidence_ref(root, interrupt_file)
            check(
                resolved is not None and resolved.exists(),
                "V3-MR206",
                f"evidence replay interrupt file is missing for {interrupt_id}: {interrupt_file}",
            )
        else:
            check(
                interrupt_id in related_text,
                "V3-MR206",
                f"evidence replay interrupt reference was not found in related evidence: {interrupt_id}",
            )

    command_evidence = claims["verification_commands"]
    for command in command_evidence:
        check(
            _text_mentions_command(related_text, command),
            "V3-MR207",
            f"evidence replay verification command lacks external evidence mention: {command}",
        )

    for label in claims["verification_labels"]:
        check(
            _text_mentions_label(related_text, label),
            "V3-MR208",
            f"evidence replay verification label lacks external evidence mention: {label}",
        )

    return {
        "claims_checked": checked_claims,
        "claims_passed": passed_claims,
        "evidence_root": root.as_posix(),
        "findings": findings,
        "records_replayed": [path_text],
    }


def _evidence_claims(path: Path, data: dict[str, Any], schema_id: str) -> dict[str, Any]:
    file_refs: set[str] = set()
    checkpoint_refs: set[str] = set()
    interrupt_ids: set[str] = set()
    verification_commands: list[str] = []
    verification_labels: list[str] = []
    mission_token = _mission_token(path, data)

    def add_file_ref(value: Any) -> None:
        if not isinstance(value, str):
            return
        ref = _clean_ref(value)
        if ref and _looks_like_path(ref):
            file_refs.add(ref)

    if schema_id in {SCHEMA_POC_STANDALONE, SCHEMA_POC_STANDALONE_AMC}:
        record = data.get("record") if isinstance(data.get("record"), dict) else {}
        execution = data.get("execution") if isinstance(data.get("execution"), dict) else {}
        amc = data.get("adaptive_mission_control") if isinstance(data.get("adaptive_mission_control"), dict) else {}

        for value in execution.get("files_changed", []) if isinstance(execution.get("files_changed"), list) else []:
            add_file_ref(value)
        for value in amc.get("verification_side_effects", []) if isinstance(amc.get("verification_side_effects"), list) else []:
            add_file_ref(value)
        add_file_ref(amc.get("mission_state_reference"))
        add_file_ref(amc.get("mission_state_file"))
        add_file_ref(record.get("closeout_reference"))

        for value in amc.get("checkpoints", []) if isinstance(amc.get("checkpoints"), list) else []:
            _add_checkpoint_or_file_ref(value, checkpoint_refs, add_file_ref)
        for value in amc.get("human_decision_interrupts", []) if isinstance(amc.get("human_decision_interrupts"), list) else []:
            if isinstance(value, dict):
                add_file_ref(value.get("reference"))
                if _nonempty_string(value.get("interrupt_id")):
                    interrupt_ids.add(value["interrupt_id"])
            elif _nonempty_string(value):
                interrupt_ids.add(value)

        verification = execution.get("verification") if isinstance(execution.get("verification"), dict) else {}
        verification_commands.extend(_verification_commands(verification))

    elif schema_id == SCHEMA_POC_STANDALONE_FLAT:
        amc = data.get("adaptive_mission_control") if isinstance(data.get("adaptive_mission_control"), dict) else {}
        add_file_ref(amc.get("mission_state_file"))
        add_file_ref(amc.get("mission_state_reference"))
        for item in data.get("checkpoint_commits", []) if isinstance(data.get("checkpoint_commits"), list) else []:
            if isinstance(item, dict) and _nonempty_string(item.get("checkpoint")):
                checkpoint_refs.add(item["checkpoint"])
        for value in amc.get("human_decision_interrupts_required", []) if isinstance(amc.get("human_decision_interrupts_required"), list) else []:
            if _nonempty_string(value):
                interrupt_ids.add(value)
        for item in data.get("interrupts", []) if isinstance(data.get("interrupts"), list) else []:
            if isinstance(item, dict) and _nonempty_string(item.get("interrupt_id")):
                interrupt_ids.add(item["interrupt_id"])
        verification = data.get("verification") if isinstance(data.get("verification"), dict) else {}
        verification_labels.extend(str(key) for key, value in verification.items() if _has_passing_verification_value(value))

    elif schema_id == SCHEMA_POC_LEGACY_FLAT:
        for value in data.get("authorized_paths", []) if isinstance(data.get("authorized_paths"), list) else []:
            add_file_ref(value)

    else:
        execution = data.get("execution") if isinstance(data.get("execution"), dict) else {}
        mission = data.get("mission") if isinstance(data.get("mission"), dict) else {}
        for value in execution.get("files_changed", []) if isinstance(execution.get("files_changed"), list) else []:
            add_file_ref(value)
        envelope = mission.get("envelope") if isinstance(mission.get("envelope"), dict) else {}
        add_file_ref(envelope.get("reference"))
        verification = execution.get("verification") if isinstance(execution.get("verification"), dict) else {}
        verification_commands.extend(_verification_commands(verification))

    return {
        "checkpoint_refs": checkpoint_refs,
        "file_refs": file_refs,
        "interrupt_ids": interrupt_ids,
        "mission_token": mission_token,
        "verification_commands": verification_commands,
        "verification_labels": verification_labels,
    }


def _add_checkpoint_or_file_ref(value: Any, checkpoint_refs: set[str], add_file_ref: Any) -> None:
    if not isinstance(value, str):
        return
    ref = _clean_ref(value)
    if not ref:
        return
    if _looks_like_path(ref):
        add_file_ref(ref)
        if "#" in ref:
            anchor = ref.split("#", 1)[1].strip()
            if anchor:
                checkpoint_refs.add(anchor)
    else:
        checkpoint_refs.add(ref)


def _verification_commands(verification: dict[str, Any]) -> list[str]:
    commands = verification.get("commands")
    if not isinstance(commands, list):
        return []
    values: list[str] = []
    for item in commands:
        if isinstance(item, str) and item.strip():
            values.append(item.strip())
        elif isinstance(item, dict) and _nonempty_string(item.get("command")):
            values.append(item["command"].strip())
    return values


def _related_evidence_text(path: Path, mission_token: str | None) -> str:
    if not mission_token:
        return ""
    parts: list[str] = []
    for candidate in sorted(path.parent.glob(f"{mission_token}_*")):
        if candidate == path or not candidate.is_file() or candidate.suffix not in {".md", ".txt", ".json"}:
            continue
        try:
            parts.append(candidate.read_text(encoding="utf-8")[:500_000])
        except OSError:
            continue
    return "\n".join(parts)


def _infer_evidence_root(path: Path) -> Path:
    parts = path.parts
    if ".factory-v3" in parts:
        index = parts.index(".factory-v3")
        if index > 0:
            return Path(*parts[:index])
    return path.parent


def _resolve_evidence_ref(root: Path, ref: str) -> Path | None:
    clean = _clean_ref(ref)
    if not clean or "://" in clean:
        return None
    clean = clean.split("#", 1)[0]
    if not clean:
        return None
    path = Path(clean)
    if path.is_absolute():
        return path
    return root / path


def _glob_evidence_ref(root: Path, ref: str) -> list[Path]:
    clean = _clean_ref(ref).split("#", 1)[0]
    if not clean or Path(clean).is_absolute():
        return []
    return sorted(root.glob(clean))


def _contains_glob(ref: str) -> bool:
    return any(char in ref for char in "*?[")


def _looks_like_path(value: str) -> bool:
    clean = _clean_ref(value)
    if not clean or "://" in clean:
        return False
    return (
        "/" in clean
        or clean.startswith(".")
        or Path(clean.split("#", 1)[0]).suffix in {".json", ".md", ".txt", ".py", ".csv", ".html", ".css", ".js", ".sql"}
    )


def _clean_ref(value: str) -> str:
    return value.strip().strip("`").strip()


def _mission_token(path: Path, data: dict[str, Any]) -> str | None:
    candidates: list[str] = [path.name]
    if _nonempty_string(data.get("mission_id")):
        candidates.append(data["mission_id"])
    record = data.get("record") if isinstance(data.get("record"), dict) else {}
    if _nonempty_string(record.get("mission_reference")):
        candidates.append(record["mission_reference"])
    for candidate in candidates:
        match = re.search(r"MISSION_\d+", candidate)
        if match:
            return match.group(0)
    return None


def _interrupt_file_for_id(mission_token: str | None, interrupt_id: str) -> str | None:
    if not mission_token:
        return None
    match = re.fullmatch(r"HDI-(\d+)-(\d+)", interrupt_id)
    if match:
        return f".factory-v3/evidence/MISSION_{match.group(1)}_INTERRUPT_HDI{match.group(2)}.json"
    if re.fullmatch(r"HDI-\d+", interrupt_id):
        return f".factory-v3/evidence/{mission_token}_INTERRUPT_{interrupt_id}.json"
    return None


def _text_mentions_command(text: str, command: str) -> bool:
    if not command.strip():
        return True
    normalized_text = _normalize_evidence_text(text)
    normalized_command = _normalize_evidence_text(command)
    if normalized_command in normalized_text:
        return True
    first_token = normalized_command.split(" ", 1)[0]
    return first_token in {"browser", "built-in"} and "browser qa" in normalized_text


def _text_mentions_label(text: str, label: str) -> bool:
    normalized_text = _normalize_evidence_text(text)
    normalized_label = _normalize_evidence_text(label).replace("_", " ").replace("-", " ")
    return normalized_label in normalized_text or label.lower() in text.lower()


def _normalize_evidence_text(value: str) -> str:
    return " ".join(value.lower().replace("`", "").split())


def _new_replay_summary(evidence_root: Path | None, record_files_only: bool) -> dict[str, Any]:
    return {
        "blocking_effect": "none",
        "claims_checked": 0,
        "claims_passed": 0,
        "claims_warned": 0,
        "evidence_root": evidence_root.as_posix() if evidence_root else "inferred_per_record",
        "enabled": True,
        "findings_count": 0,
        "mode": "passive_non_executing",
        "record_files_only": record_files_only,
        "records_replayed": [],
        "status": ADVISORY_PASS,
    }


def _merge_replay_summary(summary: dict[str, Any], replay: dict[str, Any]) -> None:
    summary["claims_checked"] += replay["claims_checked"]
    summary["claims_passed"] += replay["claims_passed"]
    summary["records_replayed"].extend(replay["records_replayed"])


def _has_passing_verification_value(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip().lower().startswith("pass")
    if isinstance(value, dict):
        return any(_has_passing_verification_value(item) for item in value.values())
    if isinstance(value, list):
        return any(_has_passing_verification_value(item) for item in value)
    return False


def _status(findings: list[dict[str, str]]) -> str:
    if not findings:
        return ADVISORY_PASS
    if any(finding["severity"] == "advisory_critical" for finding in findings):
        return ADVISORY_FAIL_NON_BLOCKING
    return ADVISORY_WARN


def _recommended_next_steps(findings: list[dict[str, str]]) -> list[str]:
    if not findings:
        return ["No mission-record findings. Keep records shadow-only until a promotion pack approves otherwise."]
    return [
        "Review findings manually; this report is advisory and non-blocking.",
        "Classify findings as accepted, false_positive, needs_more_context, or deferred.",
        "Do not wire mission-record checks into required gates without explicit Factory governance approval.",
    ]


def _json_files(target: Path, record_files_only: bool = False) -> list[Path]:
    if not target.exists():
        raise SystemExit(f"target does not exist: {target}")
    if target.is_file():
        return [target]
    return sorted(
        path
        for path in target.rglob("*.json")
        if path.is_file() and "expected" not in path.parts
        and (not record_files_only or _likely_record_file(path))
    )


def _likely_record_file(path: Path) -> bool:
    name = path.name
    return name.endswith("_RECORD.json") or name.startswith("MR_")


def _load_record(path: Path, findings: list[dict[str, str]]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        findings.append(_finding("V3-MR000", "advisory_critical", path.as_posix(), f"could not load JSON: {exc}"))
        return None


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"failed to load expected JSON {path}: {exc}") from exc


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _meaningful_reference(value: Any) -> bool:
    return _nonempty_string(value) and value.strip().lower() not in {"none", "not_recorded"}


def _invalid_safe_paths(values: list[Any]) -> list[str]:
    invalid: list[str] = []
    for value in values:
        if not isinstance(value, str):
            invalid.append(str(value))
            continue
        path = value.strip()
        if not path or path.startswith("~") or "\\" in path:
            invalid.append(value)
            continue
        parts = PurePosixPath(path).parts
        if not parts or any(part in {"", ".", ".."} for part in parts):
            invalid.append(value)
    return invalid


def _path_is_authorized_by_patterns(path: str, patterns: list[Any]) -> bool:
    for pattern in patterns:
        if not isinstance(pattern, str):
            continue
        if pattern == path:
            return True
        if "*" in pattern and PurePosixPath(path).match(pattern):
            return True
    return False


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
            "factory_v3_mission_record_lint fixture mismatch",
            "Expected:",
            json.dumps(expected, indent=2, sort_keys=True),
            "Actual:",
            json.dumps(actual, indent=2, sort_keys=True),
        ]
    )


if __name__ == "__main__":
    sys.exit(main())
