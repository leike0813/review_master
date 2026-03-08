## ADDED Requirements

### Requirement: all comment-to-location and comment-to-action relationships MUST be relation-table driven

The runtime schema MUST represent one-to-many and many-to-many comment relationships with explicit tables.

#### Scenario: one atomic comment maps to multiple manuscript locations

- **WHEN** one canonical atomic item requires edits in multiple manuscript locations
- **THEN** those locations are stored in `atomic_comment_target_locations`
- **AND** the rendered workboard shows multiple target locations for the same `comment_id`

#### Scenario: one manuscript action maps to multiple target locations

- **WHEN** one strategy action affects multiple edit locations
- **THEN** those locations are stored in `strategy_action_target_locations`
- **AND** the rendered strategy card shows the aggregated target-location list for that action

### Requirement: stage-four workboard state MUST be split into state and analysis relations

The old single-table workboard model MUST be replaced with relation-table driven state and analysis tables.

#### Scenario: stage-four planning data

- **WHEN** stage four is authored
- **THEN** `atomic_comment_state` stores status, priority, evidence gap, confirmation need, and next action
- **AND** `atomic_comment_analysis_links` stores analysis rows and optional dependencies
- **AND** the rendered view is `atomic-comment-workboard.md`
