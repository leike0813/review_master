from __future__ import annotations

import sqlite3
from pathlib import Path

from tests.helpers import (
    GATE_SCRIPT,
    INIT_SCRIPT,
    ROOT,
    copy_tree,
    run_python_script,
    seed_review_comment_coverage_from_threads,
    write_review_comment_coverage_truth,
)


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
        "14-supplement-suggestion-plan.md",
        "15-supplement-intake-plan.md",
    ]:
        assert marker in skill_text
        assert marker in digest_text


def test_gate_and_render_happy_path_contract(tmp_path: Path) -> None:
    copied_workspace = copy_tree(
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "workspace",
        tmp_path / "workspace",
    )
    seed_review_comment_coverage_from_threads(copied_workspace / "review-master.db")
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
    assert payload["instruction_payload"]["resume_packet"]["language_context"]["document_language"] == "en"
    assert payload["instruction_payload"]["resume_packet"]["language_context"]["working_language"] == "zh-CN"
    assert "先" in payload["instruction_payload"]["recommended_next_action"]["instruction"] or "保持" in payload["instruction_payload"]["recommended_next_action"]["instruction"]
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "stage_6_completed"
    assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage6_export_clean_manuscript"


def test_stage3_requests_coverage_confirmation_before_stage4(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    run_python_script(
        INIT_SCRIPT,
        "--artifact-root",
        str(artifact_root),
        "--document-language",
        "en",
        "--working-language",
        "zh-CN",
    )
    db_path = artifact_root / "review-master.db"
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("UPDATE manuscript_summary SET main_entry = 'main.tex', project_shape = 'single_tex', high_risk_areas = 'discussion'")
        connection.executemany(
            """
            INSERT INTO raw_review_threads (thread_id, reviewer_id, thread_order, source_type, original_text, normalized_summary)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                ("reviewer_1_thread_001", "reviewer_1", 1, "reviewer_comment", "Please clarify the novelty claim and cite recent work.", "Clarify novelty claim"),
                ("reviewer_1_thread_002", "reviewer_1", 2, "reviewer_comment", "Add an ablation study for the decoder.\nDiscuss the failure case.", "Ablation and failure-case request"),
            ],
        )
        connection.executemany(
            """
            INSERT INTO atomic_comments (comment_id, comment_order, canonical_summary, required_action)
            VALUES (?, ?, ?, ?)
            """,
            [
                ("atomic_001", 1, "Clarify novelty claim", "Revise introduction and related work."),
                ("atomic_002", 2, "Add decoder ablation", "Add decoder ablation evidence."),
                ("atomic_003", 3, "Explain failure case", "Discuss failure case limitations."),
            ],
        )
        connection.executemany(
            """
            INSERT INTO raw_thread_atomic_links (thread_id, comment_id, link_order)
            VALUES (?, ?, ?)
            """,
            [
                ("reviewer_1_thread_001", "atomic_001", 1),
                ("reviewer_1_thread_002", "atomic_002", 1),
                ("reviewer_1_thread_002", "atomic_003", 2),
            ],
        )
        connection.executemany(
            """
            INSERT INTO atomic_comment_source_spans (comment_id, thread_id, excerpt_text, note)
            VALUES (?, ?, ?, ?)
            """,
            [
                ("atomic_001", "reviewer_1_thread_001", "Please clarify the novelty claim and cite recent work.", "novelty request"),
                ("atomic_002", "reviewer_1_thread_002", "Add an ablation study for the decoder.", "ablation"),
                ("atomic_003", "reviewer_1_thread_002", "Discuss the failure case.", "failure case"),
            ],
        )
        connection.execute("DELETE FROM workflow_pending_user_confirmations")
        connection.execute(
            "INSERT INTO workflow_pending_user_confirmations (position, message) VALUES (1, 'Please confirm Stage 3 extraction coverage before Stage 4.')"
        )
        connection.execute(
            """
            UPDATE workflow_state
            SET current_stage = 'stage_3', stage_gate = 'blocked', active_comment_id = NULL, next_action = 'request_stage3_coverage_confirmation'
            WHERE id = 1
            """
        )
        connection.execute(
            """
            UPDATE resume_brief
            SET resume_status = 'blocked',
                current_objective = 'Confirm Stage 3 extraction coverage.',
                current_focus = 'Review comment coverage view',
                why_paused = 'Waiting for Stage 3 coverage confirmation.',
                next_operator_action = 'Show 06-review-comment-coverage.md to the user.'
            WHERE id = 1
            """
        )
        connection.execute("DELETE FROM resume_recent_decisions")
        connection.execute("DELETE FROM resume_must_not_forget")
        connection.execute(
            "INSERT INTO resume_recent_decisions (position, message) VALUES (1, 'Stage 3 split reviewer comments into three canonical atomic items.')"
        )
        connection.execute(
            "INSERT INTO resume_must_not_forget (position, message) VALUES (1, 'Do not enter Stage 4 before the user confirms Stage 3 coverage.')"
        )
        connection.commit()

    write_review_comment_coverage_truth(
        db_path,
        [
            {
                "source_document_id": "review_comments_source_001",
                "source_kind": "review_comments_source",
                "document_order": 1,
                "source_label": "Review Comments Source",
                "source_path": "tests://review-comments.md",
                "original_text": (
                    "Please clarify the novelty claim and cite recent work.\n\n"
                    "The manuscript currently only provides a heading-level statement, while the detailed rationale, "
                    "expected scope, and concrete evaluation requests remain in this paragraph and should be tracked "
                    "as supporting coverage instead of staying invisible in the review trace.\n\n"
                    "Add an ablation study for the decoder.\n"
                    "Discuss the failure case.\n"
                    "This final sentence is still uncovered.\n\n"
                ),
                "segments": [
                    {
                        "coverage_status": "covered",
                        "segment_text": "Please clarify the novelty claim and cite recent work.",
                        "thread_id": "reviewer_1_thread_001",
                        "span_role": "primary",
                        "comment_ids": ["atomic_001"],
                    },
                    {
                        "coverage_status": "covered",
                        "segment_text": (
                            "\n\n"
                            "The manuscript currently only provides a heading-level statement, while the detailed rationale, "
                            "expected scope, and concrete evaluation requests remain in this paragraph and should be tracked "
                            "as supporting coverage instead of staying invisible in the review trace.\n\n"
                        ),
                        "thread_id": "reviewer_1_thread_001",
                        "span_role": "supporting",
                        "comment_ids": ["atomic_001"],
                    },
                    {
                        "coverage_status": "covered",
                        "segment_text": "Add an ablation study for the decoder.\nDiscuss the failure case.",
                        "thread_id": "reviewer_1_thread_002",
                        "span_role": "primary",
                        "comment_ids": ["atomic_002", "atomic_003"],
                    },
                    {
                        "coverage_status": "uncovered",
                        "segment_text": "\nThis final sentence is still uncovered.\n\n",
                        "thread_id": None,
                        "comment_ids": [],
                    },
                ],
            },
            {
                "source_document_id": "editor_letter_source_001",
                "source_kind": "editor_letter_source",
                "document_order": 2,
                "source_label": "Editor Letter Source",
                "source_path": "tests://editor-letter.txt",
                "original_text": "Editor note: keep wording concise.",
                "segments": [
                    {
                        "coverage_status": "covered",
                        "segment_text": "Editor note: keep wording concise.",
                        "thread_id": "reviewer_1_thread_001",
                        "span_role": "duplicate_filtered",
                        "comment_ids": ["atomic_001"],
                    }
                ],
            },
        ],
    )

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(artifact_root))

    assert payload["status"] == "ok"
    assert payload["instruction_payload"]["recommended_next_action"]["action_id"] == "request_stage3_coverage_confirmation"
    assert payload["instruction_payload"]["recommended_next_action"]["recipe_id"] == "recipe_stage3_clear_coverage_confirmation"
    assert isinstance(payload["instruction_payload"]["coverage_review_advisories"], list)
    assert all(action["action_id"] != "enter_stage_4" for action in payload["instruction_payload"]["allowed_next_actions"])
    coverage_view = (artifact_root / "06-review-comment-coverage.md").read_text(encoding="utf-8")
    assert "[[covered" not in coverage_view
    assert "color: #d32f2f" in coverage_view
    assert "color: #f57c00" in coverage_view
    assert "[R1_T001 dup]" in coverage_view
    assert "[R1_T002]" in coverage_view
    assert "Please clarify the novelty claim and cite recent work." in coverage_view
    assert "覆盖映射附录" in coverage_view
    assert "`reviewer_1_thread_002`" in coverage_view
    assert "`duplicate_filtered`" in coverage_view
    assert "`atomic_002, atomic_003`" in coverage_view
    assert "This final sentence is still uncovered." in coverage_view
    assert "Editor Letter Source" in coverage_view
    raw_threads_view = (artifact_root / "03-raw-review-thread-list.md").read_text(encoding="utf-8")
    assert "expected scope, and concrete evaluation requests remain in this paragraph" in raw_threads_view

    with sqlite3.connect(db_path) as connection:
        connection.execute("DELETE FROM workflow_pending_user_confirmations")
        connection.execute(
            """
            UPDATE workflow_state
            SET current_stage = 'stage_3', stage_gate = 'ready', active_comment_id = NULL, next_action = 'enter_stage_4'
            WHERE id = 1
            """
        )
        connection.execute(
            """
            UPDATE resume_brief
            SET resume_status = 'active',
                why_paused = 'Stage 3 coverage confirmation completed.',
                next_operator_action = 'Enter Stage 4 workboard planning.'
            WHERE id = 1
            """
        )
        connection.commit()

    cleared_payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(artifact_root))
    assert cleared_payload["status"] == "ok"
    assert cleared_payload["instruction_payload"]["recommended_next_action"]["action_id"] == "enter_stage_4"


def test_stage3_missing_thread_source_spans_is_blocked(tmp_path: Path) -> None:
    artifact_root = tmp_path / "workspace"
    copied_workspace = copy_tree(
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "workspace",
        artifact_root,
    )
    db_path = copied_workspace / "review-master.db"
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            UPDATE workflow_state
            SET current_stage = 'stage_3', stage_gate = 'ready', active_comment_id = NULL, next_action = 'enter_stage_4'
            WHERE id = 1
            """
        )
        connection.execute("DELETE FROM atomic_comment_state")
        connection.execute("DELETE FROM atomic_comment_target_locations")
        connection.execute("DELETE FROM atomic_comment_analysis_links")
        connection.execute("DELETE FROM workflow_pending_user_confirmations")
        connection.execute("DELETE FROM workflow_global_blockers")
        connection.execute(
            """
            UPDATE resume_brief
            SET resume_status = 'active',
                current_objective = 'Validate Stage 3 coverage truth.',
                current_focus = 'Stage 3',
                why_paused = 'Coverage review should pass before Stage 4.',
                next_operator_action = 'Inspect 06-review-comment-coverage.md.'
            WHERE id = 1
            """
        )
        connection.execute("DELETE FROM resume_recent_decisions")
        connection.execute("DELETE FROM resume_must_not_forget")
        connection.execute("INSERT INTO resume_recent_decisions (position, message) VALUES (1, 'Reset sample workspace to Stage 3 for coverage validation.')")
        connection.execute("INSERT INTO resume_must_not_forget (position, message) VALUES (1, 'Covered segments must link to comment_id records.')")
        connection.commit()

    seed_review_comment_coverage_from_threads(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            DELETE FROM raw_thread_source_spans
            WHERE thread_id = 'reviewer_1_thread_001'
            """
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "issues_found"
    assert payload["summary"]["total_issue_count"] > 0
    assert any(
        issue["artifact"] == "raw_thread_source_spans"
        for issue in payload["format_errors"] + payload["dependency_errors"]
    )


def test_stage3_invalid_source_span_offsets_are_blocked(tmp_path: Path) -> None:
    copied_workspace = copy_tree(
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "workspace",
        tmp_path / "workspace",
    )
    db_path = copied_workspace / "review-master.db"
    seed_review_comment_coverage_from_threads(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            UPDATE raw_thread_source_spans
            SET end_offset = end_offset + 5000
            WHERE thread_id = (
                SELECT thread_id
                FROM raw_thread_source_spans
                ORDER BY thread_id, source_document_id, span_order
                LIMIT 1
            )
            """
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "issues_found"
    assert any(
        issue["artifact"] == "raw_thread_source_spans" and issue["issue"] in {"span_out_of_bounds", "span_text_mismatch"}
        for issue in payload["format_errors"] + payload["dependency_errors"]
    )


def test_stage3_thread_requires_primary_span(tmp_path: Path) -> None:
    copied_workspace = copy_tree(
        ROOT / "playbooks" / "examples" / "happy-path-minimal" / "workspace",
        tmp_path / "workspace",
    )
    db_path = copied_workspace / "review-master.db"
    seed_review_comment_coverage_from_threads(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            UPDATE raw_thread_source_spans
            SET span_role = 'supporting'
            WHERE thread_id = (
                SELECT thread_id
                FROM raw_thread_source_spans
                ORDER BY thread_id, source_document_id, span_order
                LIMIT 1
            )
            """
        )
        connection.commit()

    payload = run_python_script(GATE_SCRIPT, "--artifact-root", str(copied_workspace))

    assert payload["status"] == "issues_found"
    assert any(
        issue["artifact"] == "raw_thread_source_spans" and issue["issue"] == "missing_primary_span"
        for issue in payload["format_errors"] + payload["dependency_errors"]
    )
