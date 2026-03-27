from __future__ import annotations

import sqlite3
from pathlib import Path

from tests.helpers import (
    GATE_SCRIPT,
    ROOT,
    copy_tree,
    ensure_stage5_execution_item_schema,
    ensure_supplement_suggestion_tables,
    run_python_script,
    seed_review_comment_coverage_from_threads,
)


EXAMPLE_ROOT = ROOT / "playbooks" / "examples" / "evidence-supplement-failure-recovery"


def _prepare_stage5_confirmation_case(db_path: Path, *, confirmed: bool, keep_drafts: bool = False) -> None:
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        ensure_supplement_suggestion_tables(connection)
        ensure_stage5_execution_item_schema(connection)
        connection.execute("DELETE FROM workflow_global_blockers")
        connection.execute("DELETE FROM workflow_pending_user_confirmations")
        connection.execute("DELETE FROM strategy_card_pending_confirmations WHERE comment_id = 'atomic_004'")
        connection.execute("DELETE FROM comment_blockers WHERE comment_id = 'atomic_004'")
        connection.execute("DELETE FROM supplement_suggestion_intake_links")
        connection.execute("DELETE FROM supplement_suggestion_items")
        connection.execute("DELETE FROM strategy_action_manuscript_execution_items WHERE comment_id = 'atomic_004'")
        connection.execute("UPDATE atomic_comment_state SET evidence_gap = 'yes' WHERE comment_id = 'atomic_004'")
        connection.execute(
            """
            UPDATE workflow_state
            SET current_stage = 'stage_5',
                stage_gate = ?,
                active_comment_id = 'atomic_004',
                next_action = ?
            WHERE id = 1
            """,
            ("ready" if confirmed else "blocked", "author_comment_drafts" if confirmed else "request_pending_confirmation"),
        )
        connection.execute(
            """
            UPDATE comment_completion_status
            SET manuscript_execution_items_done = ?,
                response_draft_done = ?,
                evidence_gap_closed = 'no',
                user_strategy_confirmed = ?,
                one_to_one_link_checked = 'no',
                export_ready = 'no'
            WHERE comment_id = 'atomic_004'
            """,
            (
                "yes" if keep_drafts else "no",
                "yes" if keep_drafts else "no",
                "yes" if confirmed else "no",
            ),
        )
        if not keep_drafts:
            connection.execute("DELETE FROM comment_response_drafts WHERE comment_id = 'atomic_004'")
        else:
            connection.execute(
                """
                INSERT INTO strategy_action_manuscript_execution_items (
                    comment_id, action_order, item_order, category, content_text, rationale, target_scope_note
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "atomic_004",
                    1,
                    1,
                    "text_add_modify_delete",
                    "Add a stability-analysis paragraph and a short caption note.",
                    "This preserves the confirmed strategy in manuscript-facing form.",
                    "Results::stability::paragraph-plus-caption",
                ),
            )
        if not confirmed:
            connection.execute(
                """
                INSERT INTO strategy_card_pending_confirmations (comment_id, confirmation_order, message)
                VALUES ('atomic_004', 1, 'Please confirm or edit the strategy card before draft authoring.')
                """
            )
            connection.execute(
                """
                INSERT INTO workflow_pending_user_confirmations (position, message)
                VALUES (1, 'Please confirm or edit the strategy card for atomic_004 before authoring drafts.')
                """
            )
        connection.execute(
            """
            INSERT INTO supplement_suggestion_items (
                comment_id, suggestion_order, analysis_order, request_summary, request_recommendation, status
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                "atomic_004",
                1,
                1,
                "Need multi-seed stability evidence for the generalization claim.",
                "Ask for a figure plus a metrics table so the response can cite both trend and absolute variance.",
                "confirmed" if confirmed else "provisional",
            ),
        )
        connection.commit()


def test_stage5_unconfirmed_strategy_requests_pending_confirmation(tmp_path: Path) -> None:
    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    _prepare_stage5_confirmation_case(copied_workspace / "review-master.db", confirmed=False, keep_drafts=False)

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "ok"
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "request_pending_confirmation"
    assert all(action["action_id"] != "author_comment_drafts" for action in payload["instruction_payload"]["allowed_next_actions"])
    strategy_card = (copied_workspace / "response-strategy-cards" / "atomic_004.md").read_text(encoding="utf-8")
    suggestion_view = (copied_workspace / "09-supplement-suggestion-plan.md").read_text(encoding="utf-8")
    assert "用户可以继续修改这张策略卡" in strategy_card
    assert "用户可以继续修改这张策略卡" in strategy_card
    assert "在用户确认该策略前，不得生成回复草案" in strategy_card or "在确认之前" in strategy_card
    assert "当前 active comment" in suggestion_view
    assert "atomic_004" in suggestion_view


def test_stage5_confirmed_strategy_moves_to_author_comment_drafts(tmp_path: Path) -> None:
    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    _prepare_stage5_confirmation_case(copied_workspace / "review-master.db", confirmed=True, keep_drafts=False)

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "ok"
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "author_comment_drafts"
    assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage5_replace_execution_drafts"


def test_stage5_unconfirmed_strategy_with_stale_drafts_is_invalid(tmp_path: Path) -> None:
    copied_workspace = copy_tree(EXAMPLE_ROOT / "workspace", tmp_path / "workspace")
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
    _prepare_stage5_confirmation_case(copied_workspace / "review-master.db", confirmed=False, keep_drafts=True)
    with sqlite3.connect(copied_workspace / "review-master.db") as connection:
        connection.execute("DELETE FROM workflow_pending_user_confirmations")
        connection.execute(
            """
            UPDATE workflow_state
            SET stage_gate = 'ready', next_action = 'author_comment_drafts'
            WHERE id = 1
            """
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))
    details = [item["detail"] for item in payload["consistency_errors"]]

    assert payload["status"] == "issues_found"
    assert any("unconfirmed strategy must not retain Stage 5 execution items or response drafts" in detail for detail in details)
