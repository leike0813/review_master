from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_ROOT = PROJECT_ROOT / "review-master" / "scripts"
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

from workspace_db import DB_FILENAME, connect_db, load_schema_definition, render_workspace


GATE_SCRIPT = SCRIPT_ROOT / "gate_and_render_workspace.py"


def emit(payload: dict[str, Any], exit_code: int = 0) -> int:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2))
    sys.stdout.write("\n")
    return exit_code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Migrate a legacy Stage 5 workspace to the draft-model schema.")
    parser.add_argument("--artifact-root", required=True, help="Path to the runtime workspace.")
    return parser.parse_args()


def table_columns(connection: sqlite3.Connection, table_name: str) -> list[str]:
    rows = connection.execute(f"PRAGMA table_info({table_name})").fetchall()
    return [str(row[1]) for row in rows]


def table_exists(connection: sqlite3.Connection, table_name: str) -> bool:
    row = connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?",
        (table_name,),
    ).fetchone()
    return row is not None


def schema_sql_for(table_name: str) -> str:
    schema = load_schema_definition()
    for table in schema.get("tables", []):
        if isinstance(table, dict) and str(table.get("name")) == table_name:
            return str(table["sql"])
    raise RuntimeError(f"missing schema SQL for table: {table_name}")


def ensure_new_tables(connection: sqlite3.Connection) -> list[str]:
    ensured: list[str] = []
    for table_name in (
        "strategy_action_manuscript_drafts",
        "comment_response_drafts",
        "comment_blockers",
    ):
        if not table_exists(connection, table_name):
            connection.execute(schema_sql_for(table_name))
        ensured.append(table_name)
    return ensured


def migrate_comment_completion_status(connection: sqlite3.Connection) -> tuple[bool, list[str]]:
    columns = table_columns(connection, "comment_completion_status")
    if "manuscript_draft_done" in columns and "response_draft_done" in columns:
        return False, []

    if "manuscript_change_done" not in columns or "response_section_done" not in columns:
        raise RuntimeError("comment_completion_status is neither legacy nor migrated")

    reset_ids = [
        str(row[0])
        for row in connection.execute(
            "SELECT comment_id FROM comment_completion_status ORDER BY comment_id"
        ).fetchall()
    ]
    connection.execute("ALTER TABLE comment_completion_status RENAME TO comment_completion_status_legacy")
    connection.execute(schema_sql_for("comment_completion_status"))
    connection.execute(
        """
        INSERT INTO comment_completion_status (
            comment_id,
            manuscript_draft_done,
            response_draft_done,
            evidence_gap_closed,
            user_strategy_confirmed,
            one_to_one_link_checked,
            export_ready
        )
        SELECT
            comment_id,
            'no',
            'no',
            evidence_gap_closed,
            user_strategy_confirmed,
            one_to_one_link_checked,
            export_ready
        FROM comment_completion_status_legacy
        """
    )
    connection.execute("DROP TABLE comment_completion_status_legacy")
    return True, reset_ids


def migrate_active_comment_blockers(connection: sqlite3.Connection) -> int:
    workflow_state = connection.execute(
        "SELECT current_stage, active_comment_id FROM workflow_state WHERE id = 1"
    ).fetchone()
    if workflow_state is None:
        return 0

    current_stage = str(workflow_state[0])
    active_comment_id = workflow_state[1]
    if current_stage != "stage_5" or active_comment_id is None:
        return 0

    blocker_rows = connection.execute(
        "SELECT position, message FROM workflow_global_blockers ORDER BY position"
    ).fetchall()
    if not blocker_rows:
        return 0

    inserted = 0
    for blocker_order, row in enumerate(blocker_rows, start=1):
        message = str(row[1])
        connection.execute(
            """
            INSERT OR REPLACE INTO comment_blockers (comment_id, blocker_order, message)
            VALUES (?, ?, ?)
            """,
            (str(active_comment_id), blocker_order, message),
        )
        inserted += 1
    connection.execute("DELETE FROM workflow_global_blockers")
    return inserted


