## MODIFIED Requirements

### Requirement: workflow glossary is the single naming source

`review-master` MUST define one glossary document that fixes the formal names for stages, scripts, runtime truth objects, rendered views, final exports, and action ids.

#### Scenario: glossary includes migration script and Stage 5 draft terminology

- **Given** the Stage 5 draft-model migration has been implemented
- **When** a reader checks the glossary
- **Then** it must list the official migration script name
- **And** it must use `manuscript_draft_done` and `response_draft_done` as the official completion-field names
