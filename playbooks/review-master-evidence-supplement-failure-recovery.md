# review-master Evidence Supplement Failure Recovery Playbook

## Purpose

这份 playbook 展示 Stage 5 的 failure/recovery 样例：

- 用户确实提交了补材
- 但第一轮补材没有语义上覆盖 reviewer concern
- workflow 仍保持 blocked
- 直到第二轮补材真正满足证据缺口后才恢复推进

## Example Assets

- 输入：
  - `playbooks/examples/evidence-supplement-failure-recovery/inputs/manuscript/`
  - `playbooks/examples/evidence-supplement-failure-recovery/inputs/review-comments.md`
- 补材：
  - `playbooks/examples/evidence-supplement-failure-recovery/user-supplements/round-1-bad/`
  - `playbooks/examples/evidence-supplement-failure-recovery/user-supplements/round-2-good/`
- workspace：
  - `playbooks/examples/evidence-supplement-failure-recovery/workspace/`
- 最终产物：
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/response-letter.md`
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/response-letter.tex`
- gate 快照：
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/`

## What This Example Proves

- Stage 5 的 blocker 判断是语义性的，不是“只要收到文件就放行”
- `10-supplement-intake-plan.md` 负责显式记录接收、拒收与落地
- 错误补材不会自动关闭 evidence gap
- 只有 Stage 5 真正闭环后，才会进入基于 revision audit 的 Stage 6

## Current Read Order

1. `08-atomic-comment-workboard.md`
2. `09-supplement-suggestion-plan.md`
3. `10-supplement-intake-plan.md`
4. 对应 `response-strategy-cards/{comment_id}.md`
5. 成功恢复后再查看 `11-17` 的 Stage 6 工件
