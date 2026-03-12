# review-master-markdown-artifact-contract Specification

## Purpose
TBD - created by archiving change implement-review-master-skill-contract. Update Purpose after archive.
## Requirements
### Requirement: Markdown-first intermediate artifacts

`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- manuscript structure summary
- atomic review comment list
- comment-to-manuscript mapping table
- priority and dependency revision board
- per-comment response strategy cards
- supplement suggestion planning
- supplement intake and landing plan
- final assembly checklist

#### Scenario: strategy card is pre-draft before confirmation

- **WHEN** one atomic review comment enters Stage 5 but has not yet been confirmed
- **THEN** the per-comment strategy card must show the pending confirmation state
- **AND** it MUST NOT present Stage 5 drafts as already authored

#### Scenario: supplement suggestion backlog is readable before intake

- **WHEN** Stage 5 is entered with evidence-gap comments
- **THEN** `supplement-suggestion-plan.md` must be generated as a user-readable planning artifact
- **AND** `supplement-intake-plan.md` must remain the later intake/landing artifact

### Requirement: Artifact generation timing and purpose

`06-review-comment-coverage.md` MUST expose both qualitative highlighting and quantitative character-coverage signals.

#### Scenario: coverage artifact includes duplicate-aware character metrics

- **WHEN** Stage 3 coverage artifact is generated
- **THEN** it MUST display a global character coverage value that includes `duplicate_filtered` spans
- **AND** it MUST display a global non-duplicate diagnostic value
- **AND** it MUST display per-document character coverage details
- **AND** it MUST display threshold references and current classification (`hard_fail` / `soft_warn` / `pass`)

### Requirement: No template files required in this change
This change MUST define the Markdown artifacts in `SKILL.md` without requiring dedicated template files under `review-master/references/`.

#### Scenario: Contract exists without bundled templates
- **WHEN** this change is implemented
- **THEN** the artifact contract is fully expressed in `review-master/SKILL.md`
- **AND** no new template files are required under `review-master/references/`

### Requirement: Stage 3 coverage artifact must prioritize readability

`06-review-comment-coverage.md` MUST be a user-review artifact that reads like the original review-comments text instead of a machine-tagged debug view.

#### Scenario: readable body with audit appendix

- **WHEN** Stage 3 coverage is rendered for user confirmation
- **THEN** the body MUST present the source text in original order with visible covered/uncovered distinction
- **AND** covered/uncovered distinction MUST be understandable without parsing technical wrapper syntax
- **AND** an appendix table MUST preserve deterministic thread/comment mapping details for audit

