# review-master-skill-template-usage Specification

## Purpose
TBD - created by archiving change add-review-master-markdown-artifact-templates. Update Purpose after archive.
## Requirements
### Requirement: SKILL.md must reference template files
`review-master/SKILL.md` MUST explicitly reference the six Markdown template files under `review-master/references/` in its intermediate artifact guidance.

#### Scenario: SKILL.md points to template filenames
- **WHEN** a user or agent reads the intermediate artifact section in `SKILL.md`
- **THEN** it can find the exact filenames of the six templates

### Requirement: SKILL.md must define stage-by-stage template usage
`review-master/SKILL.md` MUST state which template is produced in which stage:

- stage 2 -> `manuscript-structure-summary.md`
- stage 3 -> `atomic-review-comment-list.md`
- stage 4 -> `comment-manuscript-mapping-table.md` and `revision-board.md`
- stage 5 -> `response-strategy-card.md`
- stage 6 -> `final-assembly-checklist.md`

#### Scenario: Stage 4 requires user confirmation of board artifacts
- **WHEN** stage 4 completes
- **THEN** `SKILL.md` requires the user to review the mapping table and revision board before moving into stage 5

#### Scenario: Stage 5 requires strategy-card confirmation
- **WHEN** one comment enters stage 5
- **THEN** `SKILL.md` requires generation and confirmation of `response-strategy-card.md` for that comment before execution

#### Scenario: Stage 6 requires checklist review
- **WHEN** stage 6 begins
- **THEN** `SKILL.md` requires review of `final-assembly-checklist.md` before final export

### Requirement: Templates are contract templates, not examples
`review-master/SKILL.md` MUST clarify that these template files are empty templates with field guidance, not free-form references and not sample-filled examples.

#### Scenario: Template purpose is explicit
- **WHEN** `SKILL.md` introduces the template files
- **THEN** it states they are contract templates for actual workflow use
- **AND** it does not describe them as illustrative examples

