# review-master-stage-3-coverage-review Specification

## Purpose
TBD - created by archiving change add-stage3-coverage-review-gate. Update Purpose after archive.
## Requirements
### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 MUST render a read-only coverage-review artifact that shows how the extracted review-comment truth covers the original source text.

#### Scenario: coverage artifact shows readable original text with visual highlighting

- **WHEN** `review-comment-coverage.md` is rendered
- **THEN** covered source spans MUST be visually emphasized in the body (bold red highlight)
- **AND** uncovered source text MUST remain visible without being hidden or dropped
- **AND** the artifact MUST include a coverage-mapping appendix that lists covered segments with `source_document_id`, `segment_order`, `thread_id`, and mapped `comment_id` values
- **AND** the body MUST NOT rely on inline wrapper syntax like `[[covered ...]]...[[/covered]]` to express coverage status

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

