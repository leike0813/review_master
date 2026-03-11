## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for Stage 3 coverage review and confirmation gating.

## 2. Runtime Schema and Rendering

- [x] 2.1 Add Stage 3 coverage truth tables to the runtime schema.
- [x] 2.2 Add `review-comment-coverage.md` to the render manifest and template set.
- [x] 2.3 Extend workspace render helpers to build the new coverage artifact from DB truth.

## 3. Gate and Confirmation Flow

- [x] 3.1 Make Stage 3 write coverage truth and enter a blocked confirmation state.
- [x] 3.2 Add `request_stage3_coverage_confirmation` and Stage 3 blocked-action handling.
- [x] 3.3 Add validation rules for missing source documents, missing covered segments, and covered segments without comment links.

## 4. Docs and Tests

- [x] 4.1 Update `SKILL.md`, runtime digest, Stage 3 guide, SQL recipes, and workflow-state-machine docs.
- [x] 4.2 Add tests for Stage 3 coverage rendering, Stage 3 confirmation gating, confirmation clearing, uncovered-text visibility, and invalid coverage truth blocking.
