# review-master-stage-6-export-gate-and-final-confirmation-instructions Delta

## MODIFIED Requirements

### Requirement: Stage 6 completion uses revision closure rather than patch export gates

Stage 6 MUST close when revision plan actions are resolved, response rows cover every original review thread, and final outputs are ready; optional `latexdiff` output must not be a hard prerequisite.

#### Scenario: semantic revision logs replace unaudited diff blocking

- **GIVEN** Stage 6 has active or unresolved revision plan actions
- **WHEN** the runtime evaluates Stage 6 readiness
- **THEN** it MUST request `record_revision_action`
- **AND** completion MUST NOT depend on file hash comparison, `working_copy_file_state`, or generated diff excerpts
- **AND** `gate-and-render` MUST NOT silently write revision logs
