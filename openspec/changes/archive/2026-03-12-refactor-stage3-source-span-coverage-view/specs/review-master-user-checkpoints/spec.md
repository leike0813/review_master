## MODIFIED Requirements

### Requirement: Mandatory user checkpoints

Stage 3 coverage confirmation MUST remain mandatory and MUST target full-text highlight review.

#### Scenario: Stage 3 checkpoint uses full-text coverage artifact

- **WHEN** Stage 3 modeling is complete and confirmation is requested
- **THEN** the user checkpoint MUST include `06-review-comment-coverage.md` as the primary coverage-review artifact
- **AND** the artifact MUST show covered and uncovered source text inline for user inspection
- **AND** Stage 4 entry MUST remain blocked until user confirmation is explicitly recorded
