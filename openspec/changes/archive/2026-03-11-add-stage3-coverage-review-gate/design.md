## Context

`review-master` already keeps Stage 3 truth in `raw_review_threads`, `atomic_comments`, `raw_thread_atomic_links`, and `atomic_comment_source_spans`. That is enough to reason about the internal mapping, but not enough to render a stable “copy of the original review comments with inline coverage markers” unless the runtime also stores the source-document order and the explicit covered/uncovered segments.

The design therefore adds coverage truth as first-class runtime state instead of reconstructing it ad hoc from `excerpt_text`.

## Decisions

### Decision 1: Coverage review is a separate Stage 3 checkpoint

- Stage 3 keeps its own confirmation gate.
- Stage 4 confirmation remains unchanged.
- Result:
  - Stage 3 confirms extraction completeness and mapping correctness.
  - Stage 4 confirms planning, priority, and execution order.

### Decision 2: Coverage truth is stored as ordered source documents plus ordered segments

- `review_comment_source_documents` stores the source-document identity and full text.
- `review_comment_coverage_segments` stores the sequential covered/uncovered fragments.
- `review_comment_coverage_segment_comment_links` stores one-to-many `comment_id` links for each covered segment.
- This avoids packing comment lists into a single text field and keeps the runtime DB-first contract intact.

### Decision 3: The rendered artifact is a near-original text copy, not a rewritten summary

- `review-comment-coverage.md` renders one section per source document.
- The body preserves source order and emits:
  - `[[covered thread:<thread_id> comments:<comment_id,...>]]...[[/covered]]`
  - uncovered text with no wrapper
- The output remains a read-only Markdown artifact and never rewrites the user’s input files.

## Risks / Trade-offs

- More Stage 3 schema and validation logic
  - Accepted, because silent extraction omissions are higher risk than additional deterministic tables
- Existing sample DB fixtures may not contain the new tables
  - Mitigation: tests seed coverage truth in temporary workspace copies rather than mutating checked-in SQLite fixtures

## Migration Notes

- `recipe_stage3_replace_threaded_atomic_model` now blocks on Stage 3 confirmation after writing coverage truth
- `recipe_stage3_clear_coverage_confirmation` clears the pending confirmation and reopens Stage 3 for `enter_stage_4`
- Validation now treats missing Stage 3 coverage truth as a gate-blocking error for Stage 3 and later
