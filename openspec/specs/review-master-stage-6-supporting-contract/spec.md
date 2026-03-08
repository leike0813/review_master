# review-master-stage-6-supporting-contract Specification

## Purpose
TBD - created by archiving change correct-review-master-stage-6-copy-variant-semantics. Update Purpose after archive.
## Requirements
### Requirement: Supporting docs, runtime, and fixtures use the corrected Stage 6 semantics

Documentation, runtime guidance, rendered views, and sample fixtures MUST all use the same corrected Stage 6 semantics.

#### Scenario: docs distinguish Stage 5 strategy from Stage 6 wording

- **GIVEN** the Stage 5 and Stage 6 guidance documents
- **WHEN** they describe the workflow boundary
- **THEN** Stage 5 MUST own strategy and draft direction
- **AND** Stage 6 MUST own final manuscript wording and export packaging

#### Scenario: sample fixtures reflect manuscript-only variants

- **GIVEN** sample workspaces and playbook examples
- **WHEN** they illustrate Stage 6
- **THEN** `action-copy-variants.md` MUST only show manuscript-final-copy variants
- **AND** sample data MUST NOT depend on response-side action-level variants
- **AND** each sample `variant_text` MUST be final landing prose instead of a direction-style instruction

