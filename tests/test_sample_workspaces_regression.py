from __future__ import annotations

from pathlib import Path

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script


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
        payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
        assert payload["status"] == "ok"
        assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
        assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage6_export_clean_manuscript"


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
