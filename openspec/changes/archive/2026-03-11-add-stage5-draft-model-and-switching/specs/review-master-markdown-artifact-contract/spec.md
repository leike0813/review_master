## MODIFIED Requirements

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
