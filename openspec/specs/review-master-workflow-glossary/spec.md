# review-master-workflow-glossary Specification

## Purpose
TBD - created by archiving change normalize-review-master-workflow-cross-cutting-consistency. Update Purpose after archive.
## Requirements
### Requirement: workflow glossary is the single naming source

`review-master` MUST define one glossary document that fixes the formal names for stages, scripts, runtime truth objects, rendered views, final exports, and action ids.

#### Scenario: glossary locks the official names

- **Given** the skill already spans multiple docs, playbooks, and fixtures
- **When** a reader needs to know the official term for a stage, script, output, or action
- **Then** `review-master/references/workflow-glossary.md` must provide that official term
- **And** other docs must align with it rather than inventing aliases

