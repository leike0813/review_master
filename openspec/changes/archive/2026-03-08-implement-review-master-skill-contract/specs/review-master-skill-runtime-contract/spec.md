## ADDED Requirements

### Requirement: Skill runtime input slots
`review-master/SKILL.md` MUST define the first-release skill runtime inputs with the following slots:

- required `manuscript_source`
- required `review_comments_source`
- optional `editor_letter_source`
- optional `user_notes`

The required inputs MUST be sufficient to start the workflow. Missing optional inputs MUST NOT block the workflow from starting.

#### Scenario: Required inputs are enough to start
- **WHEN** the user provides `manuscript_source` and `review_comments_source`
- **AND** does not provide `editor_letter_source` or `user_notes`
- **THEN** the workflow may start normally

#### Scenario: Optional editor letter enriches but does not block
- **WHEN** the user provides `editor_letter_source`
- **THEN** the workflow may use it to absorb editor-level requirements
- **AND** the absence of `editor_letter_source` must not block startup

#### Scenario: Optional user notes enrich but do not block
- **WHEN** the user provides `user_notes`
- **THEN** the workflow may use them as user preference and context input
- **AND** the absence of `user_notes` must not block startup

### Requirement: Input shape restrictions
`review-master/SKILL.md` MUST define the accepted first-release shapes of each input slot:

- `manuscript_source`: a single main `.tex` file path or a LaTeX project directory path
- `review_comments_source`: a Markdown or plain text file path
- `editor_letter_source`: an optional file path
- `user_notes`: optional free-form text

#### Scenario: User notes remain free text
- **WHEN** the user provides strategy explanations, concerns, or constraints inline
- **THEN** `SKILL.md` treats `user_notes` as valid free-form text input rather than requiring a file path

### Requirement: Final output slots
`review-master/SKILL.md` MUST define the first-release final outputs as:

- `revised_manuscript`
- `response_letter_path`

The response letter output MUST be Markdown. The manuscript output shape MUST follow the manuscript input shape.

#### Scenario: Single-file manuscript output
- **WHEN** the manuscript input is a single main `.tex` file
- **THEN** `revised_manuscript` is a revised main `.tex` file
- **AND** `response_letter_path` points to a Markdown response letter

#### Scenario: Project-directory manuscript output
- **WHEN** the manuscript input is a LaTeX project directory
- **THEN** `revised_manuscript` is a revised project directory
- **AND** `response_letter_path` points to a Markdown response letter
