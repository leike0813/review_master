## MODIFIED Requirements

### Requirement: Artifact generation timing and purpose

`06-review-comment-coverage.md` MUST keep original-text readability while showing extraction role semantics.

#### Scenario: duplicate visibility without summary pollution

- **WHEN** repeated substantive text is deduplicated in canonical summaries
- **THEN** coverage artifact MUST still visibly highlight repeated source locations
- **AND** those repeated highlights MUST be visually distinct from normal covered spans
