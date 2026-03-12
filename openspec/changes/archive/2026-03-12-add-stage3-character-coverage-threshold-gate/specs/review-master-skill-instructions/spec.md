## MODIFIED Requirements

### Requirement: SKILL.md must define the executable six-stage workflow

Stage 3 instructions MUST define character-level coverage thresholds as part of coverage review semantics.

#### Scenario: Stage 3 instructions include hard/soft coverage thresholds

- **WHEN** `SKILL.md` describes Stage 3 coverage confirmation
- **THEN** it MUST define character-level coverage as duplicate-aware global metric
- **AND** it MUST define hard threshold `30%` as blocking
- **AND** it MUST define soft threshold `50%` as non-blocking advisory
- **AND** it MUST keep user confirmation as the gate to Stage 4
