# Tasks

- [x] Replace the runtime SQLite schema with the new raw-thread / canonical-atomic / response-thread link model.
- [x] Replace the render manifest and runtime templates with thread-aware mapping, workboard, and response-outline views.
- [x] Rewrite `workspace_db.py` to build contexts from the new relation tables and render the new view set.
- [x] Rewrite `gate_and_render_workspace.py` to validate thread coverage, atomic coverage, and response-outline coverage.
- [x] Update `SKILL.md` and stage 3/4/5/6 reference documents to describe the three-layer mapping model.
- [x] Rewrite `sql-write-recipes.md` for the new relation-table workflow.
- [x] Update playbooks and sample runtime assets to demonstrate raw-thread splitting, duplicate atomic merges, and thread-indexed response export.
