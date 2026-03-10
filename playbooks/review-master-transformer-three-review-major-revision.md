# review-master Transformer Three-Review Major Revision Playbook

## Purpose

这份 playbook 演示 SQLite 唯一真源模式下的完整复杂成功路径。

特点：

- 多文件 LaTeX 工程
- 3 位 reviewer
- 15 个原始 reviewer thread
- 9 条固定 canonical atomic item
- 3 轮 supplement 驱动的 `blocked -> ready_to_resume -> continue` 闭环
- 首次进入走 bootstrap，此后每轮都先恢复再继续
- Agent 只写 `review-master.db`
- `gate-and-render` 每轮都重渲染 Markdown 视图、恢复包和下一步动作
- 最终停在 `stage_6_completed`

## Example Assets

- 输入：
  - `playbooks/examples/transformer-three-review-major-revision/inputs/manuscript/`
  - `playbooks/examples/transformer-three-review-major-revision/inputs/review-comments.md`
- 用户补材：
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-1/`
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-2/`
  - `playbooks/examples/transformer-three-review-major-revision/user-supplements/round-3/`
- 终稿参考与追踪：
  - `playbooks/examples/transformer-three-review-major-revision/reference/accepted-paper.md`
  - `playbooks/examples/transformer-three-review-major-revision/reference/degradation-traceability.md`
  - 以上 `reference/*` 仅用于案例构造与离线验收，不属于 runtime 中 Agent 的输入读取范围
- 最终态 workspace：
  - `playbooks/examples/transformer-three-review-major-revision/workspace/`
- 最终输出：
  - `playbooks/examples/transformer-three-review-major-revision/outputs/marked-manuscript/`
  - `playbooks/examples/transformer-three-review-major-revision/outputs/revised-manuscript/`
  - `playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.md`
  - `playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.tex`
- `gate-and-render` 输出：
  - `playbooks/examples/transformer-three-review-major-revision/gate-and-render-output/`

## Fixed Canonical Atomic Items

- `atomic_001`
  - 解释 attention-only 为何能替代 recurrence/convolution
  - 映射 `R1.1`, `R3.4`
- `atomic_002`
  - 澄清 novelty positioning 与 prior work 边界
  - 映射 `R1.2`
- `atomic_003`
  - 组件贡献、head 数、维度与敏感性分析
  - 映射 `R1.3`, `R1.4`, `R2.4`
- `atomic_004`
  - 主结果里 baseline gain 的机制性解释
  - 映射 `R1.5`
- `atomic_005`
  - 数据、预处理、checkpoint averaging、解码细节复现
  - 映射 `R2.1`, `R2.2`
- `atomic_006`
  - training-cost / FLOPs accounting 与 fair-comparison caveat
  - 映射 `R2.3`
- `atomic_007`
  - headline result 之外的稳定性与 variance 表述
  - 映射 `R2.5`
- `atomic_008`
  - limitations、failure buckets、scope boundaries
  - 映射 `R3.1`, `R3.3`, `R3.5`
- `atomic_009`
  - interpretability case study 与 attention qualitative evidence
  - 映射 `R3.2`

合并原则固定为：

- 以“是否是同一个可独立完成的修回动作”为标准
- 不把机制解释和结果解释混成一条
- 不把复现 protocol 和成本 accounting 混成一条
- 不把 limitations 和 interpretability 混成一条

## Supplement Intake Scheme

本案例的 Stage 5 补材接收方案固定为“文件级强制判定 + accepted 强制落地”：

- 每个 round 的每个补材文件都必须写入 `supplement_intake_items`
- 每个文件都必须是 `accepted` 或 `rejected`，并带非空 `decision_rationale`
- 任何 `accepted` 文件都必须至少有一条 `supplement_landing_links`
- `supplement_landing_links` 必须指向有效的 `comment_id/action_order/location_order`
- 所有判定与落地关系统一渲染到 `workspace/supplement-intake-plan.md`

本案例的固定判定结果（摘要）：

- round-1：
  - accepted：`method-positioning-note.md`、`reproducibility-note.md`、`wmt-decode-settings.tex`
  - rejected：`round-1-cover-note.md`（仅流程说明，不形成稿件落点）
- round-2：
  - accepted：`component-ablation.csv`、`ablation-interpretation-note.md`、`efficiency-cost-comparison.csv`、`efficiency-accounting-note.md`
  - rejected：`round-2-cover-note.md`
