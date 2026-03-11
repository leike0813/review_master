## MODIFIED Requirements

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

#### Scenario: language context exists in runtime schema

- **WHEN** the runtime database schema is initialized
- **THEN** it MUST include `runtime_language_context`
- **AND** the schema MUST treat `document_language` and `working_language` as persisted runtime state rather than transient Agent memory
