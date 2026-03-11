## Why

当前 Stage 5 存在两个结构性断层：

- `comment_completion_status` 要求 `manuscript_change_done` 和 `response_section_done` 为完成，但 runtime 中没有对应的正式草案真源表，导致“要求存在、真源缺位”。
- `active_comment_id` 采用近似 one-by-one 的推进模型，导致当前 comment 只要有局部 blocker，就会把整个 Stage 5 的操作体验锁死，用户无法显式切换焦点。

同时，仓库里已经存在推进到 Stage 5 的 workspace。若直接切换 schema 而不给迁移路径，这些 workspace 会失去续跑能力。

## What Changes

- 将 Stage 5 的完成语义改成草案语义：
  - `manuscript_change_done` -> `manuscript_draft_done`
  - `response_section_done` -> `response_draft_done`
- 新增 Stage 5 草案真源表：
  - `strategy_action_manuscript_drafts`
  - `comment_response_drafts`
  - `comment_blockers`
- 更新 gate-and-render：
  - Stage 5 允许显式 `set_active_comment`
  - comment-scoped blocker 不再禁止切换到其他 comment
  - 只有真正的 `workflow_global_blockers` 才阻断整个 Stage 5
- 新增通用迁移脚本：
  - `artifacts/migrate_workspace_stage5_draft_model.py`
  - 用于把旧版 Stage 5 workspace 升级到新 schema，并强制把所有 comment 的两个 draft completion 字段重置为 `no`
- 同步更新文档、playbook fixture、workspace render 输出和测试

## Capabilities

### Modified Capabilities

- `review-master-sqlite-runtime`
- `review-master-stage-5-strategy-card-instructions`
- `review-master-stage-5-confirmation-blocker-completion-instructions`
- `review-master-workflow-state-machine-rules`
- `review-master-sql-write-recipes`
- `review-master-markdown-artifact-contract`
- `review-master-artifact-authoring-rules`
- `review-master-workflow-glossary`

### New Capabilities

- `review-master-stage-5-workspace-migration`

## Impact

- 影响 runtime schema、gate、workspace render、Stage 5 handbook、SQL recipes、workflow glossary、SKILL/runtime digest。
- 影响所有已提交的 Stage 5/Stage 6 playbook example workspace，因为它们需要迁移到新 schema 并重渲染。
- 不改变 Stage 6 导出脚本的导出契约。
