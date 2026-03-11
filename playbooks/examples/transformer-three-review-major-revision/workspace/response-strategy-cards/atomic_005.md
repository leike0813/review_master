# Response Strategy Card: atomic_005

这张卡是从数据库渲染出的单 canonical atomic item 只读策略视图。数据库真源包括 `atomic_comments`、`raw_thread_atomic_links`、`atomic_comment_state`、`atomic_comment_target_locations`、`strategy_cards`、`strategy_card_actions`、`strategy_action_target_locations`、`strategy_card_evidence_items`、`strategy_card_pending_confirmations` 和 `comment_completion_status`。一张卡只服务一个 `comment_id`。

## Header

| Field | Value |
| --- | --- |
| `comment_id` | atomic_005 |
| Source reviewers | reviewer_2 |
| Source threads | reviewer_2_thread_001, reviewer_2_thread_002 |
| `status` | ready |
| `priority` | high |
| `evidence_gap` | yes |
| Target locations | sections/training.tex::Data::paragraph 1, sections/training.tex::Implementation Notes::paragraph 1 |

## Canonical Atomic Item

- Canonical summary: Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details.
- Required action: Make the training and decoding protocol reproducible.

## Response Stance

- Proposed stance: Accept and restore all replication-critical protocol details.
- Why this stance is defensible: Round 1 focuses on atomic_005 because its revision depends on the current supplement tranche.

## Planned Manuscript Actions

| Action ID | Manuscript Change | Target Locations | Expected Response-Letter Effect |
| --- | --- | --- | --- |
| A1 | Restore WMT data, preprocessing, checkpoint averaging, and beam-search details in the training section. | sections/training.tex::Data::paragraph 1, sections/training.tex::Implementation Notes::paragraph 1 | Provide a direct point-to-point response for atomic_005. |

## Manuscript Drafts

| Action ID | Location | Target Location | Draft Text | Rationale |
| --- | --- | --- | --- | --- |
| A1 | L1 | sections/training.tex::Data::paragraph 1 | English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. | Recovered from the selected Stage 6 manuscript variant to preserve replay continuity after Stage 5 draft-model migration. |
| A1 | L2 | sections/training.tex::Implementation Notes::paragraph 1 | English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. | Recovered from the selected Stage 6 manuscript variant to preserve replay continuity after Stage 5 draft-model migration. |

## Response Draft

- Draft text: We restored the data, preprocessing, and evaluation protocol details needed for replication.

We made checkpoint averaging and decoding settings explicit in the training section.
- Rationale: Recovered from existing thread-level response content after Stage 5 draft-model migration.

## Required Evidence

| Evidence ID | Required Material | Available Now (`yes/no`) | Gap Note |
| --- | --- | --- | --- |
| E1 | round-1 reproducibility materials | yes | Need protocol and decoding details. |

## Pending Confirmations

- None

## Comment Blockers

- None

## Completion Definition

- [x] 稿件修改草案已形成
- [x] 对应 response 草案已形成
- [x] 证据缺口已关闭
- [x] 用户已确认该条策略
