# Capability: review-master-stage-5-strategy-card-instructions

## ADDED Requirements

### Requirement: Stage 5 strategy-card instructions are operations-manual grade

Stage 5 MUST define how the Agent locks an active atomic item, forms a strategy card, and prepares execution drafts before the item may be treated as complete.

#### Scenario: Lock and author a strategy card

- **Given** Stage 4 has completed and Stage 5 is allowed to begin
- **When** the Agent chooses a `comment_id` to process
- **Then** the docs must require the Agent to lock `workflow_state.active_comment_id`
- **And** the docs must require the Agent to populate `strategy_cards`
- **And** the docs must require at least one `strategy_card_actions` row
- **And** the docs must explain when `strategy_action_target_locations` are needed

#### Scenario: Strategy card must be confirmable before execution

- **Given** the Agent has written a strategy card for the active item
- **When** the item is about to enter manuscript-change draft and response-paragraph draft work
- **Then** the docs must state that the user must first confirm the strategy for that specific item
- **And** the docs must forbid skipping this per-item confirmation by relying only on Stage 4 confirmation
