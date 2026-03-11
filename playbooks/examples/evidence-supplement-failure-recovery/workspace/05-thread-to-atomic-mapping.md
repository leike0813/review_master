# Thread to Atomic Mapping

这是原始 reviewer thread 到 canonical atomic 意见的映射视图。数据库真源是 `raw_thread_atomic_links` 与 `atomic_comment_source_spans`。用户和 Agent 都应通过它确认拆分、合并与去重是否合理。

## reviewer_1_thread_001 (reviewer_1)

- 归一化摘要: Explain why the method is better than the baseline.
- 原文: Please explain why your method is better than the baseline.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_001 | Explain why the main method outperforms the baseline. | Please explain why your method is better than the baseline. | Primary baseline-comparison request. |

## reviewer_1_thread_002 (reviewer_1)

- 归一化摘要: Request ablation justification.
- 原文: Add an ablation study or explain the missing components.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_002 | Provide an ablation explanation. | Add an ablation study or explain the missing components. | Ablation request. |

## reviewer_1_thread_003 (reviewer_1)

- 归一化摘要: Clarify splits and reproducibility.
- 原文: Clarify data splits and reproducibility settings.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_003 | Clarify data split and reproducibility settings. | Clarify data splits and reproducibility settings. | Reproducibility request. |

## reviewer_2_thread_001 (reviewer_2)

- 归一化摘要: Request multi-seed stability evidence.
- 原文: Please add multi-seed stability results and a figure.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_004 | Add multi-seed stability evidence and a figure. | Please add multi-seed stability results and a figure. | Evidence-gap request. |

## reviewer_2_thread_002 (reviewer_2)

- 归一化摘要: Repeat the baseline question and ask for stronger limitations.
- 原文: Please justify the baseline comparison more clearly and expand the limitations discussion.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_001 | Explain why the main method outperforms the baseline. | Please justify the baseline comparison more clearly | Merged duplicate baseline concern from reviewer_2. |
| 2 | atomic_005 | Expand limitations and discussion. | expand the limitations discussion. | Limitations expansion request. |

