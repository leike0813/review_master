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

