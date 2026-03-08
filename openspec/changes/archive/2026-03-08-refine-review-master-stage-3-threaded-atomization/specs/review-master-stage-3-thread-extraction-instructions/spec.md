## ADDED Requirements

### Requirement: stage 3 guidance MUST define raw review thread extraction rules

`review-master` MUST describe Stage 3 as a workflow that first extracts reviewer/editor raw threads before it performs any canonical atomic modeling.

#### Scenario: one raw reviewer entry maps to multiple atomic items

- **WHEN** a single reviewer thread contains multiple substantive problems
- **THEN** the Stage 3 guidance tells the Agent to preserve one `thread_id`
- **AND** split the content into multiple `comment_id` rows
- **AND** record the mapping through `raw_thread_atomic_links`

#### Scenario: editor and reviewer comments both become raw threads

- **WHEN** the input contains editor comments and reviewer comments
- **THEN** Stage 3 guidance tells the Agent to write both into `raw_review_threads`
- **AND** preserve their source identity through `source_type`
