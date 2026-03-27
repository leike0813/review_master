# Manuscript Execution Graph

这是 Stage 5 派生出的 revision action 依赖视图，用于在 Stage 6 中安排实际改稿顺序。

| `plan_order` | `plan_action_id` | `comment_id` | `action_order` | `execution_category` | 动作标题 | `status` | 依赖动作 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | atomic_001_action_001 | atomic_001 | 1 | modification_strategy | Expand the baseline-comparison explanation in the results discussion. | completed |  |
| 2 | atomic_002_action_001 | atomic_002 | 1 | modification_strategy | Add a scoped ablation rationale paragraph to the results discussion. | completed |  |
| 3 | atomic_003_action_001 | atomic_003 | 1 | modification_strategy | Clarify data splits and seeds in the method section. | completed |  |
| 4 | atomic_004_action_001 | atomic_004 | 1 | modification_strategy | Add the multi-seed stability figure and describe the trend. | completed |  |
| 5 | atomic_005_action_001 | atomic_005 | 1 | modification_strategy | Expand the limitations and discussion section. | completed |  |
