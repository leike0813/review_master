# review-master Evidence Supplement Playbook

## Purpose

这份 playbook 演示 SQLite 唯一真源模式下的复杂成功路径。

特点：

- 多文件 LaTeX 工程
- 2 位 reviewer
- 5 个原始 reviewer thread
- 5 条 canonical atomic item
- 其中 1 条 atomic item 被两个 reviewer thread 共享
- 1 次 `stage_5 blocked -> 用户补材 -> 解除 blocked`
- Stage 5 强制补材文件级 intake 判定与 accepted 落地映射
- 演示一次中断后重新进入，同样先恢复再继续
- Agent 只写数据库，用户只读渲染视图

## Example Assets

- 输入：
  - `playbooks/examples/evidence-supplement-multi-review/inputs/manuscript/`
  - `playbooks/examples/evidence-supplement-multi-review/inputs/review-comments.md`
- 用户补材：
  - `playbooks/examples/evidence-supplement-multi-review/user-supplements/`
- 最终态 workspace：
  - `playbooks/examples/evidence-supplement-multi-review/workspace/`
- 最终输出：
  - `playbooks/examples/evidence-supplement-multi-review/outputs/marked-manuscript/`
  - `playbooks/examples/evidence-supplement-multi-review/outputs/revised-manuscript/`
  - `playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.md`
  - `playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.tex`
- `gate-and-render` 输出（保存在 `gate-and-render-output/` 目录）：
  - `playbooks/examples/evidence-supplement-multi-review/gate-and-render-output/`

## Fixed Canonical Atomic Items

- `atomic_001`：解释主方法为何优于 baseline
- `atomic_002`：补充 ablation 说明
- `atomic_003`：澄清数据划分与复现设置
- `atomic_004`：新增多随机种子稳定性实验与图表
- `atomic_005`：扩展 limitations/discussion

其中：

- `atomic_001` 同时服务 `reviewer_1_thread_001` 与 `reviewer_2_thread_002`
- 只有 `atomic_004` 触发显式 evidence gap

## Walkthrough

### Stage 1

Agent 调用：

```bash
python -u review-master/scripts/detect_main_tex.py \
  --manuscript-source playbooks/examples/evidence-supplement-multi-review/inputs/manuscript

python -u review-master/scripts/init_artifact_workspace.py \
  --artifact-root playbooks/examples/evidence-supplement-multi-review/workspace
```

Agent 写入：

- 初始化 `review-master.db`
- 采用 `recipe_stage1_set_entry_state`
- 更新表：
  - `workflow_state`

`gate-and-render` 输出：

- `stage-1-entry-ready.json`
- `recommended_next_action.recipe_id = recipe_stage2_upsert_manuscript_summary`

`gate-and-render` 更新视图：

- `agent-resume.md`
- `manuscript-structure-summary.md`
- `raw-review-thread-list.md`
- `atomic-review-comment-list.md`
- `thread-to-atomic-mapping.md`
- `atomic-comment-workboard.md`
- `supplement-intake-plan.md`

### Stage 2

Agent 写入数据库：

- `manuscript_summary`
- `manuscript_sections`
- `manuscript_claims`
- 采用 `recipe_stage2_upsert_manuscript_summary`
- 更新表：
  - `manuscript_summary`
  - `manuscript_sections`
  - `manuscript_claims`
  - `workflow_state`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE manuscript_summary
SET main_entry = 'main.tex',
    project_shape = 'latex_project',
    high_risk_areas = 'Methods; Results; Discussion'
WHERE id = 1;

