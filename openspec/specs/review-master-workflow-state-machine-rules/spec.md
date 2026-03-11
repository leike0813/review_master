# review-master-workflow-state-machine-rules Specification

## Purpose
TBD - created by archiving change define-review-master-state-machine-instruction-loop. Update Purpose after archive.
## Requirements
### Requirement: The first release must define workflow state-machine rules

The first release SHALL provide a state-machine instruction reference at `review-master/references/workflow-state-machine.md`.

#### Scenario: Stage five allows explicit focus switching

- **WHEN** the workflow is at `stage_5`
- **AND** there is no `workflow_global_blockers` entry
- **THEN** the state-machine rules must allow `set_active_comment`
- **AND** they must explain that explicit switching is legal even if the current comment is not yet done

#### Scenario: Global blockers still freeze Stage five

- **WHEN** the workflow is at `stage_5`
- **AND** `workflow_global_blockers` is non-empty
- **THEN** the state-machine rules must forbid `set_active_comment`
- **AND** they must require the Agent to resolve the global blocker first

