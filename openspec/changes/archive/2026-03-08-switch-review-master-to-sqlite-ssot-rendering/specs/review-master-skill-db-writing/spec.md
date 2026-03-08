## ADDED Requirements

### Requirement: skill writes runtime state through SQL

The skill MUST treat the runtime database as the only writable runtime surface.

#### Scenario: agent advances the workflow

- **WHEN** the agent needs to update workflow state or comment-scoped data
- **THEN** it MUST write `review-master.db`
- **AND** it MUST NOT directly edit runtime Markdown artifacts
- **AND** it MUST rerun the validator after the write

### Requirement: direct SQL requires foreign key enforcement

Direct SQL writes MUST enforce foreign keys.

#### Scenario: agent opens a writable database connection

- **WHEN** the agent writes to `review-master.db`
- **THEN** it MUST enable `PRAGMA foreign_keys = ON`
