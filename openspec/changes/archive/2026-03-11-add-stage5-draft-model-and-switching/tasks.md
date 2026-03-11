## 1. OpenSpec Artifacts

- [x] 1.1 Add `proposal.md`, `design.md`, and `tasks.md` for the Stage 5 draft-model change.
- [x] 1.2 Add delta specs for runtime schema, Stage 5 strategy/completion rules, workflow state machine, SQL recipes, artifact contract, artifact authoring rules, workflow glossary, and workspace migration.

## 2. Runtime Schema and Gate

- [x] 2.1 Add Stage 5 draft/source tables to the runtime schema and rename completion fields to draft semantics.
- [x] 2.2 Extend workspace rendering so strategy cards show manuscript drafts, response draft, and comment blockers.
- [x] 2.3 Update gate-and-render to validate the new draft truth sources and allow explicit `set_active_comment` during Stage 5 when no global blocker exists.

## 3. Documentation and Contracts

- [x] 3.1 Update Stage 5 handbook, workflow state machine, SQL recipes, helper script guidance, workflow glossary, `SKILL.md`, and runtime digest.
- [x] 3.2 Document the new migration script and the rule that legacy draft completion flags must be reset.
- [x] 3.3 Update playbooks and example-facing docs so they describe Stage 5 as a draft stage rather than a final-authoring stage.

## 4. Migration and Regression

- [x] 4.1 Add `artifacts/migrate_workspace_stage5_draft_model.py`.
- [x] 4.2 Add tests for migration, new Stage 5 gate behavior, and render output.
- [x] 4.3 Migrate the checked-in example workspaces, rerender their workspace views, and refresh their gate snapshots.
- [x] 4.4 Run targeted pytest coverage and `openspec validate add-stage5-draft-model-and-switching --type change --strict`.
