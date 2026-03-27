# Atomic Review Comment List

这是从 `review-master.db` 渲染出的 canonical atomic 意见只读视图。数据库真源是 `atomic_comments`、`raw_thread_atomic_links`、`raw_review_threads` 和 `atomic_comment_state`。同一条 atomic item 可以同时服务多个原始 reviewer 线程。

## Canonical Atomic 表

| `comment_id` | 来源审稿人 | 来源线程 | Canonical 摘要 | 所需动作 |
| --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1 | reviewer_1_thread_001 | Explain why the proposed method outperforms the baseline. | Provide a concise causal explanation for the baseline advantage claim. |
| atomic_002 | reviewer_1 | reviewer_1_thread_001 | Identify the manuscript evidence that supports the baseline-comparison claim. | Point the reviewer to the exact evidence location in the results discussion. |
