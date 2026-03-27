from __future__ import annotations

from pathlib import Path

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script, seed_review_comment_coverage_from_threads


def test_sample_workspaces_gate_and_render_regression(tmp_path: Path) -> None:
    for name in [
        "happy-path-minimal",
        "evidence-supplement-multi-review",
        "evidence-supplement-failure-recovery",
        "transformer-three-review-major-revision",
    ]:
        copied_workspace = copy_tree(
            ROOT / "playbooks" / "examples" / name / "workspace",
            tmp_path / name,
        )
        seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
        payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
        assert payload["status"] == "ok"
        assert payload["artifact_presence"]["supplement_suggestion_plan_view"]["status"] == "present"
        assert payload["artifact_presence"]["supplement_intake_plan_view"]["status"] == "present"
        assert payload["artifact_presence"]["review_comment_coverage_view"]["status"] == "present"
        assert payload["artifact_presence"]["runtime_localization"]["status"] == "present"
        assert payload["instruction_payload"]["resume_packet"]["language_context"]["document_language"] == "en"
        assert payload["instruction_payload"]["resume_packet"]["language_context"]["working_language"] == "zh-CN"
        assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
        assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage6_finalize_outputs"


def test_sample_response_latex_outputs_have_front_matter() -> None:
    latex_outputs = [
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "outputs" / "response-letter.tex",
        ROOT / "playbooks" / "examples" / "evidence-supplement-multi-review" / "outputs" / "response-letter.tex",
        ROOT / "playbooks" / "examples" / "evidence-supplement-failure-recovery" / "outputs" / "response-letter.tex",
        ROOT / "playbooks" / "examples" / "transformer-three-review-major-revision" / "outputs" / "response-letter.tex",
    ]
    for latex_output in latex_outputs:
        text = latex_output.read_text(encoding="utf-8")
        assert "\\documentclass" in text
        assert "\\begin{document}" in text
        assert "\\end{document}" in text
        assert "\\subsection*{ reviewer_" not in text
        assert "\\subsection*{ reviewer\\_" in text


def test_sample_workspace_checklists_use_stage5_draft_columns(tmp_path: Path) -> None:
    for name in [
        "happy-path-minimal",
        "evidence-supplement-multi-review",
        "evidence-supplement-failure-recovery",
        "transformer-three-review-major-revision",
    ]:
        workspace = copy_tree(
            ROOT / "playbooks" / "examples" / name / "workspace",
            tmp_path / name,
        )
        seed_review_comment_coverage_from_threads(workspace / "review-master.db")
        run_python_script(GATE_SCRIPT, "--artifact-root", str(workspace))
        text = (workspace / "17-final-assembly-checklist.md").read_text(encoding="utf-8")
        assert "manuscript_execution_items_done" in text
        assert "response_draft_done" in text
        assert "manuscript_change_done" not in text
        assert "response_section_done" not in text
