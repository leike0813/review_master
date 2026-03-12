## MODIFIED Requirements

### Requirement: SKILL.md must define the executable six-stage workflow

Stage 3 instructions in `SKILL.md` MUST describe source-span anchoring and rebuild guidance.

#### Scenario: Stage 3 instructions require source-span truth

- **WHEN** `SKILL.md` describes Stage 3 modeling outputs
- **THEN** it MUST require `review_comment_source_documents` and `raw_thread_source_spans` as coverage truth inputs
- **AND** it MUST state that `raw_review_threads.original_text` must stay source-traceable
- **AND** it MUST require user confirmation on `06-review-comment-coverage.md` before Stage 4

#### Scenario: legacy Stage 3 data requires rebuild guidance

- **WHEN** Stage 3 coverage data is legacy thread-level synthetic truth without full-document source spans
- **THEN** `SKILL.md` guidance MUST require rerunning Stage 3 from original reviewer/editor files before proceeding
