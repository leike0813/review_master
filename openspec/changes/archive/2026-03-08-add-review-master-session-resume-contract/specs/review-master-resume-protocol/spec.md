## ADDED Requirements

### Requirement: the runtime MUST use a unified resume-first entry protocol

`review-master` MUST use the same entry sequence for first invocation, cross-session continuation, and post-compression continuation.

#### Scenario: bootstrap workspace still resumes first

- **WHEN** a newly initialized workspace is opened for the first time
- **THEN** the Agent first runs `gate-and-render`
- **AND** reads `instruction_payload.resume_packet`
- **AND** reads `agent-resume.md`
- **AND** only then continues to the next SQL write recipe

#### Scenario: resumed workspace uses the same protocol

- **WHEN** an existing workspace is reopened in a later session
- **THEN** the Agent follows the same resume-first sequence
- **AND** the only difference is that the resume packet contains continuation state instead of bootstrap state
