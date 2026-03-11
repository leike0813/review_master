# review-master-supplement-intake-and-landing Specification

## Purpose
TBD - created by archiving change add-supplement-intake-and-landing-plan. Update Purpose after archive.
## Requirements
### Requirement: Stage 5 MUST record file-level supplement intake decisions

When a supplement round is processed, the runtime MUST persist one intake record per user-provided supplement file, including a deterministic decision and rationale.

#### Scenario: Intake records are complete for a supplement round

- **WHEN** the Agent processes a supplement round
- **THEN** every supplement file in that round MUST have one intake record
- **AND** each record MUST include `decision` (`accepted` or `rejected`)
- **AND** each record MUST include a non-empty decision rationale

### Requirement: Accepted supplements MUST be linked to planned manuscript landing targets

For every accepted supplement file, the runtime MUST persist at least one landing mapping to canonical comment actions and target locations.

#### Scenario: Accepted supplement has executable landing mapping

- **WHEN** a supplement file is marked `accepted`
- **THEN** at least one landing link MUST exist for that file
- **AND** each landing link MUST reference a valid `comment_id`, `action_order`, and `location_order`
- **AND** each landing link MUST include a non-empty planned usage note

### Requirement: Supplement intake and landing MUST be user-visible in one workspace view

The runtime workspace MUST expose a dedicated read-only view that shows supplement intake decisions and landing mappings by round.

#### Scenario: User reviews supplement intake plan

- **WHEN** the workspace is rendered after supplement intake data is written
- **THEN** `supplement-intake-plan.md` MUST be generated
- **AND** the view MUST show accepted and rejected files with rationales
- **AND** accepted files MUST show their mapped comment/action/location targets

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

