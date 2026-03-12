## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for Stage 3 original-text highlight coverage view.

## 2. Runtime Coverage Rendering

- [x] 2.1 Extend Stage 3 coverage render context with HTML-safe segment text and appendix mapping rows.
- [x] 2.2 Rewrite `review-comment-coverage.md.j2` to render red-highlighted covered spans and default uncovered spans.
- [x] 2.3 Add a coverage-mapping appendix table for covered segments.

## 3. Documentation and Localization

- [x] 3.1 Update `en.json` and `zh-CN.json` coverage legend/copy text from wrapper syntax to highlight + appendix semantics.
- [x] 3.2 Sync `SKILL.md`, Stage 3 reference guidance, and runtime digest wording with the new coverage artifact behavior.

## 4. Verification

- [x] 4.1 Update Stage 3 coverage assertions in `tests/test_gate_and_render_contract.py`.
- [x] 4.2 Run `pytest` regression checks.
- [x] 4.3 Run `mypy` checks for scripts/tests.
- [x] 4.4 Run `openspec validate refine-stage3-coverage-original-text-highlight-view --type change --strict`.
