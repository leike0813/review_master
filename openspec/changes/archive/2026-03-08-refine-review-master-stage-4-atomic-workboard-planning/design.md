schema: spec-driven
created: 2026-03-08

# Design: refine-review-master-stage-4-atomic-workboard-planning

## Overview

本 change 只处理 Stage 4 的执行细化，不改运行时能力边界。目标是把现有“atomic workboard 规划”的高层描述，收敛成可以直接指导 Agent 的操作手册级说明。

## Decisions

### Stage 4 uses a mandatory confirmation gate by default

Stage 4 的默认主路径不是“建完 workboard 立即进入 Stage 5”，而是：

1. 建立 atomic workboard
2. 写入待确认事项
3. 运行 gate-and-render
4. 展示给用户
5. 用户确认后才进入 Stage 5

### Stage 4 allows provisional planning, but not empty planning

`target_location` 和部分分析字段可以先写到章节级或 `TBD`，但以下核心规划字段不得为空：

- `priority`
- `evidence_gap`
- `next_action`

如果 provisional 信息已经多到无法支撑 Stage 5，则 Stage 4 不得视为完成。

### No new scripts for semantic work

本 change 不新增任何语义脚本。priority、dependency、evidence gap、provisional location 和 user confirmation need 的判断仍由 Agent 大语言模型主导；脚本只在写库后承担 gate-and-render 职责。

## Documentation Model

`SKILL.md` 继续承担总纲入口，但会把 Stage 4 提升到“摘要版操作手册”：

- 说明 Stage 4 做什么
- 说明默认确认门禁
- 说明哪些字段必须写实、哪些可 provisional
- 显式指向 Stage 4 细化文档

Stage 4 的完整操作手册则落到：

- `references/stage-4-workboard-planning.md`

## Acceptance Model

实现后，阅读 Stage 4 文档的人应能独立回答：

- 如何建立 atomic workboard
- 哪些字段必须写实
- 哪些字段可以 provisional
- 何时必须向用户确认
- 何时可以进入 Stage 5