def recompute_stage5_state(connection: sqlite3.Connection) -> None:
    workflow_state = connection.execute(
        "SELECT current_stage, active_comment_id FROM workflow_state WHERE id = 1"
    ).fetchone()
    if workflow_state is None or str(workflow_state[0]) != "stage_5":
        return

    active_comment_id = str(workflow_state[1]) if workflow_state[1] is not None else None
    pending_count = int(
        connection.execute("SELECT COUNT(*) FROM workflow_pending_user_confirmations").fetchone()[0]
    )
    global_blocker_count = int(
        connection.execute("SELECT COUNT(*) FROM workflow_global_blockers").fetchone()[0]
    )
    if global_blocker_count > 0:
        stage_gate = "blocked"
        next_action = "resolve_blockers"
    elif active_comment_id is None:
        stage_gate = "ready"
        next_action = "set_active_comment"
    else:
        strategy_row = connection.execute(
            "SELECT 1 FROM strategy_cards WHERE comment_id = ?",
            (active_comment_id,),
        ).fetchone()
        stage_gate = "blocked" if pending_count > 0 else "ready"
        next_action = "author_strategy_card" if strategy_row is None else "advance_active_comment"

    connection.execute(
        """
        UPDATE workflow_state
        SET stage_gate = ?, next_action = ?
        WHERE id = 1
        """,
        (stage_gate, next_action),
    )


def run_gate(artifact_root: Path) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-u", str(GATE_SCRIPT), "--artifact-root", str(artifact_root)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"gate_and_render_workspace.py failed with code {completed.returncode}\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    return json.loads(completed.stdout)


def main() -> int:
    args = parse_args()
    artifact_root = Path(args.artifact_root).expanduser().resolve()
    db_path = artifact_root / DB_FILENAME
    if not artifact_root.exists():
        return emit({"status": "error", "error": f"artifact root does not exist: {artifact_root}"}, exit_code=1)
    if not db_path.exists():
        return emit({"status": "error", "error": f"database does not exist: {db_path}"}, exit_code=1)

    migrated_tables: list[str] = []
    reset_completion_comment_ids: list[str] = []
    moved_blockers = 0
    already_migrated = False

    try:
        with connect_db(db_path) as connection:
            completion_columns = table_columns(connection, "comment_completion_status")
            already_migrated = (
                "manuscript_draft_done" in completion_columns
                and "response_draft_done" in completion_columns
                and table_exists(connection, "strategy_action_manuscript_drafts")
                and table_exists(connection, "comment_response_drafts")
                and table_exists(connection, "comment_blockers")
            )
            if not already_migrated:
                created_tables = ensure_new_tables(connection)
                migrated_tables.extend(created_tables)
                migrated_completion, reset_completion_comment_ids = migrate_comment_completion_status(connection)
                if migrated_completion:
                    migrated_tables.append("comment_completion_status")
                moved_blockers = migrate_active_comment_blockers(connection)
                recompute_stage5_state(connection)
                connection.commit()
            workflow_state = connection.execute(
                "SELECT current_stage, stage_gate, active_comment_id FROM workflow_state WHERE id = 1"
            ).fetchone()
            active_comment_id = str(workflow_state[2]) if workflow_state is not None and workflow_state[2] is not None else None
            stage_after_migration = str(workflow_state[0]) if workflow_state is not None else "unknown"
            gate_after_migration = str(workflow_state[1]) if workflow_state is not None else "blocked"
    except (sqlite3.DatabaseError, OSError, RuntimeError) as exc:
        return emit({"status": "error", "error": str(exc)}, exit_code=1)

    try:
        render_workspace(db_path, artifact_root)
        gate_payload = run_gate(artifact_root)
    except (OSError, RuntimeError, ValueError) as exc:
        return emit({"status": "error", "error": str(exc)}, exit_code=1)

    return emit(
        {
            "status": "ok",
            "artifact_root": str(artifact_root),
            "database_path": str(db_path),
            "already_migrated": already_migrated,
            "migrated_tables": migrated_tables,
            "reset_completion_comment_ids": reset_completion_comment_ids,
            "moved_comment_blocker_count": moved_blockers,
            "active_comment_id": active_comment_id,
            "stage_after_migration": stage_after_migration,
            "gate_after_migration": gate_after_migration,
            "gate_status": gate_payload["status"],
            "gate_recommended_next_action": gate_payload["instruction_payload"]["recommended_next_action"]["action_id"],
        }
    )


if __name__ == "__main__":
    raise SystemExit(main())
