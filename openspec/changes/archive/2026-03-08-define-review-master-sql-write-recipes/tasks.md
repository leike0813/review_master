# Tasks: define-review-master-sql-write-recipes

- [ ] 新增 `review-master/references/sql-write-recipes.md`，定义标准 `recipe_id`、适用阶段、推荐 SQL 顺序和写后校验要求
- [ ] 更新 `review-master/SKILL.md`，增加 SQL write recipe 使用规则
- [ ] 更新 `review-master/references/helper-scripts.md`，说明 validator 动作对象会返回 `recipe_id`
- [ ] 扩展 `review-master/scripts/validate_artifact_consistency.py`，为 `allowed_next_actions`、`recommended_next_action`、`repair_sequence` 和 `blocked_actions` 中的动作对象增加 `recipe_id`
- [ ] 更新两份 playbook，补充关键 `recipe_id`、SQL 片段和表更新范围
- [ ] 更新样例 validator JSON，使其动作对象包含 `recipe_id`
- [ ] 运行 OpenSpec 严格校验
- [ ] 运行类型检查
