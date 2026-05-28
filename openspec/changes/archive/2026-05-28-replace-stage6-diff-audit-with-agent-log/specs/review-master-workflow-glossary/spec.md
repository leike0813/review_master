# review-master-workflow-glossary Delta

## MODIFIED Requirements

### Requirement: workflow glossary is the single naming source

The workflow glossary MUST describe Stage 6 revision logging as Agent-owned semantic log writing.

#### Scenario: glossary defines Agent-owned Stage 6 log truth

- **WHEN** the glossary lists Stage 6 runtime truth and helper scripts
- **THEN** it MUST list `revision_action_log_entries` as the primary per-log detail table
- **AND** it MUST describe `revision_action_log_file_diffs` and `working_copy_file_state` as legacy compatibility tables
- **AND** it MUST describe `commit_revision_round.py` as `semantic log write -> gate-and-render`
