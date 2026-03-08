# review-master-artifact-authoring-rules Specification

## Purpose
TBD - created by archiving change define-review-master-artifact-authoring-rules. Update Purpose after archive.
## Requirements
### Requirement: Central authoring rules reference
The first release SHALL provide a central authoring-rules reference document at:

- `review-master/references/artifact-authoring-rules.md`

This document MUST serve as the single source of truth for how the six Markdown artifact templates are filled.

#### Scenario: Templates defer to central rules
- **WHEN** a user or agent opens any artifact template
- **THEN** the template points to `artifact-authoring-rules.md` for detailed filling rules

### Requirement: Minimal required fields per artifact
The authoring rules MUST define the minimal required fields for each artifact and MUST allow non-critical fields to remain blank.

At minimum:

- `manuscript-structure-summary.md`: `main_entry`, `project_shape`, at least one section row, at least one claim row
- `atomic-review-comment-list.md`: `comment_id`, `reviewer_id`, `status`, `Original Comment Excerpt`, `Required Action`
- `comment-manuscript-mapping-table.md`: `comment_id`, `target_location`, `Manuscript Claim or Section`
- `revision-board.md`: `comment_id`, `status`, `priority`, `evidence_gap`, `next_action`
- `response-strategy-card.md`: card header fields, `Original comment excerpt`, `Proposed stance`, at least one action row, completion checklist
- `final-assembly-checklist.md`: `comment_id`, `status`, `manuscript_change_done`, `response_section_done`, `export_ready`

#### Scenario: Partially filled but valid artifact
- **WHEN** an artifact has all of its minimal required fields filled
- **AND** some non-critical fields remain blank
- **THEN** the artifact is still considered valid for the first release

#### Scenario: Missing required fields makes artifact incomplete
- **WHEN** a template instance is missing one or more required fields from its minimal required set
- **THEN** that artifact is considered incomplete

