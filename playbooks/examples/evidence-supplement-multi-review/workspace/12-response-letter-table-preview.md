# Response Letter Table Preview

This is the final Response Letter Markdown preview rendered from `review-master.db`. Its source of truth is `response_thread_rows`. The final output must preserve one point-to-point table row per original reviewer thread.

## reviewer_1

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please explain why the proposed multimodal transformer outperforms the baseline methods in the main results. | sections/results.tex::Main Comparison::paragraph 2 | The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. | We revised the main-comparison discussion to give a mechanism-based explanation of the baseline gain. This response also supports the overlapping baseline-justification concern raised by Reviewer 2. |
| Please include an ablation that clarifies the contribution of the image and spectral branches. | sections/results.tex::Ablation Discussion::paragraph 1 | Removing either the image branch or the spectral branch weakens performance, indicating that the gain comes from complementary cross-modal evidence rather than a single dominant stream. | We added a focused ablation explanation to clarify the role of each modality without overstating the scope of the experiment. |
| Please clarify the train/validation/test split and the random seed configuration so that the work is reproducible. | sections/method.tex::Implementation Details::paragraph 3 | We use a fixed train/validation/test split of 640/160/200 plots and repeat all stochastic experiments with seeds 11, 17, 23, 29, and 37. | We expanded the implementation-details paragraph so the split counts and multi-seed setup are explicit and reproducible. |

## reviewer_2

| Original Comment | Modification Scope | Key Revision Excerpt | Response Explanation |
| --- | --- | --- | --- |
| Please add a multi-seed stability experiment with a table or figure to demonstrate robustness. | sections/results.tex::Stability Analysis::paragraph 1-2; figures/seed-stability-figure.svg | Across five random seeds, the mean macro-F1 remains stable and the spread stays narrow enough to support the robustness claim. | We performed the requested five-seed stability experiment, added a dedicated Stability Analysis subsection, and included a figure plus summary statistics to document the robustness trend. |
| Please justify the baseline comparison more clearly and also expand the discussion of limitations and deployment constraints. | sections/results.tex::Main Comparison::paragraph 2; sections/discussion.tex::Limitations::paragraph 1-2 | The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. | We addressed this thread in two coordinated parts. First, we strengthened the baseline-comparison explanation with a mechanism-based account shared with Reviewer 1. Second, we expanded the Discussion section to state the main limitations, deployment constraints, and calibration caveats explicitly. |

