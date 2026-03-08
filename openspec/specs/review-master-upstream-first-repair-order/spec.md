# review-master-upstream-first-repair-order Specification

## Purpose
TBD - created by archiving change define-review-master-state-machine-instruction-loop. Update Purpose after archive.
## Requirements
### Requirement: Repair sequencing must prioritize upstream artifacts
When validation issues exist, the validator SHALL emit `repair_sequence` using upstream-first ordering.

The first-release repair order MUST be:

1. `workflow-state.yaml`
2. `manuscript-structure-summary.md`
3. `atomic-review-comment-list.md`
4. `comment-manuscript-mapping-table.md`
5. `revision-board.md`
6. `response-strategy-cards/{comment_id}.md`
7. `final-assembly-checklist.md`

The validator MUST NOT recommend repairing a downstream derived artifact before the upstream source artifact that invalidated it.

#### Scenario: Atomic-list issue outranks mapping-table repair
- **WHEN** both the atomic list and mapping table contain issues
- **THEN** the first repair instruction targets `atomic-review-comment-list.md`
- **AND** the mapping table repair appears later in the sequence

#### Scenario: Missing strategy card is repaired after revision board
- **WHEN** an active comment is missing its strategy card
- **AND** the revision board still contains unresolved upstream issues
- **THEN** the strategy-card repair does not appear before the revision-board repair

