# Final Assembly Checklist

这是从 `review-master.db` 渲染出的最终闭环视图。数据库真源是 `comment_completion_status`、`response_thread_resolution_links`、`response_thread_rows`、`export_artifacts`、`raw_review_threads` 和 `atomic_comments`。导出前既要检查 canonical atomic item 是否闭环，也要检查 reviewer 线程是否已被最终 row 覆盖，以及 marked/clean 双阶段导出状态是否就绪。

## Atomic 完成表

| `comment_id` | 来源审稿人 | 来源线程 | `status` | `priority` | `evidence_gap` | 目标位置 | `manuscript_draft_done` | `response_draft_done` | `one_to_one_link_checked` | `export_ready` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1, reviewer_2 | reviewer_1_thread_001, reviewer_2_thread_002 | ready | high | no | sections/results.tex::Main Comparison::paragraph 2 | yes | yes | yes | yes |
| atomic_002 | reviewer_1 | reviewer_1_thread_002 | ready | medium | no | sections/results.tex::Ablation Placeholder::paragraph 1 | yes | yes | yes | yes |
| atomic_003 | reviewer_1 | reviewer_1_thread_003 | ready | medium | no | sections/method.tex::Implementation Details::paragraph 3 | yes | yes | yes | yes |
| atomic_004 | reviewer_2 | reviewer_2_thread_001 | blocked | high | yes | sections/results.tex::Stability Analysis::figure placeholder, sections/results.tex::Stability Analysis::paragraph 2 | yes | yes | yes | yes |
| atomic_005 | reviewer_2 | reviewer_2_thread_002 | ready | medium | no | sections/discussion.tex::Limitations::paragraph 1 | yes | yes | yes | yes |

## 线程覆盖表

| `thread_id` | `reviewer_id` | 关联 atomic comments | 响应链接已覆盖（`yes/no`） | 最终行已就绪（`yes/no`） | 关联 atomic 已可导出（`yes/no`） | 线程已可导出（`yes/no`） |
| --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | atomic_001 | yes | yes | yes | yes |
| reviewer_1_thread_002 | reviewer_1 | atomic_002 | yes | yes | yes | yes |
| reviewer_1_thread_003 | reviewer_1 | atomic_003 | yes | yes | yes | yes |
| reviewer_2_thread_001 | reviewer_2 | atomic_004 | yes | yes | yes | yes |
| reviewer_2_thread_002 | reviewer_2 | atomic_001, atomic_005 | yes | yes | yes | yes |

## 导出产物表

| 产物 | 状态 | 输出路径 |
| --- | --- | --- |
| clean_manuscript | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/evidence-supplement-multi-review/outputs/revised-manuscript/main.tex |
| marked_manuscript | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/evidence-supplement-multi-review/outputs/marked-manuscript/main.tex |
| response_latex | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.tex |
| response_markdown | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/evidence-supplement-multi-review/outputs/response-letter.md |
