## MODIFIED Requirements

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
