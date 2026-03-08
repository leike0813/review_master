## ADDED Requirements

### Requirement: Playbook must include minimal example assets

The first release SHALL provide a minimal example asset set alongside the happy-path playbook.

At minimum, the example asset set MUST include:

- a minimal LaTeX manuscript input
- a minimal Markdown or txt review-comment input
- a final-state runtime workspace that uses the current fixed workspace layout
- representative validator JSON outputs whose top-level structure matches the current validator contract
- sample final deliverables for the revised manuscript and Markdown response letter

The example assets MUST stay consistent with the current:

- workspace layout
- `workflow-state.yaml` field names
- artifact authoring rules
- validator `instruction_payload` shape

#### Scenario: Final-state workspace uses the current runtime layout

- **WHEN** the example asset set provides a sample workspace
- **THEN** the workspace contains `workflow-state.yaml`
- **AND** it contains the six Markdown runtime artifacts plus `response-strategy-cards/`

#### Scenario: Validator outputs match the current contract

- **WHEN** the playbook stores representative validator outputs
- **THEN** each JSON sample includes `status`, `summary`, `artifact_presence`, `format_errors`, `dependency_errors`, `consistency_errors`, and `instruction_payload`
- **AND** `instruction_payload` includes `current_state`, `allowed_next_actions`, `recommended_next_action`, `repair_sequence`, and `blocked_actions`
