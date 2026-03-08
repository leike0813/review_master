# review-master-environment-gating Specification

## Purpose
TBD - created by archiving change restructure-review-master-package-for-template-driven-rendering. Update Purpose after archive.
## Requirements
### Requirement: script-driven execution MUST begin with runtime-environment confirmation

Before the Agent relies on the Python renderer or validator, it MUST verify that the required runtime dependencies are available.

#### Scenario: environment available

- **WHEN** the required Python dependencies are available
- **THEN** the Agent proceeds with the normal script-driven workflow

#### Scenario: environment missing and user approves installation

- **WHEN** the dependencies are missing
- **AND** the user approves installation
- **THEN** the Agent may install the required environment or dependencies
- **AND** continue with script-driven rendering and validation

#### Scenario: environment missing and user rejects installation

- **WHEN** the dependencies are missing
- **AND** the user rejects installation
- **THEN** the Agent MUST not assume the renderer is available
- **AND** the database remains the runtime source of truth
- **AND** the rendered Markdown outputs are produced manually by the Agent as a fallback

