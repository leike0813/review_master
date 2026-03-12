## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

Coverage rendering MUST be source-text-first, not wrapper-token-first.

#### Scenario: Stage 3 coverage view is full-text with inline highlight

- **WHEN** the template renderer builds `06-review-comment-coverage.md`
- **THEN** it MUST reconstruct covered/uncovered runs from source text plus `raw_thread_source_spans`
- **AND** it MUST highlight covered runs inline in red with a short `thread_id` tag
- **AND** it MUST keep uncovered text visible in the body
- **AND** it MUST keep an appendix mapping table for traceability
- **AND** it MUST NOT rely on `[[covered ...]]...[[/covered]]` wrapper syntax
