from __future__ import annotations

import sqlite3
from pathlib import Path

from tests.helpers import EXPORT_SCRIPT, INIT_SCRIPT, run_python_script, strip_changes_markup


def test_export_script_generates_full_marked_and_clean_manuscripts(tmp_path: Path) -> None:
    source_root = tmp_path / "source"
    source_root.mkdir()
    original_text = """\\documentclass{article}
\\begin{document}
Old sentence.
\\end{document}
"""
    (source_root / "main.tex").write_text(original_text, encoding="utf-8")

    artifact_root = tmp_path / "artifact-root"
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
    marked_root = tmp_path / "marked"
    clean_root = tmp_path / "clean"

    marked_text = original_text.replace(
        "Old sentence.",
        r"\replaced{New final sentence.}{Old sentence.}",
    )
    clean_text = original_text.replace("Old sentence.", "New final sentence.")

    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            UPDATE manuscript_summary
            SET main_entry = 'main.tex', project_shape = 'single_tex'
            WHERE id = 1
            """
        )
        connection.execute(
            """
            INSERT INTO atomic_comments (comment_id, comment_order, canonical_summary, required_action)
            VALUES ('atomic_001', 1, 'Minimal export patch test', 'Apply the final sentence to the manuscript.')
            """
        )
        connection.executemany(
            """
            INSERT INTO export_patch_sets (patch_set_id, artifact_kind, source_root, output_root, status)
            VALUES (?, ?, ?, ?, 'ready')
            """,
            [
                ("marked_set", "marked_manuscript", str(source_root), str(marked_root)),
                ("clean_set", "clean_manuscript", str(source_root), str(clean_root)),
            ],
        )
        connection.executemany(
            """
            INSERT INTO export_patches (
                patch_set_id, patch_order, comment_id, action_order, location_order,
                target_file, anchor_text, operation, marked_text, clean_text, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    "marked_set",
                    1,
                    "atomic_001",
                    1,
                    1,
                    "main.tex",
                    original_text,
                    "replace",
                    marked_text,
                    clean_text,
                    "full file replace for marked output",
                ),
                (
                    "clean_set",
                    1,
                    "atomic_001",
                    1,
                    1,
                    "main.tex",
                    original_text,
                    "replace",
                    marked_text,
                    clean_text,
                    "full file replace for clean output",
                ),
            ],
        )
        connection.commit()

    run_python_script(EXPORT_SCRIPT, "--artifact-root", str(artifact_root), "--patch-set-id", "marked_set")
    run_python_script(EXPORT_SCRIPT, "--artifact-root", str(artifact_root), "--patch-set-id", "clean_set")

    marked_output = (marked_root / "main.tex").read_text(encoding="utf-8")
    clean_output = (clean_root / "main.tex").read_text(encoding="utf-8")

    assert (source_root / "main.tex").read_text(encoding="utf-8") == original_text
    assert "\\usepackage[markup=default]{changes}" in marked_output
    assert "\\replaced{New final sentence.}{Old sentence.}" in marked_output
    assert clean_output == clean_text
    assert strip_changes_markup(marked_output) == clean_output
