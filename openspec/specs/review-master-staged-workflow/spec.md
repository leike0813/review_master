# review-master-staged-workflow Specification

## Purpose
TBD - created by archiving change define-review-master-staged-workflow. Update Purpose after archive.
## Requirements
### Requirement: Six-stage workflow
The first release of `review-master` SHALL follow a six-stage workflow:

1. Input intake and entry resolution
2. Manuscript structure understanding and working-copy setup
3. Review comment decomposition into atomic items
4. Mapping, prioritization, and global revision board construction
5. Per-comment closed-loop execution
6. Final assembly and export

Each stage MUST define its required inputs, expected outputs, and gate conditions for moving forward.

#### Scenario: Workflow reaches global planning before execution
- **WHEN** the workflow starts with valid required inputs
- **THEN** it must complete stages 1 through 4 before any final manuscript rewrite or final response letter assembly is allowed

### Requirement: Explicit intermediate artifacts
The workflow MUST materialize its analysis outputs as explicit intermediate artifacts rather than leaving them only in transient conversation state.

At minimum, the workflow MUST produce:

- a manuscript structure summary
- an atomic review comment list
- a comment-to-manuscript mapping table
- a priority and dependency revision board
- per-comment response strategy cards
- a final assembly checklist

#### Scenario: Mapping stage produces a work board
- **WHEN** stage 4 is completed
- **THEN** the workflow has already produced the atomic review comment list, the mapping table, and the priority/dependency revision board

### Requirement: Per-comment closed-loop cycle
Stage 5 MUST process review comments one atomic item at a time using the following fixed loop:

1. select one atomic comment
2. generate a response strategy, target manuscript changes, and required evidence for that comment
3. obtain user confirmation or correction
4. if evidence is missing, pause that comment and request materials
5. after materials are provided, execute the manuscript change and generate the corresponding response section
6. mark the comment complete before advancing to the next comment

#### Scenario: Evidence gap pauses one comment without forcing final export
- **WHEN** one atomic comment requires new data, experiments, or arguments that are not available in the current inputs
- **THEN** that comment must pause at the evidence-request step
- **AND** it must not be marked complete

#### Scenario: Confirmed comment advances to execution
- **WHEN** the user confirms the strategy for one atomic comment and required evidence is available
- **THEN** the workflow may execute the manuscript change and generate the matching response section for that comment

### Requirement: Final export gate
The workflow MUST NOT enter final assembly and export unless all export gates are satisfied.

The export gates are:

- no unconfirmed comments remain
- no evidence-gap comments are incorrectly marked complete
- the response letter sections and manuscript changes form a one-to-one correspondence

#### Scenario: Final export blocked by unfinished comment state
- **WHEN** at least one comment remains unconfirmed or blocked by missing evidence
- **THEN** stage 6 must not produce the final revised manuscript and final response letter

#### Scenario: Final export allowed after all comments close
- **WHEN** every atomic comment has been confirmed, executed or validly resolved, and linked to a manuscript change and response section
- **THEN** stage 6 may assemble and export the final revised manuscript and Markdown response letter

