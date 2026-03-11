# Response Strategy Card: atomic_005

这张卡是从数据库渲染出的单 canonical atomic item 只读策略视图。数据库真源包括 `atomic_comments`、`raw_thread_atomic_links`、`atomic_comment_state`、`atomic_comment_target_locations`、`strategy_cards`、`strategy_card_actions`、`strategy_action_target_locations`、`strategy_card_evidence_items`、`strategy_card_pending_confirmations` 和 `comment_completion_status`。一张卡只服务一个 `comment_id`。

## Header

| Field | Value |
| --- | --- |
| `comment_id` | atomic_005 |
| Source reviewers | reviewer_2 |
| Source threads | reviewer_2_thread_002 |
| `status` | ready |
| `priority` | medium |
| `evidence_gap` | no |
| Target locations | sections/discussion.tex::Limitations::paragraph 1 |

## Canonical Atomic Item

- Canonical summary: Expand limitations and discussion.
- Required action: Strengthen the limitations section.

## Response Stance

- Proposed stance: accept_and_expand
- Why this stance is defensible: The limitations section is now explicitly expanded.

## Planned Manuscript Actions

| Action ID | Manuscript Change | Target Locations | Expected Response-Letter Effect |
| --- | --- | --- | --- |
| A1 | Expand the limitations and discussion section. | sections/discussion.tex::Limitations::paragraph 1 | Responds to the request for a stronger discussion of limitations. |

## Manuscript Drafts

| Action ID | Location | Target Location | Draft Text | Rationale |
| --- | --- | --- | --- | --- |
| A1 | L1 | sections/discussion.tex::Limitations::paragraph 1 | Our evaluation is limited to the current sensing setup and still requires deployment-time calibration under distribution shift. | Recovered from the selected Stage 6 manuscript variant to preserve replay continuity after Stage 5 draft-model migration. |

## Response Draft

- Draft text: We addressed this thread in two coordinated parts. First, we strengthened the baseline-comparison explanation with a mechanism-based account shared with Reviewer 1. Second, we expanded the Discussion section to state the main limitations, deployment constraints, and calibration caveats explicitly.
- Rationale: Recovered from existing thread-level response content after Stage 5 draft-model migration.

## Required Evidence

| Evidence ID | Required Material | Available Now (`yes/no`) | Gap Note |
| --- | --- | --- | --- |
|  |  |  |  |

## Pending Confirmations

- None

## Comment Blockers

- None

## Completion Definition

- [x] 稿件修改草案已形成
- [x] 对应 response 草案已形成
- [x] 证据缺口已关闭
- [x] 用户已确认该条策略
