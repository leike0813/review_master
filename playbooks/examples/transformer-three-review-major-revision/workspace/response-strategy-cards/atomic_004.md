# Response Strategy Card: atomic_004

这张卡是从数据库渲染出的单 canonical atomic item 只读策略视图。数据库真源包括 `atomic_comments`、`raw_thread_atomic_links`、`atomic_comment_state`、`atomic_comment_target_locations`、`strategy_cards`、`strategy_card_actions`、`strategy_action_target_locations`、`strategy_card_evidence_items`、`strategy_card_pending_confirmations` 和 `comment_completion_status`。一张卡只服务一个 `comment_id`。

## Header

| Field | Value |
| --- | --- |
| `comment_id` | atomic_004 |
| Source reviewers | reviewer_1 |
| Source threads | reviewer_1_thread_005 |
| `status` | ready |
| `priority` | high |
| `evidence_gap` | no |
| Target locations | sections/results.tex::Machine Translation::paragraph 2 |

## Canonical Atomic Item

- Canonical summary: Explain the mechanism behind the baseline gain in the main results.
- Required action: Provide a causal explanation for why the Transformer improves over baselines.

## Response Stance

- Proposed stance: Accept and strengthen the mechanism-based explanation of the main baseline gain.
- Why this stance is defensible: Round 1 focuses on atomic_004 because its revision depends on the current supplement tranche.

## Planned Manuscript Actions

| Action ID | Manuscript Change | Target Locations | Expected Response-Letter Effect |
| --- | --- | --- | --- |
| A1 | Revise the main-results discussion to explain why short attention paths plausibly improve the baseline comparison. | sections/results.tex::Machine Translation::paragraph 2 | Provide a direct point-to-point response for atomic_004. |

## Required Evidence

| Evidence ID | Required Material | Available Now (`yes/no`) | Gap Note |
| --- | --- | --- | --- |
| E1 | existing results paragraph plus round-1 mechanism note | yes | This comment can be revised once the mechanism framing is stabilized. |

## Pending Confirmations

- None

## Completion Definition

- [x] 稿件修改已执行
- [x] 对应 response 段落已生成
- [x] 证据缺口已关闭
- [x] 用户已确认该条策略
