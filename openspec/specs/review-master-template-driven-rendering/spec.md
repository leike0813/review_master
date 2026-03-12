# review-master-template-driven-rendering Specification

## Purpose
TBD - created by archiving change restructure-review-master-package-for-template-driven-rendering. Update Purpose after archive.
## Requirements
### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons, and they MUST support workspace-local localization overlays on top of packaged assets.

#### Scenario: rendered Stage 3 coverage view is highlight-based and user-readable

- **WHEN** the renderer materializes `06-review-comment-coverage.md`
- **THEN** it MUST render the body as readable original text with visual highlight for covered spans
- **AND** it MUST render a structured mapping appendix from database truth
- **AND** it MUST not emit inline machine wrappers such as `[[covered ...]]` in the body

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

