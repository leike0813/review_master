## MODIFIED Requirements

### Requirement: Per-comment closed-loop cycle

Stage 5 MUST process review comments one atomic item at a time using the following fixed loop:

1. select one atomic comment
2. generate a response strategy, target manuscript changes, required evidence, and supplement suggestions
3. obtain user confirmation or correction
4. only after confirmation, author Stage 5 manuscript and response drafts
5. if evidence is missing, pause that comment and request materials
6. mark the comment complete before advancing to the next comment

#### Scenario: confirmed comment advances to draft authoring

- **WHEN** the user confirms the strategy for one atomic comment
- **AND** required blockers are not preventing execution
- **THEN** the workflow may author the manuscript draft and matching response draft for that comment
- **AND** it must not skip directly from strategy card creation to completion
