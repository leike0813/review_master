## MODIFIED Requirements

### Requirement: Stage 4 workboard instructions are operations-manual grade

Stage 4 MUST define the atomic workboard as the main live view for planning, confirmation, later execution tracking, and workflow recovery.

#### Scenario: workboard is the live board

- **WHEN** the docs tell the Agent which artifact to inspect after Stage 3 atomization
- **THEN** they must direct the Agent to use `07-atomic-comment-workboard.md` as the evolving lifecycle board
- **AND** they must not require `04-atomic-review-comment-list.md` to repeat live planning or execution fields
