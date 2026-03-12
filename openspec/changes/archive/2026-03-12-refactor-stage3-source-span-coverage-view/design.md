## Overview

This change converts Stage 3 coverage from a pre-segmented view model to a source-span model:

- Source documents remain in `review_comment_source_documents`.
- Each `raw_review_threads.thread_id` is anchored to one or more offset spans in `raw_thread_source_spans`.
- Coverage view segments are reconstructed at render time from source text + span offsets.

## Data Model

### New Table

- `raw_thread_source_spans`
  - `thread_id`
  - `source_document_id`
  - `span_order`
  - `start_offset`
  - `end_offset`
  - `span_text`

### Core Constraints

- Every `raw_review_threads.thread_id` must have at least one span.
- `span_text` must equal `original_text[start_offset:end_offset]` (newline normalization allowed).
- Spans within the same `source_document_id` must not overlap.
- Stage 3 dependency remains: every `thread_id` must map to at least one `comment_id` through `raw_thread_atomic_links`.

## Rendering Behavior

`06-review-comment-coverage.md` is rendered as:

- Full source text order per source document.
- Covered spans highlighted in bold red with short labels like `[R2_T003]`.
- Uncovered spans shown unchanged.
- Appendix table listing source document, thread, mapped comment IDs, span order, offset range, and excerpt.

## Validation and Migration

- Gate validation checks span bounds, span-text match, and overlap.
- If legacy thread-level synthetic source documents are detected (for example `legacy-thread::...`), gate blocks Stage 3+ progression with a rebuild instruction.
- Migration strategy is rebuild-oriented: rerun Stage 3 from original reviewer/editor files.
