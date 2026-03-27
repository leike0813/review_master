# Manuscript Revision Guide

这是从 `review-master.db` 渲染出的 Stage 5 稿件修改指南。它把已确认策略卡派生成可执行的 Stage 6 revision backlog。

## `atomic_001`

- Canonical 摘要: Explain why attention-only can replace recurrence and convolution in this translation setting.
- 所需动作: Add a concrete mechanism-based explanation of the attention-only claim.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_001_action_001 | 1 | 1 | modification_strategy | Revise the introduction and main-results explanation to state why short attention paths help long-range dependency modeling. | Revise the introduction and main-results explanation to state why short attention paths help long-range dependency modeling. | Provide a direct point-to-point response for atomic_001. | completed |

## `atomic_002`

- Canonical 摘要: Clarify novelty positioning against ByteNet, ConvS2S, and related prior work.
- 所需动作: Strengthen the prior-work boundary and novelty statement.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_002_action_001 | 2 | 1 | modification_strategy | Rewrite the background positioning paragraph to distinguish the paper from ByteNet, ConvS2S, and memory-style attention. | Rewrite the background positioning paragraph to distinguish the paper from ByteNet, ConvS2S, and memory-style attention. | Provide a direct point-to-point response for atomic_002. | completed |

## `atomic_003`

- Canonical 摘要: Justify architecture sensitivity, including heads, dimensions, and model-scale effects.
- 所需动作: Add ablation and sensitivity support for the architecture choices.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_003_action_001 | 3 | 1 | modification_strategy | Add a concise architecture-sensitivity paragraph summarizing head-count, dropout, and scale variations. | Add a concise architecture-sensitivity paragraph summarizing head-count, dropout, and scale variations. | Provide a direct point-to-point response for atomic_003. | completed |

## `atomic_004`

- Canonical 摘要: Explain the mechanism behind the baseline gain in the main results.
- 所需动作: Provide a causal explanation for why the Transformer improves over baselines.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_004_action_001 | 4 | 1 | modification_strategy | Revise the main-results discussion to explain why short attention paths plausibly improve the baseline comparison. | Revise the main-results discussion to explain why short attention paths plausibly improve the baseline comparison. | Provide a direct point-to-point response for atomic_004. | completed |

## `atomic_005`

- Canonical 摘要: Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details.
- 所需动作: Make the training and decoding protocol reproducible.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_005_action_001 | 5 | 1 | modification_strategy | Restore WMT data, preprocessing, checkpoint averaging, and beam-search details in the training section. | Restore WMT data, preprocessing, checkpoint averaging, and beam-search details in the training section. | Provide a direct point-to-point response for atomic_005. | completed |

## `atomic_006`

- Canonical 摘要: Clarify training-cost accounting and fairness caveats in the efficiency claim.
- 所需动作: Qualify the FLOPs and hardware comparison claim.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_006_action_001 | 6 | 1 | modification_strategy | Add a cost-accounting paragraph clarifying hardware, FLOPs, and fairness caveats. | Add a cost-accounting paragraph clarifying hardware, FLOPs, and fairness caveats. | Provide a direct point-to-point response for atomic_006. | completed |

## `atomic_007`

- Canonical 摘要: Add stability or variance evidence beyond headline BLEU.
- 所需动作: Report stability support and calibrate the single-run claim.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_007_action_001 | 7 | 1 | modification_strategy | Add a stability paragraph calibrated by the supplemental multi-run evidence. | Add a stability paragraph calibrated by the supplemental multi-run evidence. | Provide a direct point-to-point response for atomic_007. | completed |

## `atomic_008`

- Canonical 摘要: Expand limitations, failure buckets, and scope boundaries.
- 所需动作: Add a fuller limitations and failure-mode discussion.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_008_action_001 | 8 | 1 | modification_strategy | Expand the discussion to name failure buckets, scope boundaries, and long-sequence cost caveats. | Expand the discussion to name failure buckets, scope boundaries, and long-sequence cost caveats. | Provide a direct point-to-point response for atomic_008. | completed |

## `atomic_009`

- Canonical 摘要: Add an interpretability case study with qualitative attention evidence.
- 所需动作: Support the interpretability claim with a concrete example.

| `plan_action_id` | `plan_order` | `action_order` | `execution_category` | 修改目标 | 建议修改 | 证据要求 | `status` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| atomic_009_action_001 | 9 | 1 | modification_strategy | Add a qualitative attention case-study paragraph tied to a long sentence example. | Add a qualitative attention case-study paragraph tied to a long sentence example. | Provide a direct point-to-point response for atomic_009. | completed |

