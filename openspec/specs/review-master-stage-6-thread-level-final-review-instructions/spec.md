# review-master-stage-6-thread-level-final-review-instructions Specification

## Purpose
TBD - created by archiving change refine-review-master-stage-6-final-review-and-export. Update Purpose after archive.
## Requirements
### Requirement: Stage 6 final review instructions are operations-manual grade

Stage 6 MUST define how the Agent moves from Stage 5 drafts to thread-level final rows, marked export, and final clean export.

#### Scenario: Stage 6 includes style profiling and copy-variant generation

- **Given** Stage 5 has completed and Stage 6 is allowed to begin
- **When** the Agent starts Stage 6
- **Then** the docs must require a global style profile for manuscript text
- **And** the docs must require a global style profile for response-letter text
- **And** the docs must require three wording variants per strategy action and per output target

#### Scenario: Final Response Letter stays indexed by original threads

- **Given** response wording is ready for assembly
- **When** the Agent produces final response rows
- **Then** the docs must require one final response row per `thread_id`
- **And** the docs must forbid direct final output by flat `comment_id` order
- **And** the docs must require thread-level aggregation of selected action wording

