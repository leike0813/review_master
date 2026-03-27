from __future__ import annotations

import json
from pathlib import Path

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script, seed_review_comment_coverage_from_threads


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "evidence-supplement-failure-recovery"
REQUIRED_SNAPSHOTS = {
    "stage-1-enter-stage-2.json",
    "stage-2-enter-stage-3.json",
    "stage-3-request-stage3-coverage-confirmation.json",
    "stage-4-request-stage4-confirmation.json",
    "stage-5-request-pending-confirmation.json",
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
        "workspace/manuscript-copies",
        "workspace/manuscript-copies/source-snapshot",
        "workspace/manuscript-copies/working-manuscript",
        "outputs",
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
        "workspace/10-supplement-intake-plan.md",
        "workspace/response-strategy-cards/atomic_004.md",
        "outputs/response-letter.tex",
    ]
    for relative_file in required_files:
        assert (EXAMPLE_ROOT / relative_file).is_file()


def test_failure_recovery_snapshot_contract() -> None:
    actual_snapshots = {path.name for path in (EXAMPLE_ROOT / "gate-and-render-output").iterdir() if path.is_file()}
    completed_payload = _read_json("gate-and-render-output/stage-6-completed.json")
    stage5_payload = _read_json("gate-and-render-output/stage-5-request-pending-confirmation.json")

    assert actual_snapshots == REQUIRED_SNAPSHOTS

    assert completed_payload["status"] == "ok"
    assert completed_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
    assert stage5_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "request_pending_confirmation"


def test_failure_recovery_assets_explain_mismatch_and_final_workspace_replays(tmp_path: Path) -> None:
    final_resume = _read("workspace/01-agent-resume.md")
    final_strategy_card = _read("workspace/response-strategy-cards/atomic_004.md")
    response_latex = _read("outputs/response-letter.tex")

    assert "Rejected the round-1 supplement" in final_resume
    assert "Available but insufficient" in final_strategy_card
    assert "\\documentclass" in response_latex
    assert "\\begin{document}" in response_latex
    assert "\\end{document}" in response_latex

    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
    assert payload["status"] == "ok"
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
