## ADDED Requirements

### Requirement: Stage 3 coverage artifact must prioritize readability

`06-review-comment-coverage.md` MUST be a user-review artifact that reads like the original review-comments text instead of a machine-tagged debug view.

#### Scenario: readable body with audit appendix

- **WHEN** Stage 3 coverage is rendered for user confirmation
- **THEN** the body MUST present the source text in original order with visible covered/uncovered distinction
- **AND** covered/uncovered distinction MUST be understandable without parsing technical wrapper syntax
- **AND** an appendix table MUST preserve deterministic thread/comment mapping details for audit
