## MODIFIED Requirements

### Requirement: Markdown-first intermediate artifacts
`review-master/SKILL.md` MUST define the first-release intermediate artifacts as Markdown-first textual artifacts rather than YAML-first or JSON-first artifacts.

At minimum, `SKILL.md` MUST define the role of:

- `02-manuscript-structure-summary.md`
- `04-atomic-review-comment-list.md`
- `05-thread-to-atomic-mapping.md`
- `07-atomic-comment-workboard.md`
- `response-strategy-cards/{comment_id}.md`
- `15-supplement-intake-plan.md`
- `16-final-assembly-checklist.md`

#### Scenario: Artifacts are readable and confirmable
- **WHEN** the workflow produces one of the first-release intermediate artifacts
- **THEN** `SKILL.md` treats it as a Markdown-first artifact intended for user reading, review, and confirmation
- **AND** it references the numbered filename for each non-strategy-card artifact

### Requirement: Artifact generation timing and purpose

`review-master/SKILL.md` MUST describe when each Markdown artifact is generated and how it is used in the workflow.

#### Scenario: Strategy card shows Stage 5 draft truth

- **WHEN** one atomic review comment enters Stage 5
- **THEN** the per-comment strategy card must show manuscript drafts
- **AND** it must show the response draft
- **AND** it must show any comment-scoped blockers for that item

#### Scenario: Final assembly checklist uses draft completion names

- **WHEN** `16-final-assembly-checklist.md` is rendered
- **THEN** it must use `manuscript_draft_done`
- **AND** it must use `response_draft_done`
- **AND** it must not present Stage 5 as if final manuscript authoring were already complete

#### Scenario: Canonical artifact list is ordered by numbered filenames

- **WHEN** `SKILL.md` enumerates the runtime artifact workspace contents
- **THEN** it must list numbered non-strategy-card artifacts in numeric order
- **AND** it must preserve `response-strategy-cards/{comment_id}.md` as the unnumbered exception

### Requirement: No template files required in this change
This change MUST define the Markdown artifacts in `SKILL.md` without requiring dedicated template files under `review-master/references/`.

#### Scenario: Contract exists without bundled templates
- **WHEN** this change is implemented
- **THEN** the artifact contract is fully expressed in `review-master/SKILL.md`
- **AND** no new template files are required under `review-master/references/`
