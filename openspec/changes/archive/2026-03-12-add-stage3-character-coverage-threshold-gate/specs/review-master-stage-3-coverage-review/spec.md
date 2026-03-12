## MODIFIED Requirements

### Requirement: Stage 3 must produce a coverage-review artifact before Stage 4

Stage 3 coverage review MUST include character-level quantitative metrics and threshold-based gate semantics.

#### Scenario: character-level coverage metrics are computed globally

- **WHEN** Stage 3 coverage is validated
- **THEN** the system MUST compute character coverage using `review_comment_source_documents.original_text` and `raw_thread_source_spans`
- **AND** the primary gate metric MUST include `duplicate_filtered` spans
- **AND** a diagnostic non-duplicate metric MUST be emitted for operator inspection
- **AND** metrics MUST include both global aggregate and per-document breakdown

#### Scenario: hard and soft coverage thresholds classify Stage 3 gate status

- **WHEN** Stage 3 global character coverage is below `30%`
- **THEN** gate validation MUST produce a blocking dependency error
- **AND** the run status MUST be `issues_found`
- **WHEN** coverage is between `30%` (inclusive) and `50%` (exclusive)
- **THEN** gate validation MUST emit a non-blocking advisory
- **AND** Stage 3 progression remains controlled by user-confirmation gate
- **WHEN** coverage is at least `50%`
- **THEN** no threshold advisory is required
