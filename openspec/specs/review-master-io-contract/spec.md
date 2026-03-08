# review-master-io-contract Specification

## Purpose
TBD - created by archiving change define-review-master-staged-workflow. Update Purpose after archive.
## Requirements
### Requirement: Required input slots
The first release of `review-master` SHALL require exactly two primary input slots:

- `manuscript_source`: the manuscript source, provided as either a single main `.tex` file path or a LaTeX project directory path
- `review_comments_source`: the review comments source, provided as a Markdown (`.md`) or plain text (`.txt`) file path

The workflow SHALL NOT start if either required input slot is missing.

#### Scenario: Single-file manuscript input
- **WHEN** the user provides a readable main `.tex` file path as `manuscript_source`
- **AND** provides a readable `.md` review comments file as `review_comments_source`
- **THEN** the workflow accepts the run as a valid first-release input combination

#### Scenario: Project-directory manuscript input
- **WHEN** the user provides a readable LaTeX project directory as `manuscript_source`
- **AND** provides a readable `.txt` review comments file as `review_comments_source`
- **THEN** the workflow accepts the run as a valid first-release input combination

#### Scenario: Missing required input
- **WHEN** either `manuscript_source` or `review_comments_source` is not provided
- **THEN** the workflow must stop before stage execution and request the missing input

### Requirement: Review comments format restriction
`review_comments_source` MUST be limited to Markdown or plain text in the first release. Other comment formats are out of scope for this capability.

#### Scenario: Unsupported review comment format
- **WHEN** the user provides a review comments file in a format other than `.md` or `.txt`
- **THEN** the workflow must reject it as an unsupported first-release input format

### Requirement: Final output contract
The first release of `review-master` SHALL produce two final output artifacts:

- `revised_manuscript`: the revised manuscript output
- `response_letter_path`: a Markdown response letter file

The manuscript output shape MUST follow the manuscript input shape:

- single `.tex` input -> revised main `.tex` output
- project directory input -> revised project directory output

#### Scenario: Single-file input preserves single-file output
- **WHEN** `manuscript_source` is a single main `.tex` file
- **THEN** the final `revised_manuscript` output is a revised main `.tex` file
- **AND** the final response letter is emitted as a Markdown file

#### Scenario: Project input preserves project output
- **WHEN** `manuscript_source` is a LaTeX project directory
- **THEN** the final `revised_manuscript` output is a revised LaTeX project directory
- **AND** the final response letter is emitted as a Markdown file

