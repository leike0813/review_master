# review-master-artifact-rule-reference Specification

## Purpose
TBD - created by archiving change define-review-master-artifact-authoring-rules. Update Purpose after archive.
## Requirements
### Requirement: SKILL.md references artifact authoring rules
`review-master/SKILL.md` MUST explicitly require the six Markdown artifacts to be filled according to `review-master/references/artifact-authoring-rules.md`.

#### Scenario: Stage output rule points to central reference
- **WHEN** `SKILL.md` describes stage-level artifact generation
- **THEN** it tells the user or agent to follow the central authoring-rules document

### Requirement: Templates keep only concise local guidance
The six artifact templates MUST retain concise local field reminders, but detailed rules SHALL live in the central reference document rather than being fully duplicated in every template.

#### Scenario: Template header remains concise
- **WHEN** any artifact template is opened
- **THEN** it contains a short reminder to follow the central rules
- **AND** does not duplicate the entire authoring-rules document inline

