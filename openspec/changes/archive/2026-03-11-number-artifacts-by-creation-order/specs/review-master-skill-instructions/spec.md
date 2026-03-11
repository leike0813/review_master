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
2. generate a response strategy, target changes, and required evidence
3. wait for user confirmation or correction
4. if evidence is missing, emit gap analysis and request materials
5. after evidence arrives, execute the manuscript change and generate the matching response section
6. mark that comment complete before moving on

#### Scenario: Unconfirmed comment cannot execute
- **WHEN** a strategy card exists for one atomic comment but the user has not confirmed it
- **THEN** `SKILL.md` must forbid execution for that comment

#### Scenario: Evidence gap prevents completion
- **WHEN** one atomic comment lacks required data, experiments, references, figures, or arguments
- **THEN** `SKILL.md` must require gap analysis and material request
- **AND** must forbid marking that comment complete

### Requirement: Final export gates in SKILL.md
`review-master/SKILL.md` MUST explicitly forbid final export when any of the following conditions remain true:

- unconfirmed comments still exist
- evidence-gap comments are unresolved
- response-letter sections and manuscript changes do not form a one-to-one correspondence

#### Scenario: Final export waits for all comment closure
- **WHEN** at least one atomic comment is still blocked or unconfirmed
- **THEN** `SKILL.md` must forbid exporting the final revised manuscript and final response letter
