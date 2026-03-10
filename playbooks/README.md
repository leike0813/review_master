# Playbooks

- `review-master-happy-path.md`
  - 最小 happy path
  - 单文件 LaTeX、1 条原子意见、无补材闭环
  - 包含修订后执行流程的视图更新说明（含 `supplement-intake-plan.md` 空态视图）
- `review-master-evidence-supplement-playbook.md`
  - 较长样例
  - 多文件 LaTeX、2 位 reviewer、5 条原子意见、1 次 evidence gap blocked/unblocked 闭环
  - Stage 5 明确包含补材文件级 intake 决策与 accepted 补材落地映射
- `review-master-evidence-supplement-failure-recovery.md`
  - Stage 5 failure-recovery 样例
  - 复用多 reviewer 背景，只让 1 条 atomic item 先因 supplement mismatch 继续 blocked，再由第二轮正确补材恢复并闭环
  - failure/recovery 都通过 `supplement-intake-plan.md` 显式展示补材判定与落地关系
- `review-master-transformer-three-review-major-revision.md`
  - 完整 runtime 回放型复杂案例
  - 基于 `example_orig.md` 的终稿快照、多文件 LaTeX 初稿、3 位 reviewer、15 条评论、9 条 canonical atomic item、3 轮用户补材与 `stage_6_completed` 闭环
  - 三轮 Stage 5 均包含 intake/landing 强约束与分轮视图更新记录

这些 playbook 是仓库级演练资料，不属于 `review-master/` 发布包。

样例中的脚本 JSON 输出目录正式命名统一为：

- `playbooks/examples/*/gate-and-render-output/`
