# review-master-sql-write-recipes Specification

## Purpose
TBD - created by archiving change define-review-master-sql-write-recipes. Update Purpose after archive.
## Requirements
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

### Requirement: direct SQL writes follow documented recipe order

The skill MUST require the agent to follow recipe-defined write ordering instead of inventing ad hoc SQL update sequences.

#### Scenario: one action touches multiple tables

- **WHEN** the agent performs a multi-table write such as strategy-card authoring
- **THEN** it MUST follow the documented recipe order
- **AND** it MUST enable `PRAGMA foreign_keys = ON`
- **AND** it MUST rerun the validator immediately afterward

#### Scenario: Stage 5 draft truth has dedicated recipes

- **WHEN** the Agent needs to write manuscript drafts, response drafts, or comment-scoped blockers
- **THEN** the recipe catalog must expose dedicated Stage 5 recipes for those writes

