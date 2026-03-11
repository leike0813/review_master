## MODIFIED Requirements

### Requirement: Minimal required fields per artifact

The authoring rules MUST define the minimal required fields for each artifact and MUST allow non-critical fields to remain blank.

At minimum:

- `final-assembly-checklist.md`: `comment_id`, `status`, `manuscript_draft_done`, `response_draft_done`, `export_ready`
- `response-strategy-card.md`: card header fields, `Original comment excerpt`, `Proposed stance`, at least one action row, completion checklist, manuscript draft section, response draft section

#### Scenario: Stage 5 artifact labels use draft terminology

- **WHEN** the authoring rules describe `final-assembly-checklist.md` or `response-strategy-card.md`
- **THEN** they must use `manuscript_draft_done` and `response_draft_done`
- **AND** they must not describe Stage 5 as if final manuscript authoring were already complete
