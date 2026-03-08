# Design: refine-review-master-stage-6-final-review-and-export

## Overview

Stage 6 is redefined as a full drafting and export stage:

1. build style profiles
2. generate three wording variants per strategy action
3. assemble final response rows by `thread_id`
4. export a marked manuscript
5. after final confirmation, export the clean manuscript and the final Response Letter package

The internal execution index remains `comment_id`, but the final outward-facing response contract is indexed by `thread_id`.

## Key Decisions

### Stage 6 adds style analysis before final wording

The skill must not jump from Stage 5 drafts directly to final prose. Stage 6 first extracts a global style profile from the original manuscript and derives anti-AI guidance for:

- manuscript text
- response-letter text

This keeps the final wording aligned with the user's style instead of the agent's default prose style.

### Copy variants are generated per strategy action

The natural unit for wording choice is the action-level modification point from `strategy_card_actions`, not the whole atomic item or the raw reviewer thread. This lets the user select wording at the level where text is actually written.

### Final response rows are thread-indexed

The final Response Letter must preserve reviewer-visible structure. Therefore:

- execution remains atomic-item based
- final presentation returns to `thread_id`

Each `thread_id` gets exactly one final response row, aggregating all selected action-level wording under that original reviewer thread.

### Export is two-step by default

Marked manuscript export and final clean export are different checkpoints:

- marked manuscript is a review artifact
- clean manuscript is the final delivery artifact

The user must explicitly confirm after the marked export review before clean export is allowed.

## Data Model Additions

Stage 6 needs new runtime tables:

- `style_profiles`
- `style_profile_rules`
- `action_copy_variants`
- `selected_action_copy_variants`
- `response_thread_rows`
- `export_artifacts`

These tables do not replace Stage 5 data. They consume Stage 5 outputs and turn them into final outward-facing text.

## View Additions

Stage 6 needs these additional read-only views:

- `style-profile.md`
- `action-copy-variants.md`
- `response-letter-table-preview.md`
- `response-letter-table-preview.tex`

`response-letter-outline.md` remains as a planning bridge, but final row-level preview moves into the new preview views.

## Gate Logic

Stage 6 gate-and-render guidance follows this order:

1. style profiles must exist before variant generation
2. every strategy action must have three variants per target before selection
3. selected variants must exist before final row assembly
4. response rows must exist before marked export
5. marked manuscript may be exported before final confirmation
6. clean manuscript and final Response Letter exports require final confirmation and closed export gates
