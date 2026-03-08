# review-master-stage-3-supporting-guidance Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-3-threaded-atomization. Update Purpose after archive.
## Requirements
### Requirement: Stage 3 supporting docs MUST stay aligned with the refined Stage 3 instructions

The supporting guidance for recipes, the state machine, helper-script usage, and the happy-path playbook MUST explicitly align with the refined Stage 3 instructions.

#### Scenario: Stage 3 recipe and state machine alignment

- **WHEN** the Agent reads the Stage 3 reference doc
- **THEN** the linked SQL recipe, helper-script guidance, and workflow-state-machine guidance describe the same write order, block conditions, and next-step expectations

#### Scenario: happy-path playbook demonstrates Stage 3 split logic

- **WHEN** a reader uses the happy-path playbook as a concrete example
- **THEN** the Stage 3 section shows at least one raw reviewer thread splitting into multiple canonical atomic items
- **AND** explains why those atomic items are not merged

