# Design: correct-review-master-stage-6-copy-variant-semantics

## Overview

The current Stage 6 model overreaches by generating two independent variant tracks:

- manuscript-side variants
- response-side variants

That is not the intended boundary between Stage 5 and Stage 6.

The corrected model is:

1. Stage 5 fixes strategy, evidence handling, and draft direction.
2. Stage 6 generates three final manuscript wording options per strategy-action target location.
3. The user selects the manuscript wording.
4. The final response row is assembled from:
   - Stage 5 strategy truth
   - Stage 5 draft truth
   - selected manuscript wording
   - thread-level aggregation

This keeps Stage 6 focused on wording and export, not strategy variation.

## Key Decisions

### Stage 5 and Stage 6 must stay cleanly separated

Stage 5 is the last stage where “what should we do?” is decided. Stage 6 is where “what exact text should land in the final manuscript?” is decided.

Therefore:

- Stage 5 owns strategy, stance, evidence judgment, and draft structure.
- Stage 6 owns final manuscript wording and final thread-level packaging.

### Copy variants are manuscript-only

The user requested three variants of the wording that will actually be inserted into the revised manuscript. The system should not reinterpret this as:

- three strategy options
- three response explanation options

The three variants are strictly three manuscript-final-copy candidates for each `strategy_card_action` target location. Each `variant_text` must already be concrete landing prose, not a direction such as "Add", "Expand", or "Clarify".

### Response rows are single-path derived outputs

The final Response Letter should not branch at action level. Its explanation rows should be derived from one coherent source set:

- Stage 5 strategy and draft truth
- selected manuscript copy
- thread-level aggregation

That means `response_thread_rows` remains the final outward-facing truth, but it is no longer conceptually backed by response-side variant selection.

## Data Model Changes

### `action_copy_variants`

Current model:

- keyed by `(comment_id, action_order, variant_target, variant_label)`
- supports both `manuscript` and `response`

New model:

- keyed by `(comment_id, action_order, location_order, variant_label)`
- only stores manuscript-final-copy variants

Retained fields:

- `comment_id`
- `action_order`
- `location_order`
- `variant_label`
- `variant_text`
- `rationale`

### `selected_action_copy_variants`

Current model:

- keyed by `(comment_id, action_order, variant_target)`

New model:

- keyed by `(comment_id, action_order, location_order)`

This stores the selected final manuscript wording for each action.

### `response_thread_rows`

This table remains in place, but its semantics are clarified:

- it is generated from selected manuscript wording plus Stage 5 strategy/draft truth
- it is not generated from response-side variant selection

## Runtime and Rendering Impact

### `workspace_db.py`

Needs to:

- stop expecting `variant_target`
- build `action-copy-variants.md` with manuscript-only variants
- build `response-letter-outline.md` without suggesting any response-side variant dependency

### `gate_and_render_workspace.py`

Needs to:

- remove `variant_target` enum validation
- require exactly three variants per `(comment_id, action_order, location_order)`
- require one selected manuscript variant per `(comment_id, action_order, location_order)`
- stop blocking on missing response-side variants
- update Stage 6 guidance wording accordingly

## Playbook Impact

The playbooks and sample fixtures must show:

- Stage 5: plan and strategy are fixed
- Stage 6B: three manuscript wording variants per target location
- user selects manuscript wording only, per target location
- Stage 6C: response rows are assembled after manuscript wording is selected

This is especially important in the evidence-supplement playbook, because it is the richer Stage 6 example.
