from __future__ import annotations

from collections import defaultdict
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "review-master" / "scripts"
INIT_SCRIPT = SCRIPTS_DIR / "init_artifact_workspace.py"
GATE_SCRIPT = SCRIPTS_DIR / "gate_and_render_workspace.py"
EXPORT_SCRIPT = SCRIPTS_DIR / "export_manuscript_variants.py"


def run_python_script(script_path: Path, *args: str, expect_success: bool = True) -> dict:
    completed = subprocess.run(
        [sys.executable, "-u", str(script_path), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if expect_success and completed.returncode != 0:
        raise AssertionError(
            f"{script_path.name} failed with code {completed.returncode}\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    if not expect_success and completed.returncode == 0:
        raise AssertionError(f"{script_path.name} unexpectedly succeeded\nSTDOUT:\n{completed.stdout}")
    payload = json.loads(completed.stdout)
    payload["_returncode"] = completed.returncode
    payload["_stderr"] = completed.stderr
    return payload


def copy_tree(source: Path, target: Path) -> Path:
    shutil.copytree(source, target)
    return target


def strip_changes_markup(text: str) -> str:
    updated = text.replace("\\usepackage[markup=default]{changes}\n", "")
    pattern_replaced = re.compile(r"\\replaced\{([^{}]*)\}\{([^{}]*)\}")
    pattern_added = re.compile(r"\\added\{([^{}]*)\}")
    previous = None
    while previous != updated:
        previous = updated
        updated = pattern_replaced.sub(r"\1", updated)
        updated = pattern_added.sub(r"\1", updated)
    return updated


def ensure_review_comment_coverage_tables(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS review_comment_source_documents (
            source_document_id TEXT PRIMARY KEY,
            source_kind TEXT NOT NULL CHECK (source_kind IN ('review_comments_source', 'editor_letter_source')),
            document_order INTEGER NOT NULL,
            source_label TEXT NOT NULL DEFAULT '',
            source_path TEXT NOT NULL DEFAULT '',
            original_text TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_thread_source_spans (
            thread_id TEXT NOT NULL REFERENCES raw_review_threads(thread_id) ON DELETE CASCADE,
            source_document_id TEXT NOT NULL REFERENCES review_comment_source_documents(source_document_id) ON DELETE CASCADE,
            span_order INTEGER NOT NULL,
            span_role TEXT NOT NULL CHECK (span_role IN ('primary', 'supporting', 'duplicate_filtered')),
            start_offset INTEGER NOT NULL CHECK (start_offset >= 0),
            end_offset INTEGER NOT NULL CHECK (end_offset > start_offset),
            span_text TEXT NOT NULL,
            PRIMARY KEY (thread_id, source_document_id, span_order)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS review_comment_coverage_segments (
            source_document_id TEXT NOT NULL REFERENCES review_comment_source_documents(source_document_id) ON DELETE CASCADE,
            segment_order INTEGER NOT NULL,
            coverage_status TEXT NOT NULL CHECK (coverage_status IN ('covered', 'uncovered')),
            segment_text TEXT NOT NULL,
            thread_id TEXT REFERENCES raw_review_threads(thread_id) ON DELETE SET NULL,
            PRIMARY KEY (source_document_id, segment_order)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS review_comment_coverage_segment_comment_links (
            source_document_id TEXT NOT NULL,
            segment_order INTEGER NOT NULL,
            link_order INTEGER NOT NULL,
            comment_id TEXT NOT NULL REFERENCES atomic_comments(comment_id) ON DELETE CASCADE,
            PRIMARY KEY (source_document_id, segment_order, link_order),
            FOREIGN KEY (source_document_id, segment_order)
                REFERENCES review_comment_coverage_segments(source_document_id, segment_order)
                ON DELETE CASCADE
        )
        """
    )


def ensure_supplement_suggestion_tables(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS supplement_suggestion_items (
            comment_id TEXT NOT NULL REFERENCES atomic_comments(comment_id) ON DELETE CASCADE,
            suggestion_order INTEGER NOT NULL,
            analysis_order INTEGER,
            request_summary TEXT NOT NULL DEFAULT '',
            request_recommendation TEXT NOT NULL DEFAULT '',
            status TEXT NOT NULL CHECK (status IN ('provisional', 'confirmed', 'linked', 'satisfied', 'dismissed')),
            PRIMARY KEY (comment_id, suggestion_order)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS supplement_suggestion_intake_links (
            comment_id TEXT NOT NULL,
            suggestion_order INTEGER NOT NULL,
            round_id TEXT NOT NULL,
            file_path TEXT NOT NULL,
            link_note TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (comment_id, suggestion_order, round_id, file_path),
            FOREIGN KEY (comment_id, suggestion_order)
                REFERENCES supplement_suggestion_items(comment_id, suggestion_order)
                ON DELETE CASCADE,
            FOREIGN KEY (round_id, file_path)
                REFERENCES supplement_intake_items(round_id, file_path)
                ON DELETE CASCADE
        )
        """
    )


def ensure_stage5_execution_item_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS strategy_action_manuscript_execution_items (
            comment_id TEXT NOT NULL,
            action_order INTEGER NOT NULL,
            item_order INTEGER NOT NULL,
            category TEXT NOT NULL CHECK (category IN ('modification_strategy', 'rewrite_polish', 'text_add_modify_delete', 'figure_update', 'data_supplement')),
            content_text TEXT NOT NULL DEFAULT '',
            rationale TEXT NOT NULL DEFAULT '',
            target_scope_note TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (comment_id, action_order, item_order),
            FOREIGN KEY (comment_id, action_order)
                REFERENCES strategy_card_actions(comment_id, action_order)
                ON DELETE CASCADE
        )
        """
    )
    columns = list(connection.execute("PRAGMA table_info(comment_completion_status)").fetchall())
    if not any(str(column[1]) == "manuscript_execution_items_done" for column in columns):
        connection.execute(
            "ALTER TABLE comment_completion_status ADD COLUMN manuscript_execution_items_done TEXT NOT NULL DEFAULT 'no'"
        )
    has_legacy_column = any(str(column[1]) == "manuscript_draft_done" for column in columns)
    if has_legacy_column:
        connection.execute(
            """
            UPDATE comment_completion_status
            SET manuscript_execution_items_done = manuscript_draft_done
            WHERE manuscript_execution_items_done IS NULL
               OR TRIM(manuscript_execution_items_done) = ''
               OR manuscript_execution_items_done = 'no'
            """
        )
    else:
        connection.execute(
            """
            UPDATE comment_completion_status
            SET manuscript_execution_items_done = 'no'
            WHERE manuscript_execution_items_done IS NULL OR TRIM(manuscript_execution_items_done) = ''
            """
        )


def ensure_stage6_revision_loop_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS workspace_manuscript_copies (
            copy_role TEXT PRIMARY KEY,
            source_kind TEXT NOT NULL CHECK (source_kind IN ('single_tex_file', 'project_directory')),
            source_root TEXT NOT NULL DEFAULT '',
            copy_root TEXT NOT NULL DEFAULT '',
            main_entry_relative_path TEXT NOT NULL DEFAULT ''
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_plan_actions (
            plan_action_id TEXT PRIMARY KEY,
            plan_order INTEGER NOT NULL,
            comment_id TEXT NOT NULL,
            action_order INTEGER NOT NULL,
            execution_category TEXT NOT NULL DEFAULT 'modification_strategy',
            title TEXT NOT NULL DEFAULT '',
            objective TEXT NOT NULL DEFAULT '',
            suggested_change TEXT NOT NULL DEFAULT '',
            evidence_requirement TEXT NOT NULL DEFAULT '',
            status TEXT NOT NULL CHECK (status IN ('todo', 'blocked', 'in_progress', 'completed', 'dismissed'))
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_plan_dependencies (
            plan_action_id TEXT NOT NULL,
            depends_on_plan_action_id TEXT NOT NULL,
            PRIMARY KEY (plan_action_id, depends_on_plan_action_id)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_action_logs (
            log_id TEXT PRIMARY KEY,
            log_order INTEGER NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('draft', 'completed', 'cancelled')),
            operator_role TEXT NOT NULL CHECK (operator_role IN ('agent', 'user', 'collaborative')),
            summary TEXT NOT NULL DEFAULT '',
            change_note TEXT NOT NULL DEFAULT '',
            response_note TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL DEFAULT ''
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_action_log_plan_links (
            log_id TEXT NOT NULL,
            plan_action_id TEXT NOT NULL,
            PRIMARY KEY (log_id, plan_action_id)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_action_log_thread_links (
            log_id TEXT NOT NULL,
            thread_id TEXT NOT NULL,
            PRIMARY KEY (log_id, thread_id)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS revision_action_log_file_diffs (
            log_id TEXT NOT NULL,
            file_order INTEGER NOT NULL,
            relative_path TEXT NOT NULL,
            change_kind TEXT NOT NULL CHECK (change_kind IN ('modified', 'added', 'deleted')),
            diff_excerpt TEXT NOT NULL DEFAULT '',
            before_excerpt TEXT NOT NULL DEFAULT '',
            after_excerpt TEXT NOT NULL DEFAULT '',
            PRIMARY KEY (log_id, file_order)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS working_copy_file_state (
            relative_path TEXT PRIMARY KEY,
            snapshot_sha256 TEXT NOT NULL DEFAULT '',
            last_audited_sha256 TEXT NOT NULL DEFAULT '',
            current_sha256 TEXT NOT NULL DEFAULT '',
            last_log_id TEXT NOT NULL DEFAULT ''
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS response_thread_action_log_links (
            thread_id TEXT NOT NULL,
            log_id TEXT NOT NULL,
            link_order INTEGER NOT NULL,
            PRIMARY KEY (thread_id, log_id)
        )
        """
    )
    columns = list(connection.execute("PRAGMA table_info(response_thread_rows)").fetchall())
    if not any(str(column[1]) == "response_resolution_kind" for column in columns):
        connection.execute(
            "ALTER TABLE response_thread_rows ADD COLUMN response_resolution_kind TEXT NOT NULL DEFAULT 'revision_backed'"
        )
    connection.execute(
        """
        UPDATE response_thread_rows
        SET response_resolution_kind = 'revision_backed'
        WHERE response_resolution_kind IS NULL OR TRIM(response_resolution_kind) = ''
        """
    )
    connection.execute(
        """
        INSERT OR IGNORE INTO export_artifacts (artifact_name, artifact_status, output_path)
        VALUES
            ('working_manuscript', 'pending', ''),
            ('response_markdown', 'pending', ''),
            ('response_latex', 'pending', ''),
            ('latexdiff_manuscript', 'pending', '')
        """
    )


def seed_stage6_revision_loop_from_legacy_state(db_path: Path) -> None:
    artifact_root = db_path.parent
    source_snapshot_root = artifact_root / "manuscript-copies" / "source-snapshot"
    working_manuscript_root = artifact_root / "manuscript-copies" / "working-manuscript"
    source_snapshot_root.mkdir(parents=True, exist_ok=True)
    working_manuscript_root.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        ensure_stage6_revision_loop_schema(connection)
        stage_row = connection.execute("SELECT current_stage FROM workflow_state WHERE id = 1").fetchone()
        if stage_row is None or str(stage_row["current_stage"]) != "stage_6":
            connection.commit()
            return
        connection.execute(
            """
            INSERT OR REPLACE INTO workspace_manuscript_copies (
                copy_role, source_kind, source_root, copy_root, main_entry_relative_path
            ) VALUES
                ('source_snapshot', 'project_directory', ?, ?, 'main.tex'),
                ('working_manuscript', 'project_directory', ?, ?, 'main.tex')
            """,
            (
                str(source_snapshot_root),
                str(source_snapshot_root),
                str(working_manuscript_root),
                str(working_manuscript_root),
            ),
        )
        if connection.execute("SELECT 1 FROM revision_plan_actions LIMIT 1").fetchone() is None:
            strategy_action_columns = {str(row[1]) for row in connection.execute("PRAGMA table_info(strategy_card_actions)").fetchall()}
            summary_column = "action_summary" if "action_summary" in strategy_action_columns else "manuscript_change"
            rationale_column = "rationale" if "rationale" in strategy_action_columns else "expected_response_letter_effect"
            action_rows = list(
                connection.execute(
                    f"""
                    SELECT sca.comment_id, sca.action_order,
                           COALESCE(sca.{summary_column}, '') AS summary_text,
                           COALESCE(sca.{rationale_column}, '') AS rationale_text
                    FROM strategy_card_actions sca
                    ORDER BY sca.comment_id, sca.action_order
                    """
                ).fetchall()
            )
            if action_rows:
                for plan_order, row in enumerate(action_rows, start=1):
                    comment_id = str(row["comment_id"])
                    action_order = int(row["action_order"])
                    connection.execute(
                        """
                        INSERT INTO revision_plan_actions (
                            plan_action_id, plan_order, comment_id, action_order, execution_category,
                            title, objective, suggested_change, evidence_requirement, status
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            f"{comment_id}_action_{action_order:03d}",
                            plan_order,
                            comment_id,
                            action_order,
                            "modification_strategy",
                            str(row["summary_text"] or f"{comment_id} action {action_order}"),
                            str(row["summary_text"] or ""),
                            str(row["summary_text"] or ""),
                            str(row["rationale_text"] or ""),
                            "completed",
                        ),
                    )
        if connection.execute("SELECT 1 FROM revision_action_logs LIMIT 1").fetchone() is None:
            thread_rows = list(
                connection.execute(
                    """
                    SELECT rtr.thread_id, COALESCE(rtr.response_resolution_kind, 'revision_backed') AS response_resolution_kind
                    FROM response_thread_rows rtr
                    ORDER BY rtr.thread_id
                    """
                ).fetchall()
            )
            comment_links = defaultdict(list)
            for row in connection.execute(
                "SELECT thread_id, comment_id FROM raw_thread_atomic_links ORDER BY thread_id, link_order, comment_id"
            ).fetchall():
                comment_links[str(row["thread_id"])].append(str(row["comment_id"]))
            plan_links = defaultdict(list)
            for row in connection.execute(
                "SELECT plan_action_id, comment_id FROM revision_plan_actions ORDER BY plan_order, plan_action_id"
            ).fetchall():
                plan_links[str(row["comment_id"])].append(str(row["plan_action_id"]))
            log_order = 1
            for row in thread_rows:
                thread_id = str(row["thread_id"])
                if str(row["response_resolution_kind"]) == "response_only_resolution":
                    continue
                log_id = f"legacy_log_{log_order:03d}"
                connection.execute(
                    """
                    INSERT INTO revision_action_logs (
                        log_id, log_order, status, operator_role, summary, change_note, response_note, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        log_id,
                        log_order,
                        "completed",
                        "collaborative",
                        f"Legacy Stage 6 revision audit backfill for {thread_id}",
                        "Backfilled from legacy exported Stage 6 workspace for contract compatibility.",
                        "This revision log preserves thread-level traceability for the migrated Stage 6 contract.",
                        "",
                    ),
                )
                connection.execute(
                    """
                    INSERT INTO revision_action_log_thread_links (log_id, thread_id)
                    VALUES (?, ?)
                    """,
                    (log_id, thread_id),
                )
                connection.execute(
                    """
                    INSERT INTO response_thread_action_log_links (thread_id, log_id, link_order)
                    VALUES (?, ?, 1)
                    """,
                    (thread_id, log_id),
                )
                linked_plan_action_ids: list[str] = []
                for comment_id in comment_links.get(thread_id, []):
                    linked_plan_action_ids.extend(plan_links.get(comment_id, []))
                for plan_action_id in sorted(set(linked_plan_action_ids)):
                    connection.execute(
                        """
                        INSERT INTO revision_action_log_plan_links (log_id, plan_action_id)
                        VALUES (?, ?)
                        """,
                        (log_id, plan_action_id),
                    )
                log_order += 1
        connection.execute(
            """
            UPDATE export_artifacts
            SET artifact_status = CASE artifact_name
                WHEN 'working_manuscript' THEN 'ready'
                WHEN 'response_markdown' THEN 'ready'
                WHEN 'response_latex' THEN 'ready'
                ELSE artifact_status
            END,
                output_path = CASE artifact_name
                    WHEN 'working_manuscript' THEN 'manuscript-copies/working-manuscript'
                    WHEN 'response_markdown' THEN COALESCE(NULLIF(output_path, ''), '15-response-letter-preview.md')
                    WHEN 'response_latex' THEN COALESCE(NULLIF(output_path, ''), '16-response-letter-preview.tex')
                    WHEN 'latexdiff_manuscript' THEN COALESCE(output_path, '')
                    ELSE output_path
                END
            WHERE artifact_name IN ('working_manuscript', 'response_markdown', 'response_latex', 'latexdiff_manuscript')
            """
        )
        connection.commit()


def seed_supplement_suggestions_from_gaps(db_path: Path) -> None:
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        ensure_supplement_suggestion_tables(connection)
        connection.execute("DELETE FROM supplement_suggestion_intake_links")
        connection.execute("DELETE FROM supplement_suggestion_items")
        rows = list(
            connection.execute(
                """
                SELECT acs.comment_id, acl.analysis_order, COALESCE(acl.gap_summary, ''), ac.required_action
                FROM atomic_comment_state acs
                JOIN atomic_comments ac ON ac.comment_id = acs.comment_id
                LEFT JOIN atomic_comment_analysis_links acl ON acl.comment_id = acs.comment_id
                WHERE acs.evidence_gap = 'yes'
                ORDER BY acs.comment_id, acl.analysis_order
                """
            ).fetchall()
        )
        suggestion_counts: dict[str, int] = {}
        for row in rows:
            comment_id = str(row[0])
            gap_summary = str(row[2] or "").strip()
            if not gap_summary:
                continue
            suggestion_order = suggestion_counts.get(comment_id, 0) + 1
            suggestion_counts[comment_id] = suggestion_order
            connection.execute(
                """
                INSERT INTO supplement_suggestion_items (
                    comment_id, suggestion_order, analysis_order, request_summary, request_recommendation, status
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    comment_id,
                    suggestion_order,
                    row[1],
                    gap_summary,
                    f"Collect evidence to support: {row[3]}",
                    "provisional",
                ),
            )
        connection.commit()


def write_review_comment_coverage_truth(db_path: Path, documents: list[dict]) -> None:
    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        ensure_review_comment_coverage_tables(connection)
        ensure_supplement_suggestion_tables(connection)
        connection.execute("DELETE FROM review_comment_coverage_segment_comment_links")
        connection.execute("DELETE FROM review_comment_coverage_segments")
        connection.execute("DELETE FROM raw_thread_source_spans")
        connection.execute("DELETE FROM review_comment_source_documents")
        for document in documents:
            source_document_id = document["source_document_id"]
            original_text = document["original_text"]
            connection.execute(
                """
                INSERT INTO review_comment_source_documents (
                    source_document_id, source_kind, document_order, source_label, source_path, original_text
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    source_document_id,
                    document["source_kind"],
                    document["document_order"],
                    document["source_label"],
                    document["source_path"],
                    original_text,
                ),
            )
            span_order_by_thread_doc: dict[tuple[str, str], int] = defaultdict(int)
            if "spans" in document:
                for span in document["spans"]:
                    thread_id = str(span["thread_id"])
                    if "span_order" in span:
                        span_order = int(span["span_order"])
                    else:
                        span_order_by_thread_doc[(thread_id, source_document_id)] += 1
                        span_order = span_order_by_thread_doc[(thread_id, source_document_id)]
                    span_role = str(span.get("span_role", "primary"))
                    start_offset = int(span["start_offset"])
                    end_offset = int(span["end_offset"])
                    span_text = str(span.get("span_text", original_text[start_offset:end_offset]))
                    connection.execute(
                        """
                        INSERT INTO raw_thread_source_spans (
                            thread_id, source_document_id, span_order, span_role, start_offset, end_offset, span_text
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            thread_id,
                            source_document_id,
                            span_order,
                            span_role,
                            start_offset,
                            end_offset,
                            span_text,
                        ),
                    )
            cursor = 0
            for segment_order, segment in enumerate(document.get("segments", []), start=1):
                segment_text = str(segment["segment_text"])
                segment_len = len(segment_text)
                if segment_len > 0:
                    expected = original_text[cursor : cursor + segment_len]
                    if expected != segment_text:
                        raise AssertionError(
                            "segment_text does not match original_text reconstruction "
                            f"at source_document_id={source_document_id}, segment_order={segment_order}"
                        )
                start_offset = cursor
                end_offset = cursor + segment_len
                cursor = end_offset
                connection.execute(
                    """
                    INSERT INTO review_comment_coverage_segments (
                        source_document_id, segment_order, coverage_status, segment_text, thread_id
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        source_document_id,
                        segment_order,
                        segment["coverage_status"],
                        segment_text,
                        segment.get("thread_id"),
                    ),
                )
                thread_id = str(segment.get("thread_id") or "")
                if segment.get("coverage_status") == "covered" and thread_id and segment_len > 0 and "spans" not in document:
                    span_order_by_thread_doc[(thread_id, source_document_id)] += 1
                    span_role = str(segment.get("span_role", "primary"))
                    connection.execute(
                        """
                        INSERT INTO raw_thread_source_spans (
                            thread_id, source_document_id, span_order, span_role, start_offset, end_offset, span_text
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            thread_id,
                            source_document_id,
                            span_order_by_thread_doc[(thread_id, source_document_id)],
                            span_role,
                            start_offset,
                            end_offset,
                            segment_text,
                        ),
                    )
                for link_order, comment_id in enumerate(segment.get("comment_ids", []), start=1):
                    connection.execute(
                        """
                        INSERT INTO review_comment_coverage_segment_comment_links (
                            source_document_id, segment_order, link_order, comment_id
                        ) VALUES (?, ?, ?, ?)
                        """,
                        (
                            source_document_id,
                            segment_order,
                            link_order,
                            comment_id,
                        ),
                    )
            if "segments" in document and cursor != len(original_text):
                raise AssertionError(
                    f"segments do not fully reconstruct original_text for source_document_id={source_document_id}"
                )
        connection.commit()


def seed_review_comment_coverage_from_threads(
    db_path: Path,
    *,
    include_editor_letter: bool = False,
) -> None:
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        ensure_stage5_execution_item_schema(connection)
        thread_rows = list(
            connection.execute(
                """
                SELECT thread_id, reviewer_id, thread_order, original_text
                FROM raw_review_threads
                ORDER BY reviewer_id, thread_order, thread_id
                """
            ).fetchall()
        )
        comment_rows = list(
            connection.execute(
                """
                SELECT thread_id, comment_id
                FROM raw_thread_atomic_links
                ORDER BY thread_id, link_order, comment_id
                """
            ).fetchall()
        )
    comment_map: dict[str, list[str]] = {}
    for row in comment_rows:
        comment_map.setdefault(str(row["thread_id"]), []).append(str(row["comment_id"]))

    source_segments: list[dict] = []
    source_text_parts: list[str] = []
    for index, row in enumerate(thread_rows):
        if index > 0:
            source_segments.append(
                {
                    "coverage_status": "uncovered",
                    "segment_text": "\n\n",
                    "thread_id": None,
                    "comment_ids": [],
                }
            )
            source_text_parts.append("\n\n")
        thread_text = str(row["original_text"])
        source_segments.append(
            {
                "coverage_status": "covered",
                "segment_text": thread_text,
                "thread_id": str(row["thread_id"]),
                "comment_ids": comment_map.get(str(row["thread_id"]), []),
            }
        )
        source_text_parts.append(thread_text)

    documents = [
        {
            "source_document_id": "review_comments_source_001",
            "source_kind": "review_comments_source",
            "document_order": 1,
            "source_label": "Review Comments Source",
            "source_path": "tests://review-comments-source.md",
            "original_text": "".join(source_text_parts),
            "segments": source_segments,
        }
    ]
    if include_editor_letter and thread_rows:
        first_thread_id = str(thread_rows[0]["thread_id"])
        documents.append(
            {
                "source_document_id": "editor_letter_source_001",
                "source_kind": "editor_letter_source",
                "document_order": 2,
                "source_label": "Editor Letter Source",
                "source_path": "tests://editor-letter-source.md",
                "original_text": "Editor note: Please address all comments.",
                "segments": [
                    {
                        "coverage_status": "covered",
                        "segment_text": "Editor note: Please address all comments.",
                        "thread_id": first_thread_id,
                        "comment_ids": comment_map.get(first_thread_id, []),
                    }
                ],
            }
        )
    write_review_comment_coverage_truth(db_path, documents)
    seed_supplement_suggestions_from_gaps(db_path)
    seed_stage6_revision_loop_from_legacy_state(db_path)
