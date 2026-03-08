## ADDED Requirements

### Requirement: validator emits recipe hints in action payloads

The validator MUST include `recipe_id` in action objects so the agent can map runtime instructions to standard SQL recipes.

#### Scenario: validator recommends the next write action

- **WHEN** the validator emits `allowed_next_actions` or `recommended_next_action`
- **THEN** each action object MUST include `recipe_id`
- **AND** the `recipe_id` MUST align with the documented recipe catalog

### Requirement: repair actions map to upstream-first recipes

Repair guidance MUST remain upstream-first and MUST point to the corresponding repair recipe.

#### Scenario: validator finds multiple issues

- **WHEN** the validator emits `repair_sequence`
- **THEN** it MUST order repairs from upstream truth to downstream derived state
- **AND** each repair action MUST include a `recipe_id` for the primary repair path
