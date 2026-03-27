# Manuscript Execution Graph

这是 Stage 5 派生出的 revision action 依赖视图，用于在 Stage 6 中安排实际改稿顺序。

| `plan_order` | `plan_action_id` | `comment_id` | `action_order` | `execution_category` | 动作标题 | `status` | 依赖动作 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | atomic_001_action_001 | atomic_001 | 1 | modification_strategy | Expand the causal explanation for the baseline advantage in the Results discussion. | completed |  |
| 2 | atomic_001_action_002 | atomic_001 | 2 | modification_strategy | Add a sentence that points to the exact result paragraph supporting the claim. | completed |  |
| 3 | atomic_002_action_001 | atomic_002 | 1 | modification_strategy | Add an explicit signpost sentence that points to the relevant result paragraph. | completed |  |
