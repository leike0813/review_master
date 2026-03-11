# review-master-stage-5-strategy-card-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-5-strategy-and-execution. Update Purpose after archive.
## Requirements
### Requirement: Stage 5 strategy-card instructions are operations-manual grade

Stage 5 MUST define how the Agent locks an active atomic item, forms a strategy card, authors Stage 5 drafts, and prepares the item for Stage 6 without treating Stage 5 as the final export stage.

#### Scenario: Strategy card includes formal Stage 5 draft truth

- **Given** Stage 5 has locked one `comment_id`
- **When** the Agent prepares execution drafts for that item
- **Then** the docs must require manuscript drafts to be written to `strategy_action_manuscript_drafts`
- **And** the docs must require the response-side draft to be written to `comment_response_drafts`
- **And** the docs must explain that these are Stage 5 drafts rather than Stage 6 final copy variants

#### Scenario: Stage 5 allows explicit focus switching

- **Given** Stage 5 already has an `active_comment_id`
- **When** the user wants to switch to another non-done comment
- **Then** the docs must allow an explicit `set_active_comment` action
- **And** the docs must require the Agent to preserve existing strategy, draft, supplement, and blocker records for the previous comment
- **And** the docs must still forbid silent switching

