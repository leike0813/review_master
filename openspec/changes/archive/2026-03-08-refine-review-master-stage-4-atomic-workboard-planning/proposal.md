# Proposal: refine-review-master-stage-4-atomic-workboard-planning

## Summary

将 `review-master` 的 Stage 4 从高层 planning 描述细化为操作手册级指令，并同步更新与 Stage 4 直接相关的 supporting docs。

## Why

当前 Stage 4 已经有数据表职责说明，但还缺少足够明确的执行规则：

- Agent 不容易稳定判断 priority、dependency、evidence gap 和 next action
- `target_location` 不够精确时，何时仍可推进、何时必须阻断，还缺统一口径
- Stage 4 的用户确认在文档里还不是默认主路径
- `SKILL.md`、Stage 4 文档、SQL recipe、状态机说明和 playbook 之间对 Stage 4 的要求仍偏概括

## What Changes

- 新增 Stage 4 的 OpenSpec change 工件
- 将 Stage 4 细化为 canonical atomic item planning、provisional location、默认确认门禁和推进门槛的完整手册
- 同步更新 `SKILL.md`、Stage 4 文档、SQL recipe、状态机说明、helper-scripts 文档和一份 playbook

## Impact

这次改动只影响文档和 OpenSpec 工件，不改数据库 schema、不改脚本逻辑、不改总体六阶段流程。
