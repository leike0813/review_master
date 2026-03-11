# review-master-markdown-artifact-contract Specification

## Purpose
TBD - created by archiving change implement-review-master-skill-contract. Update Purpose after archive.
## Requirements
### Requirement: Markdown-first intermediate artifacts
`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- manuscript structure summary
- atomic review comment list
- comment-to-manuscript mapping table
- priority and dependency revision board
- per-comment response strategy cards
- supplement intake and landing plan
- final assembly checklist

#### Scenario: Artifacts are readable and confirmable
- **WHEN** the workflow produces one of the first-release intermediate artifacts
- **THEN** `SKILL.md` treats it as a Markdown-first artifact intended for user reading, review, and confirmation

### Requirement: Artifact generation timing and purpose

`review-master/SKILL.md` MUST describe when each Markdown artifact is generated and how it is used in the workflow.

#### Scenario: Strategy card shows Stage 5 draft truth

- **WHEN** one atomic review comment enters Stage 5
- **THEN** the per-comment strategy card must show manuscript drafts
- **AND** it must show the response draft
- **AND** it must show any comment-scoped blockers for that item

#### Scenario: Final assembly checklist uses draft completion names

- **WHEN** `final-assembly-checklist.md` is rendered
- **THEN** it must use `manuscript_draft_done`
- **AND** it must use `response_draft_done`
- **AND** it must not present Stage 5 as if final manuscript authoring were already complete

### Requirement: No template files required in this change
This change MUST define the Markdown artifacts in `SKILL.md` without requiring dedicated template files under `review-master/references/`.

#### Scenario: Contract exists without bundled templates
- **WHEN** this change is implemented
- **THEN** the artifact contract is fully expressed in `review-master/SKILL.md`
- **AND** no new template files are required under `review-master/references/`

