#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ADVISORY_PASS = "ADVISORY_PASS"
ADVISORY_WARN = "ADVISORY_WARN"
ADVISORY_FAIL_NON_BLOCKING = "ADVISORY_FAIL_NON_BLOCKING"

APPROVED_EVENT_TYPES = {
    "mission_considered",
    "envelope_created",
    "authority_declared",
    "command_run",
    "file_change_summary",
    "verification_run",
    "halt_triggered",
    "reentry_checked",
    "fallback_triggered",
    "human_decision",
    "closeout_recorded",
}
APPROVED_ACTORS = {"human", "agent", "tool", "system"}
APPROVED_SOURCES = {"live", "backfill", "fixture"}
TERMINAL_EVENTS = {"closeout_recorded", "fallback_triggered"}
SAFE_EXCLUDED_MARKERS = {
    "contains_secret",
    "contains_chain_of_thought",
    "contains_full_transcript",
    "contains_source_contents",
    "contains_vendor_private_state",
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run standalone advisory Factory v3 telemetry replay checks.",
    )
    parser.add_argument("--target", required=True, help="Telemetry JSONL file or directory to scan.")
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
    files = _jsonl_files(target)
    findings: list[dict[str, str]] = []

    for path in files:
        events = _load_events(path, findings)
        if events is None:
            continue
        findings.extend(_lint_events(path, events))

    findings.sort(key=lambda item: (item["id"], item["path"], item["message"]))
    warnings = [item for item in findings if item["severity"] == "advisory_high"]

    return {
        "blocking_effect": "none",
        "checked_logs": [path.as_posix() for path in files],
        "findings": findings,
        "generated_at": "not_recorded",
        "recommended_next_steps": _recommended_next_steps(findings),
        "report_id": "factory-v3-telemetry-replay-lint",
        "status": _status(findings),
        "target": target.as_posix(),
        "warnings": warnings,
    }


def format_text(report: dict[str, Any]) -> str:
    lines = [
        f"factory_v3_telemetry_replay_lint: {report['status']}",
        "blocking_effect=none",
        f"target={report['target']}",
        f"checked_logs={len(report['checked_logs'])} findings={len(report['findings'])}",
    ]
    if report["findings"]:
        lines.append("")
        lines.append("Findings:")
        for finding in report["findings"]:
            lines.append(f"- {finding['id']} [{finding['severity']}] {finding['path']}: {finding['message']}")
    lines.append("")
    lines.append("This report is advisory and non-blocking.")
    return "\n".join(lines)


