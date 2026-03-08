# review-master-artifact-workspace-bootstrap Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-artifact-workspace. Update Purpose after archive.
## Requirements
### Requirement: A deterministic initializer must create artifact workspaces
The first release SHALL provide `review-master/scripts/init_artifact_workspace.py` to create a runtime artifact workspace from runtime scaffold assets.

The initializer MUST:

- accept optional `--artifact-root PATH`
- create `review-master-workspace/` in the current working directory when no path is provided
- auto-increment the default directory name on conflicts (`review-master-workspace-1/`, `review-master-workspace-2/`, ...)
- create the target when it does not exist
- fill the target when it exists and is empty
- fail when the target exists and is not empty
- output exactly one JSON object to stdout

#### Scenario: Default workspace name auto-increments
- **WHEN** the agent runs the initializer twice without `--artifact-root`
- **THEN** the first run creates `review-master-workspace/`
- **AND** the second run creates `review-master-workspace-1/`

#### Scenario: Non-empty explicit target fails
- **WHEN** `--artifact-root` points to an existing non-empty directory
- **THEN** the initializer exits with a non-zero code
- **AND** it does not overwrite the existing directory

