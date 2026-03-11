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
[[covered thread:reviewer_1_thread_001 comments:atomic_001]]The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.[[/covered]]
```

## reviewer_1 / thread 2

- `source_document_id`: legacy-thread::reviewer_1_thread_002
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_1_thread_002`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_1_thread_002 comments:atomic_002]]The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.[[/covered]]
```

## reviewer_1 / thread 3

- `source_document_id`: legacy-thread::reviewer_1_thread_003
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_1_thread_003`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_1_thread_003 comments:atomic_003]]The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.[[/covered]]
```

## reviewer_1 / thread 4

- `source_document_id`: legacy-thread::reviewer_1_thread_004
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_1_thread_004`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_1_thread_004 comments:atomic_003]]The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.[[/covered]]
```

## reviewer_1 / thread 5

- `source_document_id`: legacy-thread::reviewer_1_thread_005
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_1_thread_005`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_1_thread_005 comments:atomic_004]]The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.[[/covered]]
```

## reviewer_2 / thread 1

- `source_document_id`: legacy-thread::reviewer_2_thread_001
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_2_thread_001`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_2_thread_001 comments:atomic_005]]The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.[[/covered]]
```

## reviewer_2 / thread 2

- `source_document_id`: legacy-thread::reviewer_2_thread_002
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_2_thread_002`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_2_thread_002 comments:atomic_005]]Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.[[/covered]]
```

## reviewer_2 / thread 3

- `source_document_id`: legacy-thread::reviewer_2_thread_003
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_2_thread_003`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_2_thread_003 comments:atomic_006]]The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.[[/covered]]
```

## reviewer_2 / thread 4

- `source_document_id`: legacy-thread::reviewer_2_thread_004
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_2_thread_004`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_2_thread_004 comments:atomic_003]]The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.[[/covered]]
```

## reviewer_2 / thread 5

- `source_document_id`: legacy-thread::reviewer_2_thread_005
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_2_thread_005`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_2_thread_005 comments:atomic_007]]Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.[[/covered]]
```

## reviewer_3 / thread 1

- `source_document_id`: legacy-thread::reviewer_3_thread_001
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_3_thread_001`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_3_thread_001 comments:atomic_008]]The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.[[/covered]]
```

## reviewer_3 / thread 2

- `source_document_id`: legacy-thread::reviewer_3_thread_002
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_3_thread_002`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_3_thread_002 comments:atomic_009]]The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.[[/covered]]
```

## reviewer_3 / thread 3

- `source_document_id`: legacy-thread::reviewer_3_thread_003
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_3_thread_003`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_3_thread_003 comments:atomic_008]]Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.[[/covered]]
```

## reviewer_3 / thread 4

- `source_document_id`: legacy-thread::reviewer_3_thread_004
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_3_thread_004`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_3_thread_004 comments:atomic_001]]The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.[[/covered]]
```

## reviewer_3 / thread 5

- `source_document_id`: legacy-thread::reviewer_3_thread_005
- 来源类型: `review_comments_source`
- 来源路径: `legacy://review-comments/reviewer_3_thread_005`
- 覆盖摘要: 1 个已覆盖片段，0 个未覆盖片段，覆盖 1 条 thread

### 覆盖率拷贝

```text
[[covered thread:reviewer_3_thread_005 comments:atomic_008]]The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.[[/covered]]
```

