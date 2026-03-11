# Review Comment Coverage

这是从 `review-master.db` 渲染出的 Stage 3 覆盖率审阅视图。数据库真源是 `review_comment_source_documents`、`review_comment_coverage_segments` 和 `review_comment_coverage_segment_comment_links`。用户应通过它检查原始审稿意见是否已被充分提取，以及每个已覆盖片段是否映射到了正确的 `thread_id` 和 `comment_id`。

## 图例

- `[[covered thread:<thread_id> comments:<comment_id,...>]]...[[/covered]]` 表示这段原文已经被纳入 Stage 3 真源。
- 凡是没有 `[[covered ...]]` 包裹的文本，都是仍需人工核查的未覆盖残留。

## reviewer_1 / thread 1

- `source_document_id`: legacy-thread::reviewer_1_thread_001
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_1_thread_001`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_1_thread_001 comments:atomic_001,atomic_002]]Please clarify why the proposed method outperforms the baseline and explain what part of the results section supports this claim.[[/covered]]
```

