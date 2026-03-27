# Transformer Three-Review Major Revision Example

这是仓库里最完整的 `review-master` 样例包，用来演示当前合同下的复杂 major revision 流程。

包含内容：

- `reference/`
  - 终稿参考快照与劣化追踪说明
- `inputs/manuscript/`
  - 多文件 LaTeX 初稿
- `inputs/review-comments.md`
  - 3 位 reviewer、15 条原始评论
- `user-supplements/round-1/`
- `user-supplements/round-2/`
- `user-supplements/round-3/`
- `workspace/`
  - 当前 `01-17` 工件序列
  - `response-strategy-cards/`
  - `manuscript-copies/source-snapshot/`
  - `manuscript-copies/working-manuscript/`
- `outputs/`
  - `response-letter.md`
  - `response-letter.tex`
- `gate-and-render-output/`
  - 保留 Stage 1-6 的代表性 gate 快照

当前 Stage 6 语义：

- 用户与 Agent 直接在 `working_manuscript` 上逐轮改稿
- 每轮修改通过 `commit_revision_round.py` 提交
- `revision_action_logs`、`response_thread_action_log_links` 与 `response_thread_rows` 构成最终闭环真源
