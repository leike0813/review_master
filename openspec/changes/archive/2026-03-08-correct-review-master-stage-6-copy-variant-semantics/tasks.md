# Tasks: correct-review-master-stage-6-copy-variant-semantics

- [x] 1. Create the OpenSpec change artifacts for correcting Stage 6 copy-variant semantics.
- [x] 2. Update `review-master/SKILL.md` so Stage 6 variants are manuscript-final-copy variants only.
- [x] 3. Update `review-master/references/stage-5-strategy-and-execution.md` and `stage-6-final-review-and-export.md` to separate Stage 5 strategy from Stage 6 final wording.
- [x] 4. Update `review-master/references/sql-write-recipes.md`, `workflow-state-machine.md`, `helper-scripts.md`, `workflow-glossary.md`, and `assets/runtime/skill-runtime-digest.md` to remove response-side variant semantics.
- [x] 5. Shrink the Stage 6 schema in `review-master/assets/schema/review-master-schema.yaml` to location-scoped manuscript-only variants.
- [x] 6. Update Stage 6 templates and rendering context so `action-copy-variants.md` becomes location-scoped manuscript-only final-copy text and `response-letter-outline.md` uses the corrected semantics.
- [x] 7. Update `workspace_db.py` and `gate_and_render_workspace.py` so Stage 6 validation and action guidance require three selected-ready manuscript texts per action-location tuple.
- [x] 8. Refresh playbooks and sample workspace views so Stage 6 clearly shows manuscript-copy selection rather than strategy/response selection, and the variant text is final landing prose.
- [x] 9. Migrate sample workspace databases to the new Stage 6 location-scoped tables and rerender affected sample outputs.
- [x] 10. Validate the OpenSpec change, rerun type checking, and rerun sample gate-and-render checks.
