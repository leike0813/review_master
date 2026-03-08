# review-master-workflow-state-machine-rules Specification

## Purpose
TBD - created by archiving change define-review-master-state-machine-instruction-loop. Update Purpose after archive.
## Requirements
### Requirement: The first release must define workflow state-machine rules
The first release SHALL provide a state-machine instruction reference at `review-master/references/workflow-state-machine.md`.

This document MUST define:

- allowed actions for each `current_stage` and `stage_gate` combination
- blocked actions for each stage
- entry and exit conditions for each stage
- how `pending_user_confirmations`, `global_blockers`, and `active_comment_id` affect what the agent may do next

#### Scenario: Stage four waits for confirmation
- **WHEN** the workflow is at `stage_4`
- **AND** user confirmations are still pending
- **THEN** the state-machine rules forbid entering phase-five execution
- **AND** require the agent to request user confirmation

#### Scenario: Evidence gap blocks completion
- **WHEN** an active comment still has an evidence gap
- **THEN** the state-machine rules forbid marking that comment complete
- **AND** require the agent to request materials or clarification

