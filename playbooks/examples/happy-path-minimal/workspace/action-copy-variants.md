# Action Copy Variants

这是从 `review-master.db` 渲染出的 Stage 6 文案版本视图。数据库真源是 `action_copy_variants` 与 `selected_action_copy_variants`。这里的 3 个版本，指的是最终稿里真正要落下去的 manuscript 局部落稿文本版本，而不是策略版本，也不是 response-side 方案版本。若一个 action 覆盖多个位置，则每个位置都必须各自提供一组 `v1/v2/v3`。

## atomic_001 / action 1

- Manuscript change: Expand the causal explanation for the baseline advantage in the Results discussion.
- Expected response effect: Allows the reply to explain why the method is better than the baseline.

### location 1

- Target location: main.tex::Results::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The transformer improves top-1 accuracy by 2.7 points over the CNN baseline because global attention reduces confusion between visually similar leaf patterns while preserving lesion structure. | Conservative final sentence that keeps the original quantitative framing. |
| v2 | yes | The transformer improves performance because global-context modeling reduces confusion between visually similar disease patterns while retaining discriminative lesion structure. | Balanced final sentence aligned with the selected revised manuscript wording. |
| v3 | no | The transformer outperforms the CNN baseline because global-context modeling preserves discriminative lesion structure while reducing confusion between visually similar disease patterns. | A slightly stronger but still author-consistent final sentence. |

## atomic_001 / action 2

- Manuscript change: Add a sentence that points to the exact result paragraph supporting the claim.
- Expected response effect: Lets the response cite the supporting evidence location clearly.

### location 1

- Target location: main.tex::Results::paragraph 3

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The mechanism-focused explanation is discussed in the paragraph immediately below Table 2. | Shortest signpost sentence that stays close to the Stage 5 draft. |
| v2 | yes | The supporting evidence for this mechanism-based explanation is provided in the paragraph immediately below Table 2. | Balanced signpost sentence chosen for the final manuscript. |
| v3 | no | We discuss the supporting evidence for this interpretation in the paragraph immediately below Table 2, where the gain is tied to global-context modeling. | More explicit signpost for users who prefer a fuller evidence pointer. |

## atomic_002 / action 1

- Manuscript change: Add an explicit signpost sentence that points to the relevant result paragraph.
- Expected response effect: Lets the response cite the exact supporting evidence paragraph.

### location 1

- Target location: main.tex::Results::paragraph 3

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The mechanism-focused explanation is discussed in the paragraph immediately below Table 2. | Reuses the shortest signpost sentence for the duplicate evidence-pointing action. |
| v2 | yes | The supporting evidence for this mechanism-based explanation is provided in the paragraph immediately below Table 2. | Matches the final manuscript sentence used to resolve the overlapping evidence-location action. |
| v3 | no | The paragraph immediately below Table 2 provides the supporting evidence for this claim and makes the mechanism-focused interpretation explicit. | Longer signpost sentence for users who want more explicit wording. |

