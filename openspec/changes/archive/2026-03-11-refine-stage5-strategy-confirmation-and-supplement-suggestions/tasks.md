## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for Stage 5 confirmation-first gating and supplement suggestions.

## 2. Runtime Schema and Rendering

- [x] 2.1 Add supplement suggestion truth tables to the runtime schema.
- [x] 2.2 Add `supplement-suggestion-plan.md` to the render manifest and template set.
- [x] 2.3 Extend workspace render helpers so strategy cards are phase-aware and the new supplement suggestion view is rendered from DB truth.

## 3. Stage 5 Gate Flow

- [x] 3.1 Make Stage 5 require explicit confirmation before draft authoring.
- [x] 3.2 Add `recipe_stage5_confirm_strategy` and `recipe_stage5_replace_execution_drafts`.
- [x] 3.3 Reset confirmation and clear stale drafts whenever strategy semantics change.
- [x] 3.4 Keep explicit `set_active_comment` switching legal when no global blockers exist.

## 4. Docs and Tests

- [x] 4.1 Update `SKILL.md`, runtime digest, Stage 5 guide, SQL recipes, and workflow-state-machine docs.
- [x] 4.2 Add tests for supplement suggestion rendering, confirmation-first gating, confirmation clearing, stale-draft invalidation, and suggestion-to-intake traceability.
