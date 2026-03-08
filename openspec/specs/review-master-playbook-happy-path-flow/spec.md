# review-master-playbook-happy-path-flow Specification

## Purpose
TBD - created by archiving change add-review-master-happy-path-playbook. Update Purpose after archive.
## Requirements
### Requirement: Playbook must narrate a full six-stage happy path

The first release SHALL provide a single happy-path playbook that covers one complete run of the existing six-stage review-master workflow.

Each stage section MUST explicitly record:

- the user input or confirmation received at that stage
- the agent actions and any helper scripts invoked
- the artifacts created or updated
- the validator conclusion, including the recommended next action
- the agent reply back to the user
- the user reply that allows the next stage to proceed

#### Scenario: Playbook covers the initial skill invocation

- **WHEN** the playbook starts
- **THEN** it shows the user providing `manuscript_source` and `review_comments_source`
- **AND** it shows the agent handling stage one input parsing and workspace initialization

#### Scenario: Playbook covers middle stages with user confirmations

- **WHEN** the playbook reaches stages four and five
- **THEN** it shows the user confirming the revision board and the single-comment strategy
- **AND** it shows the agent updating comment-scoped artifacts before continuing

#### Scenario: Playbook covers final review and export

- **WHEN** the playbook reaches stage six
- **THEN** it shows the validator allowing final review and export
- **AND** it shows the user providing the final confirmation before the sample deliverables are produced

