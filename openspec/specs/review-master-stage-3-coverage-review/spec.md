# review-master-stage-3-coverage-review Specification

## Purpose
TBD - created by archiving change add-stage3-coverage-review-gate. Update Purpose after archive.
## Requirements
### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 MUST render a read-only coverage-review artifact that shows how the extracted review-comment truth covers the original source text.

#### Scenario: coverage artifact exists after Stage 3 modeling

- **WHEN** Stage 3 finishes writing `raw_review_threads`, `atomic_comments`, `raw_thread_atomic_links`, and `atomic_comment_source_spans`
- **THEN** it MUST also write `review_comment_source_documents`
- **AND** it MUST write `review_comment_coverage_segments`
- **AND** it MUST write `review_comment_coverage_segment_comment_links`
- **AND** the workspace MUST render `review-comment-coverage.md`

#### Scenario: coverage artifact shows covered and uncovered text inline

- **WHEN** `review-comment-coverage.md` is rendered
- **THEN** covered text MUST appear inline as `[[covered thread:<thread_id> comments:<comment_id,...>]]...[[/covered]]`
- **AND** uncovered source text MUST remain visible without being hidden or dropped

### Requirement: Stage 3 coverage review requires user confirmation

After Stage 3 coverage truth is written, the workflow MUST stop for user confirmation before Stage 4 workboard planning can begin.

#### Scenario: Stage 3 cannot enter Stage 4 before confirmation

- **WHEN** `workflow_state.current_stage` is `stage_3`
- **AND** Stage 3 coverage confirmations are still pending
- **THEN** the recommended next action MUST be `request_stage3_coverage_confirmation`
- **AND** the workflow MUST NOT recommend `enter_stage_4`

#### Scenario: confirmation clear reopens Stage 3 for Stage 4 entry

- **WHEN** the user confirms the Stage 3 coverage artifact
- **THEN** the workflow may clear the Stage 3 pending confirmations
- **AND** the next action may become `enter_stage_4`

