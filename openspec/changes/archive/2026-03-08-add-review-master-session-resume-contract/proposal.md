# Proposal: add-review-master-session-resume-contract

## Summary

为 `review-master` 增加统一的“恢复优先”执行协议，使首次调用、跨 Session 恢复和上下文压缩后的继续执行都走同一入口：先运行 `gate-and-render`，先读恢复包，再决定下一步。

## Why

当前运行时已经有 `workflow_state`、`pending_user_confirmations`、`global_blockers` 和 `instruction_payload`，足以判断短期门禁，但还不足以支撑长周期执行：

- 新 Session 难以快速恢复当前目标、当前焦点和停下来的原因
- 上下文压缩后，Agent 很难仅凭当前门禁信息恢复完整的工作意图
- 首次调用和恢复调用的入口逻辑还不统一

## What Changes

- 新增 `resume_*` 数据表，作为恢复真源
- 新增只读恢复视图 `agent-resume.md`
- 新增静态摘要资产 `assets/runtime/skill-runtime-digest.md`
- `gate-and-render` 每次输出都附带 `instruction_payload.resume_packet`
- `SKILL.md` 与 playbook 明确“首次调用也先恢复”

## Impact

这次改动会影响：

- SQLite schema
- 只读渲染视图集合
- `gate_and_render_workspace.py` 的输出结构
- `SKILL.md`、状态机文档、SQL recipe 文档
- sample workspace 与 playbook 演示内容
