## MODIFIED Requirements

### Requirement: Final review is mandatory before export

The final checkpoint MUST review revision-action closure and thread-level response coverage rather than patch export completeness.

#### Scenario: Stage 6 completion checks response coverage and audited edits

- **GIVEN** Stage 6 is nearing completion
- **WHEN** the runtime asks for final review
- **THEN** it must surface whether all revision plan actions are closed
- **AND** whether every original review thread is covered
- **AND** whether the working manuscript contains any unaudited modifications
