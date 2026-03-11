## MODIFIED Requirements

### Requirement: Validator must emit an instruction payload

`review-master/scripts/validate_artifact_consistency.py` SHALL preserve its current JSON report fields and SHALL add `instruction_payload` at the top level.

#### Scenario: Stage five pending confirmations recommend user interaction

- **WHEN** the workflow is `stage_5`
- **AND** the active strategy still has pending confirmations
- **AND** no validation issues are present
- **THEN** `recommended_next_action` MUST be `request_pending_confirmation`
- **AND** `blocked_actions` MUST include Stage 5 draft authoring and completion-style advancement
