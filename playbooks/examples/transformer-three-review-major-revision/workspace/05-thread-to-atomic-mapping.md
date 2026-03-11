# Thread to Atomic Mapping

这是原始 reviewer thread 到 canonical atomic 意见的映射视图。数据库真源是 `raw_thread_atomic_links` 与 `atomic_comment_source_spans`。用户和 Agent 都应通过它确认拆分、合并与去重是否合理。

## reviewer_1_thread_001 (reviewer_1)

- 归一化摘要: Clarify why attention-only is a viable replacement beyond parallelism.
- 原文: The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_001 | Explain why attention-only can replace recurrence and convolution in this translation setting. | The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_1_thread_002 (reviewer_1)

- 归一化摘要: Clarify novelty positioning against efficient sequence models.
- 原文: The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_002 | Clarify novelty positioning against ByteNet, ConvS2S, and related prior work. | The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_1_thread_003 (reviewer_1)

- 归一化摘要: Request component-level sensitivity analysis.
- 原文: The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_1_thread_004 (reviewer_1)

- 归一化摘要: Request justification of architectural hyperparameters.
- 原文: The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_1_thread_005 (reviewer_1)

- 归一化摘要: Request causal explanation for baseline gains.
- 原文: The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_004 | Explain the mechanism behind the baseline gain in the main results. | The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_2_thread_001 (reviewer_2)

- 归一化摘要: Clarify data usage and evaluation protocol.
- 原文: The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_005 | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_2_thread_002 (reviewer_2)

- 归一化摘要: Clarify checkpoint averaging and decoding settings.
- 原文: Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_005 | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_2_thread_003 (reviewer_2)

- 归一化摘要: Clarify training-cost accounting and fairness caveat.
- 原文: The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_006 | Clarify training-cost accounting and fairness caveats in the efficiency claim. | The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_2_thread_004 (reviewer_2)

- 归一化摘要: Repeat the request for architecture sensitivity evidence.
- 原文: The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_2_thread_005 (reviewer_2)

- 归一化摘要: Request stability or variance support beyond headline BLEU.
- 原文: Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_007 | Add stability or variance evidence beyond headline BLEU. | Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_3_thread_001 (reviewer_3)

- 归一化摘要: Expand limitations and failure-mode discussion.
- 原文: The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_3_thread_002 (reviewer_3)

- 归一化摘要: Request a concrete attention case study.
- 原文: The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_009 | Add an interpretability case study with qualitative attention evidence. | The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_3_thread_003 (reviewer_3)

- 归一化摘要: Request explicit failure buckets.
- 原文: Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_3_thread_004 (reviewer_3)

- 归一化摘要: Request a concrete long-range dependency example.
- 原文: The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_001 | Explain why attention-only can replace recurrence and convolution in this translation setting. | The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim. | Mapped from the original reviewer comment to the canonical revision action. |

## reviewer_3_thread_005 (reviewer_3)

- 归一化摘要: Temper the conclusion and scope claims.
- 原文: The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats. | Mapped from the original reviewer comment to the canonical revision action. |

