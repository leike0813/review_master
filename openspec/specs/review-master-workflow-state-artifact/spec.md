# review-master-workflow-state-artifact Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-artifact-workspace. Update Purpose after archive.
## Requirements
### Requirement: Runtime workspace must include a workflow state artifact
Each runtime artifact workspace SHALL include `workflow-state.yaml` as the single first-release YAML runtime artifact.

`workflow-state.yaml` MUST track workflow-level control state, not per-comment detail rows.

At minimum it MUST contain:

- `current_stage`
- `stage_gate`
- `active_comment_id`
- `pending_user_confirmations`
- `global_blockers`
- `next_action`
- `artifact_root`

`active_comment_id` MAY be empty, but if present it MUST refer to a valid `comment_id` from the atomic review comment list.

#### Scenario: Active comment points to a valid atomic comment
- **WHEN** `workflow-state.yaml` sets a non-empty `active_comment_id`
- **THEN** that `comment_id` exists in `atomic-review-comment-list.md`

#### Scenario: Workflow state remains current-state only
- **WHEN** the workspace is updated during the six-stage flow
- **THEN** `workflow-state.yaml` records the current stage, gate, blockers, and next action
- **AND** it does not need to persist a full execution history

