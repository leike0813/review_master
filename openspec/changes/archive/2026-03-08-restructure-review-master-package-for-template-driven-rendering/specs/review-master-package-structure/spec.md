## ADDED Requirements

### Requirement: `review-master` MUST separate entry instructions, references, and runtime assets

The published package MUST use three distinct layers:

- `SKILL.md` for the top-level runtime contract
- `references/` for instruction-only documents
- `assets/` for schema and render resources

#### Scenario: runtime package layout

- **WHEN** the package is inspected after this change
- **THEN** `SKILL.md` remains at the package root
- **AND** `references/` contains stage guidance and cross-stage reference docs
- **AND** `assets/` contains the runtime schema and render templates
- **AND** rendered-view description files are no longer stored in `references/`

### Requirement: `SKILL.md` MUST remain concise

`SKILL.md` MUST contain only high-level execution guidance and links to detailed references.

#### Scenario: short entry contract

- **WHEN** an Agent opens `review-master/SKILL.md`
- **THEN** it can learn the goals, non-goals, runtime contract, six-stage flow, environment gate, script summary, and reference index
- **AND** it does not need to scan long template or schema explanations in that file