DELETE FROM manuscript_claims;
INSERT INTO manuscript_claims (
  claim_id,
  core_claim,
  main_evidence,
  supporting_section_ids,
  risk_level
) VALUES (
  'claim_001',
  'The proposed training pipeline improves robustness under limited labels.',
  'Main result table and discussion paragraph',
  'sec_methods,sec_results',
  'high'
);
```

`gate-and-render` 输出：

- `stage-2-structure-ready.json`
- `recommended_next_action.recipe_id = recipe_stage3_replace_threaded_atomic_model`

`gate-and-render` 更新视图：

- `manuscript-structure-summary.md`
- `agent-resume.md`
- `supplement-intake-plan.md`

### Stage 3

Agent 原子化后写入：

- `raw_review_threads`
- `atomic_comments`
- `raw_thread_atomic_links`
- `atomic_comment_source_spans`
- 采用 `recipe_stage3_replace_threaded_atomic_model`
- 更新表：
  - `raw_review_threads`
  - `atomic_comments`
  - `raw_thread_atomic_links`
  - `atomic_comment_source_spans`
  - `workflow_state`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
DELETE FROM atomic_comment_source_spans;
DELETE FROM raw_thread_atomic_links;
DELETE FROM atomic_comments;
DELETE FROM raw_review_threads;

INSERT INTO raw_review_threads (
  thread_id,
  reviewer_id,
  thread_order,
  source_type,
  original_text,
  normalized_summary
) VALUES
  ('reviewer_1_thread_001', 'reviewer_1', 1, 'reviewer_comment', 'Please explain why your method is better than the baseline.', 'Explain why the method is better than the baseline.'),
  ('reviewer_1_thread_002', 'reviewer_1', 2, 'reviewer_comment', 'Add an ablation study or explain the missing components.', 'Request ablation justification.'),
  ('reviewer_1_thread_003', 'reviewer_1', 3, 'reviewer_comment', 'Clarify data splits and reproducibility settings.', 'Clarify splits and reproducibility.'),
  ('reviewer_2_thread_001', 'reviewer_2', 1, 'reviewer_comment', 'Please add multi-seed stability results and a figure.', 'Request multi-seed stability evidence.'),
  ('reviewer_2_thread_002', 'reviewer_2', 2, 'reviewer_comment', 'Please justify the baseline comparison more clearly and expand the limitations discussion.', 'Repeat the baseline question and ask for stronger limitations.');

INSERT INTO atomic_comments (
  comment_id,
  comment_order,
  canonical_summary,
  required_action
) VALUES
  ('atomic_001', 1, 'Explain why the main method outperforms the baseline.', 'Explain the baseline comparison more clearly.'),
  ('atomic_002', 2, 'Provide an ablation explanation.', 'Explain the missing ablation components.'),
  ('atomic_003', 3, 'Clarify data split and reproducibility settings.', 'Clarify splits and reproducibility details.'),
  ('atomic_004', 4, 'Add multi-seed stability evidence and a figure.', 'Add multi-seed results and a stability figure.'),
  ('atomic_005', 5, 'Expand limitations and discussion.', 'Strengthen the limitations section.');

INSERT INTO raw_thread_atomic_links (thread_id, comment_id, link_order) VALUES
  ('reviewer_1_thread_001', 'atomic_001', 1),
  ('reviewer_1_thread_002', 'atomic_002', 1),
  ('reviewer_1_thread_003', 'atomic_003', 1),
  ('reviewer_2_thread_001', 'atomic_004', 1),
  ('reviewer_2_thread_002', 'atomic_001', 1),
  ('reviewer_2_thread_002', 'atomic_005', 2);
```

`gate-and-render` 输出：

- `stage-3-atomic-ready.json`
- `recommended_next_action.recipe_id = recipe_stage4_upsert_atomic_workboard`

`gate-and-render` 更新视图：

- `raw-review-thread-list.md`
- `atomic-review-comment-list.md`
- `thread-to-atomic-mapping.md`
- `agent-resume.md`
- `supplement-intake-plan.md`

### Stage 4

Agent 写入：

- `atomic_comment_state`
- `atomic_comment_target_locations`
- `atomic_comment_analysis_links`
- `workflow_state`
- `workflow_pending_user_confirmations`
- 采用：
  - `recipe_stage4_upsert_atomic_workboard`
  - `recipe_stage4_set_pending_confirmations`
- 更新表：
  - `atomic_comment_state`
  - `atomic_comment_target_locations`
  - `atomic_comment_analysis_links`
  - `workflow_pending_user_confirmations`
  - `workflow_state`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
INSERT INTO atomic_comment_state (
  comment_id,
  status,
  priority,
  evidence_gap,
  user_confirmation_needed,
  next_action
) VALUES (
  'atomic_004',
  'blocked',
  'high',
  'yes',
  'yes',
  'resolve_blockers'
) ON CONFLICT(comment_id) DO UPDATE SET
  status = excluded.status,
  priority = excluded.priority,
  evidence_gap = excluded.evidence_gap,
  user_confirmation_needed = excluded.user_confirmation_needed,
  next_action = excluded.next_action;

INSERT INTO atomic_comment_target_locations (
  comment_id,
  location_order,
  target_location,
  location_role
) VALUES (
  'atomic_004',
  1,
  'results.tex::Stability Analysis::figure placeholder',
  'primary'
);

