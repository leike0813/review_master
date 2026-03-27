# Review Comment Coverage

这是从 `review-master.db` 渲染出的 Stage 3 覆盖率审阅视图。数据库真源是 `review_comment_source_documents`、`raw_thread_source_spans` 和 `raw_thread_atomic_links`。用户应通过它检查原始审稿意见的抽取是否锚定到准确的原文 offset，并核对每个高亮片段映射到的 `thread_id` 与 `comment_id`。

## 图例

- 已覆盖片段用醒目红色加粗显示，并在段尾附短 `thread_id` 标签（如 `[R1_T003]`）。
- 重复去重片段用醒目橙色加粗显示，并附 `[... dup]` 标签，表示该段语义已被抽取但在摘要层做了去重。
- 未覆盖片段保持默认黑色文本，表示该段原文仍需人工核查。

## 字符级覆盖率指标

以下指标由脚本根据 source document 与 source spans 自动计算，用于 Stage 3 的覆盖率阈值门禁。

- 全局覆盖率（含 duplicate_filtered）：129/129 字符（100.0%）。
- 全局覆盖率（去重诊断）：129/129 字符（100.0%）。
- 阈值：hard=30.0%，soft=50.0%。
- 当前阈值判定：通过

### 分文档字符覆盖率

| `source_document_id` | 来源标签 | 字符总数 | 已覆盖（含 duplicate_filtered） | 已覆盖（去重诊断） |
| --- | --- | --- | --- | --- |
| `review_comments_source_001` | Review Comments Source | `129` | `129/129` (100.00%) | `129/129` (100.00%) |

## Review Comments Source

- `source_document_id`: review_comments_source_001
- 来源类型: `review_comments_source`
- 来源路径: `tests://review-comments-source.md`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread
- 其中 primary 1 段、supporting 0 段、duplicate_filtered 0 段

### 原文覆盖视图

<div style="white-space: pre-wrap; border: 1px solid #d0d7de; border-radius: 6px; padding: 12px;">
<span style="color: #d32f2f; font-weight: 700;">Please clarify why the proposed method outperforms the baseline and explain what part of the results section supports this claim.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T001]</span>
</div>

### 覆盖映射附录

下表按已覆盖片段逐行列出映射信息，方便用户在不阅读内联技术标签的情况下核对 Stage 3 提取结果。

| `source_document_id` | `thread_id` | `span_role` | `comment_ids` | `span_order` | `offset_range` | `segment_excerpt` |
| --- | --- | --- | --- | --- | --- | --- |
| `review_comments_source_001` | `reviewer_1_thread_001` | `primary` | `atomic_001, atomic_002` | `1` | `0:129` | Please clarify why the proposed method outperforms the baseline and explain what part of the results section supports this claim. |

