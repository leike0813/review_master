# Response Strategy Card: atomic_001

这张卡是从数据库渲染出的单 canonical atomic item 只读策略视图。数据库真源包括 `atomic_comments`、`raw_thread_atomic_links`、`atomic_comment_state`、`atomic_comment_target_locations`、`strategy_cards`、`strategy_card_actions`、`strategy_action_target_locations`、`strategy_card_evidence_items`、`strategy_card_pending_confirmations` 和 `comment_completion_status`。一张卡只服务一个 `comment_id`。

## Header

| Field | Value |
| --- | --- |
| `comment_id` | atomic_001 |
| Source reviewers | reviewer_1, reviewer_3 |
| Source threads | reviewer_1_thread_001, reviewer_3_thread_004 |
| `status` | ready |
| `priority` | high |
| `evidence_gap` | yes |
| Target locations | sections/introduction.tex::Introduction::paragraph 3, sections/results.tex::Machine Translation::paragraph 2 |

## Canonical Atomic Item

- Canonical summary: Explain why attention-only can replace recurrence and convolution in this translation setting.
- Required action: Add a concrete mechanism-based explanation of the attention-only claim.

## Response Stance

- Proposed stance: Accept and clarify the mechanism claim without overstating universality.
- Why this stance is defensible: Round 1 focuses on atomic_001 because its revision depends on the current supplement tranche.

## Planned Manuscript Actions

| Action ID | Manuscript Change | Target Locations | Expected Response-Letter Effect |
| --- | --- | --- | --- |
| A1 | Revise the introduction and main-results explanation to state why short attention paths help long-range dependency modeling. | sections/introduction.tex::Introduction::paragraph 3, sections/results.tex::Machine Translation::paragraph 2 | Provide a direct point-to-point response for atomic_001. |

## Manuscript Drafts

| Action ID | Location | Target Location | Draft Text | Rationale |
| --- | --- | --- | --- | --- |
| A1 | L1 | sections/introduction.tex::Introduction::paragraph 3 | Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. | Recovered from the selected Stage 6 manuscript variant to preserve replay continuity after Stage 5 draft-model migration. |
| A1 | L2 | sections/results.tex::Machine Translation::paragraph 2 | Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. | Recovered from the selected Stage 6 manuscript variant to preserve replay continuity after Stage 5 draft-model migration. |

## Response Draft

- Draft text: We revised the introduction to explain why attention-only modeling helps beyond improved parallelism.

We paired the high-level intuition with a concrete long-range dependency example.
- Rationale: Recovered from existing thread-level response content after Stage 5 draft-model migration.

## Required Evidence

| Evidence ID | Required Material | Available Now (`yes/no`) | Gap Note |
| --- | --- | --- | --- |
| E1 | round-1 method positioning note | yes | Need the recovered mechanism explanation. |

## Pending Confirmations

- None

## Comment Blockers

- None

## Completion Definition

- [x] 稿件修改草案已形成
- [x] 对应 response 草案已形成
- [x] 证据缺口已关闭
- [x] 用户已确认该条策略
