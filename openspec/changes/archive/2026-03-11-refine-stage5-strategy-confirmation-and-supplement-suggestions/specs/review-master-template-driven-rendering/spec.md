## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

The runtime scripts MUST no longer hardcode the SQLite schema statements or Markdown view skeletons, and they MUST support workspace-local localization overlays on top of packaged assets.

#### Scenario: rendered view set includes supplement suggestion planning

- **WHEN** the renderer materializes the runtime workspace views
- **THEN** it MUST include `supplement-suggestion-plan.md`
- **AND** that view MUST be rendered from database truth rather than by modifying the user’s source files

#### Scenario: strategy card rendering is phase-aware

- **WHEN** a Stage 5 strategy card is rendered before user confirmation
- **THEN** it MUST show the pending confirmation state
- **AND** it MUST explain that drafts are not yet authored until confirmation
