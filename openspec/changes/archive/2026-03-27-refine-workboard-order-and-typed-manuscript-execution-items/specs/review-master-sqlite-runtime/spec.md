## MODIFIED Requirements

### Requirement: Runtime schema must include Stage 5 execution truth

The runtime SQLite schema MUST expose typed manuscript execution truth for Stage 5 instead of the old location-bound manuscript-draft model.

#### Scenario: runtime initializes new Stage 5 execution truth

- **WHEN** the runtime initializes a workspace database
- **THEN** it MUST include `strategy_action_manuscript_execution_items`
- **AND** `comment_completion_status` MUST expose `manuscript_execution_items_done`

#### Scenario: manuscript execution items are typed per action

- **WHEN** Stage 5 manuscript-side truth is stored
- **THEN** each row must belong to one `(comment_id, action_order, item_order)`
- **AND** each row must carry a category from the fixed execution-item vocabulary
- **AND** the runtime must not require manuscript-side execution truth to be keyed by `location_order`
