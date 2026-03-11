# Response Letter Outline

这是从 `review-master.db` 渲染出的 Stage 6 预组装视图。数据库真源是 `raw_review_threads`、`response_thread_resolution_links`、`selected_action_copy_variants`、`response_thread_rows`、`atomic_comments`、`strategy_card_actions` 和 `strategy_action_target_locations`。最终 response letter 必须按原始 `thread_id` 顺序组织，而不是按 canonical atomic item 直接展开。这里的 thread-level row 来自 Stage 5 已确认的策略/草案、Stage 6 已选中的 manuscript 最终落稿文本，以及 thread-level 聚合；它不是从 response-side variants 中选出来的。

## reviewer_1

### reviewer_1_thread_001

- 原始线程: Please explain why your method is better than the baseline.
- 归一化摘要: Explain why the method is better than the baseline.
- 最终行已就绪: yes

| 回复顺序 | 角色 | `comment_id` | Canonical 摘要 | 已选 manuscript copy 摘要 |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_001 | Explain why the main method outperforms the baseline. | L1 sections/results.tex::Main Comparison::paragraph 2 / v2=The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. |

#### 最终行预览

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please explain why the proposed multimodal transformer outperforms the baseline methods in the main results. | sections/results.tex::Main Comparison::paragraph 2 | The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. | We revised the main-comparison discussion to give a mechanism-based explanation of the baseline gain. This response also supports the overlapping baseline-justification concern raised by Reviewer 2. |

### reviewer_1_thread_002

- 原始线程: Add an ablation study or explain the missing components.
- 归一化摘要: Request ablation justification.
- 最终行已就绪: yes

| 回复顺序 | 角色 | `comment_id` | Canonical 摘要 | 已选 manuscript copy 摘要 |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_002 | Provide an ablation explanation. | L1 sections/results.tex::Ablation Placeholder::paragraph 1 / v2=Removing either the image branch or the spectral branch weakens performance, indicating that the gain comes from complementary cross-modal evidence rather than a single dominant stream. |

#### 最终行预览

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please include an ablation that clarifies the contribution of the image and spectral branches. | sections/results.tex::Ablation Discussion::paragraph 1 | Removing either the image branch or the spectral branch weakens performance, indicating that the gain comes from complementary cross-modal evidence rather than a single dominant stream. | We added a focused ablation explanation to clarify the role of each modality without overstating the scope of the experiment. |

### reviewer_1_thread_003

- 原始线程: Clarify data splits and reproducibility settings.
- 归一化摘要: Clarify splits and reproducibility.
- 最终行已就绪: yes

| 回复顺序 | 角色 | `comment_id` | Canonical 摘要 | 已选 manuscript copy 摘要 |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_003 | Clarify data split and reproducibility settings. | L1 sections/method.tex::Implementation Details::paragraph 3 / v2=We use a fixed train/validation/test split of 640/160/200 plots and repeat all stochastic experiments with seeds 11, 17, 23, 29, and 37. |

#### 最终行预览

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please clarify the train/validation/test split and the random seed configuration so that the work is reproducible. | sections/method.tex::Implementation Details::paragraph 3 | We use a fixed train/validation/test split of 640/160/200 plots and repeat all stochastic experiments with seeds 11, 17, 23, 29, and 37. | We expanded the implementation-details paragraph so the split counts and multi-seed setup are explicit and reproducible. |

## reviewer_2

### reviewer_2_thread_001

- 原始线程: Please add multi-seed stability results and a figure.
- 归一化摘要: Request multi-seed stability evidence.
- 最终行已就绪: yes

| 回复顺序 | 角色 | `comment_id` | Canonical 摘要 | 已选 manuscript copy 摘要 |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_004 | Add multi-seed stability evidence and a figure. | L1 sections/results.tex::Stability Analysis::figure 2 / v2=Top-1 accuracy across five random seeds for the multimodal transformer., L2 sections/results.tex::Stability Analysis::paragraph 2 / v2=Across five random seeds, the mean macro-F1 remains stable and the spread stays narrow enough to support the robustness claim. |

#### 最终行预览

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please add a multi-seed stability experiment with a table or figure to demonstrate robustness. | sections/results.tex::Stability Analysis::paragraph 1-2; figures/seed-stability-figure.svg | Across five random seeds, the mean macro-F1 remains stable and the spread stays narrow enough to support the robustness claim. | We performed the requested five-seed stability experiment, added a dedicated Stability Analysis subsection, and included a figure plus summary statistics to document the robustness trend. |

### reviewer_2_thread_002

- 原始线程: Please justify the baseline comparison more clearly and expand the limitations discussion.
- 归一化摘要: Repeat the baseline question and ask for stronger limitations.
- 最终行已就绪: yes

| 回复顺序 | 角色 | `comment_id` | Canonical 摘要 | 已选 manuscript copy 摘要 |
| --- | --- | --- | --- | --- |
| 1 | merged_duplicate | atomic_001 | Explain why the main method outperforms the baseline. | L1 sections/results.tex::Main Comparison::paragraph 2 / v2=The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. |
| 2 | primary | atomic_005 | Expand limitations and discussion. | L1 sections/discussion.tex::Limitations::paragraph 1 / v2=Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. |

#### 最终行预览

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please justify the baseline comparison more clearly and also expand the discussion of limitations and deployment constraints. | sections/results.tex::Main Comparison::paragraph 2; sections/discussion.tex::Limitations::paragraph 1-2 | The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. | We addressed this thread in two coordinated parts. First, we strengthened the baseline-comparison explanation with a mechanism-based account shared with Reviewer 1. Second, we expanded the Discussion section to state the main limitations, deployment constraints, and calibration caveats explicitly. |

