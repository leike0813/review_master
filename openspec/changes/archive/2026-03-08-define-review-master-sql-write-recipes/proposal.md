# Proposal: define-review-master-sql-write-recipes

## Summary

为 `review-master` 的 DB-first 运行时补一套标准 SQL write recipe，并让 validator 在 `instruction_payload` 中显式输出对应 `recipe_id`。

## Why

当前 skill 已经切换到 SQLite 唯一真源，但 Agent 仍然需要自行组织 SQL 写入顺序。随着阶段和表数量增加，如果没有标准 recipe，会出现：

- 同类写库动作写法不一致
- 多表更新顺序不稳定
- validator 虽然能指出下一步动作，但不能直接指向对应写库方法
- playbook 很难示范“动作 -> SQL 写法 -> validator 指引”的完整闭环

把常见写操作规范化为 recipe，可以把运行时写库行为固定下来，让 Agent、validator 和 playbook 共享同一套动作词汇。

## What Changes

- 新增 `review-master/references/sql-write-recipes.md`
- 更新 `review-master/SKILL.md`，要求优先复用标准 SQL recipe
- 扩展 `review-master/scripts/validate_artifact_consistency.py`，为动作对象补 `recipe_id`
- 更新两份 playbook，加入 `recipe_id`、代表性 SQL 和表更新范围
- 新增这条 change 的 proposal/design/specs/tasks

## Impact

- 不修改现有 SQLite schema
- 不新增数据库写入 helper script
- Agent 仍然直接写 SQL，但要按标准 recipe 执行
- validator 仍然只读，只增加 recipe hint
