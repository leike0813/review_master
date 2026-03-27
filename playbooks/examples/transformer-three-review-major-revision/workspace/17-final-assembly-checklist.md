# Final Assembly Checklist

这是从 `review-master.db` 渲染出的最终闭环视图。数据库真源是 `comment_completion_status`、`response_thread_action_log_links`、`response_thread_rows`、`working_copy_file_state`、`export_artifacts`、`raw_review_threads` 和 `atomic_comments`。它用于检查 canonical atomic item 是否闭环、reviewer 线程是否被最终 row 覆盖、working manuscript 是否已完成审计，以及最终 response 输出是否就绪。

## Atomic 完成表

| `comment_id` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | `manuscript_execution_items_done` | `response_draft_done` | `one_to_one_link_checked` | `export_ready` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_3 | reviewer_1_thread_001, reviewer_3_thread_004 | ready | high | yes | sections/introduction.tex::Introduction::paragraph 3, sections/results.tex::Machine Translation::paragraph 2 | yes | yes | yes | yes |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | ready | medium | yes | sections/background.tex::Background::paragraph 3 | yes | yes | yes | yes |
| atomic_003 | reviewer_1, reviewer_2 | reviewer_1_thread_003, reviewer_1_thread_004, reviewer_2_thread_004 | ready | high | yes | sections/architecture.tex::Model Configuration::paragraph 1, sections/results.tex::Model Variations::paragraph 1 | yes | yes | yes | yes |
| atomic_004 | reviewer_1 | reviewer_1_thread_005 | ready | high | no | sections/results.tex::Machine Translation::paragraph 2 | yes | yes | yes | yes |
| atomic_005 | reviewer_2 | reviewer_2_thread_001, reviewer_2_thread_002 | ready | high | yes | sections/training.tex::Data::paragraph 1, sections/training.tex::Implementation Notes::paragraph 1 | yes | yes | yes | yes |
| atomic_006 | reviewer_2 | reviewer_2_thread_003 | ready | medium | yes | sections/results.tex::Machine Translation::paragraph 1, sections/conclusion.tex::Conclusion::paragraph 2 | yes | yes | yes | yes |
| atomic_007 | reviewer_2 | reviewer_2_thread_005 | ready | medium | yes | sections/results.tex::Stability Statement::paragraph 1 | yes | yes | yes | yes |
| atomic_008 | reviewer_3 | reviewer_3_thread_001, reviewer_3_thread_003, reviewer_3_thread_005 | ready | high | yes | sections/discussion.tex::Discussion::paragraph 2, sections/conclusion.tex::Conclusion::paragraph 2 | yes | yes | yes | yes |
| atomic_009 | reviewer_3 | reviewer_3_thread_002 | ready | medium | yes | sections/results.tex::Interpretability::paragraph 1, sections/discussion.tex::Discussion::paragraph 4 | yes | yes | yes | yes |

## 线程覆盖表

| `thread_id` | `reviewer_id` | 关联 atomic comments | `response_resolution_kind` | `audited_log_present` | 最终行已就绪（`yes/no`） | 关联 atomic 已可导出（`yes/no`） | 线程已可导出（`yes/no`） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | atomic_001 | revision_backed | yes | yes | yes | yes |
| reviewer_1_thread_002 | reviewer_1 | atomic_002 | revision_backed | yes | yes | yes | yes |
| reviewer_1_thread_003 | reviewer_1 | atomic_003 | revision_backed | yes | yes | yes | yes |
| reviewer_1_thread_004 | reviewer_1 | atomic_003 | revision_backed | yes | yes | yes | yes |
| reviewer_1_thread_005 | reviewer_1 | atomic_004 | revision_backed | yes | yes | yes | yes |
| reviewer_2_thread_001 | reviewer_2 | atomic_005 | revision_backed | yes | yes | yes | yes |
| reviewer_2_thread_002 | reviewer_2 | atomic_005 | revision_backed | yes | yes | yes | yes |
| reviewer_2_thread_003 | reviewer_2 | atomic_006 | revision_backed | yes | yes | yes | yes |
| reviewer_2_thread_004 | reviewer_2 | atomic_003 | revision_backed | yes | yes | yes | yes |
| reviewer_2_thread_005 | reviewer_2 | atomic_007 | revision_backed | yes | yes | yes | yes |
| reviewer_3_thread_001 | reviewer_3 | atomic_008 | revision_backed | yes | yes | yes | yes |
| reviewer_3_thread_002 | reviewer_3 | atomic_009 | revision_backed | yes | yes | yes | yes |
| reviewer_3_thread_003 | reviewer_3 | atomic_008 | revision_backed | yes | yes | yes | yes |
| reviewer_3_thread_004 | reviewer_3 | atomic_001 | revision_backed | yes | yes | yes | yes |
| reviewer_3_thread_005 | reviewer_3 | atomic_008 | revision_backed | yes | yes | yes | yes |

## Working Manuscript 审计状态

| `relative_path` | `last_log_id` | `snapshot_sha256` | `last_audited_sha256` | `current_sha256` |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 导出产物表

| 产物 | 状态 | 输出路径 |
| --- | --- | --- |
| latexdiff_manuscript | pending |  |
| response_latex | ready | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.tex |
| response_markdown | ready | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/transformer-three-review-major-revision/outputs/response-letter.md |
| working_manuscript | ready | manuscript-copies/working-manuscript |
