# review-master-template-driven-rendering Specification

## Purpose
TBD - created by archiving change restructure-review-master-package-for-template-driven-rendering. Update Purpose after archive.
## Requirements
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

### Requirement: `workflow-state.md` MUST be retired as a rendered runtime view

Workflow state MUST remain in SQLite only.

#### Scenario: rendered view set

- **WHEN** the validator renders a workspace
- **THEN** it produces:
  - `01-agent-resume.md`
  - `02-manuscript-structure-summary.md`
  - `03-raw-review-thread-list.md`
  - `04-atomic-review-comment-list.md`
  - `05-thread-to-atomic-mapping.md`
  - `06-review-comment-coverage.md`
  - `07-atomic-comment-workboard.md`
  - `08-supplement-suggestion-plan.md`
  - `09-style-profile.md`
  - `10-action-copy-variants.md`
  - `11-response-letter-outline.md`
  - `12-export-patch-plan.md`
  - `13-response-letter-table-preview.md`
  - `14-response-letter-table-preview.tex`
  - `15-supplement-intake-plan.md`
  - `16-final-assembly-checklist.md`
  - `response-strategy-cards/{comment_id}.md`
- **AND** the strategy-card template groups manuscript-side execution truth by execution-item category rather than location-bound manuscript-draft rows
- **AND** it does not create `workflow-state.md`

### Requirement: rendered templates MUST permit explanatory content

Rendered Markdown views are user-facing and MUST be allowed to keep explanatory text in addition to structured tables and lists.

#### Scenario: explanatory render templates

- **WHEN** a rendered Markdown view is generated
- **THEN** it may include usage guidance and context text above or between the structured sections
- **AND** the Agent still treats the database as the only source of truth

