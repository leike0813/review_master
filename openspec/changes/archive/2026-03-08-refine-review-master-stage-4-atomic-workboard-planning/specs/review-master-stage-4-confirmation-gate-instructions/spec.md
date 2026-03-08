## ADDED Requirements

### Requirement: stage 4 guidance MUST treat user confirmation as the default gate

`review-master` MUST describe Stage 4 so that the default workflow writes pending confirmations, shows the workboard to the user, and only then allows progression to Stage 5.

#### Scenario: workboard enters default confirmation gate

- **WHEN** Stage 4 planning is complete enough for user review
- **THEN** the guidance tells the Agent to write `workflow_pending_user_confirmations`
- **AND** run `gate-and-render`
- **AND** wait for user confirmation before entering Stage 5

#### Scenario: confirmation not completed blocks stage 5

- **WHEN** pending confirmations are still present
- **THEN** the guidance does not allow Stage 5 execution to begin
- **AND** instead keeps the workflow in a confirmation-waiting path
