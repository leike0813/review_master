from __future__ import annotations

import json
from pathlib import Path

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "evidence-supplement-failure-recovery"
REQUIRED_SNAPSHOTS = {
    "stage-1-entry-ready.json",
    "stage-2-structure-ready.json",
    "stage-3-atomic-ready.json",
    "stage-4-workboard-confirmation-needed.json",
    "stage-5-evidence-gap-blocked.json",
    "stage-5-after-bad-supplement-blocked.json",
    "stage-5-after-bad-supplement-agent-resume.md",
    "stage-5-after-bad-supplement-atomic-comment-workboard.md",
    "stage-5-after-bad-supplement-atomic_004-strategy-card.md",
    "stage-5-after-good-supplement-ready.json",
    "stage-6-export-ready.json",
    "stage-6-completed.json",
}


def _read(relative_path: str) -> str:
    return (EXAMPLE_ROOT / relative_path).read_text(encoding="utf-8")


def _read_json(relative_path: str) -> dict:
    return json.loads(_read(relative_path))


def test_failure_recovery_example_structure() -> None:
    required_dirs = [
        "inputs",
        "inputs/manuscript",
        "user-supplements",
        "user-supplements/round-1-bad",
        "user-supplements/round-2-good",
        "workspace",
        "workspace/response-strategy-cards",
        "outputs",
        "outputs/marked-manuscript",
        "outputs/revised-manuscript",
        "gate-and-render-output",
    ]
    for relative_dir in required_dirs:
        assert (EXAMPLE_ROOT / relative_dir).is_dir()

    required_files = [
        "README.md",
        "inputs/review-comments.md",
        "inputs/manuscript/main.tex",
        "user-supplements/round-1-bad/seed-loss-curve.svg",
        "user-supplements/round-1-bad/single-run-training-note.md",
        "user-supplements/round-1-bad/dev-set-checkpoints.csv",
        "user-supplements/round-2-good/seed-stability-figure.svg",
        "user-supplements/round-2-good/stability-results.csv",
        "user-supplements/round-2-good/supplement-note.md",
        "workspace/review-master.db",
        "workspace/supplement-intake-plan.md",
        "workspace/response-strategy-cards/atomic_004.md",
        "outputs/response-letter.tex",
    ]
    for relative_file in required_files:
        assert (EXAMPLE_ROOT / relative_file).is_file()


def test_failure_recovery_snapshot_contract() -> None:
    actual_snapshots = {path.name for path in (EXAMPLE_ROOT / "gate-and-render-output").iterdir() if path.is_file()}
    bad_payload = _read_json("gate-and-render-output/stage-5-after-bad-supplement-blocked.json")
    good_payload = _read_json("gate-and-render-output/stage-5-after-good-supplement-ready.json")
    export_ready_payload = _read_json("gate-and-render-output/stage-6-export-ready.json")
    completed_payload = _read_json("gate-and-render-output/stage-6-completed.json")

    assert actual_snapshots == REQUIRED_SNAPSHOTS

    assert bad_payload["status"] == "ok"
    assert bad_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "resolve_blockers"
    assert bad_payload["instruction_payload"]["resume_packet"]["active_comment_id"] == "atomic_004"
    assert bad_payload["instruction_payload"]["resume_packet"]["resume_status"] == "blocked"

    assert good_payload["status"] == "ok"
    assert good_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "advance_active_comment"
    assert good_payload["instruction_payload"]["resume_packet"]["resume_status"] == "ready_to_resume"
    assert good_payload["instruction_payload"]["resume_packet"]["active_comment_id"] == "atomic_004"

    assert export_ready_payload["status"] == "ok"
    assert export_ready_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "final_review_and_clean_export"

    assert completed_payload["status"] == "ok"
    assert completed_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"


def test_failure_recovery_assets_explain_mismatch_and_final_workspace_replays(tmp_path: Path) -> None:
    bad_resume = _read("gate-and-render-output/stage-5-after-bad-supplement-agent-resume.md")
    bad_strategy_card = _read("gate-and-render-output/stage-5-after-bad-supplement-atomic_004-strategy-card.md")
    final_resume = _read("workspace/agent-resume.md")
    final_strategy_card = _read("workspace/response-strategy-cards/atomic_004.md")
    response_latex = _read("outputs/response-letter.tex")

    assert "do not match the reviewer concern" in bad_resume
    assert "do not answer the reviewer request for multi-seed stability evidence" in bad_strategy_card
    assert "Rejected the round-1 supplement" in final_resume
    assert "Available but insufficient" in final_strategy_card
    assert "\\documentclass" in response_latex
    assert "\\begin{document}" in response_latex
    assert "\\end{document}" in response_latex

    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
    assert payload["status"] == "ok"
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
