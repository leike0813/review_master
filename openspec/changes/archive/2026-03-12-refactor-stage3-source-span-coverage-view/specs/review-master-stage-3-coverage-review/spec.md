## MODIFIED Requirements

### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 MUST render a read-only coverage-review artifact from full source documents and source-offset spans.

#### Scenario: coverage artifact is reconstructed from source spans

- **WHEN** Stage 3 data is rendered into `06-review-comment-coverage.md`
- **THEN** the renderer MUST use `review_comment_source_documents` plus `raw_thread_source_spans`
- **AND** the body MUST preserve full source-document order with covered and uncovered text both visible
- **AND** covered spans MUST be highlighted in red and display a short `thread_id` label inline
- **AND** the appendix MUST list at least `source_document_id`, `thread_id`, mapped `comment_id` values, and span offsets

#### Scenario: invalid spans block Stage 3 coverage confirmation

- **WHEN** a source span is out of bounds, mismatched with source text, or overlaps another span in the same source document
- **THEN** gate validation MUST block progression
- **AND** Stage 3 MUST not recommend entering Stage 4 until the coverage truth is repaired
