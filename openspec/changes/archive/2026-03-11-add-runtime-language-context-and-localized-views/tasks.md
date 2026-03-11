## 1. OpenSpec Artifacts

- [x] 1.1 Add `proposal.md`, `design.md`, `tasks.md`, and delta specs for runtime language context and localized views.

## 2. Runtime Schema and Bootstrap

- [x] 2.1 Add `runtime_language_context` to the SQLite schema and make it part of the required runtime contract.
- [x] 2.2 Extend `init_artifact_workspace.py` so Stage 1 bootstrap accepts `--document-language` and `--working-language`, writes the language context row, and creates `runtime-localization/`.
- [x] 2.3 Add workspace-local localization asset loading with package-default fallback.

## 3. Rendering, Gate, and Export

- [x] 3.1 Update `workspace_db.py` and all Jinja templates to use message keys plus `msg(target='working'|'document')`.
- [x] 3.2 Update `gate_and_render_workspace.py` so resume text, recommended actions, blocked actions, repair guidance, and current-state summaries render in working language.
- [x] 3.3 Update Stage 6 export/render paths so final manuscript/response outputs use document-language message catalogs while preserving source-language excerpts.

## 4. Documentation and Examples

- [x] 4.1 Update `SKILL.md`, runtime digest, Stage 1/3/5/6 guidance, workflow state machine, SQL recipes, and glossary for the dual-language model.
- [x] 4.2 Update playbooks and checked-in example workspaces to include `runtime_language_context`, localization overlays, and refreshed rendered views/gate snapshots.

## 5. Validation

- [x] 5.1 Add or update tests for Stage 1 language confirmation inputs, localization overlay fallback, Stage 3/5/6 language boundaries, and sample workspace regression.
- [x] 5.2 Run targeted pytest coverage and `openspec validate add-runtime-language-context-and-localized-views --type change --strict`.