def _lint_events(path: Path, events: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    path_text = path.as_posix()
    if not events:
        return [_finding("V3-TR000", "advisory_critical", path_text, "telemetry log must contain at least one event")]

    first_mission_id: str | None = None
    first_record_id: str | None = None
    expected_sequence = 1
    authority_seen = False
    authorized_files: set[str] = set()
    allowed_commands: set[str] = set()
    terminal_seen = False
    verification_blocking = False

    for index, event in enumerate(events, start=1):
        event_path = f"{path_text}:{index}"
        findings.extend(_check_common_event_fields(event_path, event))

        mission_id = event.get("mission_id")
        record_id = event.get("record_id")
        if isinstance(mission_id, str) and mission_id:
            if first_mission_id is None:
                first_mission_id = mission_id
            elif mission_id != first_mission_id:
                findings.append(_finding("V3-TR020", "advisory_critical", event_path, "mission_id changes within telemetry log"))
        if isinstance(record_id, str) and record_id:
            if first_record_id is None:
                first_record_id = record_id
            elif record_id != first_record_id:
                findings.append(_finding("V3-TR021", "advisory_critical", event_path, "record_id changes within telemetry log"))

        sequence = event.get("sequence")
        if sequence != expected_sequence:
            findings.append(
                _finding(
                    "V3-TR030",
                    "advisory_critical",
                    event_path,
                    f"event sequence must be gap-free and monotonic: expected {expected_sequence}",
                )
            )
            if isinstance(sequence, int):
                expected_sequence = sequence
        expected_sequence += 1

        event_type = event.get("event_type")
        payload = event.get("payload")
        if not isinstance(payload, dict):
            payload = {}

        if terminal_seen:
            findings.append(_finding("V3-TR060", "advisory_critical", event_path, "event appears after terminal event"))

        if event_type == "authority_declared":
            authority_seen = True
            authorized_files = _string_set(payload.get("authorized_files"))
            allowed_commands = _string_set(payload.get("allowed_commands"))

        if event_type in {"command_run", "file_change_summary"} and not authority_seen:
            findings.append(_finding("V3-TR040", "advisory_critical", event_path, "execution event appears before authority_declared"))

        if event_type == "command_run":
            command_label = payload.get("command_label")
            if isinstance(command_label, str) and command_label not in allowed_commands:
                findings.append(_finding("V3-TR041", "advisory_critical", event_path, f"command is outside declared authority: {command_label}"))
            if verification_blocking:
                findings.append(_finding("V3-TR050", "advisory_critical", event_path, "execution appears after failed verification without halt, fallback, or human decision"))

        if event_type == "file_change_summary":
            for file_path in sorted(_string_set(payload.get("paths")) - authorized_files):
                findings.append(_finding("V3-TR042", "advisory_critical", event_path, f"file path is outside declared authority: {file_path}"))
            if verification_blocking:
                findings.append(_finding("V3-TR050", "advisory_critical", event_path, "execution appears after failed verification without halt, fallback, or human decision"))

        if event_type == "verification_run" and payload.get("result") == "fail":
            verification_blocking = True

        if event_type in {"halt_triggered", "fallback_triggered", "human_decision"}:
            verification_blocking = False

        findings.extend(_check_excluded_data(event_path, event))

        if event_type in TERMINAL_EVENTS:
            terminal_seen = True

    return findings


def _check_common_event_fields(path: str, event: Any) -> list[dict[str, str]]:
    if not isinstance(event, dict):
        return [_finding("V3-TR001", "advisory_critical", path, "telemetry event must be an object")]

    findings: list[dict[str, str]] = []
    required_strings = ("schema_version", "mission_id", "record_id", "event_id", "event_type", "occurred_at", "actor", "source", "summary")
    for key in required_strings:
        if not _nonempty_string(event.get(key)):
            findings.append(_finding("V3-TR002", "advisory_critical", path, f"missing or empty event field: {key}"))
    if not isinstance(event.get("sequence"), int):
        findings.append(_finding("V3-TR003", "advisory_critical", path, "sequence must be an integer"))
    if not isinstance(event.get("payload"), dict):
        findings.append(_finding("V3-TR004", "advisory_critical", path, "payload must be an object"))
    if event.get("event_type") not in APPROVED_EVENT_TYPES:
        findings.append(_finding("V3-TR005", "advisory_critical", path, "event_type is not approved"))
    if event.get("actor") not in APPROVED_ACTORS:
        findings.append(_finding("V3-TR006", "advisory_critical", path, "actor is not approved"))
    if event.get("source") not in APPROVED_SOURCES:
        findings.append(_finding("V3-TR007", "advisory_critical", path, "source is not approved"))
    return findings


def _check_excluded_data(path: str, event: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    markers = event.get("excluded_data_markers")
    if markers is None:
        return findings
    if not isinstance(markers, list):
        return [_finding("V3-TR070", "advisory_critical", path, "excluded_data_markers must be a list when present")]
    for marker in sorted(str(item) for item in markers):
        if marker in SAFE_EXCLUDED_MARKERS:
            findings.append(_finding("V3-TR071", "advisory_critical", path, f"excluded data marker present: {marker}"))
    return findings


def _status(findings: list[dict[str, str]]) -> str:
    if not findings:
        return ADVISORY_PASS
    if any(finding["severity"] == "advisory_critical" for finding in findings):
        return ADVISORY_FAIL_NON_BLOCKING
    return ADVISORY_WARN


def _recommended_next_steps(findings: list[dict[str, str]]) -> list[str]:
    if not findings:
        return ["No telemetry replay findings. Keep replay checks advisory until a promotion pack approves otherwise."]
    return [
        "Review telemetry replay findings manually; this report is advisory and non-blocking.",
        "Classify findings as accepted, false_positive, needs_more_context, or deferred.",
        "Do not wire telemetry replay checks into required gates without explicit Factory governance approval.",
    ]


def _jsonl_files(target: Path) -> list[Path]:
    if not target.exists():
        raise SystemExit(f"target does not exist: {target}")
    if target.is_file():
        return [target]
    return sorted(
        path
        for path in target.rglob("*.jsonl")
        if path.is_file() and "expected" not in path.parts
    )


def _load_events(path: Path, findings: list[dict[str, str]]) -> list[dict[str, Any]] | None:
    events: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        findings.append(_finding("V3-TR000", "advisory_critical", path.as_posix(), f"could not read JSONL: {exc}"))
        return None
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            findings.append(_finding("V3-TR000", "advisory_critical", f"{path.as_posix()}:{line_number}", f"could not load JSONL event: {exc}"))
            continue
        events.append(event)
    return events


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"failed to load expected JSON {path}: {exc}") from exc


def _string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str) and item}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


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
            "factory_v3_telemetry_replay_lint fixture mismatch",
            "Expected:",
            json.dumps(expected, indent=2, sort_keys=True),
            "Actual:",
            json.dumps(actual, indent=2, sort_keys=True),
        ]
    )


if __name__ == "__main__":
    sys.exit(main())
