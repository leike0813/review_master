## Why

`review-master` 已经有了中间工件模板、填写规则和统一验证器，但还缺少一个正式的运行时 artifact workspace 机制。现在既没有一个稳定的初始化入口，也没有一个能让 agent 持续掌握全局阶段门禁、当前活跃条目和待确认事项的状态工件。

同时，现有 `references/` 模板是参考模板，不适合作为运行时工作目录直接使用。需要把“参考模板”和“运行时 scaffold”分开，并让初始化后的 workspace 从第一步起就能通过结构与格式基线校验。

## What Changes

- 新增一个正式的运行时 artifact workspace change
- 固定 workspace 目录结构，并新增 `workflow-state.yaml` 作为全局流程总控工件
- 新增 `review-master/scripts/init_artifact_workspace.py`，用于初始化运行时 workspace
- 在 `review-master/assets/artifact-workspace/` 提供运行时 scaffold，而不是直接复用 `references/`
- 扩展 `review-master/scripts/validate_artifact_consistency.py`，使其验证 `workflow-state.yaml`，并接受“初始化即干净”的 scaffold 状态
- 更新 `review-master/SKILL.md`、`review-master/references/helper-scripts.md` 和 `review-master/references/artifact-authoring-rules.md`，把初始化、状态维护、阶段验证和回修流程写清楚

## Capabilities

### New Capabilities

- `review-master-artifact-workspace-layout`: 规定运行时 artifact workspace 的固定目录结构和 `references/` 与 runtime scaffold 的职责边界
- `review-master-artifact-workspace-bootstrap`: 规定初始化脚本的 CLI、默认命名和冲突处理规则
- `review-master-workflow-state-artifact`: 规定 `workflow-state.yaml` 的职责、最小字段和与 comment 工件的一致性约束
- `review-master-artifact-workspace-validation-baseline`: 规定统一验证器如何处理运行时 scaffold、状态工件、阶段门禁和跨工件一致性

### Modified Capabilities

<!-- None -->

## Impact

- 新增 `openspec/changes/bootstrap-review-master-artifact-workspace/`
- 新增 `review-master/assets/artifact-workspace/`
- 新增 `review-master/scripts/init_artifact_workspace.py`
- 更新 `review-master/scripts/validate_artifact_consistency.py`
- 更新 `review-master/SKILL.md`
- 更新 `review-master/references/helper-scripts.md`
- 更新 `review-master/references/artifact-authoring-rules.md`
- 可选新增 `review-master/references/workflow-state.md`
