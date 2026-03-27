from __future__ import annotations

import re
from pathlib import Path

from tests.helpers import ROOT


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "transformer-three-review-major-revision"
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


def test_transformer_major_revision_runtime_example_structure() -> None:
    assert EXAMPLE_ROOT.exists()

    required_dirs = [
        "reference",
        "inputs",
        "inputs/manuscript",
        "user-supplements",
        "user-supplements/round-1",
        "user-supplements/round-2",
        "user-supplements/round-3",
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
        "reference/accepted-paper.md",
        "reference/degradation-traceability.md",
        "inputs/review-comments.md",
        "inputs/manuscript/main.tex",
        "workspace/review-master.db",
        "workspace/10-supplement-intake-plan.md",
        "workspace/06-thread-to-atomic-mapping.md",
        "workspace/17-final-assembly-checklist.md",
        "workspace/11-manuscript-revision-guide.md",
        "workspace/14-response-coverage-matrix.md",
        "outputs/response-letter.md",
        "outputs/response-letter.tex",
    ]
    for relative_file in required_files:
        assert (EXAMPLE_ROOT / relative_file).is_file()


def test_transformer_major_revision_review_comments_traceability_and_mapping_align() -> None:
    review_comments = _read("inputs/review-comments.md")
    traceability = _read("reference/degradation-traceability.md")
    mapping = _read("workspace/06-thread-to-atomic-mapping.md")

    reviewer_sections = re.findall(r"^# Reviewer \d+$", review_comments, flags=re.MULTILINE)
    numbered_comments = re.findall(r"^\d+\. ", review_comments, flags=re.MULTILINE)
    expected_comment_ids = {f"R{reviewer}.{idx}" for reviewer in range(1, 4) for idx in range(1, 6)}
    mapped_comment_ids = set(re.findall(r"R\d\.\d", traceability))
    mapped_evidence_paths = set(re.findall(r"user-supplements/[^`;\n|]+", traceability))
    expected_evidence_paths = {
        str(path.relative_to(EXAMPLE_ROOT)).replace("\\", "/")
        for path in (EXAMPLE_ROOT / "user-supplements").rglob("*")
        if path.is_file()
    }
    thread_ids = set(re.findall(r"^## (reviewer_\d+_thread_\d+)", mapping, flags=re.MULTILINE))
    atomic_ids = set(re.findall(r"\|\s*(atomic_\d{3})\s*\|", mapping))

    assert len(reviewer_sections) == 3
    assert len(numbered_comments) == 15
    assert mapped_comment_ids == expected_comment_ids
    assert mapped_evidence_paths == expected_evidence_paths
    assert len(thread_ids) == 15
    assert atomic_ids == {f"atomic_{idx:03d}" for idx in range(1, 10)}


def test_transformer_major_revision_runtime_outputs_are_complete() -> None:
    actual_snapshots = {path.name for path in (EXAMPLE_ROOT / "gate-and-render-output").iterdir() if path.is_file()}
    final_checklist = _read("workspace/17-final-assembly-checklist.md")
    strategy_card = _read("workspace/response-strategy-cards/atomic_001.md")
    response_latex = _read("outputs/response-letter.tex")

    assert actual_snapshots == REQUIRED_SNAPSHOTS
    assert "manuscript_execution_items_done" in final_checklist
    assert "response_draft_done" in final_checklist
    assert "## 稿件执行项" in strategy_card
    assert "## Response 草案" in strategy_card
    assert "## Comment Blockers" in strategy_card
    assert "| working_manuscript | ready |" in final_checklist
    assert "| response_markdown | ready |" in final_checklist
    assert "| response_latex | ready |" in final_checklist
    assert "response_thread_action_log_links" in final_checklist
    assert "\\documentclass" in response_latex
    assert "\\begin{document}" in response_latex
    assert "\\end{document}" in response_latex


def test_transformer_major_revision_snapshot_actions_match_current_state_machine() -> None:
    expected_actions = {
        "stage-1-enter-stage-2.json": "enter_stage_2",
        "stage-2-enter-stage-3.json": "enter_stage_3",
        "stage-3-request-stage3-coverage-confirmation.json": "request_stage3_coverage_confirmation",
        "stage-4-request-stage4-confirmation.json": "request_stage4_confirmation",
        "stage-5-request-pending-confirmation.json": "request_pending_confirmation",
        "stage-6-completed.json": "stage_6_completed",
    }

    for snapshot_name, action_id in expected_actions.items():
        payload = _read(f"gate-and-render-output/{snapshot_name}")
        assert f'"action_id": "{action_id}"' in payload
