# Design: normalize-review-master-workflow-cross-cutting-consistency

## Overview

这次 change 的目标不是改变 workflow，而是为现有 workflow 提供一套单一命名与术语真源，并把运行时、文档、playbook 与样例 fixture 的命名全部对齐。

## Key Decisions

### 1. 用 glossary 作为单一真源

新增 `review-master/references/workflow-glossary.md`，集中定义：

- 6 个阶段的正式名称
- 数据库真源、只读视图、最终导出产物的正式命名
- 3 个正式脚本名称与 `gate-and-render` 的唯一正式称呼
- 正式 action id 集合
- action 与 recipe 的边界

其他文档只引用和复用 glossary，不再自行发明别名。

### 2. 正式动作名只保留一套

本次锁定一套正式 action id，并要求这些名字在以下几层一致：

- `workflow_state.next_action`
- `instruction_payload.allowed_next_actions[*].action_id`
- `instruction_payload.recommended_next_action.action_id`
- recipe 文档的动作引用
- playbook 与 sample fixture

### 3. 样例路径也属于正式契约的一部分

playbook/examples 是给人和 Agent 参考的运行样例，因此它们的路径、目录名和 JSON fixture 命名也必须与正式契约一致。

因此本次直接改名：

- `validator-output/` -> `gate-and-render-output/`

同时统一 Stage 4 fixture 命名，避免最小样例和复杂样例各用一套说法。

## Affected Areas

- 发布目录文档：
  - `review-master/SKILL.md`
  - `review-master/references/*.md`
  - `review-master/assets/runtime/skill-runtime-digest.md`
- playbook 与样例：
  - `playbooks/review-master-*.md`
  - `playbooks/examples/**`
- 如有必要，微调 runtime 输出中的 action naming，使其重新与文档一致

## Non-Goals

- 不新增脚本
- 不改数据库表结构
- 不改变阶段数、阶段职责或导出流程
