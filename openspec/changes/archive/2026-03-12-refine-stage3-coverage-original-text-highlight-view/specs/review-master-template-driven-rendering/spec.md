## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons, and they MUST support workspace-local localization overlays on top of packaged assets.

#### Scenario: rendered Stage 3 coverage view is highlight-based and user-readable

- **WHEN** the renderer materializes `06-review-comment-coverage.md`
- **THEN** it MUST render the body as readable original text with visual highlight for covered spans
- **AND** it MUST render a structured mapping appendix from database truth
- **AND** it MUST not emit inline machine wrappers such as `[[covered ...]]` in the body
