# Design: switch-review-master-to-sqlite-ssot-rendering

## Decision Summary

- 运行时唯一真源：`review-master.db`
- 运行时 Markdown：只读渲染视图，不可直写
- `workflow-state.yaml` 退役，状态写入数据库
- 阶段四收缩为单一视图：`comment-workboard.md`
- validator 负责只读验证、状态机判断和全量重渲染
- Agent 正式写接口：直接 SQL

## Runtime Model

workspace 根目录固定包含：

- `review-master.db`
- `workflow-state.md`
- `manuscript-structure-summary.md`
- `atomic-review-comment-list.md`
- `comment-workboard.md`
- `final-assembly-checklist.md`
- `response-strategy-cards/`

数据库表覆盖：

- 全局状态
- 原稿结构
- 原子意见
- 阶段四主工作板
- 逐条策略
- 最终闭环状态

## Validator Responsibilities

validator 输入保持 `--artifact-root PATH`。

它必须：

- 打开数据库并检查 schema
- 补充校验 target_location、阶段门禁和覆盖关系
- 全量重渲染 Markdown 视图
- 输出 `instruction_payload`

它不再：

- 把 Markdown 当真源
- 解析多份 Markdown 之间的一致性

## Migration Notes

- 旧的 `comment-manuscript-mapping-table.md` 与 `revision-board.md` 退役
- 旧 playbook 样例 workspace 统一迁移到 DB-first 模式
- validator JSON 示例统一迁移到 DB-first 语义
