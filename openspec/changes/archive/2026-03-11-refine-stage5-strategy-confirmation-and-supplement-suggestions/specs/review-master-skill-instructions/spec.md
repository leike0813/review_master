## MODIFIED Requirements

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
