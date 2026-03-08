schema: spec-driven
created: 2026-03-08

# Design: add-review-master-session-resume-contract

## Overview

本 change 为 `review-master` 增加一层专门面向长周期恢复的 resume contract。它不替代状态机，而是补足 `workflow_*` 之外的“恢复认知层”：

- `workflow_*`：阶段门禁与当前执行状态
- `resume_*`：长周期恢复、上下文压缩补偿、Skill 核心方法提醒

## Decisions

### First invocation and resumed invocation share one entry protocol

首次调用不再是特殊分支。新 workspace 也必须先运行 `gate-and-render`，先读取 `resume_packet` 和 `agent-resume.md`，只是此时得到的是 bootstrap resume。

### Resume data is DB-backed and rendered every time

恢复真源落在 SQLite 中，避免再引入脱离运行时数据库的第二真源。`agent-resume.md` 只是对恢复状态的只读渲染。

### Static skill digest is injected into every resume packet

仅靠动态状态不足以帮助 Agent 长期保持方法纪律，因此增加 `assets/runtime/skill-runtime-digest.md` 作为静态摘要资产，并在每次恢复时回显。

## Data Model

新增表：

- `resume_brief`
- `resume_open_loops`
- `resume_recent_decisions`
- `resume_must_not_forget`

其中 `resume_brief.resume_status` 固定枚举：

- `bootstrap`
- `active`
- `blocked`
- `ready_to_resume`
- `completed`

## Rendering Model

新增只读视图：

- `agent-resume.md`

`gate-and-render` 每次运行时都要：

1. 读取 resume 表
2. 读取静态 digest
3. 生成 `instruction_payload.resume_packet`
4. 渲染 `agent-resume.md`

## Validation Model

新增一致性约束：

- `resume_brief` 必须始终存在且只有一行
- 一旦 workflow 进入中后期，`resume_status` 不得仍为 `bootstrap`
- 中后期 workspace 不允许 resume 层持续空白
