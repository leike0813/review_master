from __future__ import annotations

from pathlib import Path

from tests.helpers import INIT_SCRIPT, run_python_script


def test_init_creates_bootstrap_workspace(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    payload = run_python_script(
        INIT_SCRIPT,
        "--artifact-root",
        str(artifact_root),
        "--document-language",
        "en",
        "--working-language",
        "zh-CN",
    )

    assert payload["status"] == "ok"
    assert (artifact_root / "review-master.db").exists()
    assert (artifact_root / "01-agent-resume.md").exists()
    assert (artifact_root / "03-style-profile.md").exists()
    assert (artifact_root / "07-review-comment-coverage.md").exists()
    assert (artifact_root / "09-supplement-suggestion-plan.md").exists()
    assert (artifact_root / "10-supplement-intake-plan.md").exists()
    assert (artifact_root / "11-manuscript-revision-guide.md").exists()
    assert (artifact_root / "15-response-letter-preview.md").exists()
    assert (artifact_root / "manuscript-copies" / "source-snapshot").exists()
    assert (artifact_root / "manuscript-copies" / "working-manuscript").exists()
    assert (artifact_root / "runtime-localization").exists()
    assert (artifact_root / "runtime-localization" / "working-messages.json").exists()
    assert (artifact_root / "runtime-localization" / "document-messages.json").exists()
    agent_resume = (artifact_root / "01-agent-resume.md").read_text(encoding="utf-8")
    response_preview = (artifact_root / "15-response-letter-preview.md").read_text(encoding="utf-8")
    assert "语言上下文" in agent_resume
    assert "`文本语言` | en" in agent_resume
    assert "`工作语言` | zh-CN" in agent_resume
    assert "# Response Letter Table Preview" in response_preview
    assert not (artifact_root / "workflow-state.md").exists()


def test_init_rejects_non_empty_target(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    artifact_root.mkdir()
    (artifact_root / "keep.txt").write_text("occupied\n", encoding="utf-8")

    payload = run_python_script(
        INIT_SCRIPT,
        "--artifact-root",
        str(artifact_root),
        "--document-language",
        "en",
        "--working-language",
        "zh-CN",
        expect_success=False,
    )

    assert payload["status"] == "error"
    assert payload["_returncode"] != 0
    assert "not empty" in payload["error"]
