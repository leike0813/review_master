## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for workboard/list role separation, artifact renumbering, and typed manuscript execution items.

## 2. Runtime Schema and Rendering

- [x] 2.1 Replace `strategy_action_manuscript_drafts` with `strategy_action_manuscript_execution_items` in the schema and runtime validation model.
- [x] 2.2 Reorder numbered runtime artifact filenames in constants, render manifest, artifact presence reporting, and related helpers.
- [x] 2.3 Slim `atomic-review-comment-list.md` to stable identity fields and expand `atomic-comment-workboard.md` to Stage 4-6 lifecycle fields.
- [x] 2.4 Redesign the response strategy card manuscript section to render typed execution items grouped by category.

## 3. Gate Flow and Payload Contracts

- [x] 3.1 Update Stage 5 validation, repair mapping, and allowed-action messaging to use execution-item terminology and completion names.
- [x] 3.2 Keep strategy-edit invalidation behavior, but make it clear that execution items and response drafts are the downstream truths being cleared.
- [x] 3.3 Update instruction payload and resume/read-order references so the workboard is the live board and the renumbered artifacts are canonical.

## 4. Docs and Tests

- [x] 4.1 Update `SKILL.md`, runtime digest, Stage 4/5 guides, SQL recipes, glossary, and localization messages.
- [x] 4.2 Update tests and example-workspace expectations for artifact ordering, workboard/list contracts, and typed execution-item rendering.
- [x] 4.3 Run `pytest`, `mypy review-master/scripts tests`, and `openspec validate refine-workboard-order-and-typed-manuscript-execution-items --type change --strict`.