- round-3：
  - accepted：`attention-case-study.md`、`attention-pattern-example.svg`、`failure-bucket-summary.csv`、`limitations-and-boundaries.md`
  - rejected：`round-3-cover-note.md`

## Supplement To Revised-Manuscript Path

这份案例要求可以从补材一路追到最终修订稿段落，主链路如下：

- `round-1/method-positioning-note.md` -> `atomic_001`,`atomic_002` -> `sections/introduction.tex` 与 `sections/background.tex`
- `round-1/reproducibility-note.md` + `round-1/wmt-decode-settings.tex` -> `atomic_005` -> `sections/training.tex`
- `round-2/component-ablation.csv` + `round-2/ablation-interpretation-note.md` -> `atomic_003` -> `sections/architecture.tex`,`sections/results.tex`
- `round-2/efficiency-cost-comparison.csv` + `round-2/efficiency-accounting-note.md` -> `atomic_006`,`atomic_007` -> `sections/results.tex`,`sections/conclusion.tex`
- `round-3/attention-case-study.md` + `round-3/attention-pattern-example.svg` + `round-3/failure-bucket-summary.csv` + `round-3/limitations-and-boundaries.md` -> `atomic_008`,`atomic_009` -> `sections/results.tex`,`sections/discussion.tex`,`sections/conclusion.tex`

## Walkthrough

### Stage 1

用户输入：

- `manuscript_source = .../inputs/manuscript`
- `review_comments_source = .../inputs/review-comments.md`

Agent 调用：

```bash
python -u review-master/scripts/detect_main_tex.py \
  --manuscript-source playbooks/examples/transformer-three-review-major-revision/inputs/manuscript

python -u review-master/scripts/init_artifact_workspace.py \
  --artifact-root playbooks/examples/transformer-three-review-major-revision/workspace
```

Agent 先读：

- `review-master/SKILL.md`
- `review-master/references/stage-1-entry-and-bootstrap.md`
- `instruction_payload.resume_packet`
- `workspace/agent-resume.md`

Agent 写入：

- 初始化 `review-master.db`
- 采用 `recipe_stage1_set_entry_state`
- 更新表：
  - `workflow_state`
  - `resume_brief`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_1',
    stage_gate = 'ready',
    active_comment_id = NULL,
    next_action = 'enter_stage_2'
WHERE id = 1;

UPDATE resume_brief
SET resume_status = 'bootstrap',
    current_objective = 'Bootstrap the multi-review Transformer case and prepare manuscript analysis.',
    current_focus = 'Confirm manuscript entry and stage-two analysis handoff.',
    why_paused = 'This replay starts from a fresh workspace with no historical state to recover.',
    next_operator_action = 'Read the bootstrap resume and proceed to stage 2.'
WHERE id = 1;
```

`gate-and-render` 输出：

- `stage-1-entry-ready.json`
- `instruction_payload.resume_packet.resume_status = bootstrap`
- `instruction_payload.recommended_next_action.action_id = enter_stage_2`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage2_upsert_manuscript_summary`

`gate-and-render` 更新视图：

- `workspace/agent-resume.md`
- `workspace/manuscript-structure-summary.md`
- `workspace/raw-review-thread-list.md`
- `workspace/atomic-review-comment-list.md`
- `workspace/thread-to-atomic-mapping.md`
- `workspace/atomic-comment-workboard.md`

为什么可以推进：

- 主入口可检测
- 输入资产完整
- bootstrap 恢复包已经把首次 authored step 固定到 Stage 2

### Stage 2

Agent 先读：

- `review-master/references/stage-2-manuscript-analysis.md`
- `workspace/manuscript-structure-summary.md`
- 最新的 `instruction_payload`

Agent 写入：

- `manuscript_summary`
- `manuscript_sections`
- `manuscript_claims`
- 采用 `recipe_stage2_upsert_manuscript_summary`
- 更新表：
  - `manuscript_summary`
  - `manuscript_sections`
  - `manuscript_claims`
  - `workflow_state`

高风险区覆盖：

- `abstract`
- `architecture`
- `training`
- `results`
- `discussion`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE manuscript_summary
SET main_entry = 'main.tex',
    project_shape = 'latex_project',
    paper_topic = 'Attention-only neural machine translation',
    high_risk_areas = 'Abstract; Architecture; Training; Results; Discussion'
WHERE id = 1;

