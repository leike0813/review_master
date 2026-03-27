## MODIFIED Requirements

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
- `08-supplement-suggestion-plan.md`
- `09-style-profile.md`
- `10-action-copy-variants.md`
- `11-response-letter-outline.md`
- `12-export-patch-plan.md`
- `13-response-letter-table-preview.md`
- `14-response-letter-table-preview.tex`
- `15-supplement-intake-plan.md`
- `16-final-assembly-checklist.md`
- `response-strategy-cards/`

`review-master/references/` MUST remain the reference-template directory and MUST NOT be treated as a runtime workspace.

#### Scenario: Runtime workspace uses reordered numbered filenames

- **WHEN** an agent prepares a runtime artifact workspace after this change
- **THEN** the workspace MUST use the reordered numbered filenames listed above
- **AND** `08-supplement-suggestion-plan.md` MUST appear before the Stage 6 style and export artifacts
