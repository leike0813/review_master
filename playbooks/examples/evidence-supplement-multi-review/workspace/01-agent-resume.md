# Agent Resume

这是从 `review-master.db` 渲染出的 Agent 恢复视图。数据库真源是 `resume_brief`、`resume_open_loops`、`resume_recent_decisions`、`resume_must_not_forget`、`workflow_state` 与 `runtime_language_context`。它帮助 Agent 在首次进入、跨 Session 恢复和上下文压缩后重新对齐状态；它不是用户确认工件，也不是可直写真源。

## 恢复状态

| 字段 | 值 |
| --- | --- |
| `resume_status` | completed |
| `is_bootstrap` | no |
| `current_stage` | stage_6 |
| `stage_gate` | ready |
| `active_comment_id` | None |

## 语言上下文

| 字段 | 值 |
| --- | --- |
| `文本语言` | en |
| `工作语言` | zh-CN |
| `稿件检测语言` | en |
| `审稿意见检测语言` | en |
| `Prompt 检测语言` | zh-CN |
| `文本语言来源` | manuscript |
| `工作语言来源` | prompt |
| `语言已确认` | yes |

## 恢复时优先理解

- 当前状态摘要: 当前处于 stage_6，gate=ready，active_comment_id=None。
- 当前目标: Keep the complex evidence-supplement sample aligned with the fully exported Stage 6 contract.
- 当前焦点: All Stage 6 artifacts are exported; the workspace is retained as a replayable final-state example with blocker history already resolved.
- 暂停原因: The sample has reached its final exported state and is now paused only for inspection, regression checking, and future documentation updates.
- 下一步操作: If a new revision is requested, reopen the database truth, adjust the relevant Stage 6 records, and rerun gate-and-render before exporting again.
- 下一步锚点: stage_6_completed

## 未闭环事项

这些是当前尚未闭环的关键事项。恢复时先核对它们是否与当前 gate 输出一致。

| 序号 | 说明 |
| --- | --- |
| 1 | Preserve the final response-row mapping so the shared baseline concern remains traceable across both reviewer threads. |

## 最近决策

这些是最近已经锁定或用户已经确认的关键决策。新 Session 不应无声推翻它们。

| 序号 | 说明 |
| --- | --- |
| 1 | Selected one final manuscript wording variant for every Stage 6 action. |
| 2 | Kept reviewer_2_thread_002 as a multi-resolution thread row that aggregates both the shared baseline concern and the limitations expansion. |

## 不可遗忘事项

这些提醒来自静态 Skill 摘要与运行时恢复层，用于帮助 Agent 在长上下文跨度下持续遵守核心纪律。

| 序号 | 说明 |
| --- | --- |
| 1 | Marked manuscript review is the mandatory gate before clean export. |
| 2 | Final response rows remain indexed by raw reviewer thread, not by canonical atomic comment. |

## 恢复读取顺序

恢复时固定按以下顺序重建认知：

| 步骤 | 读取对象 |
| --- | --- |
| 1 | instruction_payload.resume_packet |
| 2 | 01-agent-resume.md |
| 3 | 当前阶段主视图 |
| 4 | 当前阶段参考文档 |

## Skill 运行摘要

下面是静态 Skill 摘要，用于提醒 Agent 当前 workflow 的核心目标、约束与执行方法。

# review-master Runtime Digest

## Goals

- 以阶段化方式推进论文修回，而不是一步到位改稿
- 用 SQLite 维持运行时唯一真源
- 显式区分文本语言与工作语言，并在运行时持续遵守它们的边界
- 把原始 reviewer thread 整理为 canonical atomic item，并在用户确认下逐条闭环
- 最终 response letter 必须回到原始 `thread_id` 顺序组织，并以 point-to-point 表格输出

## Non-Goals

- 不直接一步到位修改论文原稿
- 不替用户做未经授权的学术决策
- 不把脚本当作核心语义判断的替代品
- 不把只读 Markdown 视图当成运行时真源

## Responsibilities

- Agent 负责语义理解、学术判断、策略制定、意见映射和用户交互
- 脚本只负责确定性且可验证的工作：workspace 初始化、数据库读写辅助、状态门禁检查、恢复包输出和只读视图重渲染
- Stage 5 的 manuscript execution items 与 response drafts 由 Agent 写入正式真源表，Stage 6 基于这些真源派生 revision backlog，再进入交互式改稿与审计闭环

