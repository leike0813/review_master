# review-master-sql-write-recipes Specification

## Purpose
TBD - created by archiving change define-review-master-sql-write-recipes. Update Purpose after archive.
## Requirements
### Requirement: skill documents standard SQL write recipes

The skill MUST provide a standard SQL recipe catalog for common runtime write operations.

#### Scenario: agent needs to write the database

- **WHEN** the agent is about to update `review-master.db`
- **THEN** it MUST be able to reference a documented `recipe_id`
- **AND** the recipe MUST define the stage, when to use it, the required tables, the recommended SQL order, and the required post-write validation step

### Requirement: direct SQL writes follow documented recipe order

The skill MUST require the agent to follow recipe-defined write ordering instead of inventing ad hoc SQL update sequences.

#### Scenario: one action touches multiple tables

- **WHEN** the agent performs a multi-table write such as strategy-card authoring
- **THEN** it MUST follow the documented recipe order
- **AND** it MUST enable `PRAGMA foreign_keys = ON`
- **AND** it MUST rerun the validator immediately afterward

