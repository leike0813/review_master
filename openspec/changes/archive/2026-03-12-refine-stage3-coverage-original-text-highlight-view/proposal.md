## Why

The current Stage 3 coverage artifact is technically correct but hard for users to review quickly. It exposes machine wrappers like `[[covered ...]]` inside the body, which makes the view read like debug output rather than the original reviewer text. Users asked for a true reading view where covered spans are visually highlighted and uncovered spans remain plain.

## What Changes

- Refine `06-review-comment-coverage.md` into an original-text reading view with visual coverage highlighting.
- Keep Stage 3 coverage truth tables and gate logic unchanged.
- Replace inline machine wrapper markers in the body with red-highlighted covered spans.
- Add a coverage-mapping appendix table that lists `source_document_id`, `segment_order`, `thread_id`, `comment_id` list, and segment excerpt.
- Update localization, Stage 3 guidance, runtime digest, and tests to match the new artifact contract.

## Capabilities

### Modified Capabilities

- `review-master-stage-3-coverage-review`
- `review-master-template-driven-rendering`
- `review-master-markdown-artifact-contract`
- `review-master-markdown-artifact-templates`
- `review-master-user-checkpoints`
- `review-master-skill-instructions`

## Impact

- Affects Stage 3 coverage rendering and user-facing copy only; no database schema change.
- Preserves current Stage 3 confirmation gate before Stage 4.
- Requires test updates for coverage-view assertions.
