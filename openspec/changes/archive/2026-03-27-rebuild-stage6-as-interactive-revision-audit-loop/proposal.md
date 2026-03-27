# Proposal: rebuild-stage6-as-interactive-revision-audit-loop

## Why

当前 `review-master` 的 Stage 6 仍然基于显式锚点 patch、位置级三版本文案和 marked/clean 双阶段导出。这套设计在真实使用中暴露出两个根本问题：

1. 显式锚点无法稳定定位到真实稿件中的目标位置，自动生成的 patch 与导出稿件不可直接信任。
2. Stage 6 过于刚性，把“改稿”误建模成位置级机械替换，而现实中的论文修回仍然需要用户与 Agent 围绕确认后的策略进行细粒度、交互式共写。

因此本 change 要正式替换当前 patch-driven Stage 6 范式。

## What Changes

- 把 Stage 6 改成“working manuscript 直接改稿 + revision audit 审计 + response coverage 闭环”。
- Stage 1 初始化时建立 `source_snapshot` 与 `working_manuscript` 两份 workspace 内稿件副本。
- 保留 `style_profile`，但前移到 Stage 2；Stage 6 只消费它。
- 把 `supplement-intake-plan.md` 前移到 Stage 5，并要求在 Stage 5 闭环时完成。
- Stage 5 完成时新增 `manuscript-revision-guide` 与 `manuscript-execution-graph` 两份交付物，作为 Stage 6 backlog。
- 新增 `capture_revision_action.py` 与 `commit_revision_round.py` 两个正式脚本；前者只负责审计落库，后者作为 Stage 6 唯一合法提交入口，固定执行 `capture -> gate-and-render`。
- `gate-and-render` 保持只读，但必须硬检测未审计工作稿改动。
- Stage 6 的硬门禁改为：修改计划已结案、response 覆盖全部原始 thread、且工作稿不存在未审计 diff。
- `latexdiff` 改为可选辅助产物，不再是 Stage 6 闭环硬门禁。

## Impact

- 影响 Stage 1、Stage 2、Stage 5、Stage 6 的文档合同、运行时 schema、渲染模板、state machine、localization、helper scripts 与测试。
- 旧 Stage 6 的 `action_copy_variants`、`selected_action_copy_variants`、`export_patch_sets`、`export_patches` 将退出主流程。
- 这是破坏式重构，不提供旧 Stage 6 workspace 自动迁移。
