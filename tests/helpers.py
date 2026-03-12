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
