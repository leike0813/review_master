# Proposal: switch-review-master-to-sqlite-ssot-rendering

## Summary

将 `review-master` 的运行时架构从“Agent 直写 Markdown/YAML 工件”切换为“SQLite 唯一真源 + Markdown 只读渲染视图”。

## Why

当前模式下，Agent 需要同时维护多份 Markdown/YAML 工件，重复字段较多，validator 也必须承担厚重的跨工件一致性解析逻辑。随着工件和 playbook 复杂度提高，这种模式更容易出现漂移和维护负担。

SQLite 唯一真源模式可以把一致性前移到数据库约束层，让 validator 更聚焦于：

- 状态机门禁
- 依赖关系补充检查
- Markdown 视图重渲染
- 下一步动作指引

## What Changes

- runtime workspace 切换为 `review-master.db` + 渲染视图
- `workflow-state.yaml` 退役，状态并入数据库
- 阶段四运行时视图收缩为 `comment-workboard.md`
- `init_artifact_workspace.py` 改为初始化数据库
- `validate_artifact_consistency.py` 改为 DB-first validator/render
- `SKILL.md`、参考文档、playbook 和样例 workspace 全量迁移

## Impact

- 不保留旧 Markdown/YAML-only workspace 兼容
- Agent 正式写操作改为直接 SQL
- 用户继续通过 Markdown 视图理解当前状态
