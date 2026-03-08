# Style Profile

这是从 `review-master.db` 渲染出的 Stage 6 全局风格画像视图。数据库真源是 `style_profiles` 与 `style_profile_rules`。Stage 6 必须先完成风格画像，再进入文案版本生成与最终成文。

## manuscript

- Summary: Keep claims precise, benchmark-tied, and mechanism-oriented without overselling novelty.
- Anti-AI Focus: Avoid inflated novelty rhetoric, universal claims, or unsupported causal language.

| Rule Order | Rule Type | Rule Text |
| --- | --- | --- |
| 1 | do | State the strongest claim only where benchmark evidence directly supports it. |
| 2 | anti_ai | Prefer concrete model, dataset, and error-analysis details over generic praise of the method. |

## response_letter

- Summary: Be direct, evidence-backed, and explicit about what was added, clarified, or softened.
- Anti-AI Focus: Do not sound defensive or overclaim what the new evidence proves.

| Rule Order | Rule Type | Rule Text |
| --- | --- | --- |
| 1 | do | Tie every reply to a concrete manuscript location or supplement artifact. |
| 2 | tone | Acknowledge reviewer concerns and explain the exact revision without rhetorical flourish. |

