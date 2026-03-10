from __future__ import annotations

from pathlib import Path

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script


def test_runtime_digest_and_skill_contract_terms_align() -> None:
    skill_text = (ROOT / "review-master" / "SKILL.md").read_text(encoding="utf-8")
    digest_text = (ROOT / "review-master" / "assets" / "runtime" / "skill-runtime-digest.md").read_text(encoding="utf-8")

    for marker in [
        "marked_manuscript",
        "clean_manuscript",
        "response_markdown",
        "response_latex",
        "gate-and-render",
        "export_patch_sets",
        "export_patches",
        "supplement-intake-plan.md",
    ]:
        assert marker in skill_text
        assert marker in digest_text


def test_gate_and_render_happy_path_contract(tmp_path: Path) -> None:
    copied_workspace = copy_tree(
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "workspace",
        tmp_path / "workspace",
    )
    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "ok"
    assert payload["artifact_presence"]["export_patch_plan_view"]["status"] == "present"
    assert payload["instruction_payload"]["resume_packet"]["resume_status"] in {
        "bootstrap",
        "active",
        "blocked",
        "ready_to_resume",
        "completed",
    }
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
    assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage6_export_clean_manuscript"
