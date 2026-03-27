## MODIFIED Requirements

### Requirement: The first release must define workflow state-machine rules

The workflow state machine MUST treat Stage 6 as an interactive revision-audit loop whose formal submission path is `commit_revision_round.py`, not as a patch-export pipeline.

#### Scenario: Stage 6 actions are revision-loop actions

- **WHEN** the runtime recommends the next Stage 6 action
- **THEN** it must use revision-loop actions such as `record_revision_action`, `refresh_response_coverage`, `review_stage6_completion`, and `generate_latexdiff_preview`
- **AND** it must not recommend `generate_action_copy_variants`, `request_variant_selection`, or `prepare_export_patches`
