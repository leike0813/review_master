# review-master-target-location-format Specification

## Purpose
TBD - created by archiving change define-review-master-artifact-authoring-rules. Update Purpose after archive.
## Requirements
### Requirement: Unified target_location format
All comment-scoped artifact templates SHALL use the same half-structured `target_location` format:

- `path::section::anchor`

Where:

- `path`: `.tex` file path or relative project path
- `section`: human-readable section or subsection label
- `anchor`: paragraph, table, figure, equation, list item, or local anchor description

#### Scenario: Unknown fine-grained anchor still follows format
- **WHEN** the exact local anchor is not yet known
- **THEN** `target_location` may still be written as `path::section::TBD`

#### Scenario: Whole-document artifact remains not applicable
- **WHEN** `manuscript-structure-summary.md` is filled
- **THEN** it still marks `target_location` as `N/A`
- **AND** does not attempt to force the `path::section::anchor` format into a whole-document artifact

### Requirement: Format description is documented in the central rules
The central authoring-rules document MUST explain the `path::section::anchor` format and require templates to align with it.

#### Scenario: Templates reference the same format
- **WHEN** multiple templates use `target_location`
- **THEN** they all describe it consistently with the same `path::section::anchor` format

