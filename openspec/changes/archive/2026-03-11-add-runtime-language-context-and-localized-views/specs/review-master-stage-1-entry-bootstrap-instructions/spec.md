## MODIFIED Requirements

### Requirement: stage 1 guidance MUST define a complete entry-and-bootstrap workflow

`review-master` MUST describe Stage 1 as a complete executable subflow covering environment confirmation, language confirmation for first-time bootstrap, unified resume-first entry for existing workspaces, input checking, manuscript entry identification, workspace initialization, bootstrap alignment, and the first gate-and-render run.

#### Scenario: ambiguous manuscript entry requires user confirmation

- **WHEN** the manuscript source is a LaTeX project and the main entry is not uniquely determined
- **THEN** Stage 1 guidance tells the Agent to stop and ask the user to confirm the main entry
- **AND** the Agent does not silently choose a file

#### Scenario: first invocation confirms languages before initialization

- **WHEN** the skill is invoked for the first time and the workspace does not yet exist
- **THEN** Stage 1 guidance tells the Agent to infer `working_language` from the user prompt and `document_language` from the manuscript
- **AND** it tells the Agent to explicitly confirm both languages with the user before calling `init_artifact_workspace.py`

#### Scenario: existing workspace still resumes first

- **WHEN** the skill is invoked for a workspace that already exists
- **THEN** Stage 1 guidance tells the Agent to read `instruction_payload.resume_packet` and `agent-resume.md` first
- **AND** it does not re-run the first-time language confirmation gate unless the user explicitly changes the language settings
