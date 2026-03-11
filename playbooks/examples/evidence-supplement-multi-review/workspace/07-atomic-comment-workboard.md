# Atomic Comment Workboard

这是 Stage 4 的主视图。数据库真源是 `atomic_comment_state`、`atomic_comment_target_locations`、`atomic_comment_analysis_links`、`atomic_comments` 和 `raw_thread_atomic_links`。用户在 Stage 4 主要通过它确认 canonical atomic item 的优先级、依赖、证据缺口和下一步动作。

## Atomic Workboard 表

| `comment_id` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | 分析摘要 | `user_confirmation_needed` | `next_action` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_2 | reviewer_1_thread_001, reviewer_2_thread_002 | ready | high | no | sections/results.tex::Main Comparison::paragraph 2 | claim_001 | evidence: Main result table | gap: Need a clearer rationale for why the baseline gap appears. | no | enter_stage_5 |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | ready | medium | no | sections/results.tex::Ablation Placeholder::paragraph 1 | claim_001 | evidence: Method section component list | gap: Need an explicit ablation explanation or rationale. | no | enter_stage_5 |
| atomic_003 | reviewer_1 | reviewer_1_thread_003 | ready | medium | no | sections/method.tex::Implementation Details::paragraph 3 | claim_001 | evidence: Implementation details paragraph | gap: Need to clarify splits and seeds for reproducibility. | no | enter_stage_5 |
| atomic_004 | reviewer_2 | reviewer_2_thread_001 | blocked | high | yes | sections/results.tex::Stability Analysis::figure placeholder, sections/results.tex::Stability Analysis::paragraph 2 | claim_001 | evidence: Current results lack multi-seed stability evidence | gap: Need new evidence and a figure before closure. | no | enter_stage_5 |
| atomic_005 | reviewer_2 | reviewer_2_thread_002 | ready | medium | no | sections/discussion.tex::Limitations::paragraph 1 | sec_discussion | evidence: Existing discussion paragraph | gap: Need a stronger limitations discussion linked to reviewer concerns. | no | enter_stage_5 |
