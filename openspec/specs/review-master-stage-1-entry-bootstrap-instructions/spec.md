# review-master-stage-1-entry-bootstrap-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-1-and-2-instructions. Update Purpose after archive.
## Requirements
### Requirement: stage 1 guidance MUST define a complete entry-and-bootstrap workflow

`review-master` MUST describe Stage 1 as a complete executable subflow covering environment confirmation, unified resume-first entry, input checking, manuscript entry identification, workspace initialization, bootstrap alignment, and the first gate-and-render run.

#### Scenario: ambiguous manuscript entry requires user confirmation

- **WHEN** the manuscript source is a LaTeX project and the main entry is not uniquely determined
- **THEN** Stage 1 guidance tells the Agent to stop and ask the user to confirm the main entry
- **AND** the Agent does not silently choose a file

#### Scenario: first invocation still resumes first

- **WHEN** the skill is invoked for the first time on a new workspace
- **THEN** Stage 1 guidance tells the Agent to read `instruction_payload.resume_packet` and `agent-resume.md`
- **AND** to treat the result as bootstrap resume rather than bypassing recovery

