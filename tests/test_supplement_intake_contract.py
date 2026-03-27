from __future__ import annotations

import sqlite3
from pathlib import Path

import yaml  # type: ignore[import-untyped]

from tests.helpers import GATE_SCRIPT, ROOT, copy_tree, run_python_script, seed_review_comment_coverage_from_threads


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "evidence-supplement-failure-recovery"
SCHEMA_PATH = ROOT / "review-master" / "assets" / "schema" / "review-master-schema.yaml"


def _set_stage5_ready(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        UPDATE workflow_state
        SET current_stage = 'stage_5',
            stage_gate = 'ready',
            active_comment_id = 'atomic_004',
            next_action = 'advance_active_comment'
        WHERE id = 1
        """
    )
    connection.execute("DELETE FROM workflow_pending_user_confirmations")
    connection.execute("DELETE FROM workflow_global_blockers")


def test_schema_declares_supplement_tables_as_required_runtime_contract() -> None:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    required_tables = set(schema["required_tables"])
    declared_table_names = {table["name"] for table in schema["tables"]}

    for table_name in ("supplement_intake_items", "supplement_landing_links"):
        assert table_name in required_tables
        assert table_name in declared_table_names

    for table_name in ("supplement_suggestion_items", "supplement_suggestion_intake_links"):
        assert table_name in required_tables
        assert table_name in declared_table_names


def test_stage5_ready_is_blocked_when_supplement_decision_is_pending(tmp_path: Path) -> None:
    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    db_path = copied_workspace / "review-master.db"
    with sqlite3.connect(db_path) as connection:
        _set_stage5_ready(connection)
        connection.execute("DELETE FROM supplement_landing_links")
        connection.execute("DELETE FROM supplement_intake_items")
        connection.execute(
            """
            INSERT INTO supplement_intake_items(round_id, file_path, concern_summary, decision, decision_rationale)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                "round-pending",
                "user-supplements/round-pending/stability.csv",
                "multi-seed stability evidence for atomic_004",
                "",
                "",
            ),
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
    details = [item["detail"] for item in payload["consistency_errors"]]

    assert payload["status"] == "issues_found"
    assert any("pending decision" in detail for detail in details)


def test_stage5_ready_is_blocked_when_accepted_supplement_has_no_landing(tmp_path: Path) -> None:
    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    db_path = copied_workspace / "review-master.db"
    with sqlite3.connect(db_path) as connection:
        _set_stage5_ready(connection)
        connection.execute("DELETE FROM supplement_landing_links")
        connection.execute("DELETE FROM supplement_intake_items")
        connection.execute(
            """
            INSERT INTO supplement_intake_items(round_id, file_path, concern_summary, decision, decision_rationale)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                "round-ready-with-gap",
                "user-supplements/round-ready-with-gap/stability-results.csv",
                "multi-seed stability evidence for atomic_004",
                "accepted",
                "Metrics file appears relevant and was accepted.",
            ),
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
    details = [item["detail"] for item in payload["consistency_errors"]]

    assert payload["status"] == "issues_found"
    assert any("accepted supplement has no landing mapping" in detail for detail in details)


def test_failure_recovery_workspace_renders_supplement_intake_plan_view() -> None:
    text = (EXAMPLE_ROOT / "workspace" / "10-supplement-intake-plan.md").read_text(encoding="utf-8")

    assert "round-1-bad" in text
    assert "round-2-good" in text
    assert "rejected" in text
    assert "accepted" in text
    assert "atomic_004" in text
