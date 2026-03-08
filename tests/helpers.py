from __future__ import annotations

import json
import re
import shutil
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
