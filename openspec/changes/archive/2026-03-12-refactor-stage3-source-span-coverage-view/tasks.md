## 1. OpenSpec Artifacts

- [x] 1.1 Add proposal, design, tasks, and delta specs for source-span Stage 3 coverage rendering.

## 2. Runtime Model and Gate Validation

- [x] 2.1 Add `raw_thread_source_spans` to runtime schema requirements.
- [x] 2.2 Refactor Stage 3 gate validation to require source spans, validate span offsets/text, and block overlapping spans.
- [x] 2.3 Add legacy-coverage detection and block with rebuild guidance.

## 3. Coverage Rendering

- [x] 3.1 Refactor coverage context builder to reconstruct covered/uncovered runs from source spans.
- [x] 3.2 Render inline highlighted coverage with short thread tags and retain appendix mapping table.
- [x] 3.3 Keep Stage 3 confirmation gate behavior unchanged (`request_stage3_coverage_confirmation` before Stage 4).

## 4. Docs and Localization

- [x] 4.1 Update Stage 3 workflow docs and SQL recipe guidance for the source-span contract.
- [x] 4.2 Update localization copy and repair hints to reference `raw_thread_source_spans`.
- [x] 4.3 Sync `SKILL.md` and runtime digest with the new Stage 3 coverage model.

## 5. Verification

- [x] 5.1 Update coverage test helpers to seed source spans.
- [x] 5.2 Update/add gate-and-render contract tests for missing/invalid source spans and highlighted rendering tags.
- [x] 5.3 Run `mypy`.
- [x] 5.4 Run `openspec validate refactor-stage3-source-span-coverage-view --type change --strict`.
