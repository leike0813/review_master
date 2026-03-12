## MODIFIED Requirements

### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 MUST render a read-only coverage-review artifact that shows how the extracted review-comment truth covers the original source text.

#### Scenario: coverage artifact shows readable original text with visual highlighting

- **WHEN** `review-comment-coverage.md` is rendered
- **THEN** covered source spans MUST be visually emphasized in the body (bold red highlight)
- **AND** uncovered source text MUST remain visible without being hidden or dropped
- **AND** the artifact MUST include a coverage-mapping appendix that lists covered segments with `source_document_id`, `segment_order`, `thread_id`, and mapped `comment_id` values
- **AND** the body MUST NOT rely on inline wrapper syntax like `[[covered ...]]...[[/covered]]` to express coverage status
