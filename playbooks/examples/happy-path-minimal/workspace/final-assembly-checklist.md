# Final Assembly Checklist

这是从 `review-master.db` 渲染出的最终闭环视图。数据库真源是 `comment_completion_status`、`response_thread_resolution_links`、`response_thread_rows`、`export_artifacts`、`raw_review_threads` 和 `atomic_comments`。导出前既要检查 canonical atomic item 是否闭环，也要检查原始 reviewer 线程是否已被最终 row 覆盖，以及 marked/clean 双阶段导出状态是否就绪。

## Atomic Completion Table

| `comment_id` | Source Reviewers | Source Threads | `status` | `priority` | `evidence_gap` | Target Locations | `manuscript_change_done` | `response_section_done` | `one_to_one_link_checked` | `export_ready` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001 | reviewer_1 | reviewer_1_thread_001 | ready | high | no | main.tex::Results::paragraph 2 | yes | yes | yes | yes |
| atomic_002 | reviewer_1 | reviewer_1_thread_001 | ready | medium | no | main.tex::Results::paragraph 3 | yes | yes | yes | yes |

## Thread Coverage Table

| `thread_id` | `reviewer_id` | Linked Atomic Comments | Response Link Covered (`yes/no`) | Final Row Ready (`yes/no`) | Linked Atomic Export Ready (`yes/no`) | Thread Export Ready (`yes/no`) |
| --- | --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | atomic_001, atomic_002 | yes | yes | yes | yes |

## Export Artifact Table

| Artifact | Status | Output Path |
| --- | --- | --- |
| clean_manuscript | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/revised-manuscript/main.tex |
| marked_manuscript | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/marked-manuscript/main.tex |
| response_latex | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/response-letter.tex |
| response_markdown | exported | /home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/happy-path-minimal/outputs/response-letter.md |
