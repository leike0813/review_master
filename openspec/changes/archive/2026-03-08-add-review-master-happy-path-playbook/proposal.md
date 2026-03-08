## Why

`review-master` 现在已经有六阶段流程、运行时 workspace、状态机和统一验证器，但还缺一份“把这些组件真正串起来”的仓库级演练材料。当前的设计文档说明了每个组件是什么，却还没有展示一次从用户调用 skill 到最终产出的完整 happy-path 过程。

随着项目复杂度上升，如果没有一份统一的 playbook，后续开发者或 agent 很难快速判断：

- 每个阶段用户到底输入了什么
- agent 在每一步应该生成哪些工件
- validator 在各阶段应该输出什么类型的指令
- 用户和 agent 的往返交互应该怎样串起来

因此需要新增一份仓库级 happy-path playbook，并附带最小样例资产，作为开发、演练和回归对照资料。

## What Changes

- 新增一个仓库级 playbook change
- 在仓库根部新增 `playbooks/`，而不是把 playbook 放进 `review-master/` 发布目录
- 新增一份完整的 happy-path playbook，覆盖从 skill 调用到结束的六阶段过程
- 新增一套最小样例输入、最终态 workspace、最终输出和代表性 validator JSON 样例
- Playbook 严格复用当前已有的 workspace、状态机、工件模板和 validator 输出结构，不引入新的运行规则

## Capabilities

### New Capabilities

- `review-master-playbook-location`: 规定 playbook 属于仓库级演练文档，必须放在 `playbooks/` 而不是 skill 发布目录
- `review-master-playbook-happy-path-flow`: 规定 playbook 必须完整覆盖六阶段 happy path，并在每阶段显式记录用户输入、agent动作、工件变化、validator输出、agent回复和用户回复
- `review-master-playbook-example-assets`: 规定 playbook 必须附带一套最小样例输入、最终态 workspace、最终输出和代表性 validator JSON 样例

### Modified Capabilities

<!-- None -->

## Impact

- 新增 `openspec/changes/add-review-master-happy-path-playbook/`
- 新增 `playbooks/review-master-happy-path.md`
- 新增 `playbooks/examples/happy-path-minimal/`
- 不更新 `review-master/SKILL.md`
- 不更新 `review-master/scripts/validate_artifact_consistency.py`
- 不引入新的发布组件
