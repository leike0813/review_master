## Context

Stage 5 现在把“草案已经形成”和“最终稿已经落入导出链”混在一起，导致：

- Agent 在 Stage 5 被要求完成 manuscript/response，但数据库没有正式落点。
- 用户看到 completion checklist 时，会误以为 Stage 5 已经完成最终改稿。
- gate 近似强制 one-by-one，即便只是某条 comment 的局部 blocker，也无法显式切去别的 comment。

此外，已有 workspace 不能被粗暴废弃；必须提供一个可续跑的迁移路径。

## Goals / Non-Goals

**Goals**

- 给 Stage 5 增加正式草案真源表。
- 把 completion 语义改成 draft completion，而不是 final authored completion。
- 允许用户在 Stage 5 显式切换 `active_comment_id`。
- 提供迁移脚本，确保已有 Stage 5 workspace 可升级、可继续推进。
- 强制把旧 workspace 的两个 draft completion 标记清零，避免旧状态冒充新真源。

**Non-Goals**

- 不改变 Stage 6 的 export patch、marked manuscript、clean manuscript 和 response-letter 输出契约。
- 不自动生成草案文本；迁移脚本只迁 schema/state，不替 Agent 写语义内容。
- 不把 comment-scoped blocker 自动做复杂语义分类；迁移脚本只保守搬运当前 active comment 的 blocker 文本。

## Decisions

### Decision 1: Stage 5 manuscript draft 采用 action/location 粒度

- 方案：
  - 新增 `strategy_action_manuscript_drafts(comment_id, action_order, location_order, draft_text, rationale)`
- 理由：
  - Stage 6 的最终文案选择本来就基于 action/location 粒度，Stage 5 的 manuscript draft 若过粗，后续无法自然接到 Stage 6。
- 备选：
  - 仅按 `comment_id` 存 manuscript 草案：无法表达同一 comment 下多个动作/位置的对应关系。

### Decision 2: response draft 采用 comment 粒度

- 方案：
  - 新增 `comment_response_drafts(comment_id, draft_text, rationale)`
- 理由：
  - Stage 5 的回复草案仍以 atomic item 为单位，不需要提前展开成 thread-level row。
- 备选：
  - 提前按 `thread_id` 写最终 row：会越过 Stage 6 的 thread-level 组装职责。

### Decision 3: comment blocker 与 workflow_global_blockers 分层

- 方案：
  - `comment_blockers` 只阻断当前 comment 的完成
  - `workflow_global_blockers` 只阻断整个阶段
- 理由：
  - 这样才能支持“当前 comment 被卡住，但用户可以显式切去别的 comment”。
- 备选：
  - 继续把所有 blocker 都塞进 `workflow_global_blockers`：会维持旧的伪 one-by-one 锁死体验。

### Decision 4: 迁移时强制重置所有 draft completion 字段

- 方案：
  - 迁移后，所有 comment 的 `manuscript_draft_done` 与 `response_draft_done` 全部设为 `no`
- 理由：
  - 旧 schema 没有正式草案真源；即便旧状态写成 yes，也不能视作新模型下的真实完成。
- 备选：
  - 保留旧 yes/no：会导致 gate 与视图相信并不存在的草案真源。

## Migration Plan

1. 修改 runtime schema 与 render/gate 逻辑。
2. 新增 `artifacts/migrate_workspace_stage5_draft_model.py`。
3. 用迁移脚本升级现有 playbook example workspace。
4. 重新运行 gate-and-render，刷新 workspace 视图与 gate JSON 快照。
5. 更新测试与回归样例。

## Risks / Trade-offs

- [Risk] Stage 5 规则更多，gate 输出更复杂  
  Mitigation: 让 strategy card 直接展示 manuscript drafts、response draft 和 comment blockers。

- [Risk] 迁移后样例的两个 completion 标记都会回到 `no`  
  Mitigation: 只针对 legacy workspace；已按新模型重新落稿的 example 会在重渲染后的最终态重新变回 `yes`。

- [Risk] 用户可能把 `set_active_comment` 理解为允许静默切换  
  Mitigation: 文档与 gate 都明确要求显式写库再重跑 gate-and-render，且不得清空已有状态。
