## Overview

This change upgrades Stage 3 coverage from single-class covered spans to role-aware covered spans.

- `primary`: canonical thread anchor span.
- `supporting`: additional substantive body text for the same thread.
- `duplicate_filtered`: repeated substantive occurrence that is intentionally deduplicated at summary level.

## Data Model

### `raw_thread_source_spans`

- Add `span_role` with allowed values: `primary`, `supporting`, `duplicate_filtered`.
- Legacy compatibility:
  - Runtime auto-adds `span_role` column if missing.
  - Existing rows backfill to `primary`.

### Constraints

- Existing constraints stay: offset bounds, substring match, and no overlap in same source document.
- New hard constraint: each `thread_id` must have at least one `primary` span.
- `duplicate_filtered` rows still bind to canonical `thread_id`; comment mapping continues through `raw_thread_atomic_links`.

## Rendering

`06-review-comment-coverage.md` remains full-text and source-order-preserving.

- `primary` / `supporting`: bold red highlight.
- `duplicate_filtered`: bold orange highlight and `dup` short tag.
- Uncovered text remains visible.
- Appendix includes `span_role` column in addition to thread/comment/offset mapping.

## Gate Behavior

- Stage 3 gate semantics remain unchanged: user confirmation is still mandatory before Stage 4.
- Hard failures still block (invalid offsets/text, overlap, missing primary span, broken mapping).
- New weak advisory (non-blocking): detect likely "title-only coverage" patterns (primary-only thread followed by long uncovered adjacent paragraph) and include advisories in instruction payload.
