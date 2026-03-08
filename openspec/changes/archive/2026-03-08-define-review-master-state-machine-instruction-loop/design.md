## Context

当前 `review-master` 已经具备：

- 六阶段主流程
- `workflow-state.yaml`
- 运行时 workspace 初始化脚本
- 统一 validator

但 validator 的输出还停留在“发现问题”的层面，没有形成 agent 可直接消费的执行指令。用户已经明确要求把状态迁移规则做成指令系统，并让 validator 在每次运行后给 agent 输出“现在状态、下一步能做什么、下一步该做什么”。

因此这次 change 的重点不是引入自动修复，而是把状态机规则文档化、结构化，并把它们投影成 validator 的指令负载。

## Goals / Non-Goals

**Goals:**

- 定义一份状态机指令文档，作为状态迁移规则的单一真源
- 让 validator 输出可执行的 `instruction_payload`
- 让 `instruction_payload` 同时覆盖状态摘要、允许动作、推荐动作、修复顺序和禁止动作
- 固定修复顺序为“先上游后下游”
- 在 `SKILL.md` 中把 validator 驱动循环写成正式执行规则

**Non-Goals:**

- 不新增自动修复脚本
- 不让 validator 直接修改工件
- 不把状态机做成完整事件日志系统
- 不改变既有六阶段主流程与工件布局

## Decisions

### 1. 状态机规则的单一真源放在参考文档

- Decision: 新增 `review-master/references/workflow-state-machine.md`
- Rationale: 状态机规则需要可审阅、可扩展、可被 `SKILL.md` 和 validator 同时引用，参考文档比硬编码或塞入主文档更稳
- Alternatives considered:
  - 直接写死在 validator
  - 全部塞进 `SKILL.md`
- Why not: 前者不利于规则审阅，后者会继续压重主指令

### 2. validator 输出结构化骨架 + 清晰自然语言

- Decision: `instruction_payload` 保持 JSON 骨架，但每条指令对象都带足够清晰的自然语言 `instruction` 和 `reason`
- Rationale: agent 需要稳定消费字段，同时也需要读起来就能执行的详细说明
- Alternatives considered:
  - 仅给一个 `next_step`
  - 仅给长段落文字
- Why not: 前者信息不足，后者难以稳定消费

### 3. 修复建议必须按上游优先

- Decision: validator 将问题按工件依赖顺序聚合，生成 `repair_sequence`
- Rationale: 用户明确要求统一程序负责整体一致性，若不锁定上游优先，agent 很容易先修派生工件导致返工
- Alternatives considered:
  - 按严重度排序
  - 全量平铺无优先级
- Why not: 两者都无法稳定表达“先修真源，再修派生”的依赖关系

### 4. validator 的推荐动作始终受问题和 gate 双重约束

- Decision:
  - 有问题时，`recommended_next_action` 优先指向 `repair_sequence` 的首项
  - 无问题但 gate 为 `blocked` 时，推荐动作指向请求用户确认、补材或澄清
  - 无问题且 gate 为 `ready` 时，推荐动作指向下一阶段允许的最小前进行动
- Rationale: 这正是用户要的“用户指令 -> 推理 -> 处理 -> 验证 -> 接收下一步指令”闭环

## Instruction Payload Model

validator 保留现有顶层输出：

- `status`
- `summary`
- `artifact_presence`
- `format_errors`
- `dependency_errors`
- `consistency_errors`

新增：

- `instruction_payload`

`instruction_payload` 顶层字段固定为：

- `current_state`
- `allowed_next_actions`
- `recommended_next_action`
- `repair_sequence`
- `blocked_actions`

约束：

- `recommended_next_action` 必须总是来自 `allowed_next_actions` 或 `repair_sequence` 的首项逻辑结果
- `repair_sequence` 仅在存在问题时非空
- `blocked_actions` 必须明确描述当前不能做什么，以及为什么不能做

## State Machine Model

状态机文档至少定义：

- 各阶段 `stage_1` 到 `stage_6`
- `ready | blocked`
- 每阶段可执行动作
- 每阶段禁止动作
- 进入下一阶段前的最低条件
- 用户确认缺失、证据缺口、上游工件失效时的回退规则

validator 的实现以这份文档中的规则为准，但首期不要求代码直接解析 Markdown 文档；文档是规范真源，代码是规范实现。

## Migration Plan

1. 创建新 change 的 proposal、design、specs 和 tasks。
2. 新增 `review-master/references/workflow-state-machine.md`。
3. 扩展 `validate_artifact_consistency.py`，生成 `instruction_payload`。
4. 更新 `SKILL.md`，把 validator 驱动循环写成正式规则。
5. 更新 `helper-scripts.md` 和 `workflow-state.md`，与新状态机规则交叉引用。
6. 运行 OpenSpec 校验、mypy 和多场景 validator 验收。
