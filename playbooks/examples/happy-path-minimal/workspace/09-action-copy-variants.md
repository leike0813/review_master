# Action Copy Variants

这是从 `review-master.db` 渲染出的 Stage 6 文案版本视图。数据库真源是 `action_copy_variants` 与 `selected_action_copy_variants`。这里的 3 个版本，指的是最终稿里真正要落下去的 manuscript 局部落稿文本版本，而不是策略版本，也不是 response-side 方案版本。若一个 action 覆盖多个位置，则每个位置都必须各自提供一组 `v1/v2/v3`。

## atomic_001 / action 1

- 稿件修改动作: Expand the causal explanation for the baseline advantage in the Results discussion.
- 预期回复效果: Allows the reply to explain why the method is better than the baseline.

### 位置 1

- 目标位置: main.tex::Results::paragraph 2

#### 稿件最终落稿

| 版本 | 已选中 | 版本文本 | 理由 |
| --- | --- | --- | --- |
| v1 | no | The transformer improves top-1 accuracy by 2.7 points over the CNN baseline because global attention reduces confusion between visually similar leaf patterns while preserving lesion structure. | Conservative final sentence that keeps the original quantitative framing. |
| v2 | yes | The transformer improves performance because global-context modeling reduces confusion between visually similar disease patterns while retaining discriminative lesion structure. | Balanced final sentence aligned with the selected revised manuscript wording. |
| v3 | no | The transformer outperforms the CNN baseline because global-context modeling preserves discriminative lesion structure while reducing confusion between visually similar disease patterns. | A slightly stronger but still author-consistent final sentence. |

## atomic_001 / action 2

- 稿件修改动作: Add a sentence that points to the exact result paragraph supporting the claim.
- 预期回复效果: Lets the response cite the supporting evidence location clearly.

### 位置 1

- 目标位置: main.tex::Results::paragraph 3

#### 稿件最终落稿

| 版本 | 已选中 | 版本文本 | 理由 |
| --- | --- | --- | --- |
| v1 | no | The mechanism-focused explanation is discussed in the paragraph immediately below Table 2. | Shortest signpost sentence that stays close to the Stage 5 draft. |
| v2 | yes | The supporting evidence for this mechanism-based explanation is provided in the paragraph immediately below Table 2. | Balanced signpost sentence chosen for the final manuscript. |
| v3 | no | We discuss the supporting evidence for this interpretation in the paragraph immediately below Table 2, where the gain is tied to global-context modeling. | More explicit signpost for users who prefer a fuller evidence pointer. |

## atomic_002 / action 1

- 稿件修改动作: Add an explicit signpost sentence that points to the relevant result paragraph.
- 预期回复效果: Lets the response cite the exact supporting evidence paragraph.

### 位置 1

- 目标位置: main.tex::Results::paragraph 3

#### 稿件最终落稿

| 版本 | 已选中 | 版本文本 | 理由 |
| --- | --- | --- | --- |
| v1 | no | The mechanism-focused explanation is discussed in the paragraph immediately below Table 2. | Reuses the shortest signpost sentence for the duplicate evidence-pointing action. |
| v2 | yes | The supporting evidence for this mechanism-based explanation is provided in the paragraph immediately below Table 2. | Matches the final manuscript sentence used to resolve the overlapping evidence-location action. |
| v3 | no | The paragraph immediately below Table 2 provides the supporting evidence for this claim and makes the mechanism-focused interpretation explicit. | Longer signpost sentence for users who want more explicit wording. |

