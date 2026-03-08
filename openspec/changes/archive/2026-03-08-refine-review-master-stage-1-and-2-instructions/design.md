schema: spec-driven
created: 2026-03-08

# Design: refine-review-master-stage-1-and-2-instructions

## Overview

本 change 只处理前两阶段的执行细化，不改运行时能力边界。目标是把现有总纲收敛成可以直接指导 Agent 的操作手册级说明，同时保持 `SKILL.md` 仍是总入口，而阶段细节下沉到 `references/`。

## Decisions

### Stage 1 and Stage 2 become handbook-level guidance

这两阶段将明确：

- 进入条件
- 必读材料
- 固定分析顺序
- 要更新的数据库表
- 必须向用户追问的情形
- 禁止动作
- 完成定义

但不会细化到逐条 SQL 语句的 SOP 级别。

### Supporting docs are updated only where Stage 1 and Stage 2 depend on them

除 `SKILL.md` 和两个阶段文档外，只更新直接支撑 Stage 1/2 的文档：

- `sql-write-recipes.md`
- `workflow-state-machine.md`
- `helper-scripts.md`
- 一份 happy-path playbook

Stage 3 到 Stage 6 的正文暂不扩写。

### No script or schema changes

本 change 仅修正文档层的执行契约，不改变：

- `detect_main_tex.py`
- `init_artifact_workspace.py`
- `gate_and_render_workspace.py`
- SQLite schema

## Documentation Model

`SKILL.md` 继续承担总纲入口，但会把 Stage 1 和 Stage 2 提升到“摘要版操作手册”：

- 说明每阶段做什么
- 说明哪些文件和脚本要读
- 说明何时阻断/提问/完成
- 显式指向对应阶段文档

阶段级细则则落到：

- `references/stage-1-entry-and-bootstrap.md`
- `references/stage-2-manuscript-analysis.md`

## Acceptance Model

实现后，任何阅读 Stage 1/2 文档的人都应能独立回答：

- 什么时候进入这一阶段
- 先读什么、再做什么
- 需要写哪些表
- 什么时候必须问用户
- 什么时候不能推进
- 什么时候算完成并可进入下一阶段
