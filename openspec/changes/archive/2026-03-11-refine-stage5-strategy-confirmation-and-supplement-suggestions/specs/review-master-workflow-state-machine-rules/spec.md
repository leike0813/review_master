## MODIFIED Requirements

### Requirement: The first release must define workflow state-machine rules

The first release SHALL provide a state-machine instruction reference at `review-master/references/workflow-state-machine.md`.

#### Scenario: Stage five uses generic pending confirmations as a hard gate

- **WHEN** the workflow is at `stage_5`
- **AND** `workflow_pending_user_confirmations` is non-empty because the active strategy still needs confirmation
- **THEN** the state-machine rules must require `request_pending_confirmation`
- **AND** they must forbid `author_comment_drafts` and `advance_active_comment`
