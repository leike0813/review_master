## MODIFIED Requirements

### Requirement: Mandatory user checkpoints

Stage 3 user confirmation MUST be informed by quantitative character-coverage metrics.

#### Scenario: Stage 3 confirmation reads threshold status before user sign-off

- **WHEN** Stage 3 extraction and mapping are complete
- **THEN** the workflow MUST present `06-review-comment-coverage.md` including character-coverage metrics
- **AND** users MUST be able to inspect whether coverage is in hard-fail, soft-warn, or pass zone before confirming Stage 3
- **AND** Stage 4 remains blocked until explicit Stage 3 confirmation
