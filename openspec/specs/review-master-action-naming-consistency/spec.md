# review-master-action-naming-consistency Specification

## Purpose
TBD - created by archiving change normalize-review-master-workflow-cross-cutting-consistency. Update Purpose after archive.
## Requirements
### Requirement: action ids are consistent across workflow layers

The workflow MUST use one consistent set of formal action ids across runtime output, workflow-state guidance, SQL recipes, and playbook examples.

#### Scenario: Stage 6 final action is not renamed across layers

- **Given** Stage 6 has a final export step and a completed state
- **When** the Agent reads `workflow_state.next_action`, `instruction_payload.recommended_next_action.action_id`, recipe guidance, or playbook fixtures
- **Then** those layers must use the same formal action names
- **And** they must not mix unrelated names for the same step

