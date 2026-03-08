## ADDED Requirements

### Requirement: skill guidance MUST explicitly teach the resume-first protocol

`SKILL.md` and supporting reference documents MUST explicitly tell the Agent to resume first before it executes any new write recipe.

#### Scenario: first invocation guidance

- **WHEN** the Agent opens `review-master/SKILL.md`
- **THEN** it can see that first invocation also begins by attempting recovery
- **AND** it can find the referenced stage docs and helper-script docs that explain the same protocol

#### Scenario: resume guidance after context loss

- **WHEN** the Agent re-enters after session loss or context compression
- **THEN** the docs instruct it to rely on `resume_packet`, `agent-resume.md`, and `resume_read_order`
- **AND** not on assumed conversational memory
