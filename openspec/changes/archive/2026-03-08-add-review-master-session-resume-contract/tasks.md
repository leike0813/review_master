# Tasks

- [x] Add the new OpenSpec change artifacts for the session-resume contract.
- [x] Extend the SQLite schema with `resume_*` tables and bootstrap resume rows.
- [x] Add `assets/runtime/skill-runtime-digest.md` and the `agent-resume.md.j2` render template.
- [x] Update `workspace_db.py` so runtime rendering includes `agent-resume.md`.
- [x] Extend `gate_and_render_workspace.py` to validate resume data and emit `instruction_payload.resume_packet`.
- [x] Update `SKILL.md`, `helper-scripts.md`, `workflow-state-machine.md`, and stage docs to describe the unified resume-first protocol.
- [x] Update `sql-write-recipes.md` so phase recipes explicitly maintain `resume_*` data.
- [x] Regenerate sample workspaces and validator fixtures so they include bootstrap/continuation resume output.
- [x] Update playbooks to demonstrate bootstrap resume and resumed continuation.
- [x] Run `openspec validate add-review-master-session-resume-contract --type change --strict`.
- [x] Run `mypy` on the updated runtime scripts.
