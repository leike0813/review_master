## Why

Stage 3 already renders a readable coverage artifact, but it lacks a quantitative gate signal for extraction completeness. Operators can miss low-coverage extraction even when highlighting exists.

The workflow needs a deterministic, script-computed character-level metric that:

- measures full-source coverage across all Stage 3 source documents,
- includes `duplicate_filtered` spans in the main numerator,
- enforces a hard minimum threshold,
- and emits a non-blocking advisory zone before the preferred threshold.

## What Changes

- Add Stage 3 character-level coverage metrics (`full characters`, Unicode `len`, whitespace included) with global aggregation.
- Add dual thresholds:
  - hard: `30%` (blocking, `issues_found`)
  - soft: `50%` (non-blocking advisory)
- Expose structured `coverage_review_metrics` in `instruction_payload`.
- Extend `06-review-comment-coverage.md` with a metrics section:
  - global coverage including duplicates,
  - global non-duplicate diagnostic coverage,
  - per-document metrics,
  - threshold and gate status display.
- Keep existing Stage 3 pending-confirmation gate behavior unchanged.

## Capabilities

### Modified Capabilities

- `review-master-stage-3-coverage-review`
- `review-master-template-driven-rendering`
- `review-master-markdown-artifact-contract`
- `review-master-markdown-artifact-templates`
- `review-master-user-checkpoints`
- `review-master-skill-instructions`
- `review-master-validator-instruction-payload`
- `review-master-workflow-state-machine-rules`

## Impact

- Stage 3 gains deterministic quantitative coverage gating before Stage 4.
- Operators get consistent visibility of both hard-fail and soft-warning zones.
- Coverage metrics become available to both rendered artifacts and machine-readable instruction payloads.
