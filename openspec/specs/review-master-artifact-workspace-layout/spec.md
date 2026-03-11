# review-master-artifact-workspace-layout Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-artifact-workspace. Update Purpose after archive.
## Requirements
### Requirement: Runtime artifact workspace must use a fixed layout
The first release SHALL define a fixed runtime artifact workspace layout that is separate from `review-master/references/`.

At minimum, each workspace root must contain:

- `review-master.db`
- `runtime-localization/`
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
- `response-strategy-cards/`

`review-master/references/` MUST remain the reference-template directory and MUST NOT be treated as a runtime workspace.

#### Scenario: Runtime workspace uses fixed numbered filenames
- **WHEN** an agent prepares a runtime artifact workspace
- **THEN** the workspace uses the numbered filenames and strategy-card directory listed above

#### Scenario: Strategy cards remain unnumbered
- **WHEN** the workspace renders per-comment strategy cards
- **THEN** it keeps using `response-strategy-cards/{comment_id}.md`
- **AND** it does not introduce numbered filenames for those card files

#### Scenario: Reference templates are not the runtime workspace
- **WHEN** an agent needs files to actively fill during workflow execution
- **THEN** it initializes a runtime workspace
- **AND** it does not write directly into `review-master/references/`

