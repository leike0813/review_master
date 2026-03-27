# review-master Transformer Three-Review Major Revision Playbook

## Purpose

这份 playbook 是仓库中最完整的复杂样例，用来演示当前合同下的多 reviewer、多轮补材和 Stage 6 审计闭环。

样例特征：

- 多文件 LaTeX 工程
- 3 位 reviewer
- 15 条原始 reviewer threads
- 多轮 Stage 5 supplement intake / landing
- 最终收束到 `stage_6_completed`

## Example Assets

- 输入：
  - `playbooks/examples/transformer-three-review-major-revision/inputs/manuscript/`
  - `playbooks/examples/transformer-three-review-major-revision/inputs/review-comments.md`
- 补材：
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-1/`
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-2/`
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-3/`
- 参考材料：
  - `playbooks/examples/transformer-three-review-major-revision/reference/accepted-paper.md`
  - `playbooks/examples/transformer-three-review-major-revision/reference/degradation-traceability.md`
- workspace：
  - `playbooks/examples/transformer-three-review-major-revision/workspace/`
- 最终产物：
  - `playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.md`
  - `playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.tex`
- gate 快照：
  - `playbooks/examples/transformer-three-review-major-revision/gate-and-render-output/`

## Current Workflow Focus

这份样例当前强调的是：

- Stage 3 的整文覆盖审阅
- Stage 4 的 atomic workboard 规划
- Stage 5 的策略卡确认、typed manuscript execution items、supplement suggestion/intake
- Stage 6 的 `working_manuscript + revision_action_logs + response_thread_rows`

## Stage 6 Closure Criteria

最终闭环不是靠 patch set 导出，而是靠以下条件同时满足：

- `revision_plan_actions` 已全部 `completed` 或 `dismissed`
- `response_thread_rows` 覆盖全部原始 `thread_id`
- 每个有修改的 `working_manuscript` 文件都已通过 revision audit 落库
- `15-response-letter-preview.md` 与 `16-response-letter-preview.tex` 可完整覆盖 reviewer threads
- `17-final-assembly-checklist.md` 显式显示闭环状态
