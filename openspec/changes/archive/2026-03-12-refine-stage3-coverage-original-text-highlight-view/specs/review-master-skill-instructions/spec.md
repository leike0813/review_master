## MODIFIED Requirements

### Requirement: SKILL.md must define the executable six-stage workflow

`review-master/SKILL.md` MUST replace the previous generic four-stage outline with a first-release six-stage executable workflow:

1. 输入接收与入口解析
2. 原稿结构理解与工作副本建立
3. 审稿意见拆解与原子化
4. 映射、优先级和全局修回工作板
5. 逐条意见闭环处理
6. 最终组装与导出

For each stage, `SKILL.md` MUST describe the purpose, inputs, outputs, and gate conditions for moving forward.

#### Scenario: Stage 3 instructions define highlighted coverage review semantics

- **WHEN** `SKILL.md` describes Stage 3 coverage confirmation
- **THEN** it MUST state that `06-review-comment-coverage.md` uses visually highlighted covered spans and default-style uncovered spans in a near-original-text body
- **AND** it MUST state that mapping verification is done through the artifact appendix table
- **AND** it MUST keep the rule that Stage 4 is blocked until user confirmation