DELETE FROM workflow_pending_user_confirmations;
INSERT INTO workflow_pending_user_confirmations (position, message)
VALUES (1, 'Please confirm the stage-four processing order and overall revision strategy.');
```

用户阅读：

- `atomic-comment-workboard.md`
- `thread-to-atomic-mapping.md`
- `supplement-intake-plan.md`（此时通常为空态）

`gate-and-render` 输出：

- `stage-4-workboard-confirmation-needed.json`
- `recommended_next_action = request_stage4_confirmation`
- `recommended_next_action.recipe_id = recipe_stage4_set_pending_confirmations`
- `blocked_actions` 包含禁止进入阶段五

### Stage 5A

Agent 先锁定当前条目，并先为无证据缺口的 comment 形成可确认的策略卡。执行前，用户必须先确认该条策略，而不是直接进入草案执行。

Agent 写入：

- `strategy_cards`
- `strategy_card_actions`
- `strategy_card_pending_confirmations`
- `comment_completion_status`
- 采用：
  - `recipe_stage5_set_active_comment`
  - `recipe_stage5_upsert_strategy_card`
  - `recipe_stage5_replace_strategy_actions`
  - `recipe_stage5_replace_strategy_pending_confirmations`
  - `recipe_stage5_upsert_completion_status`

`gate-and-render` 输出：

- `stage-5-comment-ready.json`
- `recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`

`gate-and-render` 更新视图：

- `response-strategy-cards/atomic_001.md`
- `response-letter-outline.md`
- `agent-resume.md`
- `supplement-intake-plan.md`

此时“ready”的含义不是“跳过确认直接执行”，而是：

- 当前策略卡已经成熟到足以面向用户确认
- 用户确认后，Agent 才进入稿件修改草案和 response 段落草案
- 完成标记只能发生在草案与一一对应关系都落地之后

### Stage 5B

当 `active_comment_id = atomic_004` 时，Agent 写入：

- `strategy_cards`
- `strategy_card_evidence_items`
- `strategy_card_pending_confirmations`
- `workflow_global_blockers`
- `supplement_intake_items`
- `supplement_landing_links`
- 采用：
  - `recipe_stage5_set_active_comment`
  - `recipe_stage5_upsert_strategy_card`
  - `recipe_stage5_replace_strategy_evidence`
  - `recipe_stage5_replace_supplement_intake_and_landing`
  - `recipe_stage5_replace_strategy_pending_confirmations`
  - `recipe_stage5_set_blockers`
- 更新表：
  - `workflow_state`
- `strategy_cards`
- `strategy_card_evidence_items`
- `workflow_global_blockers`
- `supplement_intake_items`
- `supplement_landing_links`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_5',
    stage_gate = 'blocked',
    active_comment_id = 'atomic_004',
    next_action = 'resolve_blockers'
WHERE id = 1;

DELETE FROM workflow_global_blockers;
INSERT INTO workflow_global_blockers (position, message)
VALUES (1, 'Need multi-seed stability results and figure for atomic_004.');
```

`gate-and-render` 输出：

- `stage-5-evidence-gap-blocked.json`
- `recommended_next_action = resolve_blockers`
- `recommended_next_action.recipe_id = recipe_stage5_set_blockers`

`gate-and-render` 更新视图：

- `response-strategy-cards/atomic_004.md`
- `atomic-comment-workboard.md`
- `agent-resume.md`
- `supplement-intake-plan.md`

此时若 Session 中断，新的 Session 重新进入时不直接继续改库，而是先重复统一恢复入口：

1. 运行 `gate-and-render`
2. 读取 `instruction_payload.resume_packet`
3. 读取 `agent-resume.md`
4. 根据恢复包确认当前仍停在 `stage_5`，且 `active_comment_id = atomic_004`
5. 再继续请求或吸收补材

用户随后补充：

- `supplement-note.md`
- `stability-results.csv`
- `seed-stability-figure.svg`

Agent 读取补材后，更新数据库并关闭 blocker。补材到位后，仍需先重新确认更新后的策略卡，再进入草案执行。

补材闭环采用：

- `recipe_stage5_replace_strategy_evidence`
- `recipe_stage5_replace_supplement_intake_and_landing`
- `recipe_stage5_replace_strategy_pending_confirmations`
- `recipe_stage5_set_blockers`
- `recipe_stage5_upsert_completion_status`

`gate-and-render` 输出：

- `stage-5-after-supplement-ready.json`
- `instruction_payload.resume_packet.resume_status = ready_to_resume`
- `instruction_payload.resume_packet.is_bootstrap = false`
- `recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`

