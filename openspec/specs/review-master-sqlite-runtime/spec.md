# review-master-sqlite-runtime Specification

## Purpose
TBD - created by archiving change switch-review-master-to-sqlite-ssot-rendering. Update Purpose after archive.
## Requirements
### Requirement: DB-first runtime workspace

The runtime workspace MUST use SQLite as the only writable source of truth.

#### Scenario: initialize a runtime workspace

- **WHEN** the agent initializes a new runtime workspace
- **THEN** the workspace MUST contain `review-master.db`
- **AND** the runtime Markdown artifacts MUST be treated as read-only rendered views
- **AND** `workflow-state.yaml` MUST NOT be part of the runtime contract

### Requirement: stage-four view consolidation

Stage four MUST use a single rendered workboard view.

#### Scenario: render stage-four artifacts

- **WHEN** stage-four data exists in the runtime database
- **THEN** the workspace MUST render `comment-workboard.md`
- **AND** it MUST NOT require both `comment-manuscript-mapping-table.md` and `revision-board.md` as runtime artifacts

