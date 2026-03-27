# Final Assembly Checklist

这是从 `review-master.db` 渲染出的最终闭环视图。数据库真源是 `comment_completion_status`、`response_thread_action_log_links`、`response_thread_rows`、`working_copy_file_state`、`export_artifacts`、`raw_review_threads` 和 `atomic_comments`。它用于检查 canonical atomic item 是否闭环、reviewer 线程是否被最终 row 覆盖、working manuscript 是否已完成审计，以及最终 response 输出是否就绪。

## Atomic 完成表

| `comment_id` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | `manuscript_execution_items_done` | `response_draft_done` | `one_to_one_link_checked` | `export_ready` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1 | reviewer_1_thread_001 | ready | high | no | main.tex::Results::paragraph 2 | yes | yes | yes | yes |
| atomic_002 | reviewer_1 | reviewer_1_thread_001 | ready | medium | no | main.tex::Results::paragraph 3 | yes | yes | yes | yes |

## 线程覆盖表

| `thread_id` | `reviewer_id` | 关联 atomic comments | `response_resolution_kind` | `audited_log_present` | 最终行已就绪（`yes/no`） | 关联 atomic 已可导出（`yes/no`） | 线程已可导出（`yes/no`） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | atomic_001, atomic_002 | revision_backed | yes | yes | yes | yes |

## Working Manuscript 审计状态

| `relative_path` | `last_log_id` | `snapshot_sha256` | `last_audited_sha256` | `current_sha256` |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 导出产物表

| 产物 | 状态 | 输出路径 |
| --- | --- | --- |
| latexdiff_manuscript | pending |  |
| response_latex | ready | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/response-letter.tex |
| response_markdown | ready | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/response-letter.md |
| working_manuscript | ready | manuscript-copies/working-manuscript |
