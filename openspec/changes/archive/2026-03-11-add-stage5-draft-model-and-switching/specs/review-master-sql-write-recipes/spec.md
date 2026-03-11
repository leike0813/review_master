## MODIFIED Requirements

### Requirement: skill documents standard SQL write recipes

The skill MUST provide a standard SQL recipe catalog for common runtime write operations.

#### Scenario: Stage 5 draft truth has dedicated recipes

- **WHEN** the Agent needs to author or update Stage 5 drafts
- **THEN** the SQL recipe catalog must include a manuscript-draft recipe
- **AND** it must include a response-draft recipe
- **AND** it must document how comment-scoped blockers are written

#### Scenario: Legacy workspace migration is documented

- **WHEN** a user already has a Stage 5 workspace created under the legacy completion model
- **THEN** the SQL/script guidance must describe a supported migration path
- **AND** it must explain that legacy draft completion flags are reset during migration
