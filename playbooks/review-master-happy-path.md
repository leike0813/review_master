# review-master Happy Path Playbook

## Purpose

这份 playbook 演示 SQLite 唯一真源模式下的最小 happy path。

特点：

- 单个 `main.tex`
- 1 条原始 reviewer thread
- 2 条 canonical atomic item
- 无补材分支
- 首次调用先走 bootstrap resume
- Agent 只写 `review-master.db`
- `gate-and-render` 核心脚本每轮都重渲染 Markdown 视图并给出下一步指令

## Example Assets

- 输入：
  - `playbooks/examples/happy-path-minimal/inputs/manuscript/main.tex`
  - `playbooks/examples/happy-path-minimal/inputs/review-comments.md`
- 最终态 workspace：
  - `playbooks/examples/happy-path-minimal/workspace/`
- 最终输出：
  - `playbooks/examples/happy-path-minimal/outputs/marked-manuscript/main.tex`
  - `playbooks/examples/happy-path-minimal/outputs/revised-manuscript/main.tex`
  - `playbooks/examples/happy-path-minimal/outputs/response-letter.md`
  - `playbooks/examples/happy-path-minimal/outputs/response-letter.tex`
- `gate-and-render` 输出（保存在 `gate-and-render-output/` 目录）：
  - `playbooks/examples/happy-path-minimal/gate-and-render-output/`

## Walkthrough

### Stage 1

用户输入：

- `manuscript_source = .../inputs/manuscript/main.tex`
- `review_comments_source = .../inputs/review-comments.md`

Agent 调用：

```bash
python -u review-master/scripts/detect_main_tex.py \
  --manuscript-source playbooks/examples/happy-path-minimal/inputs/manuscript/main.tex

python -u review-master/scripts/init_artifact_workspace.py \
  --artifact-root playbooks/examples/happy-path-minimal/workspace
```

Agent 先读：

- `review-master/SKILL.md`
- `review-master/references/stage-1-entry-and-bootstrap.md`
- `instruction_payload.resume_packet`
- `agent-resume.md`

为什么可以推进：

- 输入完整
- `manuscript_source` 是单个 `main.tex`，无需额外确认主入口
- 环境满足脚本驱动要求

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
    current_objective = 'Bootstrap the workspace and prepare the first authored step.',
    current_focus = 'Confirm inputs and establish the first actionable stage.',
    why_paused = 'This is a new execution with no historical work to recover.',
    next_operator_action = 'Read the bootstrap resume and continue from the recommended action.'
WHERE id = 1;
```

`gate-and-render` 输出：

- `stage-1-entry-ready.json`
- `instruction_payload.resume_packet.resume_status = bootstrap`
- `instruction_payload.resume_packet.is_bootstrap = true`
- `agent-resume.md`
- `recommended_next_action = enter_stage_2`
- `recommended_next_action.recipe_id = recipe_stage2_upsert_manuscript_summary`
- 说明 Stage 1 已满足进入 Stage 2 的门槛

### Stage 2

Agent 先读：

- `review-master/references/stage-2-manuscript-analysis.md`
- `manuscript-structure-summary.md`
- 最新的 `instruction_payload`

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
    project_shape = 'single_tex',
    high_risk_areas = 'Abstract; Results'
WHERE id = 1;

DELETE FROM manuscript_sections;
INSERT INTO manuscript_sections (section_id, section_title, purpose_in_manuscript, key_files_or_locations)
VALUES ('sec_intro', 'Introduction', 'State the problem and contribution', 'main.tex::Introduction::paragraph 1');
```

`gate-and-render` 重渲染：

- `manuscript-structure-summary.md`

`gate-and-render` 输出：

- `stage-2-structure-ready.json`
- `recommended_next_action = enter_stage_3`
- `recommended_next_action.recipe_id = recipe_stage3_replace_threaded_atomic_model`

为什么可以推进：

- 主入口、章节结构、核心 claim 和高风险修改区都已入库
- `manuscript-structure-summary.md` 足以支撑后续 thread 抽取与 canonical atomic 建模

### Stage 3

Agent 先读：

- `review-master/references/stage-3-comment-atomization.md`
- `manuscript-structure-summary.md`
- 最新的 `instruction_payload`

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
) VALUES (
  'reviewer_1_thread_001',
  'reviewer_1',
  1,
  'reviewer_comment',
  'Please clarify why the proposed method outperforms the baseline and explain what part of the results section supports this claim.',
  'Clarify why the method outperforms the baseline and where the supporting argument lives.'
);

INSERT INTO atomic_comments (
  comment_id,
  comment_order,
  canonical_summary,
  required_action
) VALUES
  (
    'atomic_001',
    1,
    'Explain why the proposed method outperforms the baseline.',
    'Provide a concise causal explanation for the baseline advantage claim.'
  ),
  (
    'atomic_002',
    2,
    'Identify the manuscript evidence that supports the baseline-comparison claim.',
    'Point the reviewer to the exact evidence location in the results discussion.'
  );

INSERT INTO raw_thread_atomic_links (thread_id, comment_id, link_order) VALUES
  ('reviewer_1_thread_001', 'atomic_001', 1),
  ('reviewer_1_thread_001', 'atomic_002', 2);
