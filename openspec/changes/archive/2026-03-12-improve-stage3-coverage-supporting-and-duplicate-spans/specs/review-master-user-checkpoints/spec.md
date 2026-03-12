## MODIFIED Requirements

### Requirement: Mandatory user checkpoints

Stage 3 user checkpoint MUST include role-aware coverage interpretation.

#### Scenario: Stage 3 checkpoint includes duplicate and advisory review

- **WHEN** user is asked to confirm Stage 3 coverage
- **THEN** checkpoint guidance MUST explain red vs orange highlight semantics
- **AND** any non-blocking coverage advisories MUST be surfaced for user review
- **AND** Stage 4 MUST remain blocked until explicit Stage 3 confirmation is cleared
