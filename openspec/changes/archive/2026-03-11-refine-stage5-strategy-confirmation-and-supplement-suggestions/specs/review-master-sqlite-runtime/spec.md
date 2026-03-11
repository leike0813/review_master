## MODIFIED Requirements

### Requirement: DB-first runtime workspace

The runtime workspace MUST use SQLite as the only writable source of truth.

#### Scenario: Stage 5 supplement suggestion truth exists in runtime schema

- **WHEN** the runtime database schema is initialized
- **THEN** it MUST include `supplement_suggestion_items`
- **AND** it MUST include `supplement_suggestion_intake_links`

#### Scenario: supplement suggestions remain relational

- **WHEN** one supplement suggestion is linked to multiple uploaded files
- **THEN** the runtime schema MUST represent those links in a relation table
- **AND** it MUST NOT serialize the file list into one text column
