## ADDED Requirements

### Requirement: SKILL.md must define the validator-driven execution loop
`review-master/SKILL.md` MUST define the normal execution loop as:

1. receive user instruction
2. reason and update relevant artifacts plus `workflow-state.yaml`
3. run the validator
4. read `instruction_payload`
5. if the user did not override, follow `recommended_next_action`
6. if `repair_sequence` is non-empty, repair first and re-run validation

`SKILL.md` MUST treat validator output as execution guidance, not as passive logging.

#### Scenario: Repair loop is mandatory when issues exist
- **WHEN** validation issues are reported
- **THEN** `SKILL.md` requires the agent to follow `repair_sequence`
- **AND** re-run the validator before advancing

#### Scenario: Agent may follow recommendation when user has not overridden it
- **WHEN** validation reports no issues
- **AND** the user has not provided an explicit override
- **THEN** `SKILL.md` allows the agent to continue using `recommended_next_action`
