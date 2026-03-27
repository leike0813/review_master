# review-master-markdown-artifact-contract Specification

## Purpose
TBD - created by archiving change implement-review-master-skill-contract. Update Purpose after archive.
## Requirements
### Requirement: Markdown-first intermediate artifacts

`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- `04-atomic-review-comment-list.md` as the stable Stage 3 identity/index artifact
- `07-atomic-comment-workboard.md` as the live Stage 4-6 workboard
- `08-supplement-suggestion-plan.md`
- `response-strategy-cards/{comment_id}.md`
- `15-supplement-intake-plan.md`
- `16-final-assembly-checklist.md`

#### Scenario: Stage 3 list and Stage 4-6 workboard have different contracts

- **WHEN** the workspace renders both `04-atomic-review-comment-list.md` and `07-atomic-comment-workboard.md`
- **THEN** the atomic list MUST keep stable identity and source-trace fields only
- **AND** the atomic workboard MUST carry live planning and execution state

#### Scenario: strategy card shows typed manuscript execution items

- **WHEN** one atomic review comment enters confirmed Stage 5 execution
- **THEN** the per-comment strategy card must show manuscript execution items grouped by category
- **AND** it must keep the response draft as a separate response-side section

#### Scenario: final assembly checklist uses execution-item completion names

- **WHEN** `16-final-assembly-checklist.md` is rendered
- **THEN** it must use `manuscript_execution_items_done`
- **AND** it must use `response_draft_done`

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

