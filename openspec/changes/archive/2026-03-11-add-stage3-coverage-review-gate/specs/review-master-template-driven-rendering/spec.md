## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons, and they MUST support workspace-local localization overlays on top of packaged assets.

#### Scenario: rendered view set includes Stage 3 coverage review

- **WHEN** the renderer materializes the runtime workspace views
- **THEN** it MUST include `review-comment-coverage.md`
- **AND** that view MUST be rendered from database truth rather than by modifying the user’s source files