DELETE FROM manuscript_sections;
INSERT INTO manuscript_sections (
  section_id,
  section_title,
  purpose_in_manuscript,
  key_files_or_locations
) VALUES
  ('sec_abstract', 'Abstract', 'State the attention-only claim and headline benchmark result.', 'sections/abstract.tex::abstract::paragraph 1'),
  ('sec_architecture', 'Model Architecture', 'Describe scaled dot-product attention, multi-head attention, and default configuration.', 'sections/architecture.tex::Model Configuration::paragraph 1'),
  ('sec_training', 'Training', 'Document WMT data usage and reproducibility-critical protocol.', 'sections/training.tex::Implementation Notes::paragraph 1'),
  ('sec_results', 'Results', 'Report headline BLEU, variation study, stability statement, and interpretability note.', 'sections/results.tex::Machine Translation::paragraph 1'),
  ('sec_discussion', 'Discussion', 'Bound conclusions and list failure buckets.', 'sections/discussion.tex::Discussion::paragraph 2');
```

`gate-and-render` 输出：

- `stage-2-structure-ready.json`
- `instruction_payload.recommended_next_action.action_id = enter_stage_3`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage3_replace_threaded_atomic_model`

`gate-and-render` 更新视图：

- `workspace/agent-resume.md`
- `workspace/manuscript-structure-summary.md`

为什么可以推进：

- 结构摘要已经能支撑 reviewer thread 的拆分和 target location 规划
- 多文件工程的主入口、章节职责和 claims 已全部入库

### Stage 3

Agent 先读：

- `review-master/references/stage-3-comment-atomization.md`
- `workspace/manuscript-structure-summary.md`
- `inputs/review-comments.md`

Agent 写入：

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
  ('reviewer_1_thread_001', 'reviewer_1', 1, 'reviewer_comment', 'The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.', 'Clarify why attention-only is a viable replacement beyond parallelism.'),
  ('reviewer_2_thread_005', 'reviewer_2', 5, 'reviewer_comment', 'Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.', 'Request stability or variance support beyond headline BLEU.'),
  ('reviewer_3_thread_002', 'reviewer_3', 2, 'reviewer_comment', 'The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.', 'Request a concrete attention case study.');

INSERT INTO atomic_comments (
  comment_id,
  comment_order,
  canonical_summary,
  required_action
) VALUES
  ('atomic_001', 1, 'Explain why attention-only can replace recurrence and convolution in this translation setting.', 'Add a concrete mechanism-based explanation of the attention-only claim.'),
  ('atomic_007', 7, 'Add stability or variance evidence beyond headline BLEU.', 'Report stability support and calibrate the single-run claim.'),
  ('atomic_009', 9, 'Add an interpretability case study with qualitative attention evidence.', 'Support the interpretability claim with a concrete example.');

INSERT INTO raw_thread_atomic_links (thread_id, comment_id, link_order) VALUES
  ('reviewer_1_thread_001', 'atomic_001', 1),
  ('reviewer_2_thread_005', 'atomic_007', 1),
  ('reviewer_3_thread_002', 'atomic_009', 1),
  ('reviewer_3_thread_004', 'atomic_001', 1);
```

本案例固定结果：

- 15 个 raw reviewer thread 全量入库
- 9 条 canonical atomic item 全量入库
- `atomic_001` 被 `R1.1` 和 `R3.4` 共享
- `atomic_003` 被 `R1.3`、`R1.4`、`R2.4` 共享
- `atomic_008` 被 `R3.1`、`R3.3`、`R3.5` 共享

`gate-and-render` 输出：

- `stage-3-atomic-ready.json`
- `instruction_payload.recommended_next_action.action_id = enter_stage_4`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage4_upsert_atomic_workboard`

`gate-and-render` 更新视图：

- `workspace/agent-resume.md`
- `workspace/raw-review-thread-list.md`
- `workspace/atomic-review-comment-list.md`
- `workspace/thread-to-atomic-mapping.md`

为什么可以推进：

- `workspace/thread-to-atomic-mapping.md` 已能完整展示 15 -> 9 的稳定映射
- 没有 orphan thread
- 没有 orphan atomic item

### Stage 4

Agent 先读：

- `review-master/references/stage-4-workboard-planning.md`
- `workspace/thread-to-atomic-mapping.md`
- `workspace/atomic-comment-workboard.md`

Agent 写入：

