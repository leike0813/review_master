## ADDED Requirements

### Requirement: Happy-path playbook must live outside the skill package

The first release SHALL store review-master execution playbooks as repository-level documentation under `playbooks/`.

Playbooks MUST NOT be added to `review-master/` because they are developer-facing rehearsal material rather than runtime skill components.

#### Scenario: Playbook is stored as repository-level documentation

- **WHEN** the repository adds a happy-path execution playbook for review-master
- **THEN** the playbook is stored under `playbooks/`
- **AND** it is not stored inside `review-master/`

#### Scenario: Playbook uses repository-level example assets

- **WHEN** the playbook references sample inputs, workspaces, outputs, or validator reports
- **THEN** those assets are stored under `playbooks/examples/`
- **AND** they are not treated as skill runtime assets
