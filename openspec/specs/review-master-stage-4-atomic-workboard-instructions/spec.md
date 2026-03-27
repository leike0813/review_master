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

### Requirement: Stage 4 workboard instructions are operations-manual grade

Stage 4 MUST define the atomic workboard as the main live view for planning, confirmation, later execution tracking, and workflow recovery.

#### Scenario: workboard is the live board

- **WHEN** the docs tell the Agent which artifact to inspect after Stage 3 atomization
- **THEN** they must direct the Agent to use `07-atomic-comment-workboard.md` as the evolving lifecycle board
- **AND** they must not require `04-atomic-review-comment-list.md` to repeat live planning or execution fields