## Workflow Discipline

- 先恢复，后执行
- 首次初始化前先确认文本语言与工作语言
- 每次写库后都必须运行 `gate-and-render` 核心脚本
- 有 `pending_user_confirmations` 时先请求确认
- Stage 3 建模完成后必须先展示 `07-review-comment-coverage.md`（完整原文顺序 + 红色高亮 `primary/supporting` + 橙色高亮 `duplicate_filtered` + 短 `thread_id` 标签 + 覆盖映射附录）并拿到用户确认，确认前不得进入 Stage 4
- Stage 3 覆盖真源以 `review_comment_source_documents` + `raw_thread_source_spans` 为准
- 每个 `thread_id` 至少包含一条 `span_role='primary'`；“仅标题覆盖、正文疑似漏抽”作为弱提示提醒用户复核，不直接触发 repair 阻断
- Stage 3 覆盖率门禁使用字符级指标（`len` 口径、含空白）：全局主指标分子包含 `duplicate_filtered`；hard=`30%`（低于即阻断），soft=`50%`（区间内仅提示）
- 有 `global_blockers` 时先请求补材或澄清
- Stage 5 必须先形成策略卡并完成显式确认，确认前不得形成 Stage 5 execution items 或 response draft
- 进入 Stage 5 后必须形成 `09-supplement-suggestion-plan.md`，先展示全局补材建议 backlog，再处理后续 intake
- 每轮补材都要形成文件级 intake 判定；`accepted` 补材必须有落地映射
- `active_comment_id` 允许显式切换，但不得静默切换 comment
- Stage 6 以 `working_manuscript`、`revision_action_logs` 与 `response_thread_rows` 为闭环真源
- Agent 每完成一轮明确修改后，都必须通过 `commit_revision_round.py` 提交，不能绕过 revision audit
- `gate-and-render` 只负责检测未审计 diff 和闭环状态，不负责自动补写 revision log
- `response_latex` 必须是带 front matter 的完整可编译 LaTeX 文件

## Inputs And Outputs

- 必需输入：`manuscript_source`、`review_comments_source`
- 可选输入：`editor_letter_source`、`user_notes`
- 运行时真源：`review-master.db`
- 语言真源：`runtime_language_context`
- 稿件副本真源：`workspace_manuscript_copies`
- workspace 本地化覆盖层：`runtime-localization/`
- 只读视图：`01-agent-resume.md`、`02-manuscript-structure-summary.md`、`03-style-profile.md`、`04-raw-review-thread-list.md`、`05-atomic-review-comment-list.md`、`06-thread-to-atomic-mapping.md`、`07-review-comment-coverage.md`、`08-atomic-comment-workboard.md`、`09-supplement-suggestion-plan.md`、`10-supplement-intake-plan.md`、`11-manuscript-revision-guide.md`、`12-manuscript-execution-graph.md`、`13-revision-action-log.md`、`14-response-coverage-matrix.md`、`15-response-letter-preview.md`、`16-response-letter-preview.tex`、`17-final-assembly-checklist.md`、`response-strategy-cards/{comment_id}.md`
- 最终输出：`working_manuscript`、`response_markdown`、`response_latex`、可选 `latexdiff_manuscript`

## Language Rules

- 文本语言默认以 manuscript 语言为准；review comments 若不同语言，仍以 manuscript 语言为准
- 工作语言默认从当前 prompt 语言推断，并在 Stage 1 向用户确认
- reviewer / editor 原文与原稿摘录保持原语言
- Stage 3-5 的 normalized summary、canonical summary、strategy card、workboard、resume、gate 输出和 Stage 5 execution items / response drafts 使用工作语言
- Stage 6 的 manuscript final copy、response rows 与最终导出产物使用文本语言

## Six Stages

1. 入口解析与 workspace 初始化
2. 原稿结构分析
3. 原始审稿意见块抽取、去重、归并和 canonical atomic item 形成
4. atomic workboard 规划
5. 逐条策略与执行
6. 交互式 working manuscript 改稿、revision audit、thread-level response 覆盖闭环
