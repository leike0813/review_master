# Proposal: refine-review-master-stage-1-and-2-instructions

## Summary

将 `review-master` 的 Stage 1 和 Stage 2 从高层描述细化为操作手册级指令，并同步更新与这两个阶段直接相关的配套说明。

## Why

当前 Stage 1 和 Stage 2 已经有总纲说明，但还缺少足够明确的执行细节：

- Agent 不容易判断何时进入、何时阻断、何时完成
- Stage 1 的环境确认、恢复入口、入口识别和初始化顺序仍偏概括
- Stage 2 的结构分析深度、必读材料和推进门槛还不够具体
- `SKILL.md`、阶段文档、SQL recipe、状态机说明之间还缺少统一的操作手册级对齐

## What Changes

- 新增 Stage 1 / Stage 2 的 OpenSpec change 工件
- 将 Stage 1 细化为环境确认、恢复入口、输入核对、入口识别、workspace 初始化、bootstrap 对齐和首次 gate-and-render 的完整子流程
- 将 Stage 2 细化为结构分析、claim/section 抽取、高风险修改区识别、入库、resume 更新和阶段推进门槛的完整子流程
- 同步更新 `SKILL.md`、阶段文档、SQL recipe、状态机说明、helper-scripts 文档和一份 playbook

## Impact

这次改动只影响文档和 OpenSpec 工件，不改数据库 schema、不改脚本逻辑、不改六阶段总流程。
