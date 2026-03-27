# Playbooks

这些 playbook 是仓库级演练资料，用来展示 `review-master` 在当前合同下的典型运行方式。它们不属于 `review-master/` 发布包本体。

当前统一基线：

- workspace 只保留当前 `01-17` 工件序列
- Stage 6 使用 `working_manuscript + revision audit + response coverage`
- 旧的 patch/export 链路示例资产已移除
- 示例快照统一放在 `playbooks/examples/*/gate-and-render-output/`
- 每个示例默认保留一组代表性阶段快照，用来展示当前状态机下 Stage 1-6 的典型 gate 输出

现有 playbook：

- `review-master-happy-path.md`
  - 最小 happy path
  - 单文件稿件、无补材分支、直接收束到 Stage 6 完成态
- `review-master-evidence-supplement-playbook.md`
  - 多 reviewer + evidence gap + supplement intake/landing 的成功路径
- `review-master-evidence-supplement-failure-recovery.md`
  - Stage 5 中“补材已提交但语义仍不满足”的 failure/recovery 样例
- `review-master-transformer-three-review-major-revision.md`
  - 多 reviewer、多轮补材、复杂 Stage 5/6 收束的完整样例
