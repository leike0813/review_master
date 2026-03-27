## MODIFIED Requirements

### Requirement: Runtime artifact workspace must use a fixed layout

The runtime artifact workspace MUST expose the reordered Stage 2, Stage 5, and Stage 6 artifacts for the revision-audit workflow, including `03-style-profile.md`, `10-supplement-intake-plan.md`, `11-manuscript-revision-guide.md`, `12-manuscript-execution-graph.md`, `13-revision-action-log.md`, `14-response-coverage-matrix.md`, `15-response-letter-preview.md`, `16-response-letter-preview.tex`, and `17-final-assembly-checklist.md`.

#### Scenario: Stage 6 no longer renders patch-driven artifacts

- **WHEN** the runtime initializes or rerenders a workspace
- **THEN** it must expose the revised artifact numbering and filenames
- **AND** it must not require `10-action-copy-variants.md`, `11-response-letter-outline.md`, or `12-export-patch-plan.md` as Stage 6 workspace artifacts
