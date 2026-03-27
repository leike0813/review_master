## MODIFIED Requirements

### Requirement: rendered templates MUST permit explanatory content

The template-driven runtime MUST render the new revision-loop views for Stage 5 and Stage 6, including the revision guide, execution graph, revision action log, response coverage matrix, and renamed response preview outputs.

#### Scenario: render manifest switches to revision-loop views

- **WHEN** the runtime renders workspace views
- **THEN** it must provide Stage 6 outputs driven by revision-plan and revision-log truth
- **AND** it must no longer require patch-plan or copy-variant views for Stage 6 progress
