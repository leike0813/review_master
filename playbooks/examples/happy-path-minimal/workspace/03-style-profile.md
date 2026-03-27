# Style Profile

这是从 `review-master.db` 渲染出的 Stage 2 风格画像视图。数据库真源是 `style_profiles` 与 `style_profile_rules`。后续阶段会把它作为稿件与回复信写作的基线提示。

## manuscript

- 摘要: Preserve the compact empirical writing style of the original manuscript while making the causal explanation more explicit.
- 去 AI 化重点: Avoid inflated transition phrases, repetitive parallel clauses, and generic self-praise that was absent from the original paper.

| 规则序号 | 规则类型 | 规则文本 |
| --- | --- | --- |
| 1 | do | Prefer short factual sentences that extend the original Results style. |
| 2 | do | Keep terminology consistent with the baseline-comparison language already used in the manuscript. |
| 3 | anti_ai | Do not introduce generic transition filler such as 'notably' or 'importantly' unless the original draft already uses it. |
| 4 | tone | Analytical and restrained, with mechanism-focused explanation. |

## response_letter

- 摘要: Keep the reply concise, evidence-linked, and respectful; answer the reviewer directly without verbose framing.
- 去 AI 化重点: Avoid stock apology formulas, generic enthusiasm, and abstract claims that are not anchored to the manuscript revision.

| 规则序号 | 规则类型 | 规则文本 |
| --- | --- | --- |
| 1 | do | State the concrete manuscript change before elaborating on its purpose. |
| 2 | do | Point to the revised paragraph by location rather than by vague narrative reference. |
| 3 | anti_ai | Avoid overlong gratitude or apology preambles. |
| 4 | tone | Direct, respectful, and point-to-point. |

