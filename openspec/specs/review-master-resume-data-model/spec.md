# review-master-resume-data-model Specification

## Purpose
TBD - created by archiving change add-review-master-session-resume-contract. Update Purpose after archive.
## Requirements
### Requirement: the runtime MUST persist resume state in SQLite

The runtime schema MUST include dedicated resume tables in addition to the workflow-state tables.

#### Scenario: bootstrap resume exists immediately after initialization

- **WHEN** `init_artifact_workspace.py` creates a new workspace
- **THEN** the database already contains a bootstrap row in `resume_brief`
- **AND** the workspace can render a bootstrap `agent-resume.md` without requiring later manual seeding

#### Scenario: mid-workflow resume cannot remain bootstrap

- **WHEN** the workflow has advanced beyond `stage_1`
- **THEN** `resume_brief.resume_status` MUST NOT remain `bootstrap`
- **AND** the gate-and-render script reports a consistency issue if it does

