# Atomic Comment Workboard

这是贯穿 Stage 4-6 的主工作板视图。数据库真源包括 `atomic_comment_state`、`atomic_comment_target_locations`、`atomic_comment_analysis_links`、`atomic_comments`、`raw_thread_atomic_links`、`strategy_cards`、`comment_completion_status`、`comment_blockers` 与补材建议/接收关系。用户在 Stage 4 用它确认 planning，在 Stage 5/6 用它跟踪执行与闭环状态。

## Atomic Workboard 表

| `comment_id` | `active_comment` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | 分析摘要 | `next_action` | `strategy_card_present` | `user_strategy_confirmed` | `comment_blockers` | `supplement_suggestions` | `supplement_intake_links` | `manuscript_execution_items_done` | `response_draft_done` | `one_to_one_link_checked` | `export_ready` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | no | reviewer_1, reviewer_2 | reviewer_1_thread_001, reviewer_2_thread_002 | ready | high | no | sections/results.tex::Main Comparison::paragraph 2 | claim_001 | evidence: Main result table | gap: Need a clearer rationale for why the baseline gap appears. | enter_stage_5 | yes | yes | 0 | 0 | 0 | yes | yes | yes | yes |
| atomic_002 | no | reviewer_1 | reviewer_1_thread_002 | ready | medium | no | sections/results.tex::Ablation Placeholder::paragraph 1 | claim_001 | evidence: Method section component list | gap: Need an explicit ablation explanation or rationale. | enter_stage_5 | yes | yes | 0 | 0 | 0 | yes | yes | yes | yes |
| atomic_003 | no | reviewer_1 | reviewer_1_thread_003 | ready | medium | no | sections/method.tex::Implementation Details::paragraph 3 | claim_001 | evidence: Implementation details paragraph | gap: Need to clarify splits and seeds for reproducibility. | enter_stage_5 | yes | yes | 0 | 0 | 0 | yes | yes | yes | yes |
| atomic_004 | no | reviewer_2 | reviewer_2_thread_001 | blocked | high | yes | sections/results.tex::Stability Analysis::figure placeholder, sections/results.tex::Stability Analysis::paragraph 2 | claim_001 | evidence: Current results lack multi-seed stability evidence | gap: Need new evidence and a figure before closure. | enter_stage_5 | yes | yes | 0 | 1 | 0 | yes | yes | yes | yes |
| atomic_005 | no | reviewer_2 | reviewer_2_thread_002 | ready | medium | no | sections/discussion.tex::Limitations::paragraph 1 | sec_discussion | evidence: Existing discussion paragraph | gap: Need a stronger limitations discussion linked to reviewer concerns. | enter_stage_5 | yes | yes | 0 | 0 | 0 | yes | yes | yes | yes |
