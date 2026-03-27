## MODIFIED Requirements

### Requirement: workflow glossary is the single naming source

The workflow glossary MUST rename the Stage 6 action set, artifact set, and output contract to the revision-audit terminology, including the formal submission scripts and optional `latexdiff_manuscript`.

#### Scenario: glossary removes patch-driven Stage 6 names from the active contract

- **WHEN** operators read the glossary
- **THEN** it must list `commit_revision_round.py`, `capture_revision_action.py`, revision-loop action ids, and the new Stage 6 artifact filenames
- **AND** it must not present copy-variant or export-patch semantics as the active Stage 6 workflow
