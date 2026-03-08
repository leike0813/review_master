# Design: define-review-master-sql-write-recipes

## Context

`review-master` 现在已经采用 SQLite 唯一真源，运行时写入全部落在 `review-master.db`。当前缺口不在 schema，而在“如何安全写库”的操作层：同一类动作缺少统一写法，validator 的状态机指令也尚未显式对齐到对应写库动作。

这条 change 只解决“标准写库 recipe + validator recipe hint”，不改 schema、不封装新的写库脚本。

## Goals

- 为六阶段的常见写库动作建立稳定的 `recipe_id`
- 让 `SKILL.md` 明确要求优先复用标准 recipe
- 让 validator 的动作对象显式输出 `recipe_id`
- 让 playbook 展示动作、SQL 和 validator 指令之间的闭环

## Non-Goals

- 不修改数据库 schema
- 不新增自动写库脚本
- 不把 recipe 改造成 `.sql` 资产目录
- 不让 validator 自动执行任何写操作

## Decisions

### Recipe 文档优先

recipe 的单一真源放在 `review-master/references/sql-write-recipes.md`。这是因为当前项目的运行核心仍是 skill 指令和参考文档，Agent 在运行中更适合阅读和遵守明确的写入规约，而不是调用另一层写库工具。

### Validator 只输出 hint，不代写库

validator 继续保持只读。它会在动作对象上增加 `recipe_id`，但不会自动执行 recipe。这样可以保持当前“Agent 推理写库 -> validator 校验”的闭环不变。

### Repair 顺序继续以上游优先为主

当 validator 给出 `repair_sequence` 时，动作对象的 `recipe_id` 也遵守先上游后下游的原则：

1. `workflow_state`
2. `manuscript_summary`
3. `atomic_comments`
4. `comment_workboard`
5. `strategy_cards`
6. `comment_completion_status`

这和现有 validator 的 repair 排序一致，只是现在显式对齐到标准 recipe。

### Playbook 只补 SQL 视角，不改故事线

现有两份 playbook 已经稳定表达了 happy path 和补证据闭环。这里不新增第三份 playbook，只把它们补成“动作 -> recipe_id -> SQL -> validator”的链条。

## Files

- `openspec/changes/define-review-master-sql-write-recipes/proposal.md`
  - 说明 change 的必要性和影响范围
- `openspec/changes/define-review-master-sql-write-recipes/design.md`
  - 记录 recipe 文档优先、validator hint 和 playbook 同步策略
- `openspec/changes/define-review-master-sql-write-recipes/tasks.md`
  - 列出实现和验证任务
- `openspec/changes/define-review-master-sql-write-recipes/specs/review-master-sql-write-recipes/spec.md`
  - 规范 SQL recipe 文档与 skill 使用规则
- `openspec/changes/define-review-master-sql-write-recipes/specs/review-master-validator-recipe-hints/spec.md`
  - 规范 validator 输出 `recipe_id`
- `openspec/changes/define-review-master-sql-write-recipes/specs/review-master-playbook-sql-recipes/spec.md`
  - 规范 playbook 展示 recipe 与 SQL 片段
- `review-master/references/sql-write-recipes.md`
  - 新增 recipe 手册
- `review-master/SKILL.md`
  - 增加 SQL write recipe 使用规则
- `review-master/references/helper-scripts.md`
  - 补充 validator 动作对象中的 `recipe_id`
- `review-master/scripts/validate_artifact_consistency.py`
  - 为动作对象增加 `recipe_id`
- `playbooks/review-master-happy-path.md`
  - 补充关键 recipe 和 SQL 片段
- `playbooks/review-master-evidence-supplement-playbook.md`
  - 补充关键 recipe 和 SQL 片段

## Validation

- `openspec validate define-review-master-sql-write-recipes --type change --strict`
- `mypy` 检查 `review-master/scripts/validate_artifact_consistency.py`
- 核对两份 playbook 中的 `recipe_id` 是否与 validator 和 recipe 文档一致
