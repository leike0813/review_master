# review-master-stage-4-atomic-workboard-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-4-atomic-workboard-planning. Update Purpose after archive.
## Requirements
### Requirement: stage 4 guidance MUST define canonical atomic workboard planning rules

`review-master` MUST describe Stage 4 as the workflow that plans execution at the canonical atomic item level through `atomic_comment_state`, `atomic_comment_target_locations`, and `atomic_comment_analysis_links`.

#### Scenario: provisional location is still acceptable

- **WHEN** an atomic item cannot yet be mapped to a paragraph-level location
- **THEN** Stage 4 guidance allows a section-level or `TBD` location
- **AND** still requires `priority`, `evidence_gap`, and `next_action` to be explicit

#### Scenario: empty planning cannot advance

- **WHEN** Stage 4 planning leaves core decision fields unset
- **THEN** the guidance treats the workboard as incomplete
- **AND** does not allow progression to Stage 5

