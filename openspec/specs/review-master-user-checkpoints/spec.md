# review-master-user-checkpoints Specification

## Purpose
TBD - created by archiving change define-review-master-staged-workflow. Update Purpose after archive.
## Requirements
### Requirement: Mandatory user checkpoints

Stage 3 user confirmation MUST be informed by quantitative character-coverage metrics.

#### Scenario: Stage 3 confirmation reads threshold status before user sign-off

- **WHEN** Stage 3 extraction and mapping are complete
- **THEN** the workflow MUST present `06-review-comment-coverage.md` including character-coverage metrics
- **AND** users MUST be able to inspect whether coverage is in hard-fail, soft-warn, or pass zone before confirming Stage 3
- **AND** Stage 4 remains blocked until explicit Stage 3 confirmation

### Requirement: Per-comment confirmation is required before execution

Each atomic review comment MUST be confirmed by the user before that comment is allowed to enter manuscript-revision execution.

#### Scenario: unconfirmed strategy cannot author Stage 5 drafts

- **WHEN** the workflow has prepared a response strategy card for one atomic comment
- **BUT** the user has not confirmed or corrected it yet
- **THEN** that comment must not enter manuscript-draft authoring or response-draft authoring
- **AND** the guidance must explicitly tell the user that they may modify the strategy card

### Requirement: Evidence supplementation is user-provided
If an atomic comment requires additional experiments, data, references, figures, or arguments that are not present in the current inputs, the workflow MUST request those materials from the user and wait for supplementation before completing that comment.

#### Scenario: Missing evidence triggers a material request
- **WHEN** one atomic comment cannot be responsibly answered with the current manuscript and review comments inputs
- **THEN** the workflow must produce a gap analysis and a user-facing materials request for that comment

### Requirement: Final review is mandatory before export

The final checkpoint MUST review revision-action closure and thread-level response coverage rather than patch export completeness.

#### Scenario: Stage 6 completion checks response coverage and audited edits

- **GIVEN** Stage 6 is nearing completion
- **WHEN** the runtime asks for final review
- **THEN** it must surface whether all revision plan actions are closed
- **AND** whether every original review thread is covered
- **AND** whether the working manuscript contains any unaudited modifications

