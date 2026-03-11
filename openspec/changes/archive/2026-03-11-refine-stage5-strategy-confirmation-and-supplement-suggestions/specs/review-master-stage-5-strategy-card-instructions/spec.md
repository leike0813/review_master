## MODIFIED Requirements

### Requirement: Stage 5 strategy-card instructions are operations-manual grade

Stage 5 MUST define how the Agent locks an active atomic item, forms a strategy card, obtains user confirmation, authors Stage 5 drafts, and prepares the item for Stage 6 without treating Stage 5 as the final export stage.

#### Scenario: strategy card is confirm-first

- **Given** Stage 5 has locked one `comment_id`
- **When** the Agent finishes the initial strategy card for that item
- **Then** the docs must require an explicit confirmation step before any Stage 5 drafts are authored
- **And** the docs must say the user may revise the strategy card at that point

#### Scenario: Stage 5 drafts are authored only after confirmation

- **Given** the user has confirmed the strategy for one active item
- **When** the Agent prepares execution drafts for that item
- **Then** the docs must require manuscript drafts to be written to `strategy_action_manuscript_drafts`
- **And** the docs must require the response-side draft to be written to `comment_response_drafts`
- **And** the docs must explain that these are Stage 5 drafts rather than Stage 6 final copy variants
