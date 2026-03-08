# Proposal: refine-review-master-stage-3-threaded-atomization

## Summary

将 `review-master` 的 Stage 3 从原则描述细化为操作手册级指令，并同步更新与 Stage 3 直接相关的 supporting docs。

## Why

当前 Stage 3 已经明确了三层模型和核心数据表，但还缺少足够细的执行规则：

- Agent 不容易稳定判断原始 reviewer 条目的 thread 边界
- 不同 reviewer 的重复意见何时应合并、何时不应合并，还缺少统一口径
- `SKILL.md`、Stage 3 文档、SQL recipe、状态机说明和 playbook 之间对 Stage 3 的要求仍偏概括

## What Changes

- 新增 Stage 3 的 OpenSpec change 工件
- 将 Stage 3 细化为原始条目抽取、去重、归并、拆分和 canonical atomic 建模的完整手册
- 同步更新 `SKILL.md`、Stage 3 文档、SQL recipe、状态机说明、helper-scripts 文档和一份 playbook

## Impact

这次改动只影响文档和 OpenSpec 工件，不改数据库 schema、不改脚本逻辑、不改总体六阶段流程。
