## MODIFIED Requirements

### Requirement: The first release must define workflow state-machine rules

Stage 3 rules MUST define threshold-based coverage diagnostics before user confirmation.

#### Scenario: Stage 3 hard threshold violation blocks progression

- **WHEN** workflow is `stage_3`
- **AND** global duplicate-aware character coverage is below hard threshold
- **THEN** state-machine validation MUST surface a blocking issue
- **AND** Stage 4 progression remains blocked

#### Scenario: Stage 3 soft threshold warning remains non-blocking

- **WHEN** workflow is `stage_3`
- **AND** global coverage is between hard and soft thresholds
- **THEN** state-machine output MUST include advisory guidance
- **AND** Stage 3 still proceeds through the existing user-confirmation gate
