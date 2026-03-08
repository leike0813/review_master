# review-master-artifact-workspace-validation-baseline Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-artifact-workspace. Update Purpose after archive.
## Requirements
### Requirement: Unified validator must understand workspace bootstrap state
`review-master/scripts/validate_artifact_consistency.py` SHALL validate the fixed runtime artifact workspace via `--artifact-root PATH`.

The validator MUST:

- validate the presence of `workflow-state.yaml` and all fixed runtime artifacts
- validate `workflow-state.yaml` syntax and required fields
- validate Markdown artifact structure and cross-artifact consistency
- accept a freshly initialized scaffold state without reporting format errors for empty runtime tables
- report issues in JSON without failing fast; only program failures may use a non-zero exit code

#### Scenario: Freshly initialized workspace is clean
- **WHEN** the agent initializes a new workspace and immediately validates it
- **THEN** the validator reports no structure or format baseline errors

#### Scenario: Invalid workflow-state field is reported
- **WHEN** `workflow-state.yaml` contains an invalid `current_stage` or `stage_gate`
- **THEN** the validator reports a format error for the workflow state artifact

### Requirement: Stage gate readiness must match artifact readiness
The validator MUST treat `workflow-state.yaml` as the source of stage context and MUST report consistency problems when a stage is marked `ready` but its prerequisite artifacts are not yet authored.

At minimum:

- `stage_2` ready requires an authored manuscript structure summary
- `stage_3` ready requires an authored atomic review comment list
- `stage_4` ready requires authored mapping and revision-board artifacts
- `stage_5` ready with a non-empty active comment requires a matching strategy card
- `stage_6` ready requires an authored final assembly checklist

#### Scenario: Ready gate without authored artifacts is invalid
- **WHEN** `workflow-state.yaml` sets `current_stage: stage_4` and `stage_gate: ready`
- **AND** the mapping table or revision board is still only an empty scaffold
- **THEN** the validator reports a consistency error

