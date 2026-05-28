# review-master-sqlite-runtime Delta

## ADDED Requirements

### Requirement: Runtime schema must include Stage 6 semantic revision log truth

The runtime SQLite schema MUST model Stage 6 around workspace manuscript copies, revision plan actions, Agent-authored semantic revision logs, and thread-level response rows rather than diff-generated audit truth.

#### Scenario: semantic revision log truth is first-class runtime state

- **WHEN** the runtime database schema is initialized
- **THEN** it MUST include `revision_action_log_entries`
- **AND** `revision_action_log_entries` MUST store target file, target locator, change type, change summary, rationale, evidence source, and expected response use
- **AND** completed or draft revision logs MUST have at least one semantic entry
- **AND** `revision_action_log_file_diffs` and `working_copy_file_state` MUST be treated as legacy compatibility tables rather than Stage 6 gate truth
