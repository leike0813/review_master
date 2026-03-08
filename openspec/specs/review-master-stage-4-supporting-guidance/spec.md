# review-master-stage-4-supporting-guidance Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-4-atomic-workboard-planning. Update Purpose after archive.
## Requirements
### Requirement: Stage 4 supporting docs MUST stay aligned with the refined Stage 4 instructions

The supporting guidance for recipes, the state machine, helper-script usage, and the happy-path playbook MUST explicitly align with the refined Stage 4 instructions.

#### Scenario: Stage 4 recipe and state machine alignment

- **WHEN** the Agent reads the Stage 4 reference doc
- **THEN** the linked SQL recipe, helper-script guidance, and workflow-state-machine guidance describe the same planning fields, block conditions, and confirmation gate

#### Scenario: happy-path playbook demonstrates default confirmation

- **WHEN** a reader uses the happy-path playbook as a concrete example
- **THEN** the Stage 4 section shows provisional planning and a default user confirmation gate before Stage 5

