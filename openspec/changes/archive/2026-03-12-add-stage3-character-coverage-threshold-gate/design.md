## Overview

This change adds script-computed Stage 3 character-coverage metrics and dual-threshold gating while preserving existing Stage 3 confirmation flow.

- Metric base: full Unicode character count (`len(text)`), including whitespace.
- Main numerator: covered characters including `duplicate_filtered`.
- Diagnostic numerator: covered characters excluding `duplicate_filtered`.
- Scope: global aggregation across all `review_comment_source_documents`, plus per-document breakdown.

## Metric Model

## Inputs

- `review_comment_source_documents(original_text)`
- `raw_thread_source_spans(source_document_id, span_role, start_offset, end_offset)`

## Coverage Counting

- For each source document:
  - Clamp span ranges into `[0, len(original_text)]`.
  - Build interval union for:
    - including duplicates: all span roles
    - non-duplicate diagnostic: `primary` + `supporting`
  - Compute covered chars from merged intervals.
- Global metrics are sums of per-document totals.

## Threshold Classification

- `STAGE3_COVERAGE_HARD_THRESHOLD = 30.0`
- `STAGE3_COVERAGE_SOFT_THRESHOLD = 50.0`
- Gate status:
  - `< hard`: `hard_fail`
  - `>= hard` and `< soft`: `soft_warn`
  - `>= soft`: `pass`
  - no source text: `not_applicable`

## Gate Behavior

- Stage 3 dependency validation adds hard error `coverage_below_hard_threshold` when global coverage is below hard threshold.
- Soft zone writes advisory message to `coverage_review_advisories` and does not block progression by itself.
- Existing pending-confirmation gate remains unchanged.

## Rendering and Payload

- `build_review_comment_coverage_context` adds:
  - `coverage_metrics` (thresholds/global/per_document/gate_status)
- `06-review-comment-coverage.md` adds a character-metrics section.
- `instruction_payload` adds `coverage_review_metrics` with stable structure:
  - `metric_type`
  - `scope`
  - `thresholds`
  - `global`
  - `per_document`
  - `gate_status`

## Compatibility

- No schema changes.
- Existing workspaces only need rerender/revalidate; metric reads existing Stage 3 truth.
