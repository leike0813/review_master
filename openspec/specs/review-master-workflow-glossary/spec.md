# review-master-workflow-glossary Specification

## Purpose
TBD - created by archiving change normalize-review-master-workflow-cross-cutting-consistency. Update Purpose after archive.
## Requirements
### Requirement: workflow glossary is the single naming source

`review-master` MUST define one glossary document that fixes the formal names for stages, scripts, runtime truth objects, rendered views, final exports, and action ids.

#### Scenario: glossary includes migration script and Stage 5 draft terminology

- **Given** the Stage 5 draft-model migration has been implemented
- **When** a reader checks the glossary
- **Then** it must list the official migration script name
- **And** it must use `manuscript_execution_items_done` and `response_draft_done` as the official completion-field names

### Requirement: Workflow glossary uses canonical Stage 5 completion names

The workflow glossary MUST use the renamed Stage 5 completion field and define manuscript execution items as the official manuscript-side truth model.

#### Scenario: glossary defines Stage 5 completion fields

- **WHEN** the workflow glossary defines Stage 5 completion fields
- **THEN** it MUST use `manuscript_execution_items_done` and `response_draft_done` as the official completion-field names
- **AND** it MUST define manuscript execution items as the typed manuscript-side truth for Stage 5

