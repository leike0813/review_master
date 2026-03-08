# review-master-stage-5-supporting-guidance Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-5-strategy-and-execution. Update Purpose after archive.
## Requirements
### Requirement: Supporting docs must align on Stage 5 execution rules

The Stage 5 handbook, SQL recipes, workflow state machine, helper-script guidance, and at least one playbook MUST present a consistent Stage 5 model.

#### Scenario: Supporting docs use the same Stage 5 gates

- **Given** the user reads `SKILL.md`, the Stage 5 handbook, and the workflow state machine
- **When** they compare the docs
- **Then** they must find the same rules for:
  - per-item confirmation
  - evidence-gap blockers
  - completion only after landed drafts

#### Scenario: SQL recipes reflect Stage 5 execution order

- **Given** the user reads the SQL recipes
- **When** they look at Stage 5 recipes
- **Then** the recipes must describe entry conditions, write order, and write-after gate usage for Stage 5 tables

#### Scenario: Playbook shows the blocked and unblocked loop

- **Given** the complex playbook is used as reference
- **When** Stage 5 is demonstrated
- **Then** it must show per-item confirmation before execution
- **And** it must show evidence gap to blocker
- **And** it must show supplement arrival, blocker release, and completion only after drafts are considered landed

