## MODIFIED Requirements

### Requirement: Stage 5 strategy-card instructions are operations-manual grade

Stage 5 MUST define how the Agent locks an active atomic item, forms a strategy card, obtains user confirmation, authors Stage 5 execution truth, and prepares the item for Stage 6 without treating Stage 5 as the final export stage.

#### Scenario: Stage 5 execution items are authored only after confirmation

- **Given** the user has confirmed the strategy for one active item
- **When** the Agent prepares execution content for that item
- **Then** the docs must require manuscript-side execution truth to be written to `strategy_action_manuscript_execution_items`
- **And** the docs must require the response-side draft to be written to `comment_response_drafts`
- **And** the docs must explain that manuscript execution items may cover text, figure, data, and strategy work rather than only literal draft prose
