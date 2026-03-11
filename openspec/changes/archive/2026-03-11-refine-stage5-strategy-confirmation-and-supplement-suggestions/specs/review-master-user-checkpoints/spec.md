## MODIFIED Requirements

### Requirement: Per-comment confirmation is required before execution

Each atomic review comment MUST be confirmed by the user before that comment is allowed to enter manuscript-revision execution.

#### Scenario: unconfirmed strategy cannot author Stage 5 drafts

- **WHEN** the workflow has prepared a response strategy card for one atomic comment
- **BUT** the user has not confirmed or corrected it yet
- **THEN** that comment must not enter manuscript-draft authoring or response-draft authoring
- **AND** the guidance must explicitly tell the user that they may modify the strategy card
