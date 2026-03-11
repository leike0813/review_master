# Raw Review Thread List

这是从 `review-master.db` 渲染出的原始审稿意见块只读视图。数据库真源是 `raw_review_threads`。这是最终 response letter 的正式索引层，用户应优先在这里核对 reviewer 原始条目的顺序与边界。

## 原始线程表

| `thread_id` | `reviewer_id` | `thread_order` | `source_type` | 归一化摘要 | 关联 atomic comments |
| --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | 1 | reviewer_comment | Explain why the method is better than the baseline. | atomic_001 |
| reviewer_1_thread_002 | reviewer_1 | 2 | reviewer_comment | Request ablation justification. | atomic_002 |
| reviewer_1_thread_003 | reviewer_1 | 3 | reviewer_comment | Clarify splits and reproducibility. | atomic_003 |
| reviewer_2_thread_001 | reviewer_2 | 1 | reviewer_comment | Request multi-seed stability evidence. | atomic_004 |
| reviewer_2_thread_002 | reviewer_2 | 2 | reviewer_comment | Repeat the baseline question and ask for stronger limitations. | atomic_001, atomic_005 |

## 原始线程文本

### reviewer_1_thread_001

- 原文: Please explain why your method is better than the baseline.

### reviewer_1_thread_002

- 原文: Add an ablation study or explain the missing components.

### reviewer_1_thread_003

- 原文: Clarify data splits and reproducibility settings.

### reviewer_2_thread_001

- 原文: Please add multi-seed stability results and a figure.

### reviewer_2_thread_002

- 原文: Please justify the baseline comparison more clearly and expand the limitations discussion.

