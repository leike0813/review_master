schema: spec-driven
created: 2026-03-08

# Design: refine-review-master-stage-3-threaded-atomization

## Overview

本 change 只处理 Stage 3 的执行细化，不改运行时能力边界。目标是把现有“原始意见块与 canonical atomic item 建模”的高层描述，收敛成可以直接指导 Agent 的操作手册级说明。

## Decisions

### Stage 3 uses conservative deduplication

不同 reviewer 的重复意见只在以下条件同时满足时合并为同一个 canonical atomic item：

- 核心问题一致
- 期望动作一致
- 所需证据与修改方向无明显分叉

若诉求角度、修改范围或证据需求明显不同，则保留为不同 atomic item。

### Raw thread extraction stays distinct from atomic modeling

`raw_review_threads` 是原始 reviewer / editor 条目层，不做语义合并。  
`atomic_comments` 是内部执行真源层，允许在这一层跨 reviewer 合并。

### No new scripts for semantic work

本 change 不新增任何语义脚本。原始条目抽取、去重、归并、拆分和 canonical 建模仍由 Agent 大语言模型主导；脚本只在写库后承担 gate-and-render 职责。

## Documentation Model

`SKILL.md` 继续承担总纲入口，但会把 Stage 3 提升到“摘要版操作手册”：

- 说明 Stage 3 做什么
- 说明判断口径
- 说明何时阻断/提问/完成
- 显式指向 Stage 3 细化文档

Stage 3 的完整操作手册则落到：

- `references/stage-3-comment-atomization.md`

## Acceptance Model

实现后，阅读 Stage 3 文档的人应能独立回答：

- 如何抽取 `raw_review_threads`
- 如何判断一个 atomic item 是否成立
- 何时合并、何时不合并
- 何时必须问用户
- 何时可以进入 Stage 4
