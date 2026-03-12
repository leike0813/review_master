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

The Stage 3 coverage template MUST expose threshold-ready character metrics.

#### Scenario: coverage template renders character-metric summary

- **WHEN** `06-review-comment-coverage.md` is generated
- **THEN** the template MUST render global character coverage (duplicate-aware)
- **AND** it MUST render non-duplicate diagnostic coverage
- **AND** it MUST render per-document character metrics
- **AND** it MUST render hard/soft threshold values and current gate status text

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

### Requirement: Stage 3 coverage template must separate reading view and mapping view

The Stage 3 coverage template MUST combine a readable highlighted body with a separate mapping appendix.

#### Scenario: coverage template structure

- **WHEN** `06-review-comment-coverage.md` is rendered
- **THEN** the template MUST include an original-text coverage body where covered spans are visually emphasized
- **AND** it MUST include a mapping appendix table for covered segments (`thread_id` and `comment_id` mapping)
- **AND** uncovered text MUST remain visible in the body

