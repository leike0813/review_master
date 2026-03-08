# review-master-artifact-workspace-layout Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-artifact-workspace. Update Purpose after archive.
## Requirements
### Requirement: Runtime artifact workspace must use a fixed layout
The first release SHALL define a fixed runtime artifact workspace layout that is separate from `review-master/references/`.

At minimum, each workspace root must contain:

- `workflow-state.yaml`
- `manuscript-structure-summary.md`
- `atomic-review-comment-list.md`
- `comment-manuscript-mapping-table.md`
- `revision-board.md`
- `final-assembly-checklist.md`
- `response-strategy-cards/`

`review-master/references/` MUST remain the reference-template directory and MUST NOT be treated as a runtime workspace.

#### Scenario: Runtime workspace uses fixed filenames
- **WHEN** an agent prepares a runtime artifact workspace
- **THEN** the workspace uses the fixed filenames and strategy-card directory listed above

#### Scenario: Reference templates are not the runtime workspace
- **WHEN** an agent needs files to actively fill during workflow execution
- **THEN** it initializes a runtime workspace
- **AND** it does not write directly into `review-master/references/`

