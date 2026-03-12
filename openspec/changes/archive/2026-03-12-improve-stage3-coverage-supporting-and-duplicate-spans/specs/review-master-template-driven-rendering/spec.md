## MODIFIED Requirements

### Requirement: runtime rendering MUST load schema and templates from `assets/`

Stage 3 coverage template rendering MUST support span-role visual semantics.

#### Scenario: coverage template renders role-specific highlights

- **WHEN** the renderer builds `06-review-comment-coverage.md`
- **THEN** covered segments MUST include role metadata derived from `raw_thread_source_spans.span_role`
- **AND** duplicate-filtered spans MUST render with distinct orange style
- **AND** the appendix MUST include `span_role` in mapping rows
