# review-master-threaded-comment-model Specification

## Purpose
TBD - created by archiving change restructure-review-master-comment-mapping-model. Update Purpose after archive.
## Requirements
### Requirement: `review-master` MUST model review comments as raw threads plus canonical atomic items

The runtime data model MUST preserve original reviewer / editor threads and MUST not collapse the final response index directly to atomic comments.

#### Scenario: one raw thread maps to multiple atomic items

- **WHEN** a reviewer writes one original thread containing multiple substantive issues
- **THEN** the runtime model stores one `raw_review_thread`
- **AND** that thread may link to multiple `atomic_comments` through `raw_thread_atomic_links`

#### Scenario: duplicate issues across reviewers are merged canonically

- **WHEN** two reviewers raise the same substantive concern
- **THEN** the runtime model may map both original threads to the same canonical `comment_id`
- **AND** the merge rationale remains traceable through `atomic_comment_source_spans`

### Requirement: final response letter output MUST be indexed by original review threads

The final response structure MUST return to original reviewer thread order.

#### Scenario: response outline uses thread order

- **WHEN** stage six prepares the response outline
- **THEN** `response_thread_resolution_links` groups resolutions by `thread_id`
- **AND** the rendered `response-letter-outline.md` follows reviewer grouping and `thread_order`
- **AND** it does not directly render the final response letter as a flat `comment_id` list