```

为什么这两条 atomic 不合并：

- `atomic_001` 的期望动作是补一条因果性解释
- `atomic_002` 的期望动作是指出原文中证据落点
- 两者主题相关，但不是同一个可独立完成的动作，因此按保守规则保留为两条 atomic item

`gate-and-render` 输出：

- `stage-3-atomic-ready.json`
- `recommended_next_action = enter_stage_4`
- `recommended_next_action.recipe_id = recipe_stage4_upsert_atomic_workboard`

为什么可以推进：

- 一个 raw reviewer thread 被稳定拆成了两条 canonical atomic item
- 每个 `comment_id` 都已被该 `thread_id` 引用
- 不存在未映射 thread 或孤立 atomic item

### Stage 4

Agent 先读：

- `review-master/references/stage-4-workboard-planning.md`
- `atomic-comment-workboard.md`
- `thread-to-atomic-mapping.md`
- 最新的 `instruction_payload`

Agent 写入：

- `atomic_comment_state`
- `atomic_comment_target_locations`
- `atomic_comment_analysis_links`
- `workflow_state` 中的阶段与确认门禁
- 采用 `recipe_stage4_upsert_atomic_workboard`
- 更新表：
  - `atomic_comment_state`
  - `atomic_comment_target_locations`
  - `atomic_comment_analysis_links`
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
  'atomic_001',
  'ready',
  'high',
  'no',
  'no',
  'enter_stage_5'
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
  'atomic_001',
  1,
  'main.tex::Results::TBD',
  'primary'
);
```

为什么这里允许 provisional location：

- 这条 atomic item 已明确要改 Results 区域
- Stage 5 的下一步动作已经能确定
- 当前位置暂时还不需要精确到最终段落号，因此章节级 / `TBD` 仍可接受

随后 Agent 继续采用 `recipe_stage4_set_pending_confirmations`，写入默认确认门禁。

`gate-and-render` 重渲染：

- `atomic-comment-workboard.md`
- `thread-to-atomic-mapping.md`

`gate-and-render` 输出：

- `stage-4-workboard-confirmation-needed.json`
- `recommended_next_action = request_stage4_confirmation`
- `recommended_next_action.recipe_id = recipe_stage4_set_pending_confirmations`

为什么此时还不能直接进入 Stage 5：

- Stage 4 默认要求一次用户确认
- workboard 已足够审阅，但待确认事项尚未关闭
- 只有确认完成后，gate-and-render 才会推荐进入 Stage 5

### Stage 5

Agent 写入：

- `workflow_state.active_comment_id`
- `strategy_cards`
- `strategy_card_actions`
- `comment_completion_status`
- 采用：
  - `recipe_stage5_set_active_comment`
  - `recipe_stage5_upsert_strategy_card`
  - `recipe_stage5_replace_strategy_actions`
  - `recipe_stage5_upsert_completion_status`
- 更新表：
  - `workflow_state`
  - `strategy_cards`
  - `strategy_card_actions`
  - `comment_completion_status`

代表性 SQL：

```sql
PRAGMA foreign_keys = ON;
UPDATE workflow_state
SET current_stage = 'stage_5',
    stage_gate = 'ready',
    active_comment_id = 'atomic_001',
    next_action = 'advance_active_comment'
WHERE id = 1;

INSERT INTO strategy_cards (comment_id, proposed_stance, stance_rationale)
VALUES (
  'atomic_001',
  'accept_and_clarify',
  'The benchmark gain is already present in the manuscript, but the mechanism-focused explanation is too compressed.'
) ON CONFLICT(comment_id) DO UPDATE SET
  proposed_stance = excluded.proposed_stance,
  stance_rationale = excluded.stance_rationale;
```

`gate-and-render` 重渲染：

- `response-strategy-cards/atomic_001.md`

`gate-and-render` 输出：

- `stage-5-comment-ready.json`
- `recommended_next_action = advance_active_comment`
- `recommended_next_action.recipe_id = recipe_stage5_upsert_completion_status`

### Stage 6

这一阶段不再直接从 Stage 5 草案跳到最终导出，而是拆成 5 个子步骤：

1. 全局风格画像
2. 位置级三版本最终落稿文本生成
3. 用户选版与 thread-level row 组装
4. marked manuscript 导出
5. 最终确认后 clean export

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

在这个最小样例中，`atomic_001 / action 1 / location 1` 的三版本就是三句可直接写进最终稿的候选文本，而不是“扩写/澄清/补一句”这类操作描述。例如：

- `v1`: `The transformer improves top-1 accuracy by 2.7 points over the CNN baseline because global attention reduces confusion between visually similar leaf patterns while preserving lesion structure.`
- `v2`: `The transformer improves performance because global-context modeling reduces confusion between visually similar disease patterns while retaining discriminative lesion structure.`
- `v3`: `The transformer outperforms the CNN baseline because global-context modeling preserves discriminative lesion structure while reducing confusion between visually similar disease patterns.`

用户最终选择的是其中一句真正落入最终稿的文本；当前样例选择的是 `v2`。

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

这里的 marked manuscript 必须是完整稿件，不是局部摘录。导出脚本只是在完整副本上把目标位置替换成带 `changes` 标记的最终文本。

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

- marked manuscript：`outputs/marked-manuscript/main.tex`
- clean manuscript：`outputs/revised-manuscript/main.tex`
- Markdown response letter：`outputs/response-letter.md`
- LaTeX response letter：`outputs/response-letter.tex`

补充说明：

- `outputs/revised-manuscript/main.tex` 必须与用户最终确认后的 marked manuscript 内容一致，只去掉 `changes` 标记
- `outputs/response-letter.tex` 必须是带 front matter 的完整可编译 LaTeX 文件，而不是只有表格正文
