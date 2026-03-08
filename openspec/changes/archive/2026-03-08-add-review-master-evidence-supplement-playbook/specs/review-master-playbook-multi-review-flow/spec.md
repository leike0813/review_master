## ADDED Requirements

### Requirement: Complex playbook must narrate a multi-review, evidence-supplement flow

The first release SHALL provide a second repository-level playbook that narrates one complete six-stage run with:

- 2 reviewers
- 5 atomic comments
- 1 explicit `stage_5 blocked -> supplement -> ready` loop

Each stage MUST explicitly record:

- the user input or confirmation received
- the agent actions and any helper scripts invoked
- the artifacts created or updated
- the validator conclusion, including the recommended next action
- the agent reply
- the user reply that allows the next transition

#### Scenario: Stage four requires explicit confirmation

- **WHEN** the playbook reaches stage four
- **THEN** it shows pending board confirmations
- **AND** it shows validator output that blocks entry into stage five until the user confirms

#### Scenario: Stage five shows a blocked evidence gap loop

- **WHEN** the playbook reaches the evidence-gap comment
- **THEN** it shows `reviewer_2_001` entering a blocked state
- **AND** it shows the user providing supplement assets
- **AND** it shows the validator returning to a ready state after the supplement is integrated

#### Scenario: Playbook still ends in a successful export path

- **WHEN** the playbook reaches stage six
- **THEN** it shows the final checklist closing all 5 comments
- **AND** it shows validator output that allows final review and export
