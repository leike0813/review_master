# Manuscript Execution Graph

这是 Stage 5 派生出的 revision action 依赖视图，用于在 Stage 6 中安排实际改稿顺序。

| `plan_order` | `plan_action_id` | `comment_id` | `action_order` | `execution_category` | 动作标题 | `status` | 依赖动作 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | atomic_001_action_001 | atomic_001 | 1 | modification_strategy | Revise the introduction and main-results explanation to state why short attention paths help long-range dependency modeling. | completed |  |
| 2 | atomic_002_action_001 | atomic_002 | 1 | modification_strategy | Rewrite the background positioning paragraph to distinguish the paper from ByteNet, ConvS2S, and memory-style attention. | completed |  |
| 3 | atomic_003_action_001 | atomic_003 | 1 | modification_strategy | Add a concise architecture-sensitivity paragraph summarizing head-count, dropout, and scale variations. | completed |  |
| 4 | atomic_004_action_001 | atomic_004 | 1 | modification_strategy | Revise the main-results discussion to explain why short attention paths plausibly improve the baseline comparison. | completed |  |
| 5 | atomic_005_action_001 | atomic_005 | 1 | modification_strategy | Restore WMT data, preprocessing, checkpoint averaging, and beam-search details in the training section. | completed |  |
| 6 | atomic_006_action_001 | atomic_006 | 1 | modification_strategy | Add a cost-accounting paragraph clarifying hardware, FLOPs, and fairness caveats. | completed |  |
| 7 | atomic_007_action_001 | atomic_007 | 1 | modification_strategy | Add a stability paragraph calibrated by the supplemental multi-run evidence. | completed |  |
| 8 | atomic_008_action_001 | atomic_008 | 1 | modification_strategy | Expand the discussion to name failure buckets, scope boundaries, and long-sequence cost caveats. | completed |  |
| 9 | atomic_009_action_001 | atomic_009 | 1 | modification_strategy | Add a qualitative attention case-study paragraph tied to a long sentence example. | completed |  |
