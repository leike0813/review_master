# review-master-cross-artifact-tracking Specification

## Purpose
TBD - created by archiving change add-review-master-markdown-artifact-templates. Update Purpose after archive.
## Requirements
### Requirement: Shared tracking fields
The Markdown artifact templates SHALL share the following minimum tracking fields wherever they apply:

- `comment_id`
- `reviewer_id`
- `status`
- `priority`
- `evidence_gap`
- `target_location`

The following enum values MUST be fixed in the templates:

- `status`: `todo | blocked | ready | in_progress | done`
- `priority`: `high | medium | low`
- `evidence_gap`: `yes | no`

#### Scenario: Shared fields are visible in templates
- **WHEN** a comment-scoped template is opened
- **THEN** the shared tracking fields and enum values are explicitly documented in that template

### Requirement: comment_id as primary cross-artifact key
`comment_id` MUST be the primary cross-artifact tracking key across comment-scoped artifacts.

Artifacts or sections that do not use `comment_id` MUST explicitly mark it as not applicable.

#### Scenario: Non-comment-wide artifact marks comment_id as not applicable
- **WHEN** `manuscript-structure-summary.md` is used
- **THEN** the template explicitly states that `comment_id` is not applicable for that artifact

#### Scenario: Mapping and board share comment_id
- **WHEN** one atomic review comment appears in the atomic list, mapping table, revision board, strategy card, and final checklist
- **THEN** the same `comment_id` is used to track that comment across those artifacts

