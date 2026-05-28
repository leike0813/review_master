# review-master-workflow-glossary Specification

## Purpose
TBD - created by archiving change normalize-review-master-workflow-cross-cutting-consistency. Update Purpose after archive.
## Requirements
### Requirement: workflow glossary is the single naming source

The workflow glossary MUST describe Stage 6 revision logging as Agent-owned semantic log writing.

#### Scenario: glossary defines Agent-owned Stage 6 log truth

- **WHEN** the glossary lists Stage 6 runtime truth and helper scripts
- **THEN** it MUST list `revision_action_log_entries` as the primary per-log detail table
- **AND** it MUST describe `revision_action_log_file_diffs` and `working_copy_file_state` as legacy compatibility tables
- **AND** it MUST describe `commit_revision_round.py` as `semantic log write -> gate-and-render`

### Requirement: Workflow glossary uses canonical Stage 5 completion names

The workflow glossary MUST use the renamed Stage 5 completion field and define manuscript execution items as the official manuscript-side truth model.

#### Scenario: glossary defines Stage 5 completion fields

- **WHEN** the workflow glossary defines Stage 5 completion fields
- **THEN** it MUST use `manuscript_execution_items_done` and `response_draft_done` as the official completion-field names
- **AND** it MUST define manuscript execution items as the typed manuscript-side truth for Stage 5

