## MODIFIED Requirements

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
