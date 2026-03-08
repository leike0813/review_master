# review-master-stage-5-confirmation-blocker-completion-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-5-strategy-and-execution. Update Purpose after archive.
## Requirements
### Requirement: Stage 5 must define confirmation, blocker, and completion gates

Stage 5 MUST explicitly define:

- when confirmation is required
- when a blocker must be written
- when a comment may be marked complete

#### Scenario: Evidence gap creates a blocker

- **Given** an active item needs supporting material that is not yet available
- **When** the Agent judges `evidence_gap = yes`
- **Then** the docs must require a blocker to be written
- **And** the docs must forbid marking the item complete until the blocker is cleared

#### Scenario: Completion requires landed drafts

- **Given** the Agent has a strategy and evidence judgment for an active item
- **When** manuscript-change and response-paragraph drafts are still missing
- **Then** the docs must forbid marking the item complete
- **And** the completion bar must require both draft artifacts and one-to-one linkage

#### Scenario: Silent switching is forbidden

- **Given** `workflow_state.active_comment_id` is already set
- **When** the Agent wants to move to another item
- **Then** the docs must explain when switching is allowed
- **And** the docs must forbid silent switching without closure, blocker, or explicit user instruction

