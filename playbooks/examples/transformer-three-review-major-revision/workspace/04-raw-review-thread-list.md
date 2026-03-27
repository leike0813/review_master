# Raw Review Thread List

这是从 `review-master.db` 渲染出的原始审稿意见块只读视图。数据库真源是 `raw_review_threads`。这是最终 response letter 的正式索引层，用户应优先在这里核对 reviewer 原始条目的顺序与边界。

## 原始线程表

| `thread_id` | `reviewer_id` | `thread_order` | `source_type` | 归一化摘要 | 关联 atomic comments |
| --- | --- | --- | --- | --- | --- |
| reviewer_1_thread_001 | reviewer_1 | 1 | reviewer_comment | Clarify why attention-only is a viable replacement beyond parallelism. | atomic_001 |
| reviewer_1_thread_002 | reviewer_1 | 2 | reviewer_comment | Clarify novelty positioning against efficient sequence models. | atomic_002 |
| reviewer_1_thread_003 | reviewer_1 | 3 | reviewer_comment | Request component-level sensitivity analysis. | atomic_003 |
| reviewer_1_thread_004 | reviewer_1 | 4 | reviewer_comment | Request justification of architectural hyperparameters. | atomic_003 |
| reviewer_1_thread_005 | reviewer_1 | 5 | reviewer_comment | Request causal explanation for baseline gains. | atomic_004 |
| reviewer_2_thread_001 | reviewer_2 | 1 | reviewer_comment | Clarify data usage and evaluation protocol. | atomic_005 |
| reviewer_2_thread_002 | reviewer_2 | 2 | reviewer_comment | Clarify checkpoint averaging and decoding settings. | atomic_005 |
| reviewer_2_thread_003 | reviewer_2 | 3 | reviewer_comment | Clarify training-cost accounting and fairness caveat. | atomic_006 |
| reviewer_2_thread_004 | reviewer_2 | 4 | reviewer_comment | Repeat the request for architecture sensitivity evidence. | atomic_003 |
| reviewer_2_thread_005 | reviewer_2 | 5 | reviewer_comment | Request stability or variance support beyond headline BLEU. | atomic_007 |
| reviewer_3_thread_001 | reviewer_3 | 1 | reviewer_comment | Expand limitations and failure-mode discussion. | atomic_008 |
| reviewer_3_thread_002 | reviewer_3 | 2 | reviewer_comment | Request a concrete attention case study. | atomic_009 |
| reviewer_3_thread_003 | reviewer_3 | 3 | reviewer_comment | Request explicit failure buckets. | atomic_008 |
| reviewer_3_thread_004 | reviewer_3 | 4 | reviewer_comment | Request a concrete long-range dependency example. | atomic_001 |
| reviewer_3_thread_005 | reviewer_3 | 5 | reviewer_comment | Temper the conclusion and scope claims. | atomic_008 |

## 原始线程文本

### reviewer_1_thread_001

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.</div>

### reviewer_1_thread_002

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.</div>

### reviewer_1_thread_003

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.</div>

### reviewer_1_thread_004

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.</div>

### reviewer_1_thread_005

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.</div>

### reviewer_2_thread_001

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.</div>

### reviewer_2_thread_002

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.</div>

### reviewer_2_thread_003

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.</div>

### reviewer_2_thread_004

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.</div>

### reviewer_2_thread_005

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.</div>

### reviewer_3_thread_001

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.</div>

### reviewer_3_thread_002

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.</div>

### reviewer_3_thread_003

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.</div>

### reviewer_3_thread_004

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.</div>

### reviewer_3_thread_005

- 原文（按 Primary + Supporting 聚合）:

<div style="white-space: pre-wrap;">The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.</div>

