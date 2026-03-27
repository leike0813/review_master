# Tasks: rebuild-stage6-as-interactive-revision-audit-loop

- [x] 1. Create the OpenSpec change artifacts for the Stage 6 redesign.
- [x] 2. Add delta specs that replace the patch-driven Stage 6 contract with the revision-audit loop contract.
- [x] 3. Update `review-master/SKILL.md`, Stage 1/5/6 references, workflow docs, SQL recipes, and runtime digest.
- [x] 4. Reorder artifact numbering and update the render manifest, workspace constants, and resume/read-order references.
- [x] 5. Extend the schema for manuscript copies, revision plan actions, revision audit logs, and working-copy file state.
- [x] 6. Update `init_artifact_workspace.py` so Stage 1 can establish `source_snapshot` and `working_manuscript`.
- [x] 7. Replace Stage 6 gate logic in `gate_and_render_workspace.py` with revision-plan closure, response coverage, and unaudited-diff checks.
- [x] 8. Add `capture_revision_action.py` and `commit_revision_round.py` as the Stage 6 audit and submission scripts.
- [x] 9. Replace Stage 6 templates/views with revision guide, execution graph, revision action log, response coverage matrix, and new preview/checklist outputs.
- [x] 10. Update localization strings, sample/runtime fixtures, and helper contracts to the new Stage 6 names and actions.
- [x] 11. Update tests for Stage 1 copies, Stage 5 final outputs, Stage 6 audit flow, and retired patch-driven requirements.
- [x] 12. Run `pytest`, `mypy review-master/scripts tests`, and `openspec validate rebuild-stage6-as-interactive-revision-audit-loop --type change --strict`.
