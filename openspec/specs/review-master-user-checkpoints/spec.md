# review-master-user-checkpoints Specification

## Purpose
TBD - created by archiving change define-review-master-staged-workflow. Update Purpose after archive.
## Requirements
### Requirement: Mandatory user checkpoints

User interaction SHALL be a mandatory control mechanism in the first release, not an optional enhancement.

At minimum, the workflow MUST include the following checkpoints:

- initial submission of manuscript and review comments
- entry confirmation when a project directory contains multiple plausible main `.tex` files
- Stage 3 coverage review confirmation based on the rendered original-text coverage artifact
- revision-board confirmation after decomposition, mapping, prioritization, and ordering
- per-comment confirmation before executing manuscript changes for that comment
- evidence supplementation when a comment cannot be completed from current inputs
- final review before final export

#### Scenario: Stage 3 coverage confirmation uses readable highlighted artifact

- **WHEN** Stage 3 extraction and mapping are complete
- **THEN** the workflow must present `06-review-comment-coverage.md` for explicit user confirmation
- **AND** the user must be able to identify covered text visually and verify mapping details from the appendix before Stage 4

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
After all comments are individually closed, the workflow MUST still require a final user review before exporting the final revised manuscript and response letter.

#### Scenario: Final package waits for user review
- **WHEN** all per-comment items have reached a completed state
- **THEN** the workflow must present the final package for review
- **AND** only export after the user confirms the final review

