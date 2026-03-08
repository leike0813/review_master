# review-master-validator-instruction-payload Specification

## Purpose
TBD - created by archiving change define-review-master-state-machine-instruction-loop. Update Purpose after archive.
## Requirements
### Requirement: Validator must emit an instruction payload
`review-master/scripts/validate_artifact_consistency.py` SHALL preserve its current JSON report fields and SHALL add `instruction_payload` at the top level.

At minimum, `instruction_payload` MUST contain:

- `current_state`
- `allowed_next_actions`
- `recommended_next_action`
- `repair_sequence`
- `blocked_actions`

Each action object in `allowed_next_actions`, `recommended_next_action`, and `repair_sequence` MUST include:

- `action_id`
- `instruction`
- `reason`
- `target_artifacts`

#### Scenario: Stage one recommends stage two work
- **WHEN** `workflow-state.yaml` is `stage_1` and `ready`
- **AND** no validation issues are present
- **THEN** `recommended_next_action` tells the agent to begin stage two and author the manuscript structure summary

#### Scenario: Stage four with pending confirmations recommends user interaction
- **WHEN** `workflow-state.yaml` is `stage_4`
- **AND** `pending_user_confirmations` is not empty
- **AND** no validation issues are present
- **THEN** `recommended_next_action` tells the agent to request user confirmation
- **AND** `blocked_actions` includes phase-five execution

