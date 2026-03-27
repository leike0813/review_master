# Evidence Supplement Failure Recovery

这个 example 展示当前合同下的 Stage 5 failure/recovery：

- 第一轮补材看似相关，但没有真正覆盖 reviewer concern
- workflow 继续 blocked
- 第二轮补材才真正关闭 evidence gap
- 后续进入基于 revision audit 的 Stage 6

目录说明：

- `inputs/`
- `user-supplements/round-1-bad/`
- `user-supplements/round-2-good/`
- `workspace/`
- `outputs/`
- `gate-and-render-output/`
  - 保留 Stage 1-6 的代表性 gate 快照

当前 workspace 使用 `01-17` 工件序列，Stage 6 使用 `working_manuscript + revision audit + response coverage`。
