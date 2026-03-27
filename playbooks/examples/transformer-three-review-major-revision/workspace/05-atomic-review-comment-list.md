# Atomic Review Comment List

这是从 `review-master.db` 渲染出的 canonical atomic 意见只读视图。数据库真源是 `atomic_comments`、`raw_thread_atomic_links`、`raw_review_threads` 和 `atomic_comment_state`。同一条 atomic item 可以同时服务多个原始 reviewer 线程。

## Canonical Atomic 表

| `comment_id` | 来源审稿人 | 来源线程 | Canonical 摘要 | 所需动作 |
| --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_3 | reviewer_1_thread_001, reviewer_3_thread_004 | Explain why attention-only can replace recurrence and convolution in this translation setting. | Add a concrete mechanism-based explanation of the attention-only claim. |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | Clarify novelty positioning against ByteNet, ConvS2S, and related prior work. | Strengthen the prior-work boundary and novelty statement. |
| atomic_003 | reviewer_1, reviewer_2 | reviewer_1_thread_003, reviewer_1_thread_004, reviewer_2_thread_004 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | Add ablation and sensitivity support for the architecture choices. |
| atomic_004 | reviewer_1 | reviewer_1_thread_005 | Explain the mechanism behind the baseline gain in the main results. | Provide a causal explanation for why the Transformer improves over baselines. |
| atomic_005 | reviewer_2 | reviewer_2_thread_001, reviewer_2_thread_002 | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | Make the training and decoding protocol reproducible. |
| atomic_006 | reviewer_2 | reviewer_2_thread_003 | Clarify training-cost accounting and fairness caveats in the efficiency claim. | Qualify the FLOPs and hardware comparison claim. |
| atomic_007 | reviewer_2 | reviewer_2_thread_005 | Add stability or variance evidence beyond headline BLEU. | Report stability support and calibrate the single-run claim. |
| atomic_008 | reviewer_3 | reviewer_3_thread_001, reviewer_3_thread_003, reviewer_3_thread_005 | Expand limitations, failure buckets, and scope boundaries. | Add a fuller limitations and failure-mode discussion. |
| atomic_009 | reviewer_3 | reviewer_3_thread_002 | Add an interpretability case study with qualitative attention evidence. | Support the interpretability claim with a concrete example. |