`gate-and-render` 更新视图：

- `response-strategy-cards/atomic_004.md`
- `response-letter-outline.md`
- `agent-resume.md`
- `supplement-intake-plan.md`

这一轮恢复到 `ready_to_resume` 后，Agent 应理解为：

- blocker 已解除
- 当前 item 可以重新进入逐条确认
- 当前轮每个补材文件都必须有 `accepted/rejected` 与理由，且 accepted 文件必须已有 landing 映射
- 只有确认完成并形成稿件修改草案、response 段落草案以及一一对应关系后，才可把 `atomic_004` 标记为完成

### Stage 6

这一阶段不再直接从 Stage 5 草案跳到最终导出，而是拆成 5 个子步骤：

1. 全局风格画像
2. 位置级三版本最终落稿文本生成
3. 用户选版
4. thread-level response row 组装
5. marked manuscript -> 最终确认 -> clean export

#### Stage 6A: 风格画像

Agent 先写入：

- `style_profiles`
- `style_profile_rules`

采用：

- `recipe_stage6_upsert_style_profiles`

渲染后，用户可查看：

- `workspace/style-profile.md`

#### Stage 6B: 位置级三版本最终落稿文本生成

Agent 再按 `strategy_card_actions` 的每个 `target_location` 生成 3 个 manuscript 最终落地文案版本。这里给用户看的不是修改方向，而是可直接写进最终稿的具体句子或局部段落。写入：

- `action_copy_variants`

采用：

- `recipe_stage6_replace_action_copy_variants`

渲染后，用户可查看：

- `workspace/action-copy-variants.md`

复杂样例里，`atomic_004 / action 1` 覆盖两个位置，所以是“每个位置各自三选一”，而不是整条 action 共用一组三版本。比如：

- `location 1`（图注）选中的 `v2`：`Top-1 accuracy across five random seeds for the multimodal transformer.`
- `location 2`（结果段落）选中的 `v2`：`Across five random seeds, the mean macro-F1 remains stable and the spread stays narrow enough to support the robustness claim.`

这里用户选择的是最终稿要落下去的具体图注和具体结果句子，而不是“加一个稳定性图并解释趋势”这种方向性方案。

#### Stage 6C: 用户选版与 thread-level row 组装

用户确认每个 action 的每个 `target_location` 的最终 manuscript 文案版本后，Agent 再基于已选 manuscript 文案和 Stage 5 已确认的策略/草案写入：

- `selected_action_copy_variants`
- `response_thread_resolution_links`
- `response_thread_rows`

采用：

- `recipe_stage6_select_action_copy_variants`
- `recipe_stage6_upsert_response_thread_rows`

此时 `gate-and-render` 会渲染：

- `response-letter-outline.md`
- `response-letter-table-preview.md`
- `response-letter-table-preview.tex`

最终 Response Letter 的正式索引仍然是原始 `thread_id`，而不是 `comment_id`。

#### Stage 6D: marked manuscript 导出

Agent 先导出带 `changes` 宏包标注的稿件，并写入：

- `export_artifacts.marked_manuscript`

在正式导出前，Agent 还要先写入：

- `export_patch_sets`
- `export_patches`

采用：

- `recipe_stage6_replace_export_patches`
- `recipe_stage6_export_marked_manuscript`

用户先复核：

- `outputs/marked-manuscript/main.tex`
- `workspace/response-letter-table-preview.md`
- `workspace/final-assembly-checklist.md`

这里的 marked manuscript 必须是完整稿件树，而不是若干局部摘录文件。导出脚本在完整副本上按显式锚点补丁应用最终文本。

#### Stage 6E: 最终确认与 clean export

用户确认 marked manuscript 与最终表格回复均无误后，Agent 再导出：

- clean manuscript
- Markdown response letter
- LaTeX response letter

采用：

- `recipe_stage6_export_clean_manuscript`

`gate-and-render` 输出：

- `stage-6-export-ready.json`
- `recommended_next_action = stage_6_completed`
- `recommended_next_action.recipe_id = recipe_stage6_export_clean_manuscript`

最终交付物：

- marked manuscript：`outputs/marked-manuscript/`
- clean manuscript：`outputs/revised-manuscript/`
- Markdown response letter：`outputs/response-letter.md`
- LaTeX response letter：`outputs/response-letter.tex`

补充说明：

- clean manuscript 必须与用户最终确认后的 marked manuscript 内容一致，只去掉 `changes` 标记
- LaTeX response letter 必须是带 front matter 的完整可编译文件
