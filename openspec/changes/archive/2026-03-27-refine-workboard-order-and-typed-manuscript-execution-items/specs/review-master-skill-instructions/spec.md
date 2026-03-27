## MODIFIED Requirements

### Requirement: Skill instructions must keep runtime and docs in sync

`review-master/SKILL.md` MUST keep the numbered workspace contract and the Stage 5 execution-item terminology aligned with runtime implementation and runtime digest documentation.

#### Scenario: skill and digest stay aligned

- **WHEN** `review-master/SKILL.md` is updated for artifact order or Stage 5 execution terminology
- **THEN** `review-master/assets/runtime/skill-runtime-digest.md` MUST be updated in the same change
- **AND** the skill instructions MUST present `07-atomic-comment-workboard.md` as the live board
- **AND** they MUST use `08-supplement-suggestion-plan.md` as the canonical numbered filename
- **AND** they MUST use "manuscript execution items / 稿件执行项" rather than the old narrow manuscript-draft wording
