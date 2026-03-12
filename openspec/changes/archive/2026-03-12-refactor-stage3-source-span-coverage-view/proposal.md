## Why

The Stage 3 coverage artifact still carries a segment-first model that does not reliably show coverage against the full original reviewer document. Users need a full-text reading view where extracted substantive threads are highlighted in place, while untouched text remains visible.

## What Changes

- Refactor Stage 3 coverage truth to use source-offset spans (`raw_thread_source_spans`) as the primary coverage model.
- Render `06-review-comment-coverage.md` from full source documents plus span offsets, with inline red highlights and short thread tags.
- Keep an appendix mapping table with `thread_id`, mapped `comment_id` list, and offset/excerpt metadata.
- Keep Stage 3 user-confirmation gating unchanged before Stage 4.
- For legacy workspaces that only have thread-level synthetic coverage, require rerunning Stage 3 from original reviewer/editor source files.

## Capabilities

### Modified Capabilities

- `review-master-stage-3-coverage-review`
- `review-master-threaded-comment-model`
- `review-master-template-driven-rendering`
- `review-master-user-checkpoints`
- `review-master-skill-instructions`

## Impact

- Adds one Stage 3 schema table: `raw_thread_source_spans`.
- Changes Stage 3 validation and rendering logic to span/offset-driven coverage.
- Updates Stage 3 docs, localization, templates, and tests.
