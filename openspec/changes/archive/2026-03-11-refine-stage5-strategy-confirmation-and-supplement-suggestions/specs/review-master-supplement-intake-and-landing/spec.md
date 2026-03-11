## ADDED Requirements

### Requirement: Stage 5 MUST expose supplement planning before intake

Before the user uploads supplement files, the runtime MUST expose a separate read-only view for evidence-gap-driven supplement requests.

#### Scenario: Stage 5 renders a supplement suggestion backlog

- **WHEN** Stage 5 is entered and at least one comment still has `evidence_gap = yes`
- **THEN** the workspace MUST render `supplement-suggestion-plan.md`
- **AND** that view MUST include at least one suggestion row for each such comment
- **AND** it MUST highlight the current `active_comment_id`

#### Scenario: supplement suggestions link to intake rounds

- **WHEN** supplement files are later processed through intake
- **THEN** the runtime MUST be able to link intake files back to one or more suggestion rows
- **AND** `supplement-intake-plan.md` MUST remain the file-level intake and landing view
