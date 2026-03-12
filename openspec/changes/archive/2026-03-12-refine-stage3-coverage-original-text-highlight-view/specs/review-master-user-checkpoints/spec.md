## MODIFIED Requirements

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
