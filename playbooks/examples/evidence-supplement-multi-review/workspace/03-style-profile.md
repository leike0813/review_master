# Style Profile

这是从 `review-master.db` 渲染出的 Stage 2 风格画像视图。数据库真源是 `style_profiles` 与 `style_profile_rules`。后续阶段会把它作为稿件与回复信写作的基线提示。

## manuscript

- 摘要: Preserve the paper's technical, evidence-driven voice across Methods, Results, and Discussion while keeping late-stage additions stylistically consistent.
- 去 AI 化重点: Avoid repetitive booster language, generic claims of impact, and over-explaining transitions that were absent from the original manuscript.

| 规则序号 | 规则类型 | 规则文本 |
| --- | --- | --- |
| 1 | do | Match the terse empirical style already used in the Results and Discussion sections. |
| 2 | do | Keep technical terminology stable across the baseline, ablation, reproducibility, and stability discussions. |
| 3 | anti_ai | Do not add generic significance language unless it is directly supported by the revision. |
| 4 | tone | Measured, technical, and evidence-linked. |

## response_letter

- 摘要: Use concise reviewer-facing prose that names the exact revised location, summarizes the change, and avoids decorative framing.
- 去 AI 化重点: Avoid stock LLM apology phrases and broad claims not tied to the selected action-level revisions.

| 规则序号 | 规则类型 | 规则文本 |
| --- | --- | --- |
| 1 | do | Answer each reviewer thread with explicit location, scope, and concrete revision evidence. |
| 2 | do | When one thread aggregates multiple atomic items, keep the response row cohesive but still point to each revised range. |
| 3 | anti_ai | Avoid ceremonial gratitude or generic reassurance without manuscript-level evidence. |
| 4 | tone | Respectful, precise, and point-to-point. |

