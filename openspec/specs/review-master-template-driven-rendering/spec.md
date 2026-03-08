# review-master-template-driven-rendering Specification

## Purpose
TBD - created by archiving change restructure-review-master-package-for-template-driven-rendering. Update Purpose after archive.
## Requirements
### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons.

#### Scenario: initialize and render from assets

- **WHEN** `init_artifact_workspace.py` initializes a workspace
- **THEN** it reads the schema from `assets/schema/review-master-schema.yaml`
- **AND** it reads the render manifest and Jinja2 templates from `assets/templates/`
- **AND** it creates `review-master.db`
- **AND** it renders the read-only Markdown views from those template assets

### Requirement: `workflow-state.md` MUST be retired as a rendered runtime view

Workflow state MUST remain in SQLite only.

#### Scenario: rendered view set

- **WHEN** the validator renders a workspace
- **THEN** it produces:
  - `manuscript-structure-summary.md`
  - `atomic-review-comment-list.md`
  - `comment-workboard.md`
  - `final-assembly-checklist.md`
  - `response-strategy-cards/{comment_id}.md`
- **AND** it does not create `workflow-state.md`

### Requirement: rendered templates MUST permit explanatory content

Rendered Markdown views are user-facing and MUST be allowed to keep explanatory text in addition to structured tables and lists.

#### Scenario: explanatory render templates

- **WHEN** a rendered Markdown view is generated
- **THEN** it may include usage guidance and context text above or between the structured sections
- **AND** the Agent still treats the database as the only source of truth