- `atomic_comment_state`
- `atomic_comment_target_locations`
- `atomic_comment_analysis_links`
- `workflow_pending_user_confirmations`
- `workflow_state`
- 采用：
  - `recipe_stage4_upsert_atomic_workboard`
  - `recipe_stage4_set_pending_confirmations`

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
) VALUES
  ('atomic_001', 'blocked', 'high', 'yes', 'yes', 'resolve_blockers'),
  ('atomic_003', 'blocked', 'high', 'yes', 'yes', 'resolve_blockers'),
  ('atomic_008', 'blocked', 'high', 'yes', 'yes', 'resolve_blockers')
ON CONFLICT(comment_id) DO UPDATE SET
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
) VALUES
  ('atomic_005', 1, 'sections/training.tex::Data::paragraph 1', 'primary'),
  ('atomic_005', 2, 'sections/training.tex::Implementation Notes::paragraph 1', 'supporting'),
  ('atomic_009', 1, 'sections/results.tex::Interpretability::paragraph 1', 'primary');

DELETE FROM workflow_pending_user_confirmations;
INSERT INTO workflow_pending_user_confirmations (position, message)
VALUES (1, 'Confirm the canonical 9-item workboard and the planned supplement order before entering stage 5.');
```

`gate-and-render` 输出：

- `stage-4-workboard-confirmation-needed.json`
- `instruction_payload.recommended_next_action.action_id = request_stage4_confirmation`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage4_set_pending_confirmations`
- `resume_packet.stage_gate = blocked`

`gate-and-render` 更新视图：

- `workspace/agent-resume.md`
- `workspace/atomic-comment-workboard.md`
- `workspace/thread-to-atomic-mapping.md`

为什么停住：

- 这是第一次正式停在 `confirmation-needed`
- Agent 已经完成 canonical workboard，但尚未获准按三轮 supplement 顺序推进

### Stage 5 Round 1

Round 1 固定解决：

- `atomic_001`
- `atomic_002`
- `atomic_004`
- `atomic_005`

补材来源：

- `user-supplements/round-1/`

这轮聚焦：

- method positioning
- attention-only 机制澄清
- reproducibility protocol

Agent 先读：

- 最新的 `instruction_payload.resume_packet`
- `workspace/agent-resume.md`
- `user-supplements/round-1/`

恢复与对齐规则：

- Stage 5 不能凭记忆续写
- 每次都必须先读 `resume_packet.active_comment_id`
- 本轮 blocked 与 ready 快照都把焦点固定到 `atomic_005`
- 这代表当前恢复入口对齐到“复现细节是最后一个仍未闭环的 round-1 focal item”

Agent 写入：

- `strategy_cards`
- `strategy_card_actions`
- `strategy_card_evidence_items`
- `strategy_card_pending_confirmations`
- `supplement_intake_items`
- `supplement_landing_links`
- `comment_completion_status`
- `workflow_global_blockers`
- `resume_brief`

补材接收与落地采用：

- `recipe_stage5_replace_supplement_intake_and_landing`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_5',
    stage_gate = 'blocked',
    active_comment_id = 'atomic_005',
    next_action = 'resolve_blockers'
WHERE id = 1;

DELETE FROM workflow_global_blockers;
INSERT INTO workflow_global_blockers (position, message)
VALUES
  (1, 'Need reproducibility-critical data usage and decoding details from round-1 supplement.'),
  (2, 'Need a concrete wording bridge for the attention-only mechanism and novelty boundary.');
```

blocked 快照：

- `stage-5-round-1-blocked.json`
- `instruction_payload.recommended_next_action.action_id = resolve_blockers`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage5_set_blockers`
- `resume_packet.active_comment_id = atomic_005`

blocked 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_005.md`
- `workspace/atomic-comment-workboard.md`
- `workspace/supplement-intake-plan.md`

用户补材吸收后：

- round-1 证据写回 `strategy_card_evidence_items`
- round-1 文件级 intake 决策写回 `supplement_intake_items`
- accepted 文件落地映射写回 `supplement_landing_links`
- `atomic_001`、`atomic_002`、`atomic_004`、`atomic_005` 的 strategy 和 completion 状态补齐

ready 快照：

- `stage-5-round-1-ready.json`
- `instruction_payload.recommended_next_action.action_id = advance_active_comment`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`
- `resume_packet.active_comment_id = atomic_005`

