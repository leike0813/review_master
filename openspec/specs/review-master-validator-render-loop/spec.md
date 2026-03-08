# review-master-validator-render-loop Specification

## Purpose
TBD - created by archiving change switch-review-master-to-sqlite-ssot-rendering. Update Purpose after archive.
## Requirements
### Requirement: validator reads DB and rerenders views

The validator MUST read the runtime database, validate runtime state, and rerender all Markdown views.

#### Scenario: validate a healthy workspace

- **WHEN** the workspace contains a valid `review-master.db`
- **THEN** the validator MUST rerender:
  - `workflow-state.md`
  - `manuscript-structure-summary.md`
  - `atomic-review-comment-list.md`
  - `comment-workboard.md`
  - `final-assembly-checklist.md`
  - `response-strategy-cards/{comment_id}.md`
- **AND** it MUST emit `instruction_payload`

### Requirement: validator remains gatekeeper

The validator MUST continue to enforce state-machine gatekeeping.

#### Scenario: stage four still has pending confirmations

- **WHEN** the database state is `stage_4`
- **AND** pending user confirmations are still present
- **THEN** the validator MUST block entry into stage five
- **AND** it MUST recommend requesting confirmation first

