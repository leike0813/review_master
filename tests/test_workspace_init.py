from __future__ import annotations

from pathlib import Path

from tests.helpers import INIT_SCRIPT, run_python_script


def test_init_creates_bootstrap_workspace(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    payload = run_python_script(INIT_SCRIPT, "--artifact-root", str(artifact_root))

    assert payload["status"] == "ok"
    assert (artifact_root / "review-master.db").exists()
    assert (artifact_root / "agent-resume.md").exists()
    assert (artifact_root / "export-patch-plan.md").exists()
    assert (artifact_root / "supplement-intake-plan.md").exists()
    assert not (artifact_root / "workflow-state.md").exists()


def test_init_rejects_non_empty_target(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    artifact_root.mkdir()
    (artifact_root / "keep.txt").write_text("occupied\n", encoding="utf-8")

    payload = run_python_script(INIT_SCRIPT, "--artifact-root", str(artifact_root), expect_success=False)

    assert payload["status"] == "error"
    assert payload["_returncode"] != 0
    assert "not empty" in payload["error"]
