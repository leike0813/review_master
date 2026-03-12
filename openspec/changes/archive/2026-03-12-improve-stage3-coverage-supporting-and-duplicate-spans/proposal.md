## Why

The current Stage 3 coverage view can still miss user trust expectations in two cases:

- Only heading-like primary spans are highlighted while nearby substantive paragraph body remains uncovered.
- Repeated substantive comments are deduplicated in summaries and become visually invisible in repeated source locations.

Users need a coverage artifact that keeps deduplication in canonical summaries but still shows all substantive source occurrences.

## What Changes

- Extend `raw_thread_source_spans` with `span_role` (`primary`, `supporting`, `duplicate_filtered`).
- Keep schema compatibility by auto-adding the new column for legacy workspaces and backfilling `primary`.
- Keep Stage 3 gate structure unchanged, but add non-blocking advisory diagnostics for likely "title-only coverage" gaps.
- Render `06-review-comment-coverage.md` with role-aware highlighting:
  - `primary` / `supporting`: red
  - `duplicate_filtered`: orange + `dup` tag
- Extend the coverage appendix to include `span_role`.

## Capabilities

### Modified Capabilities

- `review-master-threaded-comment-model`
- `review-master-stage-3-coverage-review`
- `review-master-template-driven-rendering`
- `review-master-markdown-artifact-contract`
- `review-master-markdown-artifact-templates`
- `review-master-user-checkpoints`
- `review-master-skill-instructions`

## Impact

- Runtime schema and gate validation now enforce role-aware Stage 3 source spans.
- Coverage rendering now exposes duplicate occurrences without polluting canonical summaries.
- Stage 3 keeps hard gate behavior while surfacing weak coverage advisories for operator review.
