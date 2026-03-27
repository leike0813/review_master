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

### Requirement: Skill instructions must keep runtime and docs in sync

`review-master/SKILL.md` MUST keep the numbered workspace contract and the Stage 5 execution-item terminology aligned with runtime implementation and runtime digest documentation.

#### Scenario: skill and digest stay aligned

- **WHEN** `review-master/SKILL.md` is updated for artifact order or Stage 5 execution terminology
- **THEN** `review-master/assets/runtime/skill-runtime-digest.md` MUST be updated in the same change
- **AND** the skill instructions MUST present `07-atomic-comment-workboard.md` as the live board
- **AND** they MUST use `08-supplement-suggestion-plan.md` as the canonical numbered filename
- **AND** they MUST use "manuscript execution items / 稿件执行项" rather than the old narrow manuscript-draft wording

### Requirement: Final export gates in SKILL.md
`review-master/SKILL.md` MUST explicitly forbid final export when any of the following conditions remain true:

- unconfirmed comments still exist
- evidence-gap comments are unresolved
- response-letter sections and manuscript changes do not form a one-to-one correspondence

#### Scenario: Final export waits for all comment closure
- **WHEN** at least one atomic comment is still blocked or unconfirmed
- **THEN** `SKILL.md` must forbid exporting the final revised manuscript and final response letter

