# Response Coverage Matrix

这是按原始 `thread_id` 渲染的 Stage 6 覆盖矩阵。它用于检查每条审稿意见是否已被 revision log 或 response-only 处理覆盖。

| `thread_id` | `reviewer_id` | 原始意见摘要 | `comment_ids` | 覆盖方式 | `log_ids` | 修改范围 | 已覆盖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | Explain why the method is better than the baseline. | atomic_001 | revision_backed | legacy_log_001 | sections/results.tex::Main Comparison::paragraph 2 | yes |
| reviewer_1_thread_002 | reviewer_1 | Request ablation justification. | atomic_002 | revision_backed | legacy_log_002 | sections/results.tex::Ablation Discussion::paragraph 1 | yes |
| reviewer_1_thread_003 | reviewer_1 | Clarify splits and reproducibility. | atomic_003 | revision_backed | legacy_log_003 | sections/method.tex::Implementation Details::paragraph 3 | yes |
| reviewer_2_thread_001 | reviewer_2 | Request multi-seed stability evidence. | atomic_004 | revision_backed | legacy_log_004 | sections/results.tex::Stability Analysis::paragraph 1-2; figures/seed-stability-figure.svg | yes |
| reviewer_2_thread_002 | reviewer_2 | Repeat the baseline question and ask for stronger limitations. | atomic_001, atomic_005 | revision_backed | legacy_log_005 | sections/results.tex::Main Comparison::paragraph 2; sections/discussion.tex::Limitations::paragraph 1-2 | yes |
