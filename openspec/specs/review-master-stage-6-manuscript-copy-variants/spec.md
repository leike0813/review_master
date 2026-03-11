# review-master-stage-6-manuscript-copy-variants Specification

## Purpose
TBD - created by archiving change correct-review-master-stage-6-copy-variant-semantics. Update Purpose after archive.
## Requirements
### Requirement: Stage 6 variants are manuscript-final-copy variants only

Stage 6 MUST treat location-level variants as document-language manuscript-final-copy variants only.

#### Scenario: response-side variants are not modeled

- **GIVEN** Stage 5 has already fixed strategy and draft boundaries
- **WHEN** Stage 6 generates location-level variants
- **THEN** it MUST generate exactly three manuscript-final-copy variants per `strategy_card_action` target location
- **AND** it MUST NOT require three response-side variants

#### Scenario: user selects manuscript wording only

- **GIVEN** a Stage 6 action-location has three manuscript-final-copy variants
- **WHEN** the user chooses among them
- **THEN** the chosen value MUST represent the wording that lands in the revised manuscript at that target location
- **AND** the runtime model MUST NOT expect an additional response-side variant selection

#### Scenario: variant text is final landing prose in document language

- **GIVEN** a stored `variant_text`
- **WHEN** Stage 6 renders `action-copy-variants.md`
- **THEN** the text MUST be directly insertable manuscript prose in the confirmed document language
- **AND** it MUST NOT be a working-language rewrite instruction such as `Add`, `Expand`, or `Clarify`

