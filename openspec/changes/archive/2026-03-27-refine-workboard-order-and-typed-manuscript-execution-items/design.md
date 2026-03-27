## Context

The runtime already uses SQLite as the only source of truth and renders Markdown views from Jinja templates. That makes the requested changes best handled as a coordinated contract update across schema, render helpers, and gate validation.

Two design tensions need to be resolved together:

1. The Stage 3 list and the Stage 4-6 workboard should not both try to be the "main table".
2. The Stage 5 manuscript-side truth should describe execution work, not just literal draft prose.

## Decisions

### Decision 1: `atomic list` becomes a stable index, `atomic workboard` becomes the live board

`04-atomic-review-comment-list.md` will retain only stable identity-and-origin fields:

- `comment_id`
- source reviewers / source threads
- canonical summary
- required action

All planning/execution fields that evolve after Stage 3 move out of that artifact.

`07-atomic-comment-workboard.md` becomes the live multi-stage board and aggregates:

- Stage 4: status, priority, evidence gap, target locations, analysis summary, next action
- Stage 5: active-comment marker, strategy-card presence, user-strategy-confirmed state, blocker summary, supplement suggestion/intake summary, manuscript execution items done, response draft done
- Stage 6: one-to-one link checked, export ready

### Decision 2: Artifact numbering is reordered to match actual creation order

The canonical non-strategy-card filenames become:

1. `01-agent-resume.md`
2. `02-manuscript-structure-summary.md`
3. `03-raw-review-thread-list.md`
4. `04-atomic-review-comment-list.md`
5. `05-thread-to-atomic-mapping.md`
6. `06-review-comment-coverage.md`
7. `07-atomic-comment-workboard.md`
8. `08-supplement-suggestion-plan.md`
9. `09-style-profile.md`
10. `10-action-copy-variants.md`
11. `11-response-letter-outline.md`
12. `12-export-patch-plan.md`
13. `13-response-letter-table-preview.md`
14. `14-response-letter-table-preview.tex`
15. `15-supplement-intake-plan.md`
16. `16-final-assembly-checklist.md`

Per-comment strategy cards remain at `response-strategy-cards/{comment_id}.md`.

### Decision 3: Stage 5 manuscript-side truth becomes typed execution items

The narrow table `strategy_action_manuscript_drafts` is replaced by `strategy_action_manuscript_execution_items`.

The new rows are keyed by `(comment_id, action_order, item_order)` and classified with a fixed enum:

- `modification_strategy`
- `rewrite_polish`
- `text_add_modify_delete`
- `figure_update`
- `data_supplement`

Each row stores:

- `comment_id`
- `action_order`
- `item_order`
- `category`
- `content_text`
- `rationale`
- `target_scope_note`

Text-like categories must carry usable text. Non-text categories may use `content_text` as an execution note rather than literal manuscript prose.

### Decision 4: Completion and repair semantics follow the new execution-item model

The completion field is renamed from `manuscript_draft_done` to `manuscript_execution_items_done`.

Any strategy-semantic edit must continue to invalidate downstream execution truth:

- clear execution items for that comment
- clear response draft
- reset `manuscript_execution_items_done` and `response_draft_done`
- reset confirmation and pending gate state

### Decision 5: Old workspace migration is out of scope for this change

This change guarantees the new contract for newly initialized workspaces and for freshly rendered example assets in the repository. It does not promise automatic upgrade of existing user workspaces that still use the old Stage 5 draft model.

## Risks / Trade-offs

- Renaming a widely referenced completion field touches many files.
  - Accepted, because leaving mixed terminology would keep the model ambiguous.
- Example workspace fixtures and runtime-localization snapshots may need regeneration.
  - Accepted, because numbering and strategy-card wording are visible user-facing contracts.
- The live workboard becomes denser.
  - Mitigation: keep the Stage 3 list intentionally minimal and stable.

## Migration Notes

- New workspaces initialize directly with the reordered filenames and the new Stage 5 execution-item table.
- Existing workspaces are not auto-migrated in this change. Operators who want the new model must rebuild or migrate in a future dedicated change.
