# Design: stabilize-review-master-runtime-digest-and-stage-6-export-path

## Overview

本次 change 的核心是把 Stage 6 的最终导出路径收紧为：

1. Agent 先在数据库中写入显式导出补丁真源
2. 导出脚本基于补丁真源复制并修改导出副本
3. 先生成完整 marked manuscript
4. 用户确认后，再基于同一批 patch 生成 clean manuscript
5. 同时生成 Markdown 与 LaTeX 两个 response letter 文件，其中 LaTeX 版本必须带 front matter

## Key Decisions

### Runtime digest maintenance rule belongs to root AGENTS

这是仓库维护纪律，不属于 skill 执行时的运行规则。因此把“修改 `SKILL.md` 时必须同步更新 runtime digest”的要求放在根 `AGENTS.md`，而不是 skill 发布包内。

### Export script is deterministic and patch-driven

`export_manuscript_variants.py` 只负责：

- 复制原稿到导出目录
- 按显式锚点执行插入/替换
- 生成完整 marked / clean manuscript

它不负责文案生成、不负责语义判断，也不推断修改策略。

### Export patch tables are the machine-applicable truth

`export_patch_sets` 和 `export_patches` 用于承载能被脚本直接执行的 patch 计划。Stage 6 的 marked / clean manuscript 都必须来自同一批 patch 真源，这样才能保证：

- marked manuscript 与 clean manuscript 一致
- clean manuscript 只是去掉 `changes` 标记，而不是重新生成一份可能偏移的文本

### response_latex must be fully compilable

Stage 6 的 `response_latex` 不再允许输出局部表格片段。它必须是一个完整的、可独立编译的 LaTeX 文档，至少包含：

- `\documentclass`
- 必需 `\usepackage`
- `\begin{document}` / `\end{document}`
- 最小标题或节标题
- point-to-point 表格正文

## Affected Files

- `AGENTS.md`
- `review-master/SKILL.md`
- `review-master/assets/runtime/skill-runtime-digest.md`
- `review-master/assets/schema/review-master-schema.yaml`
- `review-master/assets/templates/render-manifest.yaml`
- `review-master/assets/templates/response-letter-table-preview.tex.j2`
- `review-master/assets/templates/export-patch-plan.md.j2`
- `review-master/scripts/workspace_db.py`
- `review-master/scripts/gate_and_render_workspace.py`
- `review-master/scripts/init_artifact_workspace.py`
- `review-master/scripts/export_manuscript_variants.py`
- `review-master/references/stage-6-final-review-and-export.md`
- `review-master/references/helper-scripts.md`
- `review-master/references/sql-write-recipes.md`
- `review-master/references/workflow-state-machine.md`
- `review-master/references/workflow-glossary.md`
- `playbooks/review-master-happy-path.md`
- `playbooks/review-master-evidence-supplement-playbook.md`
- `playbooks/examples/**`
- `tests/**`

## Risks

- sample `.db` fixtures 需要一并迁移，否则 schema/runtime 与样例会失配
- marked manuscript 全量导出后，sample outputs 与 playbook 中的文字引用需要整体重灌
- 若 `response_latex` 的 front matter 不统一，Stage 6 契约会继续漂移
