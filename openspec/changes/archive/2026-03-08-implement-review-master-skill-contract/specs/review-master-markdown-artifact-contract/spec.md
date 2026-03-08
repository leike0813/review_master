## ADDED Requirements

### Requirement: Markdown-first intermediate artifacts
`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- manuscript structure summary
- atomic review comment list
- comment-to-manuscript mapping table
- priority and dependency revision board
- per-comment response strategy cards
- final assembly checklist

#### Scenario: Artifacts are readable and confirmable
- **WHEN** the workflow produces one of the first-release intermediate artifacts
- **THEN** `SKILL.md` treats it as a Markdown-first artifact intended for user reading, review, and confirmation

### Requirement: Artifact generation timing and purpose
`review-master/SKILL.md` MUST describe when each Markdown artifact is generated and how it is used in the workflow.

#### Scenario: Revision board is generated before execution
- **WHEN** the workflow completes mapping and prioritization
- **THEN** `SKILL.md` requires generation of the revision board before stage 5 execution begins

#### Scenario: Strategy card is generated before per-comment confirmation
- **WHEN** one atomic review comment enters stage 5
- **THEN** `SKILL.md` requires generation of a per-comment strategy card before asking the user to confirm that comment

### Requirement: No template files required in this change
This change MUST define the Markdown artifacts in `SKILL.md` without requiring dedicated template files under `review-master/references/`.

#### Scenario: Contract exists without bundled templates
- **WHEN** this change is implemented
- **THEN** the artifact contract is fully expressed in `review-master/SKILL.md`
- **AND** no new template files are required under `review-master/references/`
