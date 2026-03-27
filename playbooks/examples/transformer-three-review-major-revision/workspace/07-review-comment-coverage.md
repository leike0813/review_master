# Review Comment Coverage

这是从 `review-master.db` 渲染出的 Stage 3 覆盖率审阅视图。数据库真源是 `review_comment_source_documents`、`raw_thread_source_spans` 和 `raw_thread_atomic_links`。用户应通过它检查原始审稿意见的抽取是否锚定到准确的原文 offset，并核对每个高亮片段映射到的 `thread_id` 与 `comment_id`。

## 图例

- 已覆盖片段用醒目红色加粗显示，并在段尾附短 `thread_id` 标签（如 `[R1_T003]`）。
- 重复去重片段用醒目橙色加粗显示，并附 `[... dup]` 标签，表示该段语义已被抽取但在摘要层做了去重。
- 未覆盖片段保持默认黑色文本，表示该段原文仍需人工核查。

## 字符级覆盖率指标

以下指标由脚本根据 source document 与 source spans 自动计算，用于 Stage 3 的覆盖率阈值门禁。

- 全局覆盖率（含 duplicate_filtered）：2637/2665 字符（98.95%）。
- 全局覆盖率（去重诊断）：2637/2665 字符（98.95%）。
- 阈值：hard=30.0%，soft=50.0%。
- 当前阈值判定：通过

### 分文档字符覆盖率

| `source_document_id` | 来源标签 | 字符总数 | 已覆盖（含 duplicate_filtered） | 已覆盖（去重诊断） |
| --- | --- | --- | --- | --- |
| `review_comments_source_001` | Review Comments Source | `2665` | `2637/2665` (98.95%) | `2637/2665` (98.95%) |

## Review Comments Source

- `source_document_id`: review_comments_source_001
- 来源类型: `review_comments_source`
- 来源路径: `tests://review-comments-source.md`
- 覆盖摘要: 15 个已覆盖片段，14 个未覆盖片段，覆盖 15 条 thread
- 其中 primary 15 段、supporting 0 段、duplicate_filtered 0 段

### 原文覆盖视图

<div style="white-space: pre-wrap; border: 1px solid #d0d7de; border-radius: 6px; padding: 12px;">
<span style="color: #d32f2f; font-weight: 700;">The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T001]</span>



<span style="color: #d32f2f; font-weight: 700;">The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T002]</span>



<span style="color: #d32f2f; font-weight: 700;">The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T003]</span>



<span style="color: #d32f2f; font-weight: 700;">The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T004]</span>



<span style="color: #d32f2f; font-weight: 700;">The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.</span><span style="color: #6a737d; font-size: 0.85em;"> [R1_T005]</span>



<span style="color: #d32f2f; font-weight: 700;">The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.</span><span style="color: #6a737d; font-size: 0.85em;"> [R2_T001]</span>



<span style="color: #d32f2f; font-weight: 700;">Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.</span><span style="color: #6a737d; font-size: 0.85em;"> [R2_T002]</span>



<span style="color: #d32f2f; font-weight: 700;">The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.</span><span style="color: #6a737d; font-size: 0.85em;"> [R2_T003]</span>



<span style="color: #d32f2f; font-weight: 700;">The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.</span><span style="color: #6a737d; font-size: 0.85em;"> [R2_T004]</span>



<span style="color: #d32f2f; font-weight: 700;">Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.</span><span style="color: #6a737d; font-size: 0.85em;"> [R2_T005]</span>



<span style="color: #d32f2f; font-weight: 700;">The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.</span><span style="color: #6a737d; font-size: 0.85em;"> [R3_T001]</span>



<span style="color: #d32f2f; font-weight: 700;">The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.</span><span style="color: #6a737d; font-size: 0.85em;"> [R3_T002]</span>



<span style="color: #d32f2f; font-weight: 700;">Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.</span><span style="color: #6a737d; font-size: 0.85em;"> [R3_T003]</span>



<span style="color: #d32f2f; font-weight: 700;">The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.</span><span style="color: #6a737d; font-size: 0.85em;"> [R3_T004]</span>



<span style="color: #d32f2f; font-weight: 700;">The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.</span><span style="color: #6a737d; font-size: 0.85em;"> [R3_T005]</span>
</div>

### 覆盖映射附录

下表按已覆盖片段逐行列出映射信息，方便用户在不阅读内联技术标签的情况下核对 Stage 3 提取结果。

| `source_document_id` | `thread_id` | `span_role` | `comment_ids` | `span_order` | `offset_range` | `segment_excerpt` |
| --- | --- | --- | --- | --- | --- | --- |
| `review_comments_source_001` | `reviewer_1_thread_001` | `primary` | `atomic_001` | `1` | `0:195` | The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly... |
| `review_comments_source_001` | `reviewer_1_thread_002` | `primary` | `atomic_002` | `1` | `197:386` | The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here an... |
| `review_comments_source_001` | `reviewer_1_thread_003` | `primary` | `atomic_003` | `1` | `388:592` | The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes fro... |
| `review_comments_source_001` | `reviewer_1_thread_004` | `primary` | `atomic_003` | `1` | `594:794` | The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide ... |
| `review_comments_source_001` | `reviewer_1_thread_005` | `primary` | `atomic_004` | `1` | `796:971` | The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing ... |
| `review_comments_source_001` | `reviewer_2_thread_001` | `primary` | `atomic_005` | `1` | `973:1167` | The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the e... |
| `review_comments_source_001` | `reviewer_2_thread_002` | `primary` | `atomic_005` | `1` | `1169:1341` | Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices.... |
| `review_comments_source_001` | `reviewer_2_thread_003` | `primary` | `atomic_006` | `1` | `1343:1519` | The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what make... |
| `review_comments_source_001` | `reviewer_2_thread_004` | `primary` | `atomic_003` | `1` | `1521:1684` | The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger abla... |
| `review_comments_source_001` | `reviewer_2_thread_005` | `primary` | `atomic_007` | `1` | `1686:1874` | Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can... |
| `review_comments_source_001` | `reviewer_3_thread_001` | `primary` | `atomic_008` | `1` | `1876:2062` | The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in... |
| `review_comments_source_001` | `reviewer_3_thread_002` | `primary` | `atomic_009` | `1` | `2064:2214` | The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualizatio... |
| `review_comments_source_001` | `reviewer_3_thread_003` | `primary` | `atomic_008` | `1` | `2216:2359` | Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phen... |
| `review_comments_source_001` | `reviewer_3_thread_004` | `primary` | `atomic_001` | `1` | `2361:2527` | The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or e... |
| `review_comments_source_001` | `reviewer_3_thread_005` | `primary` | `atomic_008` | `1` | `2529:2665` | The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats. |

