## Why

`review-master` 现在已经有运行时 workspace、全局状态工件和统一验证器，但 validator 仍然只会报告问题，不会把问题和状态转成 agent 可直接执行的下一步指令。缺少这层“验证后指令”，agent 虽然能看到错误，却还没有一套固定的状态机执行闭环来约束自己如何推进、回修和等待用户确认。

现在需要把状态迁移规则正式做成一套指令系统，并让 validator 在每次验证后输出当前状态、允许动作、推荐动作和修复顺序，确保 agent 始终在状态机约束下行动。

## What Changes

- 新增 `define-review-master-state-machine-instruction-loop` change
- 新增 `review-master/references/workflow-state-machine.md` 作为状态机指令的单一真源
- 扩展 `review-master/scripts/validate_artifact_consistency.py`，在现有 JSON 报告中新增 `instruction_payload`
- 固定 validator 的修复建议顺序为“先上游后下游”
- 更新 `review-master/SKILL.md`，把 validator 驱动的状态机循环写成正式指令
- 更新 `review-master/references/helper-scripts.md` 和 `review-master/references/workflow-state.md`，对齐状态机和 instruction payload

## Capabilities

### New Capabilities

- `review-master-workflow-state-machine-rules`: 定义状态机规则文档、阶段门禁、允许动作、禁止动作和回退规则
- `review-master-validator-instruction-payload`: 定义 validator 的 `instruction_payload` 结构和语义
- `review-master-upstream-first-repair-order`: 定义 validator 的修复建议顺序必须遵守上游优先
- `review-master-skill-validation-loop`: 定义 `SKILL.md` 中 validator 驱动的执行闭环

### Modified Capabilities

<!-- None -->

## Impact

- 新增 `openspec/changes/define-review-master-state-machine-instruction-loop/`
- 新增 `review-master/references/workflow-state-machine.md`
- 更新 `review-master/scripts/validate_artifact_consistency.py`
- 更新 `review-master/SKILL.md`
- 更新 `review-master/references/helper-scripts.md`
- 更新 `review-master/references/workflow-state.md`
