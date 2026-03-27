# Atomic Review Comment List

这是从 `review-master.db` 渲染出的 canonical atomic 意见只读视图。数据库真源是 `atomic_comments`、`raw_thread_atomic_links`、`raw_review_threads` 和 `atomic_comment_state`。同一条 atomic item 可以同时服务多个原始 reviewer 线程。

## Canonical Atomic 表

| `comment_id` | 来源审稿人 | 来源线程 | Canonical 摘要 | 所需动作 |
| --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_2 | reviewer_1_thread_001, reviewer_2_thread_002 | Explain why the main method outperforms the baseline. | Explain the baseline comparison more clearly. |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | Provide an ablation explanation. | Explain the missing ablation components. |
| atomic_003 | reviewer_1 | reviewer_1_thread_003 | Clarify data split and reproducibility settings. | Clarify splits and reproducibility details. |
| atomic_004 | reviewer_2 | reviewer_2_thread_001 | Add multi-seed stability evidence and a figure. | Add multi-seed results and a stability figure. |
| atomic_005 | reviewer_2 | reviewer_2_thread_002 | Expand limitations and discussion. | Strengthen the limitations section. |
