# review-master-playbook-sql-recipes Specification

## Purpose
TBD - created by archiving change define-review-master-sql-write-recipes. Update Purpose after archive.
## Requirements
### Requirement: playbooks show recipe-driven SQL writes

The repository playbooks MUST show how agent actions map to recipe IDs and representative SQL.

#### Scenario: documenting a stage transition

- **WHEN** a playbook describes a key stage transition
- **THEN** it MUST identify the `recipe_id`
- **AND** it MUST show a representative SQL fragment
- **AND** it MUST state which tables were updated

### Requirement: playbooks echo validator recipe hints

Playbooks MUST show the validator's returned `recipe_id` for the next action.

#### Scenario: validator recommends the next action

- **WHEN** a playbook cites `recommended_next_action`
- **THEN** it MUST include the corresponding `recipe_id`
- **AND** the recipe name MUST match the validator and recipe handbook

