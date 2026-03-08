# Style Profile

这是从 `review-master.db` 渲染出的 Stage 6 全局风格画像视图。数据库真源是 `style_profiles` 与 `style_profile_rules`。Stage 6 必须先完成风格画像，再进入文案版本生成与最终成文。

## manuscript

- Summary: Preserve the compact empirical writing style of the original manuscript while making the causal explanation more explicit.
- Anti-AI Focus: Avoid inflated transition phrases, repetitive parallel clauses, and generic self-praise that was absent from the original paper.

| Rule Order | Rule Type | Rule Text |
| --- | --- | --- |
| 1 | do | Prefer short factual sentences that extend the original Results style. |
| 2 | do | Keep terminology consistent with the baseline-comparison language already used in the manuscript. |
| 3 | anti_ai | Do not introduce generic transition filler such as 'notably' or 'importantly' unless the original draft already uses it. |
| 4 | tone | Analytical and restrained, with mechanism-focused explanation. |

## response_letter

- Summary: Keep the reply concise, evidence-linked, and respectful; answer the reviewer directly without verbose framing.
- Anti-AI Focus: Avoid stock apology formulas, generic enthusiasm, and abstract claims that are not anchored to the manuscript revision.

| Rule Order | Rule Type | Rule Text |
| --- | --- | --- |
| 1 | do | State the concrete manuscript change before elaborating on its purpose. |
| 2 | do | Point to the revised paragraph by location rather than by vague narrative reference. |
| 3 | anti_ai | Avoid overlong gratitude or apology preambles. |
| 4 | tone | Direct, respectful, and point-to-point. |

