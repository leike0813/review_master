# review-master-template-driven-rendering Delta

## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

Stage 6 rendered views MUST expose Agent-authored semantic revision log entries and plan/thread closure state.

#### Scenario: revision log view shows semantic entries

- **WHEN** Stage 6 revision logs exist
- **THEN** `13-revision-action-log.md` MUST render entries from `revision_action_log_entries`
- **AND** it MUST show change type, target file, target locator, change summary, rationale, evidence source, and expected response use
- **AND** it MUST NOT render a diff excerpt table as the primary log surface

#### Scenario: final checklist uses closure truth

- **WHEN** `17-final-assembly-checklist.md` is rendered
- **THEN** it MUST show revision plan closure and thread-level response coverage
- **AND** it MUST NOT require a working-copy hash table for Stage 6 completion
