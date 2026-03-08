# Proposal: stabilize-review-master-runtime-digest-and-stage-6-export-path

## Why

当前 runtime digest 已与 `review-master/SKILL.md` 发生漂移，Stage 6 的 marked manuscript 仍是局部摘录而非完整稿件，同时缺少一个正式的导出辅助脚本来把数据库中的明确 patch 真源应用到导出副本。这三个问题会同时削弱：

- Agent 的恢复与执行一致性
- Stage 6 导出的可信度
- sample playbook 对最终导出路径的示范价值

此外，`response_latex` 目前仍可能只渲染表格正文片段，而不是带 front matter 的可编译完整 LaTeX 文件。

## What Changes

- 同步 `review-master/SKILL.md` 与 `review-master/assets/runtime/skill-runtime-digest.md`
- 在仓库级 `AGENTS.md` 中明确维护纪律：修改 `SKILL.md` 时必须同步更新 runtime digest
- 为 Stage 6 增加 export patch 真源：
  - `export_patch_sets`
  - `export_patches`
- 新增正式导出脚本：
  - `review-master/scripts/export_manuscript_variants.py`
- 将 Stage 6D / 6E 重定义为：
  - 先导出完整 marked manuscript
  - 用户确认后再导出 clean manuscript
- 将 `response_latex` 固定为带 front matter 的完整可编译文件
- 新增只读视图：
  - `export-patch-plan.md`
- 更新 playbook、sample workspace、sample outputs 和 `gate-and-render-output` fixtures，使其与新的 Stage 6 导出路径一致

## Impact

- 数据库 schema 会新增导出补丁真源表，但不改变既有 comment/workflow 主模型
- Stage 6 的运行契约会从“只看 export_artifacts 状态”升级为“export patches + export artifacts + 完整导出文件”
- sample outputs 将从局部片段升级为完整稿件与完整 LaTeX response 文件
