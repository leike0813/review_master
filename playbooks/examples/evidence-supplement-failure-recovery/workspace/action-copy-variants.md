# Action Copy Variants

这是从 `review-master.db` 渲染出的 Stage 6 文案版本视图。数据库真源是 `action_copy_variants` 与 `selected_action_copy_variants`。这里的 3 个版本，指的是最终稿里真正要落下去的 manuscript 局部落稿文本版本，而不是策略版本，也不是 response-side 方案版本。若一个 action 覆盖多个位置，则每个位置都必须各自提供一组 `v1/v2/v3`。

## atomic_001 / action 1

- Manuscript change: Expand the baseline-comparison explanation in the results discussion.
- Expected response effect: Supports both reviewer threads tied to the shared baseline concern.

### location 1

- Target location: sections/results.tex::Main Comparison::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The multimodal transformer improves top-1 accuracy because contextual fusion reduces confusion between visually similar stress patterns while preserving the spectral cues needed for class separation. | Conservative explanation that remains close to the Stage 5 draft structure. |
| v2 | yes | The multimodal encoder improves separation because contextual fusion reduces confusion between visually similar stress patterns while preserving spectral contrast cues. | Balanced final sentence aligned with the marked and clean manuscript. |
| v3 | no | The main gain comes from contextual fusion, which preserves spectral contrast cues and reduces confusion between visually similar stress patterns more effectively than the baselines. | Stronger final sentence for users who want a firmer causal claim. |

## atomic_002 / action 1

- Manuscript change: Add a scoped ablation rationale paragraph to the results discussion.
- Expected response effect: Explains why a full ablation is not included while addressing the review point.

### location 1

- Target location: sections/results.tex::Ablation Placeholder::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Removing either the image branch or the spectral branch degrades performance, which indicates that both modalities contribute to the final gain. | Shortest ablation sentence that stays close to the manuscript tone. |
| v2 | yes | Removing either the image branch or the spectral branch weakens performance, indicating that the gain comes from complementary cross-modal evidence rather than a single dominant stream. | Balanced final ablation sentence chosen for the revised manuscript. |
| v3 | no | Ablation results show that performance drops whenever one modality is removed, confirming that the improvement depends on complementary cross-modal evidence rather than one dominant stream. | More explicit ablation interpretation for users who want a firmer claim. |

## atomic_003 / action 1

- Manuscript change: Clarify data splits and seeds in the method section.
- Expected response effect: Lets the response point to explicit reproducibility details.

### location 1

- Target location: sections/method.tex::Implementation Details::paragraph 3

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | We use a fixed train/validation/test split of 640/160/200 plots and repeat all stochastic experiments with seeds 11, 17, 23, 29, and 37. | Shortest reproducibility sentence that directly states the split and seeds. |
| v2 | yes | We use a fixed train/validation/test split of 640/160/200 plots and repeat all stochastic experiments with seeds 11, 17, 23, 29, and 37. | Balanced final reproducibility sentence chosen for the revised manuscript. |
| v3 | no | For reproducibility, we keep a fixed 640/160/200 train/validation/test split and rerun all stochastic experiments with seeds 11, 17, 23, 29, and 37. | Slightly more explicit reproducibility framing for users who prefer stronger signposting. |

## atomic_004 / action 1

- Manuscript change: Add the multi-seed stability figure and describe the trend.
- Expected response effect: Directly answers the new-evidence request.

### location 1

- Target location: sections/results.tex::Stability Analysis::figure 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Top-1 accuracy across five random seeds for the multimodal transformer. | Shortest figure caption that stays close to the current draft. |
| v2 | yes | Top-1 accuracy across five random seeds for the multimodal transformer. | Balanced final caption aligned with the exported figure. |
| v3 | no | Top-1 accuracy across five random seeds, showing the stability of the multimodal transformer across random initializations. | Longer caption for users who want the stability point spelled out in the figure caption. |

### location 2

- Target location: sections/results.tex::Stability Analysis::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Across five random seeds, the mean top-1 accuracy remains 91.92 and the standard deviation stays below 0.2, indicating that the reported improvement is stable across random initializations. | Direct numeric summary with minimal extra interpretation. |
| v2 | yes | Across five random seeds, the mean macro-F1 remains stable and the spread stays narrow enough to support the robustness claim. | Balanced final sentence aligned with the marked manuscript and response letter. |
| v3 | no | The five-seed experiment shows a stable mean performance and only narrow variation, which supports the robustness claim across random initializations. | More interpretive sentence for users who prefer less metric-heavy wording. |

## atomic_005 / action 1

- Manuscript change: Expand the limitations and discussion section.
- Expected response effect: Responds to the request for a stronger discussion of limitations.

### location 1

- Target location: sections/discussion.tex::Limitations::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. | Shortest limitation sentence that captures the main caveat. |
| v2 | yes | Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. | Balanced limitation sentence aligned with the marked manuscript and response letter. |
| v3 | no | The current study is limited to the present sensing setup, and deployment will still require calibration when lighting or sensor conditions shift. | Alternative limitation sentence with a slightly broader deployment framing. |

