## ADDED Requirements

### Requirement: Repository-level playbook index must list minimal and complex scenarios

The repository SHALL provide `playbooks/README.md` as an index for review-master playbooks.

The index MUST list at least:

- the minimal happy-path playbook
- the evidence-supplement multi-review playbook

#### Scenario: Playbook index lists both scenarios

- **WHEN** a developer opens `playbooks/README.md`
- **THEN** the index explains the purpose of the minimal happy-path playbook
- **AND** it explains the purpose of the evidence-supplement multi-review playbook
