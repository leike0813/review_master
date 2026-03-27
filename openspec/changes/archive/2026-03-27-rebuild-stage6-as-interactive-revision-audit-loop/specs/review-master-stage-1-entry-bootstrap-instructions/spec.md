## MODIFIED Requirements

### Requirement: stage 1 guidance MUST define a complete entry-and-bootstrap workflow

Stage 1 guidance MUST require the workspace initializer to establish `source_snapshot` and `working_manuscript` manuscript copies before later stages can use the manuscript as a stable review-writing baseline.

#### Scenario: bootstrap creates workspace-local manuscript copies

- **GIVEN** a confirmed `manuscript_source`
- **WHEN** Stage 1 initializes the artifact workspace
- **THEN** it must create both a read-only `source_snapshot` copy and an editable `working_manuscript` copy inside the workspace
- **AND** it must record them in runtime truth rather than relying on the external source path during Stage 6