ready 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_005.md`
- `workspace/response-letter-outline.md`
- `workspace/supplement-intake-plan.md`

为什么可以继续：

- method/positioning/reproducibility 的缺口已被 round-1 补材封口
- 但 quantitative support 还没进入，所以只能推进到下一轮而不能直接导出

### Stage 5 Round 2

Round 2 固定解决：

- `atomic_003`
- `atomic_006`
- `atomic_007`

补材来源：

- `user-supplements/round-2/`

这轮聚焦：

- ablation
- sensitivity
- efficiency accounting
- stability statement

恢复与对齐规则：

- 重新进入前再次先读 `resume_packet`
- blocked 与 ready 快照把 `active_comment_id` 对齐到 `atomic_007`
- 这表示 round-2 中最后一个需要恢复焦点的是稳定性陈述

Agent 写入：

- `strategy_cards`
- `strategy_card_evidence_items`
- `supplement_intake_items`
- `supplement_landing_links`
- `workflow_global_blockers`
- `comment_completion_status`
- `resume_brief`

补材接收与落地采用：

- `recipe_stage5_replace_supplement_intake_and_landing`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_5',
    stage_gate = 'blocked',
    active_comment_id = 'atomic_007',
    next_action = 'resolve_blockers'
WHERE id = 1;

DELETE FROM workflow_global_blockers;
INSERT INTO workflow_global_blockers (position, message)
VALUES
  (1, 'Need architecture sensitivity evidence from round-2 supplement before closing atomic_003.'),
  (2, 'Need FLOPs accounting and multi-run stability summary before closing efficiency and variance claims.');
```

blocked 快照：

- `stage-5-round-2-blocked.json`
- `instruction_payload.recommended_next_action.action_id = resolve_blockers`
- `resume_packet.active_comment_id = atomic_007`

blocked 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_007.md`
- `workspace/atomic-comment-workboard.md`
- `workspace/supplement-intake-plan.md`

ready 快照：

- `stage-5-round-2-ready.json`
- `instruction_payload.recommended_next_action.action_id = advance_active_comment`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`
- `resume_packet.active_comment_id = atomic_007`

ready 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_007.md`
- `workspace/response-letter-outline.md`
- `workspace/supplement-intake-plan.md`

为什么可以继续：

- 量化支持已经补齐
- workboard 上只剩 discussion/interpretability 类后半程问题

### Stage 5 Round 3

Round 3 固定解决：

- `atomic_008`
- `atomic_009`

补材来源：

- `user-supplements/round-3/`

这轮聚焦：

- limitations
- failure buckets
- scope boundaries
- qualitative attention evidence

恢复与对齐规则：

- 继续先读恢复包
- blocked 与 ready 快照都对齐到 `atomic_009`
- 这说明最后一个仍需用户补证的 focal item 是 interpretability case study

Agent 写入：

- `strategy_cards`
- `strategy_card_evidence_items`
- `supplement_intake_items`
- `supplement_landing_links`
- `comment_completion_status`
- `workflow_global_blockers`
- `resume_brief`

补材接收与落地采用：

- `recipe_stage5_replace_supplement_intake_and_landing`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_5',
    stage_gate = 'blocked',
    active_comment_id = 'atomic_009',
    next_action = 'resolve_blockers'
WHERE id = 1;

DELETE FROM workflow_global_blockers;
INSERT INTO workflow_global_blockers (position, message)
VALUES
  (1, 'Need concrete failure buckets and scope caveats from round-3 supplement.'),
  (2, 'Need the qualitative attention case study before closing the interpretability claim.');
```

blocked 快照：

- `stage-5-round-3-blocked.json`
- `instruction_payload.recommended_next_action.action_id = resolve_blockers`
- `resume_packet.active_comment_id = atomic_009`

blocked 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_009.md`
- `workspace/atomic-comment-workboard.md`
- `workspace/supplement-intake-plan.md`

ready 快照：

- `stage-5-round-3-ready.json`
- `instruction_payload.recommended_next_action.action_id = advance_active_comment`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`
- `resume_packet.active_comment_id = atomic_009`

ready 快照对应的视图更新：

- `workspace/agent-resume.md`
- `workspace/response-strategy-cards/atomic_009.md`
- `workspace/response-letter-outline.md`
- `workspace/supplement-intake-plan.md`

为什么可以推进到 Stage 6：

- 9 条 atomic item 全部达到 response-ready
- 15 条原始 reviewer thread 都已有稳定的 canonical 落点
- final assembly 已经没有未解决 blocker

