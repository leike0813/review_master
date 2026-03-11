# review-master-sqlite-runtime Specification

## Purpose
TBD - created by archiving change switch-review-master-to-sqlite-ssot-rendering. Update Purpose after archive.
## Requirements
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

### Requirement: stage-four view consolidation

Stage four MUST use a single rendered workboard view.

#### Scenario: render stage-four artifacts

- **WHEN** stage-four data exists in the runtime database
- **THEN** the workspace MUST render `comment-workboard.md`
- **AND** it MUST NOT require both `comment-manuscript-mapping-table.md` and `revision-board.md` as runtime artifacts

