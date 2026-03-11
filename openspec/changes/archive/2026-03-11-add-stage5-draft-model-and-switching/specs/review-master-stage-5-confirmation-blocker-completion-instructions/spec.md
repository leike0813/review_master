## MODIFIED Requirements

### Requirement: Stage 5 must define confirmation, blocker, and completion gates

Stage 5 MUST explicitly define confirmation, blocker, and completion using the new draft-truth model.

#### Scenario: Completion requires formal draft truth rows

- **Given** an active item has a confirmed strategy and closed evidence gap
- **When** `strategy_action_manuscript_drafts` or `comment_response_drafts` are still missing
- **Then** the docs must forbid marking the item complete
- **And** the completion bar must require formal draft rows rather than implied or off-record drafts

#### Scenario: Comment-scoped blocker does not freeze the whole stage

- **Given** the current `active_comment_id` has a blocker written in `comment_blockers`
- **When** no `workflow_global_blockers` exist
- **Then** the docs must keep that comment blocked from completion
- **And** they must still allow an explicit switch to another non-done comment

#### Scenario: Legacy completion flags are not trusted after migration

- **Given** a legacy Stage 5 workspace is migrated to the new draft model
- **When** the migration finishes
- **Then** the docs must require `manuscript_draft_done = no` for every comment
- **And** they must require `response_draft_done = no` for every comment
- **And** they must explain that the Agent has to rebuild formal draft truth before completion can resume
