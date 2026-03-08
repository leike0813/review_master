# Atomic Review Comment List

这是从 `review-master.db` 渲染出的 canonical atomic 意见只读视图。数据库真源是 `atomic_comments`、`raw_thread_atomic_links`、`raw_review_threads` 和 `atomic_comment_state`。同一条 atomic item 可以同时服务多个原始 reviewer 意见块。

## Canonical Atomic Table

| `comment_id` | Source Reviewers | Source Threads | `status` | `priority` | `evidence_gap` | Canonical Summary | Required Action | Target Locations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_3 | reviewer_1_thread_001, reviewer_3_thread_004 | ready | high | yes | Explain why attention-only can replace recurrence and convolution in this translation setting. | Add a concrete mechanism-based explanation of the attention-only claim. | sections/introduction.tex::Introduction::paragraph 3, sections/results.tex::Machine Translation::paragraph 2 |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | ready | medium | yes | Clarify novelty positioning against ByteNet, ConvS2S, and related prior work. | Strengthen the prior-work boundary and novelty statement. | sections/background.tex::Background::paragraph 3 |
| atomic_003 | reviewer_1, reviewer_2 | reviewer_1_thread_003, reviewer_1_thread_004, reviewer_2_thread_004 | ready | high | yes | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | Add ablation and sensitivity support for the architecture choices. | sections/architecture.tex::Model Configuration::paragraph 1, sections/results.tex::Model Variations::paragraph 1 |
| atomic_004 | reviewer_1 | reviewer_1_thread_005 | ready | high | no | Explain the mechanism behind the baseline gain in the main results. | Provide a causal explanation for why the Transformer improves over baselines. | sections/results.tex::Machine Translation::paragraph 2 |
| atomic_005 | reviewer_2 | reviewer_2_thread_001, reviewer_2_thread_002 | ready | high | yes | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | Make the training and decoding protocol reproducible. | sections/training.tex::Data::paragraph 1, sections/training.tex::Implementation Notes::paragraph 1 |
| atomic_006 | reviewer_2 | reviewer_2_thread_003 | ready | medium | yes | Clarify training-cost accounting and fairness caveats in the efficiency claim. | Qualify the FLOPs and hardware comparison claim. | sections/results.tex::Machine Translation::paragraph 1, sections/conclusion.tex::Conclusion::paragraph 2 |
| atomic_007 | reviewer_2 | reviewer_2_thread_005 | ready | medium | yes | Add stability or variance evidence beyond headline BLEU. | Report stability support and calibrate the single-run claim. | sections/results.tex::Stability Statement::paragraph 1 |
| atomic_008 | reviewer_3 | reviewer_3_thread_001, reviewer_3_thread_003, reviewer_3_thread_005 | ready | high | yes | Expand limitations, failure buckets, and scope boundaries. | Add a fuller limitations and failure-mode discussion. | sections/discussion.tex::Discussion::paragraph 2, sections/conclusion.tex::Conclusion::paragraph 2 |
| atomic_009 | reviewer_3 | reviewer_3_thread_002 | ready | medium | yes | Add an interpretability case study with qualitative attention evidence. | Support the interpretability claim with a concrete example. | sections/results.tex::Interpretability::paragraph 1, sections/discussion.tex::Discussion::paragraph 4 |
