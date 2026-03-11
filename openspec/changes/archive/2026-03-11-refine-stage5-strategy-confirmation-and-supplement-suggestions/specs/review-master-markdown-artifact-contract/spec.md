## MODIFIED Requirements

### Requirement: Markdown-first intermediate artifacts

`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- manuscript structure summary
- atomic review comment list
- comment-to-manuscript mapping table
- priority and dependency revision board
- per-comment response strategy cards
- supplement suggestion planning
- supplement intake and landing plan
- final assembly checklist

#### Scenario: strategy card is pre-draft before confirmation

- **WHEN** one atomic review comment enters Stage 5 but has not yet been confirmed
- **THEN** the per-comment strategy card must show the pending confirmation state
- **AND** it MUST NOT present Stage 5 drafts as already authored

#### Scenario: supplement suggestion backlog is readable before intake

- **WHEN** Stage 5 is entered with evidence-gap comments
- **THEN** `supplement-suggestion-plan.md` must be generated as a user-readable planning artifact
- **AND** `supplement-intake-plan.md` must remain the later intake/landing artifact
