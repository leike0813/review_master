## ADDED Requirements

### Requirement: stage 2 guidance MUST define the manuscript-analysis completion bar

`review-master` MUST describe Stage 2 as the workflow that turns a confirmed manuscript entry into a structure summary sufficient to support Stage 3 thread extraction and later mapping.

#### Scenario: structure analysis cannot yet support stage 3

- **WHEN** section hierarchy, core claims, or high-risk modification areas are still materially unclear
- **THEN** Stage 2 guidance tells the Agent not to advance to Stage 3
- **AND** to continue the analysis or ask the user a targeted clarifying question

#### Scenario: stage 2 completion is explicit

- **WHEN** the Agent has written `manuscript_summary`, `manuscript_sections`, and `manuscript_claims`
- **AND** the rendered manuscript structure summary is sufficient for later thread/atomic mapping
- **THEN** the guidance treats Stage 2 as complete and allows progression to Stage 3
