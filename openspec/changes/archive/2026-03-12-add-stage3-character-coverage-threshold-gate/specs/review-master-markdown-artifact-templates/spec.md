## MODIFIED Requirements

### Requirement: Template format style

The Stage 3 coverage template MUST expose threshold-ready character metrics.

#### Scenario: coverage template renders character-metric summary

- **WHEN** `06-review-comment-coverage.md` is generated
- **THEN** the template MUST render global character coverage (duplicate-aware)
- **AND** it MUST render non-duplicate diagnostic coverage
- **AND** it MUST render per-document character metrics
- **AND** it MUST render hard/soft threshold values and current gate status text
