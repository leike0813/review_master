# review-master-playbook-evidence-supplement-assets Specification

## Purpose
TBD - created by archiving change add-review-master-evidence-supplement-playbook. Update Purpose after archive.
## Requirements
### Requirement: Complex playbook must include multi-file assets and supplement package

The evidence-supplement playbook SHALL include a repository-level example asset set under `playbooks/examples/evidence-supplement-multi-review/`.

At minimum, the asset set MUST include:

- a multi-file LaTeX manuscript input
- a review-comments input with 2 reviewer sections
- a supplement package containing `supplement-note.md`, `stability-results.csv`, and `seed-stability-figure.svg`
- a final-state workspace that uses the current runtime workspace layout
- 5 response-strategy cards
- a revised multi-file manuscript output
- a Markdown response letter
- 8 representative validator JSON files

#### Scenario: Final-state workspace keeps all five comments consistent

- **WHEN** the sample workspace is validated
- **THEN** `workflow-state.yaml`, `revision-board.md`, the final checklist, and all 5 strategy cards use the same 5 `comment_id` values
- **AND** the workspace passes the current unified validator

#### Scenario: Validator output samples cover the blocked supplement loop

- **WHEN** a developer reads `validator-output/`
- **THEN** it includes `stage-5-evidence-gap-blocked.json`
- **AND** it includes `stage-5-after-supplement-ready.json`
- **AND** both files use the current `instruction_payload` structure

