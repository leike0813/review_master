# review-master-threaded-comment-model Specification

## Purpose
TBD - created by archiving change restructure-review-master-comment-mapping-model. Update Purpose after archive.
## Requirements
### Requirement: `review-master` MUST model review comments as raw threads plus canonical atomic items

The runtime model MUST anchor each raw review thread back to source-document offsets.

#### Scenario: raw thread source anchoring is mandatory

- **WHEN** Stage 3 writes `raw_review_threads`
- **THEN** each `thread_id` MUST have at least one row in `raw_thread_source_spans`
- **AND** each span MUST include `source_document_id`, `start_offset`, `end_offset`, and `span_text`
- **AND** `span_text` MUST match the substring slice of `review_comment_source_documents.original_text`

#### Scenario: substantive-only extraction remains canonical policy

- **WHEN** raw threads are extracted from reviewer/editor comments
- **THEN** Stage 3 MUST default to extracting actionable substantive comments
- **AND** non-substantive boilerplate (for example pure Yes/No form ticks or courtesy-only text) MUST not be forced into raw threads by default

### Requirement: final response letter output MUST be indexed by original review threads

The final response structure MUST return to original reviewer thread order.

#### Scenario: response outline uses thread order

- **WHEN** stage six prepares the response outline
- **THEN** `response_thread_resolution_links` groups resolutions by `thread_id`
- **AND** the rendered `response-letter-outline.md` follows reviewer grouping and `thread_order`
- **AND** it does not directly render the final response letter as a flat `comment_id` list

