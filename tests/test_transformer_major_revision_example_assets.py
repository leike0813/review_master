from __future__ import annotations

import re
from pathlib import Path

from tests.helpers import ROOT


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "transformer-three-review-major-revision"
REQUIRED_SNAPSHOTS = {
    "stage-1-entry-ready.json",
    "stage-2-structure-ready.json",
    "stage-3-atomic-ready.json",
    "stage-4-workboard-confirmation-needed.json",
    "stage-5-round-1-blocked.json",
    "stage-5-round-1-ready.json",
    "stage-5-round-2-blocked.json",
    "stage-5-round-2-ready.json",
    "stage-5-round-3-blocked.json",
    "stage-5-round-3-ready.json",
    "stage-6-export-ready.json",
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
        "outputs",
        "outputs/marked-manuscript",
        "outputs/revised-manuscript",
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
        "workspace/thread-to-atomic-mapping.md",
        "workspace/final-assembly-checklist.md",
        "outputs/response-letter.md",
        "outputs/response-letter.tex",
        "outputs/marked-manuscript/main.tex",
        "outputs/revised-manuscript/main.tex",
    ]
    for relative_file in required_files:
        assert (EXAMPLE_ROOT / relative_file).is_file()


def test_transformer_major_revision_review_comments_traceability_and_mapping_align() -> None:
    review_comments = _read("inputs/review-comments.md")
    traceability = _read("reference/degradation-traceability.md")
    mapping = _read("workspace/thread-to-atomic-mapping.md")

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
    final_checklist = _read("workspace/final-assembly-checklist.md")
    response_latex = _read("outputs/response-letter.tex")

    assert actual_snapshots == REQUIRED_SNAPSHOTS
    assert "| clean_manuscript | exported |" in final_checklist
    assert "| marked_manuscript | exported |" in final_checklist
    assert "| response_markdown | exported |" in final_checklist
    assert "| response_latex | exported |" in final_checklist
    assert "\\documentclass" in response_latex
    assert "\\begin{document}" in response_latex
    assert "\\end{document}" in response_latex
