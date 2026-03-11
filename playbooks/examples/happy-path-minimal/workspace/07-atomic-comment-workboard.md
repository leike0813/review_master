# Atomic Comment Workboard

这是 Stage 4 的主视图。数据库真源是 `atomic_comment_state`、`atomic_comment_target_locations`、`atomic_comment_analysis_links`、`atomic_comments` 和 `raw_thread_atomic_links`。用户在 Stage 4 主要通过它确认 canonical atomic item 的优先级、依赖、证据缺口和下一步动作。

## Atomic Workboard 表

| `comment_id` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | 分析摘要 | `user_confirmation_needed` | `next_action` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1 | reviewer_1_thread_001 | ready | high | no | main.tex::Results::paragraph 2 | claim_001 | evidence: Main comparison sentence in Results | gap: Need a more explicit causal explanation. | no | enter_stage_5 |
| atomic_002 | reviewer_1 | reviewer_1_thread_001 | ready | medium | no | main.tex::Results::paragraph 3 | claim_001 | evidence: Results discussion paragraph | gap: Need to point the reviewer to the supporting location. | no | enter_stage_5 |
