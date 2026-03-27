## MODIFIED Requirements

### Requirement: Stage 6 completion uses revision closure rather than patch export gates

Stage 6 MUST close when revision plan actions are resolved, response rows cover every original review thread, and the working manuscript has no unaudited changes; optional `latexdiff` output must not be a hard prerequisite.

#### Scenario: unaudited manuscript edits block Stage 6

- **GIVEN** the working manuscript has changed since the last recorded audit round
- **WHEN** the runtime evaluates Stage 6 readiness
- **THEN** it must block completion and request revision-action capture
- **AND** it must not silently write audit records inside `gate-and-render`

#### Scenario: latexdiff stays optional

- **GIVEN** Stage 6 is otherwise complete
- **WHEN** `latexdiff` is unavailable
- **THEN** the runtime may emit an advisory
- **AND** it must not treat missing `latexdiff` output as a hard gate failure
