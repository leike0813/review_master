## MODIFIED Requirements

### Requirement: Workflow glossary uses canonical Stage 5 completion names

The workflow glossary MUST use the renamed Stage 5 completion field and define manuscript execution items as the official manuscript-side truth model.

#### Scenario: glossary defines Stage 5 completion fields

- **WHEN** the workflow glossary defines Stage 5 completion fields
- **THEN** it MUST use `manuscript_execution_items_done` and `response_draft_done` as the official completion-field names
- **AND** it MUST define manuscript execution items as the typed manuscript-side truth for Stage 5
