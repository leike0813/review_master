# review-master-skill-instructions Specification

## Purpose
TBD - created by archiving change implement-review-master-skill-contract. Update Purpose after archive.
## Requirements
### Requirement: SKILL.md must define the executable six-stage workflow
`review-master/SKILL.md` MUST replace the previous generic four-stage outline with a first-release six-stage executable workflow:

1. 输入接收与入口解析
2. 原稿结构理解与工作副本建立
3. 审稿意见拆解与原子化
4. 映射、优先级和全局修回工作板
5. 逐条意见闭环处理
6. 最终组装与导出

For each stage, `SKILL.md` MUST describe the purpose, inputs, outputs, and gate conditions for moving forward.

#### Scenario: Stage 4 remains mandatory
- **WHEN** the workflow has completed early analysis
- **THEN** `SKILL.md` must still require stage 4 completion before any final manuscript rewriting or final response-letter assembly can begin

#### Scenario: Stage instructions cite numbered artifacts
- **WHEN** `SKILL.md` tells the user which runtime artifacts to inspect during a stage
- **THEN** it must cite the numbered filenames for all non-strategy-card artifacts
- **AND** it must keep `response-strategy-cards/{comment_id}.md` as the strategy-card reference form

### Requirement: Per-comment closed-loop execution in SKILL.md

`review-master/SKILL.md` MUST directly describe the per-comment closed-loop cycle used in stage 5:

1. select one atomic review comment
2. generate a response strategy, target changes, required evidence, and supplement suggestions
3. wait for user confirmation or correction
4. only after confirmation, author Stage 5 manuscript and response drafts
5. if evidence is missing, emit gap analysis and request materials
6. mark that comment complete before moving on

#### Scenario: strategy changes reset execution readiness

- **WHEN** a previously confirmed strategy card is materially revised
- **THEN** `SKILL.md` must require confirmation to be reopened
- **AND** it must require old drafts to be discarded before new execution can continue

### Requirement: Final export gates in SKILL.md
`review-master/SKILL.md` MUST explicitly forbid final export when any of the following conditions remain true:

- unconfirmed comments still exist
- evidence-gap comments are unresolved
- response-letter sections and manuscript changes do not form a one-to-one correspondence

#### Scenario: Final export waits for all comment closure
- **WHEN** at least one atomic comment is still blocked or unconfirmed
- **THEN** `SKILL.md` must forbid exporting the final revised manuscript and final response letter

