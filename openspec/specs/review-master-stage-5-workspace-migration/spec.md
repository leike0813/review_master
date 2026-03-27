# review-master-stage-5-workspace-migration Specification

## Purpose
TBD - created by archiving change add-stage5-draft-model-and-switching. Update Purpose after archive.
## Requirements
### Requirement: Legacy Stage 5 workspace can be migrated in place

The skill MUST provide a supported migration script for legacy Stage 5 workspaces.

#### Scenario: migrate a legacy workspace

- **WHEN** a workspace still uses `manuscript_change_done` and `response_section_done`
- **THEN** the migration script MUST rebuild `comment_completion_status` with draft field names
- **AND** it MUST create `strategy_action_manuscript_execution_items`
- **AND** it MUST create `comment_response_drafts`
- **AND** it MUST create `comment_blockers`

#### Scenario: migration keeps the workspace resumable

- **WHEN** the migration finishes
- **THEN** it MUST preserve `workflow_state.active_comment_id`
- **AND** it MUST rerender the workspace views
- **AND** it MUST emit a machine-readable summary of the migrated state

#### Scenario: draft completion flags are reset

- **WHEN** the migration finishes
- **THEN** every comment MUST have `manuscript_execution_items_done = no`
- **AND** every comment MUST have `response_draft_done = no`
- **AND** the remaining completion fields may be preserved
