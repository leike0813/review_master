# Degradation Traceability

下表把终稿中被有意劣化的内容、对应触发的审稿意见，以及后续用户补交的证据串起来。目标不是制造低质量论文，而是制造一篇“主线成立但信息不足”的 major revision 初稿。

| Step ID | Draft location | Degraded content | Triggered reviewer comments | Evidence files |
| --- | --- | --- | --- | --- |
| DG-01 | `sections/abstract.tex`; `sections/introduction.tex` | 弱化了“为何仅用 attention 就能替代 recurrence/convolution”的机制性解释，只保留高层结论。 | `R1.1`; `R1.5`; `R3.4` | `user-supplements/round-1/method-positioning-note.md`; `user-supplements/round-1/round-1-cover-note.md` |
| DG-02 | `sections/background.tex` | 压缩了与 ByteNet、ConvS2S、memory networks 的关系定位，没把 novelty 边界说清。 | `R1.2`; `R3.5` | `user-supplements/round-1/method-positioning-note.md` |
| DG-03 | `sections/architecture.tex` | 保留结构描述，但删除了多头数、位置编码与关键超参数选择背后的支撑说明。 | `R1.3`; `R1.4`; `R2.4` | `user-supplements/round-2/component-ablation.csv`; `user-supplements/round-2/ablation-interpretation-note.md`; `user-supplements/round-2/round-2-cover-note.md` |
| DG-04 | `sections/training.tex` | 删除了 seed、checkpoint averaging、beam search、长度惩罚和数据处理约束的可复现细节。 | `R2.1`; `R2.2` | `user-supplements/round-1/reproducibility-note.md`; `user-supplements/round-1/wmt-decode-settings.tex` |
| DG-05 | `sections/results.tex` | 只保留 headline BLEU 表述，删除了变体分析和对“哪些组件带来收益”的解释。 | `R1.3`; `R2.4`; `R2.5` | `user-supplements/round-2/component-ablation.csv`; `user-supplements/round-2/ablation-interpretation-note.md` |
| DG-06 | `sections/results.tex`; `sections/conclusion.tex` | 保留训练成本优势结论，但删除了 FLOPs 口径、硬件边界和跨模型比较限定。 | `R2.3`; `R3.5` | `user-supplements/round-2/efficiency-cost-comparison.csv`; `user-supplements/round-2/efficiency-accounting-note.md` |
| DG-07 | `sections/discussion.tex` | 将局限性、失败模式和外推边界压缩成一小段，删除了更明确的风险讨论。 | `R3.1`; `R3.3`; `R3.5` | `user-supplements/round-3/failure-bucket-summary.csv`; `user-supplements/round-3/limitations-and-boundaries.md`; `user-supplements/round-3/round-3-cover-note.md` |
| DG-08 | `sections/results.tex`; `sections/discussion.tex` | 移除了注意力可解释性的具体示例与定性分析，只保留一条轻量断言。 | `R3.2`; `R3.4` | `user-supplements/round-3/attention-case-study.md`; `user-supplements/round-3/attention-pattern-example.svg`; `user-supplements/round-3/attention-pattern-example.pdf` |

## Round Summary

- Round 1: 先补充方法定位与可复现性说明，足以回复 reviewer 对 mechanism 和 protocol 的首批质疑。
- Round 2: 再补组件贡献与训练成本口径，让 response letter 有更强的 quantitative support。
- Round 3: 最后补失败模式、注意力示例与局限性讨论，完成讨论层面的收尾。
