# review-master-stage-5-confirmation-blocker-completion-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-5-strategy-and-execution. Update Purpose after archive.
## Requirements
### Requirement: Stage 5 must define confirmation, blocker, and completion gates

Stage 5 MUST explicitly define confirmation, blocker, and completion using the new confirmation-first draft model.

#### Scenario: unconfirmed strategy blocks draft authoring

- **Given** the current `active_comment_id` already has a strategy card
- **When** `user_strategy_confirmed` is still `no` or strategy confirmations are still pending
- **Then** the docs must forbid Stage 5 draft authoring
- **And** they must require the workflow to request user confirmation first

#### Scenario: strategy changes invalidate downstream drafts

- **Given** one comment already had Stage 5 drafts
- **When** the Agent changes the strategy stance, actions, target locations, or evidence items for that comment
- **Then** the docs must require `user_strategy_confirmed = no`
- **And** they must require the stale manuscript and response drafts to be cleared before execution can resume

