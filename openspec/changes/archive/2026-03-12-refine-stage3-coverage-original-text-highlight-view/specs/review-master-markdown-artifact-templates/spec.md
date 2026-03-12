## ADDED Requirements

### Requirement: Stage 3 coverage template must separate reading view and mapping view

The Stage 3 coverage template MUST combine a readable highlighted body with a separate mapping appendix.

#### Scenario: coverage template structure

- **WHEN** `06-review-comment-coverage.md` is rendered
- **THEN** the template MUST include an original-text coverage body where covered spans are visually emphasized
- **AND** it MUST include a mapping appendix table for covered segments (`thread_id` and `comment_id` mapping)
- **AND** uncovered text MUST remain visible in the body
