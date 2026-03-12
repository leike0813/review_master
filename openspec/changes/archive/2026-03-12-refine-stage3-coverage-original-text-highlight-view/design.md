## Context

Stage 3 already stores correct coverage truth (`review_comment_source_documents`, `review_comment_coverage_segments`, `review_comment_coverage_segment_comment_links`) and enforces a confirmation gate before Stage 4. The gap is presentation: users need an original-text reading experience with immediate visual distinction between covered and uncovered text.

## Decisions

### Decision 1: Keep the existing Stage 3 data model and gate behavior

- No schema changes.
- No gate/action changes.
- Only the rendered artifact and wording are refined.

### Decision 2: Render coverage body as readable original text with visual highlighting

- `06-review-comment-coverage.md` keeps source-document order.
- Covered segments are rendered in bold red text.
- Uncovered segments remain in default text color.
- Body no longer contains inline `[[covered ...]]` wrappers.

### Decision 3: Move mapping detail to an appendix table

- Each covered segment is listed in a structured appendix row:
  - `source_document_id`
  - `segment_order`
  - `thread_id`
  - `comment_ids`
  - excerpt
- This keeps the body readable while preserving auditability.

## Trade-offs

- Markdown viewers differ in HTML/CSS support; red emphasis may degrade in some renderers.
- Mitigation: mapping appendix stays fully textual and deterministic, so verification does not depend on color support.
