## ADDED Requirements

### Requirement: First helper scripts are read-only
The first helper scripts for `review-master` SHALL be read-only helpers. They MAY read manuscript paths or filled Markdown artifacts, but they MUST NOT modify any manuscript source, artifact template, or user directory content.

#### Scenario: Helper script processes project inputs
- **WHEN** a helper script is invoked with valid file or directory paths
- **THEN** it reads those inputs and emits a JSON result
- **AND** it does not rewrite any source file or artifact in place

### Requirement: Helper scripts stay within deterministic support work
The first helper scripts MUST support deterministic entry assistance or artifact validation only. They MUST NOT generate atomic review items, final academic strategy decisions, final manuscript rewrites, or final response-letter prose on behalf of the user.

#### Scenario: Script output remains advisory
- **WHEN** a helper script returns candidate entries or validation findings
- **THEN** the workflow still requires user confirmation and agent judgment before downstream decisions are locked

### Requirement: Missing helper scripts do not block the skill
`review-master/SKILL.md` SHALL define a manual fallback path when a helper script is missing or fails.

#### Scenario: Helper script unavailable
- **WHEN** a helper script cannot be used
- **THEN** the workflow falls back to manual analysis instead of aborting the skill
