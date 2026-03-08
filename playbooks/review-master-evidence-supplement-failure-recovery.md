# review-master Evidence Supplement Failure Recovery Playbook

## Purpose

这份 playbook 演示一个简单但真实的 Stage 5 failure case：

- 多 reviewer / 多 atomic 的背景仍然保留
- 只有 `atomic_004` 进入 evidence gap 路径
- 第一轮补材已经“给了东西”，但语义上没有回答 reviewer 的真正关切
- Agent 必须判断 failure 原因是 concern mismatch，而不是把“材料存在”误判成“证据已足够”
- 第二轮补材才真正关闭 blocker，并最终恢复到 `stage_6_completed`

## Example Assets

- 输入：
  - `playbooks/examples/evidence-supplement-failure-recovery/inputs/manuscript/`
  - `playbooks/examples/evidence-supplement-failure-recovery/inputs/review-comments.md`
- 补材：
  - `playbooks/examples/evidence-supplement-failure-recovery/user-supplements/round-1-bad/`
  - `playbooks/examples/evidence-supplement-failure-recovery/user-supplements/round-2-good/`
- 最终态 workspace：
  - `playbooks/examples/evidence-supplement-failure-recovery/workspace/`
- 最终输出：
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/marked-manuscript/`
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/revised-manuscript/`
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/response-letter.md`
  - `playbooks/examples/evidence-supplement-failure-recovery/outputs/response-letter.tex`
- 关键 checkpoint：
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/stage-5-evidence-gap-blocked.json`
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/stage-5-after-bad-supplement-blocked.json`
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/stage-5-after-good-supplement-ready.json`
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/stage-6-export-ready.json`
  - `playbooks/examples/evidence-supplement-failure-recovery/gate-and-render-output/stage-6-completed.json`

## Why This Failure Matters

这个案例要强调的不是“文件没给到”，而是“文件给到了，但没有回答问题”。

`atomic_004` 的 reviewer concern 是：

- 需要 multi-seed stability evidence
- 需要 repeated-run summary
- 需要一张能支撑保守 robustness statement 的 figure

第一轮补材故意只给：

- 单次训练 loss 曲线
- 单次 run 的 checkpoint 表
- 一份强调“这次训练很稳”的说明

这些材料表面上都像实验补证，但它们只描述一条 run 的轨迹，无法支持跨 seed 稳定性判断。所以 Agent 必须保持 `blocked`，而不是因为“用户已经上传文件”就关闭 evidence gap。

## Walkthrough

### Stage 1-4

Stage 1 到 Stage 4 与 `evidence-supplement-multi-review` 的主线保持一致：

- 输入仍是多文件 LaTeX 工程
- 2 位 reviewer、5 个原始 thread、5 条 canonical atomic item
- `atomic_004` 在 Stage 4 已经被标记成：
  - `status = blocked`
  - `evidence_gap = yes`
  - 需要稳定性实验和 figure

对应 checkpoint：

- `stage-1-entry-ready.json`
- `stage-2-structure-ready.json`
- `stage-3-atomic-ready.json`
- `stage-4-workboard-confirmation-needed.json`

### Stage 5A: Initial Blocker

在任何补材到位之前，案例先停在：

- `stage-5-evidence-gap-blocked.json`

这时的状态语义是：

- `active_comment_id = atomic_004`
- `recommended_next_action = resolve_blockers`
- open loop 仍是“需要稳定性结果与 figure”

这一步只是正常 blocker，不是 failure。

### Stage 5B: Bad Supplement Still Fails

用户随后给出第一轮补材：

- `round-1-bad/seed-loss-curve.svg`
- `round-1-bad/single-run-training-note.md`
- `round-1-bad/dev-set-checkpoints.csv`

此时案例进入：

- `stage-5-after-bad-supplement-blocked.json`

必须这样解释 failure：

- 材料不是缺失
- 材料也不是格式错误
- 但它们只描述 one-run behavior
- reviewer 要求的是 cross-seed stability evidence
- 所以 evidence gap 仍未关闭

这个判断在脚本层面并不能自动推出，必须由 Agent 根据策略卡、reviewer concern 和补材语义做出判断。

为了让 replay 足够直观，这个 checkpoint 还额外保留了 3 份只读视图：

- `stage-5-after-bad-supplement-agent-resume.md`
- `stage-5-after-bad-supplement-atomic-comment-workboard.md`
- `stage-5-after-bad-supplement-atomic_004-strategy-card.md`

其中最关键的是策略卡会明确写出：

- round-1 补材 available = yes
- 但 gap note 仍说明“只描述单次训练轨迹，不回答 multi-seed stability concern”

### Stage 5C: Good Supplement Closes The Gap

第二轮补材才真正回答 reviewer concern：

- `round-2-good/stability-results.csv`
- `round-2-good/seed-stability-figure.svg`
- `round-2-good/supplement-note.md`

此时案例进入：

- `stage-5-after-good-supplement-ready.json`

状态语义固定为：

- `recommended_next_action = advance_active_comment`
- `resume_status = ready_to_resume`
- open loop 从“继续补材”变成“把 verified five-seed evidence 落到 manuscript 和 response text”

也就是说，第二轮补材不是简单“更多材料”，而是第一次真正与既定策略对齐的材料。

### Stage 6

在 corrected supplement 被整合后，案例进入完整导出链路：

- `stage-6-export-ready.json`
- `stage-6-completed.json`

最终 workspace 和 outputs 保留完整成功态：

- `workspace/agent-resume.md` 记录了“round-1 被拒绝、round-2 被接受”的决策历史
- `workspace/response-strategy-cards/atomic_004.md` 保留了两轮补材的 evidence history
- `workspace/final-assembly-checklist.md` 与 outputs 说明最终所有导出产物都已落地

## Failure Judgment Rule

这个案例的正式判断规则固定为：

- “材料存在”不等于“证据足够”
- 只要补材没有回答当前 reviewer concern，就不能关闭 blocker
- Stage 5 的 failure judgment 属于 Agent 的语义职责，不属于脚本的自动职责
- 脚本只负责渲染当前数据库状态，不负责判断某份补材是否真正支持当前策略

所以本案例的教学重点是：

- 不要把 upload success 当成 evidence success
- 不要把 one-run training trace 误判成 multi-seed stability evidence

## Replay Contract

理解这份案例时，推荐固定按这个顺序回放：

1. `stage-5-evidence-gap-blocked.json`
2. `round-1-bad/`
3. `stage-5-after-bad-supplement-blocked.json`
4. `stage-5-after-bad-supplement-agent-resume.md`
5. `stage-5-after-bad-supplement-atomic_004-strategy-card.md`
6. `round-2-good/`
7. `stage-5-after-good-supplement-ready.json`
8. `workspace/agent-resume.md`
9. `workspace/response-strategy-cards/atomic_004.md`
10. `stage-6-completed.json`

这样最容易看清：

- 初始 blocker 是什么
- 第一轮补材为什么失败
- 第二轮补材为什么能恢复
- 最终成功态如何把 failure history 保留下来
