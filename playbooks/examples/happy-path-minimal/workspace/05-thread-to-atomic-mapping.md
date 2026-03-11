# Thread to Atomic Mapping

这是原始 reviewer thread 到 canonical atomic 意见的映射视图。数据库真源是 `raw_thread_atomic_links` 与 `atomic_comment_source_spans`。用户和 Agent 都应通过它确认拆分、合并与去重是否合理。

## reviewer_1_thread_001 (reviewer_1)

- 归一化摘要: Clarify why the method outperforms the baseline and where the supporting argument lives.
- 原文: Please clarify why the proposed method outperforms the baseline and explain what part of the results section supports this claim.

| 链接顺序 | `comment_id` | Canonical 摘要 | 来源片段 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | atomic_001 | Explain why the proposed method outperforms the baseline. | Please clarify why the proposed method outperforms the baseline | Primary causal explanation request. |
| 2 | atomic_002 | Identify the manuscript evidence that supports the baseline-comparison claim. | explain what part of the results section supports this claim | Supporting evidence-location request. |

