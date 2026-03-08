# Design: restructure-review-master-comment-mapping-model

## Overview

本 change 将 `review-master` 的 comment/workflow 结构固定为三层：

1. `raw_review_threads`
   - 原始 reviewer / editor 条目层
   - 这是最终 response letter 的正式索引层
2. `atomic_comments`
   - canonical atomic item 层
   - 这是内部执行真源索引层
3. `response_thread_resolution_links`
   - 从原始 thread 回收 atomic-level resolution 的聚合层

## Design Decisions

### Final response letter is indexed by raw review threads

最终 response letter 不再直接按 `comment_id` 输出，而是按 `thread_id` 输出。这样可以保持 reviewer 原始条目的结构与顺序，减少最终回信与 reviewer 原文脱节的问题。

### Duplicate reviewer comments are merged in the atomic layer

不同 reviewer 的重复意见在 `atomic_comments` 层真正合并。`comment_id` 不再携带 reviewer 身份，而是改为 canonical id。合并关系通过 `raw_thread_atomic_links` 和 `atomic_comment_source_spans` 保留。

### All many-to-many relationships are modeled as tables

以下关系全部表化：

- `thread_id -> comment_id`
- `comment_id -> source spans`
- `comment_id -> target locations`
- `comment_id -> analysis rows`
- `comment_id/action_order -> target locations`
- `thread_id -> response outline comment coverage`

不再使用 JSON/TEXT 多值列。

## Data Model Changes

### Added tables

- `raw_review_threads`
- `raw_thread_atomic_links`
- `atomic_comment_source_spans`
- `atomic_comment_target_locations`
- `atomic_comment_analysis_links`
- `strategy_action_target_locations`
- `response_thread_resolution_links`

### Refactored tables

- `atomic_comments`
  - reviewer-scoped row -> canonical atomic item
- `comment_workboard`
  - removed
- `atomic_comment_state`
  - new state table for atomic-level workboard state

## Rendered Views

The runtime rendered views become:

- `manuscript-structure-summary.md`
- `raw-review-thread-list.md`
- `atomic-review-comment-list.md`
- `thread-to-atomic-mapping.md`
- `atomic-comment-workboard.md`
- `response-letter-outline.md`
- `final-assembly-checklist.md`
- `response-strategy-cards/{comment_id}.md`

`workflow_state` remains database-only.

## Validation Model

`gate-and-render` now checks:

- thread coverage
- atomic coverage
- atomic workboard completeness
- strategy-card completeness
- response-thread outline coverage
- stage-6 export readiness at both atomic level and thread level

## Documentation Changes

The following documents must align with the new model:

- `review-master/SKILL.md`
- `review-master/references/stage-3-comment-atomization.md`
- `review-master/references/stage-4-workboard-planning.md`
- `review-master/references/stage-5-strategy-and-execution.md`
- `review-master/references/stage-6-final-review-and-export.md`
- `review-master/references/sql-write-recipes.md`
