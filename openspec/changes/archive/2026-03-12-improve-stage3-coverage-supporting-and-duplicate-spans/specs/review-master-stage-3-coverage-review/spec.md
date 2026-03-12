## MODIFIED Requirements

### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 coverage rendering MUST be role-aware while preserving full source-text readability.

#### Scenario: role-aware coverage highlights are rendered

- **WHEN** `06-review-comment-coverage.md` is rendered from Stage 3 truth
- **THEN** `span_role='primary'` and `span_role='supporting'` spans MUST be highlighted in red
- **AND** `span_role='duplicate_filtered'` spans MUST be highlighted in orange with `dup` tag
- **AND** uncovered source text MUST remain visible

#### Scenario: Stage 3 still enforces hard correctness and soft advisory

- **WHEN** a span has invalid offsets/text, overlaps, missing mapping, or a thread lacks `primary` span
- **THEN** gate validation MUST block progression
- **WHEN** title-only coverage is suspected (primary-only thread with long adjacent uncovered paragraph)
- **THEN** gate MUST emit non-blocking advisories and still require user confirmation before Stage 4
