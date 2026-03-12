## MODIFIED Requirements

### Requirement: `review-master` MUST model review comments as raw threads plus canonical atomic items

Stage 3 source anchoring MUST be role-aware.

#### Scenario: each raw thread has primary span anchor

- **WHEN** Stage 3 writes `raw_thread_source_spans`
- **THEN** each `thread_id` MUST include at least one `span_role='primary'`
- **AND** each span MUST keep offset-traceable source anchoring (`source_document_id`, `start_offset`, `end_offset`, `span_text`)

#### Scenario: deduplicated repeats remain source-visible

- **WHEN** a substantive source fragment is repeated and deduplicated in canonical summaries
- **THEN** Stage 3 SHOULD keep repeated source locations in `raw_thread_source_spans` using `span_role='duplicate_filtered'`
- **AND** the repeated span MUST still map to an existing canonical `thread_id`
