# review-master-sqlite-runtime Specification

## Purpose
TBD - created by archiving change switch-review-master-to-sqlite-ssot-rendering. Update Purpose after archive.
## Requirements
### Requirement: DB-first runtime workspace

The runtime workspace MUST use SQLite as the only writable source of truth.

#### Scenario: Stage 5 draft tables exist in runtime schema

- **WHEN** the runtime database schema is initialized
- **THEN** it MUST include `strategy_action_manuscript_drafts`
- **AND** it MUST include `comment_response_drafts`
- **AND** it MUST include `comment_blockers`
- **AND** these tables MUST be part of the required runtime contract

#### Scenario: Completion status uses draft semantics

- **WHEN** the runtime database schema is initialized
- **THEN** `comment_completion_status` MUST expose `manuscript_draft_done`
- **AND** it MUST expose `response_draft_done`
- **AND** it MUST NOT depend on `manuscript_change_done` or `response_section_done` as the active schema contract

### Requirement: stage-four view consolidation

Stage four MUST use a single rendered workboard view.

#### Scenario: render stage-four artifacts

- **WHEN** stage-four data exists in the runtime database
- **THEN** the workspace MUST render `comment-workboard.md`
- **AND** it MUST NOT require both `comment-manuscript-mapping-table.md` and `revision-board.md` as runtime artifacts

