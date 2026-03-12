## MODIFIED Requirements

### Requirement: SKILL.md must define the executable six-stage workflow

Stage 3 instruction contract MUST define role-aware source spans and confirmation semantics.

#### Scenario: Stage 3 instructions define span-role extraction policy

- **WHEN** `SKILL.md` describes Stage 3 modeling
- **THEN** it MUST define `raw_thread_source_spans.span_role` with `primary`, `supporting`, and `duplicate_filtered`
- **AND** it MUST state that duplicate-filtered source spans remain visible in coverage review even if summaries are deduplicated
- **AND** it MUST state that heading-only-coverage diagnostics are advisory (non-blocking) and require user review
