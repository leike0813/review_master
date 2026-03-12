# review-master-skill-instructions Specification

## Purpose
TBD - created by archiving change implement-review-master-skill-contract. Update Purpose after archive.
## Requirements
### Requirement: SKILL.md must define the executable six-stage workflow

Stage 3 instructions MUST define character-level coverage thresholds as part of coverage review semantics.

#### Scenario: Stage 3 instructions include hard/soft coverage thresholds

- **WHEN** `SKILL.md` describes Stage 3 coverage confirmation
- **THEN** it MUST define character-level coverage as duplicate-aware global metric
- **AND** it MUST define hard threshold `30%` as blocking
- **AND** it MUST define soft threshold `50%` as non-blocking advisory
- **AND** it MUST keep user confirmation as the gate to Stage 4

### Requirement: Per-comment closed-loop execution in SKILL.md

`review-master/SKILL.md` MUST directly describe the per-comment closed-loop cycle used in stage 5:

1. select one atomic review comment
2. generate a response strategy, target changes, required evidence, and supplement suggestions
3. wait for user confirmation or correction
4. only after confirmation, author Stage 5 manuscript and response drafts
5. if evidence is missing, emit gap analysis and request materials
6. mark that comment complete before moving on

#### Scenario: strategy changes reset execution readiness

- **WHEN** a previously confirmed strategy card is materially revised
- **THEN** `SKILL.md` must require confirmation to be reopened
- **AND** it must require old drafts to be discarded before new execution can continue

### Requirement: Final export gates in SKILL.md
`review-master/SKILL.md` MUST explicitly forbid final export when any of the following conditions remain true:

- unconfirmed comments still exist
- evidence-gap comments are unresolved
- response-letter sections and manuscript changes do not form a one-to-one correspondence

#### Scenario: Final export waits for all comment closure
- **WHEN** at least one atomic comment is still blocked or unconfirmed
- **THEN** `SKILL.md` must forbid exporting the final revised manuscript and final response letter

