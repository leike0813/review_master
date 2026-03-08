# review-master-stage-1-2-supporting-guidance Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-1-and-2-instructions. Update Purpose after archive.
## Requirements
### Requirement: Stage 1 and Stage 2 supporting docs MUST stay aligned with the refined instructions

The supporting guidance for recipes, the state machine, helper-script usage, and the happy-path playbook MUST explicitly align with the refined Stage 1 and Stage 2 instructions.

#### Scenario: Stage 1 recipe and state machine alignment

- **WHEN** the Agent reads the Stage 1 reference doc
- **THEN** the linked SQL recipe, helper-script guidance, and workflow-state-machine guidance describe the same entry conditions, block conditions, and next-step expectations

#### Scenario: happy-path playbook demonstrates refined stage behavior

- **WHEN** a reader uses the happy-path playbook as a concrete example
- **THEN** Stage 1 and Stage 2 show what the Agent reads, writes, asks, and why the workflow is allowed to advance

