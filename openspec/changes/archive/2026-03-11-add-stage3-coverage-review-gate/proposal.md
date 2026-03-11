## Why

Stage 3 currently stops after raw-thread extraction, canonical atomization, and mapping. The user can inspect the thread list and mapping table, but there is no dedicated artifact that shows which parts of the original review-comments source were actually covered by the Stage 3 extraction. That makes it too easy to miss reviewer text, silently over-merge, or move to Stage 4 before the user has verified extraction completeness.

## What Changes

- Add a new Stage 3 read-only artifact: `review-comment-coverage.md`
- Add Stage 3 coverage truth tables:
  - `review_comment_source_documents`
  - `review_comment_coverage_segments`
  - `review_comment_coverage_segment_comment_links`
- Require Stage 3 to enter a user-confirmation gate after coverage rendering and before Stage 4
- Add a new Stage 3 clear-confirmation recipe:
  - `recipe_stage3_clear_coverage_confirmation`
- Update gate/render, docs, and tests so Stage 3 coverage review becomes part of the executable contract

## Capabilities

### New Capabilities

- `review-master-stage-3-coverage-review`

### Modified Capabilities

- `review-master-sqlite-runtime`
- `review-master-template-driven-rendering`
- `review-master-validator-instruction-payload`
- `review-master-stage-3-canonical-atomization-instructions`
- `review-master-skill-instructions`

## Impact

- Affects runtime schema, render manifest, template set, Stage 3 gate logic, and localization messages
- Affects `SKILL.md`, runtime digest, Stage 3 instructions, SQL recipes, and workflow state-machine docs
- Adds new OpenSpec artifacts and new test coverage for Stage 3 confirmation and coverage validation
