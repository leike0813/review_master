## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for Stage 3 character-coverage threshold gating.

## 2. Coverage Metrics and Gate

- [x] 2.1 Add Stage 3 character-coverage metric computation (global + per-document, include-duplicate + non-duplicate diagnostic).
- [x] 2.2 Add hard/soft threshold constants and classification (`hard_fail` / `soft_warn` / `pass`).
- [x] 2.3 Add hard dependency gate when global coverage is below hard threshold.
- [x] 2.4 Add soft advisory output when global coverage is in the soft-warning range.

## 3. Rendering and Payload

- [x] 3.1 Extend review-comment-coverage render context with structured metrics.
- [x] 3.2 Update `review-comment-coverage.md.j2` to show metrics block and threshold status.
- [x] 3.3 Extend instruction payload with `coverage_review_metrics`.
- [x] 3.4 Update localization messages for metrics section and threshold status text.

## 4. Documentation Sync

- [x] 4.1 Update `review-master/SKILL.md` Stage 3 gate rules with character-level thresholds.
- [x] 4.2 Update Stage 3 references (`stage-3-comment-atomization.md`, `workflow-state-machine.md`, `sql-write-recipes.md`) and runtime digest.

## 5. Verification

- [x] 5.1 Add/extend contract tests for `<30%` hard fail, `[30%,50%)` soft advisory, and `>=50%` pass.
- [x] 5.2 Verify payload includes `coverage_review_metrics` and coverage view includes the metrics section.
- [x] 5.3 Run `pytest`.
- [x] 5.4 Run `mypy review-master/scripts tests`.
- [x] 5.5 Run `openspec validate add-stage3-character-coverage-threshold-gate --type change --strict`.
