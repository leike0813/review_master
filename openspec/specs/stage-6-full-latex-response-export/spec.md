# stage-6-full-latex-response-export Specification

## Purpose
TBD - created by archiving change stabilize-review-master-runtime-digest-and-stage-6-export-path. Update Purpose after archive.
## Requirements
### Requirement: response_latex must be a compilable LaTeX document

The Stage 6 LaTeX response letter MUST be exported as a complete compilable file rather than a table-body fragment.

#### Scenario: Full LaTeX response export

- **WHEN** `response_latex` is exported
- **THEN** the output contains LaTeX front matter including `\\documentclass`
- **AND** it includes required packages and a document body
- **AND** the point-to-point response table is rendered inside the document

