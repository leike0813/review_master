## Why

The current Stage 3-6 workspace still duplicates too much information between `04-atomic-review-comment-list.md` and `07-atomic-comment-workboard.md`. The list mixes stable identity data with later planning and execution state, while the workboard does not yet serve as the single evolving view for Stage 4-6 recovery and day-to-day progress.

Artifact numbering also drifted away from the actual creation order. `supplement-suggestion-plan.md` is produced for Stage 5 entry but is still numbered after later Stage 6 outputs, which makes the runtime workspace harder to scan in the intended order.

Finally, Stage 5 manuscript-side truth is still modeled as narrow location-bound "drafts". That shape works for literal text snippets, but it does not represent other execution forms such as revision strategy, figure work, or data supplementation. The runtime needs a typed execution-item model so the strategy card can reflect the real breadth of manuscript work without forcing everything into one draft-text bucket.

## What Changes

- Re-scope `04-atomic-review-comment-list.md` into a stable Stage 3 identity/index artifact.
- Upgrade `07-atomic-comment-workboard.md` into the dynamic Stage 4-6 lifecycle board.
- Reorder numbered runtime artifacts so `08-supplement-suggestion-plan.md` follows the workboard and later files shift accordingly.
- Replace `strategy_action_manuscript_drafts` with typed `strategy_action_manuscript_execution_items`.
- Rename manuscript-side completion semantics from `manuscript_draft_done` to `manuscript_execution_items_done`.
- Update Stage 5 rendering, gate validation, repair mapping, docs, localization, and tests to use the new terminology and artifact order.

## Capabilities

### Modified Capabilities

- `review-master-artifact-workspace-layout`
- `review-master-template-driven-rendering`
- `review-master-markdown-artifact-contract`
- `review-master-stage-4-atomic-workboard-instructions`
- `review-master-stage-5-strategy-card-instructions`
- `review-master-sqlite-runtime`
- `review-master-skill-instructions`
- `review-master-user-checkpoints`
- `review-master-validator-instruction-payload`
- `review-master-workflow-glossary`

## Impact

- Affects runtime schema, render manifest, workspace filename constants, and Stage 5 validation logic.
- Affects `SKILL.md`, runtime digest, Stage 4/5 guides, SQL recipe docs, localization messages, and glossary.
- Affects numbered artifact references across tests and example workspace expectations.
