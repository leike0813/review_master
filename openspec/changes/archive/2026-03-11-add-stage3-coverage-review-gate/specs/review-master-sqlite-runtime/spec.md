## MODIFIED Requirements

### Requirement: DB-first runtime workspace

The runtime workspace MUST use SQLite as the only writable source of truth.

#### Scenario: Stage 3 coverage truth exists in runtime schema

- **WHEN** the runtime database schema is initialized
- **THEN** it MUST include `review_comment_source_documents`
- **AND** it MUST include `review_comment_coverage_segments`
- **AND** it MUST include `review_comment_coverage_segment_comment_links`

#### Scenario: Stage 3 coverage truth remains relational

- **WHEN** one covered segment maps to multiple canonical atomic comments
- **THEN** the runtime schema MUST represent those links in a relation table
- **AND** it MUST NOT serialize the `comment_id` list into one text column
