## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

Stage 3 coverage rendering MUST expose character-level coverage metrics alongside highlighted source text.

#### Scenario: rendered coverage view includes thresholded character metrics

- **WHEN** the renderer materializes `06-review-comment-coverage.md`
- **THEN** it MUST include a character-level coverage metrics section with global and per-document values
- **AND** it MUST show hard/soft thresholds and current gate classification
- **AND** it MUST keep the readable highlighted source body and mapping appendix
