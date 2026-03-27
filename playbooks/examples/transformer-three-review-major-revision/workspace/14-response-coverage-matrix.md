# Response Coverage Matrix

这是按原始 `thread_id` 渲染的 Stage 6 覆盖矩阵。它用于检查每条审稿意见是否已被 revision log 或 response-only 处理覆盖。

| `thread_id` | `reviewer_id` | 原始意见摘要 | `comment_ids` | 覆盖方式 | `log_ids` | 修改范围 | 已覆盖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | Clarify why attention-only is a viable replacement beyond parallelism. | atomic_001 | revision_backed | legacy_log_001 | sections/introduction.tex::paragraph 3 | yes |
| reviewer_1_thread_002 | reviewer_1 | Clarify novelty positioning against efficient sequence models. | atomic_002 | revision_backed | legacy_log_002 | sections/background.tex::paragraph 3 | yes |
| reviewer_1_thread_003 | reviewer_1 | Request component-level sensitivity analysis. | atomic_003 | revision_backed | legacy_log_003 | sections/architecture.tex::Model Configuration::paragraph 1 | yes |
| reviewer_1_thread_004 | reviewer_1 | Request justification of architectural hyperparameters. | atomic_003 | revision_backed | legacy_log_004 | sections/architecture.tex::Model Configuration::paragraph 1 | yes |
| reviewer_1_thread_005 | reviewer_1 | Request causal explanation for baseline gains. | atomic_004 | revision_backed | legacy_log_005 | sections/results.tex::Machine Translation::paragraph 3 | yes |
| reviewer_2_thread_001 | reviewer_2 | Clarify data usage and evaluation protocol. | atomic_005 | revision_backed | legacy_log_006 | sections/training.tex::Data::paragraph 1 | yes |
| reviewer_2_thread_002 | reviewer_2 | Clarify checkpoint averaging and decoding settings. | atomic_005 | revision_backed | legacy_log_007 | sections/training.tex::Implementation Notes::paragraph 1 | yes |
| reviewer_2_thread_003 | reviewer_2 | Clarify training-cost accounting and fairness caveat. | atomic_006 | revision_backed | legacy_log_008 | sections/results.tex::Machine Translation::paragraph 1 | yes |
| reviewer_2_thread_004 | reviewer_2 | Repeat the request for architecture sensitivity evidence. | atomic_003 | revision_backed | legacy_log_009 | sections/results.tex::Model Variations::paragraph 1 | yes |
| reviewer_2_thread_005 | reviewer_2 | Request stability or variance support beyond headline BLEU. | atomic_007 | revision_backed | legacy_log_010 | sections/results.tex::Stability Statement::paragraph 1 | yes |
| reviewer_3_thread_001 | reviewer_3 | Expand limitations and failure-mode discussion. | atomic_008 | revision_backed | legacy_log_011 | sections/discussion.tex::paragraph 2-4 | yes |
| reviewer_3_thread_002 | reviewer_3 | Request a concrete attention case study. | atomic_009 | revision_backed | legacy_log_012 | sections/results.tex::Interpretability::paragraph 1 | yes |
| reviewer_3_thread_003 | reviewer_3 | Request explicit failure buckets. | atomic_008 | revision_backed | legacy_log_013 | sections/discussion.tex::paragraph 3 | yes |
| reviewer_3_thread_004 | reviewer_3 | Request a concrete long-range dependency example. | atomic_001 | revision_backed | legacy_log_014 | sections/introduction.tex::paragraph 3; sections/results.tex::Interpretability::paragraph 1 | yes |
| reviewer_3_thread_005 | reviewer_3 | Temper the conclusion and scope claims. | atomic_008 | revision_backed | legacy_log_015 | sections/conclusion.tex::paragraph 2 | yes |
