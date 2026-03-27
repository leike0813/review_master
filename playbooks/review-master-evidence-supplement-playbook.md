# review-master Evidence Supplement Playbook

## Purpose

这份 playbook 展示多 reviewer、多 atomic item、包含 evidence gap 与 supplement intake/landing 的成功路径。

重点不是旧式导出，而是：

- Stage 4 的 workboard 规划确认
- Stage 5 的策略卡确认、补材建议、补材接收与落地
- Stage 6 的 revision audit 与 response coverage 闭环

## Example Assets

- 输入：
  - `playbooks/examples/evidence-supplement-multi-review/inputs/manuscript/`
  - `playbooks/examples/evidence-supplement-multi-review/inputs/review-comments.md`
- 用户补材：
  - `playbooks/examples/evidence-supplement-multi-review/user-supplements/`
- workspace：
  - `playbooks/examples/evidence-supplement-multi-review/workspace/`
- 最终产物：
  - `playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.md`
  - `playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.tex`
- gate 快照：
  - `playbooks/examples/evidence-supplement-multi-review/gate-and-render-output/`

## What To Inspect

- Stage 3：
  - `07-review-comment-coverage.md`
- Stage 4：
  - `08-atomic-comment-workboard.md`
- Stage 5：
  - `09-supplement-suggestion-plan.md`
  - `10-supplement-intake-plan.md`
  - `response-strategy-cards/{comment_id}.md`
- Stage 6：
  - `11-manuscript-revision-guide.md`
  - `12-manuscript-execution-graph.md`
  - `13-revision-action-log.md`
  - `14-response-coverage-matrix.md`
  - `15-response-letter-preview.md`
  - `16-response-letter-preview.tex`
  - `17-final-assembly-checklist.md`

## Current Stage 6 Contract

Stage 6 不再依赖 variant selection、patch sets 或 marked/clean manuscript 双轨导出。当前闭环规则是：

- 所有 `revision_plan_actions` 必须结案
- 每个原始 `thread_id` 都必须被 `response_thread_rows` 覆盖
- 每个已改动的 `working_manuscript` 文件都必须有已审计的 revision log
- 回复信预览与最终 checklist 必须能回溯到 revision audit
