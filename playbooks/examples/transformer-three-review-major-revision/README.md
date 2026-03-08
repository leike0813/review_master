# Transformer Three-Review Major Revision Example

这个 example 包基于仓库中的 `examples/example_orig.md` 构建，用来演示一种更接近真实场景的“从已通过终稿倒推初稿”的修回案例。

## Purpose

- 把 `example_orig.md` 视为已经修回并通过审核的完整版论文
- 从终稿中有控制地删除、模糊或弱化一部分内容，生成一个仍然可送审、但明显会收到 major revision 的初稿
- 为这些被劣化的位置模拟生成 3 位 reviewer 的审稿意见
- 把每一步被删改的内容整理成后续用户补充的证据材料，并按轮次放入 `user-supplements/`

## Included Assets

- `reference/accepted-paper.md`
  - 终稿参考快照，复制自 `examples/example_orig.md`
- `reference/degradation-traceability.md`
  - 记录每一步劣化动作、被影响位置、触发的 reviewer comment 和对应补证文件
- `inputs/manuscript/`
  - 一份接近全文级的 LaTeX 工程初稿
- `inputs/review-comments.md`
  - 3 位 reviewer、共 15 条评论
- `user-supplements/round-1/`
  - 方法定位、复现与解码设定补充
- `user-supplements/round-2/`
  - 组件贡献与训练成本补充
- `user-supplements/round-3/`
  - 失败模式、注意力示例和局限性补充

## Scope Notes

- 本轮只提供内容资产，不提供 `workspace/`、`review-master.db` 或 `gate-and-render-output/`
- 不修改现有 runtime、schema、脚本接口或现有 examples
- 这个案例强调“真实修回素材的组织方式”，而不是直接演示 end-to-end runtime 回放
