## Context

当前 `review-master` 已具备：

- 六阶段交互流程
- 六类 Markdown 中间工件模板
- 中间工件填写总规范
- 统一验证器 `validate_artifact_consistency.py`

但真正执行时还缺三块：

- 没有正式的运行时 workspace 初始化入口
- 没有一个全局状态工件来显式表达当前阶段、门禁、活跃 comment 和待确认事项
- `references/` 模板不是可直接用于 runtime 的 scaffold，直接拷贝会让验证器一开始就报大量格式问题

因此这次 change 的重点不是再增加语义能力，而是把运行时工件工作目录做实，并让它从 bootstrap 起就是一个可验证、可推进的工作区。

## Goals / Non-Goals

**Goals:**

- 提供一个初始化运行时 artifact workspace 的确定性脚本
- 固定 workspace 目录结构，并引入 `workflow-state.yaml` 作为全局总控工件
- 提供一套“初始化即干净”的 runtime scaffold
- 扩展统一验证器，使其同时理解 bootstrap state、authored state 和 workflow state
- 在 `SKILL.md` 中写清初始化、状态维护、验证和回修闭环

**Non-Goals:**

- 不新增稿件写回脚本
- 不新增导出脚本
- 不把 YAML 扩展成所有中间工件的主形态
- 不把全局状态工件做成历史事件日志
- 不改变六阶段主流程和逐条 comment 闭环处理模型

## Decisions

### 1. 运行时 scaffold 与参考模板分离

- Decision: 在 `review-master/assets/artifact-workspace/` 放置运行时 scaffold，`references/` 继续作为参考模板目录
- Rationale: 参考模板侧重“怎么填”，runtime scaffold 侧重“初始化后立刻可验证”；两者目标不同
- Alternatives considered:
  - 直接复制 `references/`
  - 在 `references/` 中同时维护 runtime 和 reference 双用途文件
- Why not: 直接复制会产生大量基线错误；混用会让文档与运行时约束纠缠

### 2. 全局状态工件采用单个固定 YAML 主文件

- Decision: 新增 `workflow-state.yaml`，放在 artifact-root 顶层
- Rationale: 这是面向 agent 的流程总控工件，不是用户主要阅读工件；YAML 更适合表达当前阶段、列表型待办和 gate 状态
- Alternatives considered:
  - 把状态区块并入 `revision-board.md`
  - 使用 Markdown 状态文件
  - 使用事件日志目录
- Why not: `revision-board` 已经承担 comment 级工作板职责；Markdown 不如 YAML 稳定；事件日志超出首期范围

### 3. `workflow-state.yaml` 只保存当前态

- Decision: 首期只保存当前阶段、当前门禁、当前活跃 comment、待确认项、全局 blocker 和下一步动作
- Rationale: 当前态足以支撑阶段门禁和 agent 的流程导航，同时避免把状态工件膨胀成执行日志
- Alternatives considered:
  - 保存最近历史
  - 保存完整事件流
- Why not: 会显著提高写入和验证复杂度，且不影响当前阶段目标

### 4. 初始化后的 workspace 必须是“结构与格式基线干净”的

- Decision: 统一验证器接受无数据行的 scaffold 状态，只要文件结构、表头和状态文件合法，就视为有效初始化态
- Rationale: 用户已经明确希望 bootstrap 产物初始化即干净，而不是初始化后立刻报错
- Alternatives considered:
  - 允许初始报错
  - 预填伪造示例行
- Why not: 前者破坏工作区初始化体验；后者会混入虚假业务数据

### 5. 阶段门禁与工件要求由状态文件驱动校验

- Decision: 验证器读取 `workflow-state.yaml`，将 `current_stage` 与 `stage_gate` 作为判定“当前应具备哪些工件内容”的上下文
- Rationale: 同一个工件目录在 bootstrap、分析中、处理中和导出前的有效性标准不同，必须显式区分
- Alternatives considered:
  - 只做静态格式检查
  - 靠文件是否为空推断阶段
- Why not: 静态检查无法表达阶段门禁；仅靠内容推断阶段不稳定

## Runtime Workspace Model

artifact-root 顶层固定包含：

- `workflow-state.yaml`
- `manuscript-structure-summary.md`
- `atomic-review-comment-list.md`
- `comment-manuscript-mapping-table.md`
- `revision-board.md`
- `final-assembly-checklist.md`
- `response-strategy-cards/`

`response-strategy-cards/` 在初始化时为空目录；进入阶段五后再按 `{comment_id}.md` 创建卡片。

## Validation Model

验证器继续使用：

- `--artifact-root PATH`

顶层输出继续保持：

- `status`
- `summary`
- `artifact_presence`
- `format_errors`
- `dependency_errors`
- `consistency_errors`

新增规则：

- `workflow-state.yaml` 缺失计入 presence error
- YAML 语法错误、非法字段值、缺字段计入 format errors
- `active_comment_id` 无法在原子清单中找到时计入 consistency errors
- `stage_gate = ready` 时，必须满足当前阶段进入下一阶段的最低工件条件
- 在 bootstrap state（`stage_1`）下，空表格、空策略卡目录和空 comment 工件允许通过

## Migration Plan

1. 创建新 change 的 proposal、design、specs 和 tasks。
2. 新增 `review-master/assets/artifact-workspace/` 及 runtime scaffold 文件。
3. 新增 `review-master/scripts/init_artifact_workspace.py`。
4. 扩展 `review-master/scripts/validate_artifact_consistency.py` 支持状态文件和 bootstrap 基线。
5. 更新 `review-master/SKILL.md`、`review-master/references/helper-scripts.md` 和 `review-master/references/artifact-authoring-rules.md`。
6. 运行 OpenSpec 校验、类型检查和初始化/验证脚本验收。
