# Design: rebuild-stage6-as-interactive-revision-audit-loop

## Overview

新的 Stage 6 不再尝试通过“生成位置级最终文本 -> 用户选一版 -> 组装 export patches -> 导出整稿”的方式替代真实改稿过程，而是把 Stage 6 建模成一个明确的修订轮次循环：

1. Stage 5 输出修订 backlog。
2. 用户与 Agent 在 `working_manuscript` 上直接修改。
3. 每轮修改通过正式提交入口写入审计记录。
4. response rows 由 revision logs 反向驱动生成。
5. 当计划动作闭环、response 覆盖闭环、且工作稿无未审计修改时，Stage 6 结束。

## Why capture must stay out of gate-and-render

`gate-and-render` 的现有价值在于：

- 读取数据库真源
- 做只读状态校验
- 重渲染视图
- 给出下一步动作

如果把 revision capture 合并进去，它就会变成一个带副作用的“读写混合入口”，带来三类问题：

1. 恢复协议不再稳定：恢复时的一次 gate 调用可能意外写库。
2. 状态机失去清晰边界：`recommended_next_action` 与“已经做过什么”混在一起。
3. 用户手动改稿的异常路径会难以追溯：是 gate 检测到了未审计修改，还是 gate 自己偷偷把它记掉了，会变得不可解释。

因此新设计明确拆分：

- `capture_revision_action.py`：只负责审计写库
- `commit_revision_round.py`：固定执行 `capture -> gate`
- `gate-and-render`：保持只读，只负责检测未审计修改并阻断

## Why Stage 1 needs source_snapshot and working_manuscript

旧 Stage 6 直接依赖外部输入稿件路径，会遇到两个不稳定源：

- 用户在 skill 执行中手工修改了原稿
- Agent 导出路径与原稿目录混杂，无法稳定追溯“改前/改后”的基线

因此 Stage 1 必须复制两份 workspace 内稿件副本：

- `source_snapshot`：只读基线
- `working_manuscript`：唯一允许修改的工作稿

此后所有 Stage 6 diff、审计、可选 `latexdiff` 都以这两份副本为基准，外部原稿不再参与 Stage 6 写作路径。

## Why Stage 6 becomes a revision-round model

论文修回的真实操作不是“给定位置，把一句话替换成另一句话”这么简单。一个 reviewer thread 可能引发：

- 多处改写
- 图表调整
- 数据补充
- response-only 解释

因此新的执行粒度不是 `action + location + variant_label`，而是“本轮完成了什么修改动作”。这允许一次 revision round 同时关联：

- 多个 `plan_action_id`
- 多个 `thread_id`
- 多个文件 diff

但仍然保持正式、可追溯、可渲染。

## Runtime Model

### Stage 5 derived backlog

新增：

- `revision_plan_actions`
- `revision_plan_dependencies`

它们承接已确认的策略卡和 execution items，形成 Stage 6 backlog。

### Stage 6 audit truth

新增：

- `revision_action_logs`
- `revision_action_log_plan_links`
- `revision_action_log_thread_links`
- `revision_action_log_file_diffs`
- `working_copy_file_state`

它们共同表达：

- 一轮修改做了什么
- 改了哪些文件
- 涉及哪些计划动作
- 支撑了哪些 reviewer threads
- 当前 working manuscript 是否还有未审计修改

### Response rows

`response_thread_rows` 保留，但语义改写为：

- 由 Stage 5 确认策略
- 加上 Stage 6 revision logs
- 再做 thread-level 聚合

而不是来自 selected copy variants 或 export patches。

## Artifact Replacement

### Retained but moved

- `03-style-profile.md`：前移到 Stage 2
- `10-supplement-intake-plan.md`：前移到 Stage 5

### New Stage 5 outputs

- `11-manuscript-revision-guide.md`
- `12-manuscript-execution-graph.md`

### New Stage 6 outputs

- `13-revision-action-log.md`
- `14-response-coverage-matrix.md`
- `15-response-letter-preview.md`
- `16-response-letter-preview.tex`
- `17-final-assembly-checklist.md`

### Retired from main Stage 6 flow

- `10-action-copy-variants.md`
- `11-response-letter-outline.md`
- `12-export-patch-plan.md`

## Gate Semantics

Stage 6 closes only when all three conditions hold:

1. All `revision_plan_actions` are `completed` or `dismissed`.
2. Every `thread_id` has a final `response_thread_rows` entry backed by either revision logs or `response_only_resolution`.
3. Every changed working manuscript file has been audited, meaning `current_sha256 == last_audited_sha256` and a `last_log_id` exists.

`latexdiff` is optional. If available, it may produce `latexdiff_manuscript`; if unavailable, the runtime emits an advisory but does not block Stage 6 completion.
