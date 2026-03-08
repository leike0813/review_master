# Proposal: restructure-review-master-comment-mapping-model

## Why

当前 `review-master` 的 comment/workflow 模型缺少两层关键映射：

- 原始审稿意见块到 canonical atomic item 的映射
- 原始审稿意见块到最终 response letter 条目的映射

这会导致两个问题：

- 原子化之后难以稳定回映到 reviewer 的原始条目
- 多 reviewer 的重复意见难以在内部执行层真正合并

同时，原文位置、分析条目、修改动作位置等关系仍然带有单值假设，不足以支撑真实修回过程中的一对多、多对多场景。

## What Changes

本 change 重构 `review-master` 的 comment/workflow 数据模型：

- 新增 `raw_review_threads` 作为原始 reviewer 条目层
- 把 `atomic_comments` 明确为 canonical atomic item 层
- 新增 `raw_thread_atomic_links`、`atomic_comment_source_spans`、`response_thread_resolution_links`
- 把阶段四 workboard 从单表改为关系表驱动：
  - `atomic_comment_state`
  - `atomic_comment_target_locations`
  - `atomic_comment_analysis_links`
- 新增 thread-level 只读渲染视图：
  - `raw-review-thread-list.md`
  - `thread-to-atomic-mapping.md`
  - `response-letter-outline.md`
- 最终 response letter 的正式索引改为 `thread_id`

## Impact

这次改动会影响：

- 运行时 SQLite schema
- `gate-and-render` 核心脚本的门禁与渲染逻辑
- 只读 Markdown 视图集合
- `SKILL.md` 与 stage 3/4/5/6 指令
- SQL recipe 文档
- 后续 playbook 与样例资产的组织方式
