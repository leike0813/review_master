## MODIFIED Requirements

### Requirement: Artifact generation timing and purpose

`06-review-comment-coverage.md` MUST expose both qualitative highlighting and quantitative character-coverage signals.

#### Scenario: coverage artifact includes duplicate-aware character metrics

- **WHEN** Stage 3 coverage artifact is generated
- **THEN** it MUST display a global character coverage value that includes `duplicate_filtered` spans
- **AND** it MUST display a global non-duplicate diagnostic value
- **AND** it MUST display per-document character coverage details
- **AND** it MUST display threshold references and current classification (`hard_fail` / `soft_warn` / `pass`)
