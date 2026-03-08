# review-master-resume-output Specification

## Purpose
TBD - created by archiving change add-review-master-session-resume-contract. Update Purpose after archive.
## Requirements
### Requirement: gate-and-render MUST emit and render a resume package every run

The core gate-and-render script MUST produce both a machine-readable and a rendered recovery surface on every invocation.

#### Scenario: machine-readable resume output

- **WHEN** `gate_and_render_workspace.py` runs
- **THEN** `instruction_payload` includes `resume_packet`
- **AND** `resume_packet` includes bootstrap vs continuation status, current focus, open loops, and next action anchor

#### Scenario: rendered resume output

- **WHEN** `gate_and_render_workspace.py` completes
- **THEN** it renders `agent-resume.md`
- **AND** that view includes both the static Skill digest and the current dynamic resume state

