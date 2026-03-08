# review-master-markdown-artifact-templates Specification

## Purpose
TBD - created by archiving change add-review-master-markdown-artifact-templates. Update Purpose after archive.
## Requirements
### Requirement: Six Markdown artifact templates
The first release of `review-master` SHALL provide six standalone Markdown template files under `review-master/references/`:

- `manuscript-structure-summary.md`
- `atomic-review-comment-list.md`
- `comment-manuscript-mapping-table.md`
- `revision-board.md`
- `response-strategy-card.md`
- `final-assembly-checklist.md`

#### Scenario: Template directory contains all six artifacts
- **WHEN** the template change is implemented
- **THEN** `review-master/references/` contains all six named Markdown files

### Requirement: Template format style
Each template MUST use the format pattern:

- title
- purpose description
- field definitions
- table or checklist skeleton

The templates MUST be table-driven or checklist-driven rather than narrative-first templates.

#### Scenario: Template remains skeleton-only
- **WHEN** a template is opened
- **THEN** it presents an empty reusable skeleton with field guidance
- **AND** does not rely on embedded example data to explain the format

### Requirement: Minimum role of each template
The templates MUST cover the minimum roles below:

- `manuscript-structure-summary.md`: main entry, section structure, core claims, key evidence, high-risk revision zones
- `atomic-review-comment-list.md`: one row per atomic comment
- `comment-manuscript-mapping-table.md`: link comments to manuscript locations, claims, and evidence
- `revision-board.md`: summarize priority, status, dependencies, evidence gaps, and suggested order
- `response-strategy-card.md`: one card for one comment only
- `final-assembly-checklist.md`: verify manuscript changes, response sections, evidence closure, and export gates

#### Scenario: Strategy card stays single-comment
- **WHEN** `response-strategy-card.md` is used
- **THEN** it must serve exactly one `comment_id`
- **AND** must not combine multiple comments into one card

