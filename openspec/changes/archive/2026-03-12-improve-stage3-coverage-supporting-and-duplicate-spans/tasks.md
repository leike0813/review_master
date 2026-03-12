## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for role-aware Stage 3 coverage spans.

## 2. Runtime Schema and Compatibility

- [x] 2.1 Add `span_role` enum and column to `raw_thread_source_spans`.
- [x] 2.2 Add runtime compatibility migration to auto-add missing `span_role` column and backfill `primary`.
- [x] 2.3 Enforce new hard rule: every `thread_id` must contain at least one `primary` span.

## 3. Coverage Rendering and Gate Advisory

- [x] 3.1 Extend coverage context with `span_role` and role-level counts.
- [x] 3.2 Render `duplicate_filtered` spans in orange with `dup` thread tag while keeping `primary/supporting` in red.
- [x] 3.3 Extend appendix with `span_role` mapping column.
- [x] 3.4 Add non-blocking Stage 3 coverage advisories for likely heading-only coverage gaps.

## 4. Docs and Localization

- [x] 4.1 Update `SKILL.md`, Stage 3 reference docs, SQL recipes, workflow-state-machine, and runtime digest.
- [x] 4.2 Update `en/zh-CN` localization for duplicate-highlight legend and Stage 3 advisory messaging.

## 5. Verification

- [x] 5.1 Update test helpers for `span_role`.
- [x] 5.2 Update gate/render contract tests for orange duplicate highlighting, advisory output, and missing primary span blocking.
- [x] 5.3 Run `pytest`.
- [x] 5.4 Run `mypy`.
- [x] 5.5 Run `openspec validate improve-stage3-coverage-supporting-and-duplicate-spans --type change --strict`.