### Stage 6

Agent 先读：

- `review-master/references/stage-6-final-review-and-export.md`
- `workspace/final-assembly-checklist.md`
- `workspace/thread-to-atomic-mapping.md`
- 最新的 `instruction_payload`

Agent 写入：

- `style_profiles`
- `response_thread_rows`
- `response_thread_resolution_links`
- `response_letter_variants`
- `selected_response_variant`
- `export_patch_sets`
- `export_patches`
- `export_artifacts`
- `workflow_state`

thread-level response row 组装逻辑：

- 数据真源不是 reviewer 原文文件，而是 `raw_review_threads`
- 每个 raw thread 都必须被至少一条最终 `response_thread_row` 覆盖
- 多 reviewer 共享的 atomic item 允许共享修订动作，但不能省略 thread-level 回应

export patch plan 真源：

- `export_patch_sets`
- `export_patches`

marked manuscript 与 clean manuscript 的关系：

- 两者都由 Stage 6 导出
- `marked-manuscript/` 复制完整稿件树并保留 `changes` 标记
- `revised-manuscript/` 使用相同 patch set，只去掉 `changes` 宏与标记内容
- patch plan 真源保持唯一，不能各自手工改一份稿件

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
INSERT INTO response_thread_rows (
  row_id,
  thread_id,
  row_order,
  response_markdown,
  manuscript_change_summary
) VALUES (
  'row_r2_005',
  'reviewer_2_thread_005',
  10,
  'We added a stability statement grounded in the new five-run evidence and clarified the limits of single-run conclusions.',
  'Expanded the Results section with a bounded variance statement.'
);

INSERT INTO export_patch_sets (
  patch_set_id,
  artifact_kind,
  source_root,
  description
) VALUES (
  'clean_manuscript',
  'clean_manuscript',
  'inputs/manuscript',
  'Final clean manuscript assembled from the canonical stage-6 patch plan.'
);

INSERT INTO export_artifacts (
  artifact_kind,
  status,
  output_path
) VALUES
  ('marked_manuscript', 'exported', 'outputs/marked-manuscript/main.tex'),
  ('clean_manuscript', 'exported', 'outputs/revised-manuscript/main.tex'),
  ('response_markdown', 'exported', 'outputs/response-letter.md'),
  ('response_latex', 'exported', 'outputs/response-letter.tex');
```

导出前快照：

- `stage-6-export-ready.json`
- `instruction_payload.recommended_next_action.action_id = final_review_and_clean_export`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage6_export_clean_manuscript`

导出前快照对应的视图更新：

- `workspace/style-profile.md`
- `workspace/action-copy-variants.md`
- `workspace/response-letter-outline.md`
- `workspace/response-letter-table-preview.md`
- `workspace/response-letter-table-preview.tex`
- `workspace/export-patch-plan.md`
- `workspace/final-assembly-checklist.md`
- `workspace/agent-resume.md`

最终快照：

- `stage-6-completed.json`
- `instruction_payload.recommended_next_action.action_id = stage_6_completed`
- `instruction_payload.recommended_next_action.recipe_id = recipe_stage6_export_clean_manuscript`

最终快照对应的视图更新：

- `workspace/final-assembly-checklist.md`
- `workspace/response-letter-table-preview.md`
- `workspace/response-letter-table-preview.tex`
- `workspace/agent-resume.md`

最终闭环检查：

- `workspace/final-assembly-checklist.md` 中：
  - `marked_manuscript = exported`
  - `clean_manuscript = exported`
  - `response_markdown = exported`
  - `response_latex = exported`
- `outputs/response-letter.tex` 含完整 front matter，可独立编译
- `outputs/response-letter.md` 与 `response-letter.tex` 覆盖全部 15 条 raw reviewer thread

## Why This Case Matters

这份 playbook 与前两个示例的区别，不在于阶段定义不同，而在于它把复杂性固定成了可回放资产：

- reviewer comments 足够多，但仍然能被压缩为稳定的 9 条 canonical atomic item
- supplement 不是一次性输入，而是分 3 轮解除不同类型的 blocker
- 恢复入口每次都通过 `resume_packet.active_comment_id` 重新对齐当前轮次焦点
- Stage 6 不是抽象说明，而是真正产出了完整 marked/clean manuscript 和双格式 response letter

因此它已经不是“资产说明型案例”，而是与仓库中现有两份样例同级的完整 runtime 回放案例。
