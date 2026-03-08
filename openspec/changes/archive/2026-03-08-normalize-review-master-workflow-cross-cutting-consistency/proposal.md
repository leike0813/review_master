# Change Proposal: normalize-review-master-workflow-cross-cutting-consistency

## Why

`review-master` 的六阶段 workflow 已经比较完整，但横向材料之间仍有一些明显漂移：

- 同一动作在运行时、recipe 文档、playbook 和样例 fixture 中名字不完全一致
- 样例 fixture 目录仍保留 `validator-output/` 这类历史命名
- 部分运行时摘要和最终输出命名仍停留在旧契约
- 发布目录缺少一份统一术语真源，导致后续文档容易各写各的

这些问题不会改变核心能力，但会持续制造理解成本和维护风险。

## What Changes

- 新增 `review-master/references/workflow-glossary.md`，锁定正式术语、动作名、脚本称呼和最终导出产物命名。
- 统一发布目录文档中的阶段口径、完成定义、脚本称呼和动作命名。
- 把样例 fixture 目录从 `validator-output/` 统一改为 `gate-and-render-output/`。
- 同步刷新 playbook 文案和 JSON fixture 的术语、路径与 runtime digest。

## Scope

本次 change 只做横向一致性收口。

它不会：

- 增加新能力
- 修改数据库业务 schema
- 增加新脚本
- 改变现有六阶段 workflow 的职责边界

## Default Decisions

- `gate-and-render` 是唯一正式脚本称呼。
- 最终导出产物的正式命名固定为：
  - `marked_manuscript`
  - `clean_manuscript`
  - `response_markdown`
  - `response_latex`
- Stage 6 完成后的正式完成动作固定为 `stage_6_completed`。
- 样例 fixture 目录统一使用 `gate-and-render-output/`，不再把 `validator-output/` 作为正式路径。
