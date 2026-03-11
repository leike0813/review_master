## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons.

#### Scenario: initialize and render from assets

- **WHEN** `init_artifact_workspace.py` initializes a workspace
- **THEN** it reads the schema from `assets/schema/review-master-schema.yaml`
- **AND** it reads the render manifest and Jinja2 templates from `assets/templates/`
- **AND** it creates `review-master.db`
- **AND** it renders the read-only Markdown views from those template assets using the numbered canonical filenames for all non-strategy-card artifacts

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
  - `08-style-profile.md`
  - `09-action-copy-variants.md`
  - `10-response-letter-outline.md`
  - `11-export-patch-plan.md`
  - `12-response-letter-table-preview.md`
  - `13-response-letter-table-preview.tex`
  - `14-supplement-suggestion-plan.md`
  - `15-supplement-intake-plan.md`
  - `16-final-assembly-checklist.md`
  - `response-strategy-cards/{comment_id}.md`
- **AND** it does not create `workflow-state.md`
- **AND** it does not treat the old unnumbered filenames as the canonical rendered outputs

### Requirement: rendered templates MUST permit explanatory content

Rendered Markdown views are user-facing and MUST be allowed to keep explanatory text in addition to structured tables and lists.

#### Scenario: explanatory render templates

- **WHEN** a rendered Markdown view is generated
- **THEN** it may include usage guidance and context text above or between the structured sections
- **AND** the Agent still treats the database as the only source of truth
