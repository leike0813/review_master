## Why

`review-master` 当前把所有中间视图、gate 指令和最终导出默认写成同一种语言，无法区分“原稿/审稿意见使用的文本语言”和“用户与 Agent 协作用的工作语言”。这会直接破坏多语言修回场景：原文摘录可能被误翻译，中间工件可能不符合用户交流语言，而最终论文与 response letter 也缺少稳定的文档语言约束。

## What Changes

- 新增运行时语言真源：
  - `runtime_language_context`
  - 明确记录 `document_language`、`working_language`、检测结果、来源和确认状态
- 重构 Stage 1：
  - 首次进入且 workspace 尚未初始化时，先识别并确认文本语言/工作语言
  - 确认后再初始化 workspace 与本地化覆盖层
- 为 runtime 增加 workspace-local localization overlay：
  - `runtime-localization/source-messages.yaml`
  - `runtime-localization/working-messages.json`
  - `runtime-localization/document-messages.json`
  - `runtime-localization/templates/`
- 把所有用户可读的中间视图、resume 文案和推荐动作文本切换到工作语言
- 固定语言边界：
  - 原文摘录保持文本语言
  - Stage 5 drafts 使用工作语言
  - Stage 6 最终 manuscript copy、response rows 与导出产物使用文本语言
- 同步更新模板、导出链、文档、playbook fixtures、gate 快照和测试

## Capabilities

### New Capabilities

- `review-master-runtime-language-context`: 运行时维护文本语言/工作语言真源，并提供 workspace-local localization overlay。

### Modified Capabilities

- `review-master-sqlite-runtime`: runtime schema 需要纳入语言上下文表。
- `review-master-stage-1-entry-bootstrap-instructions`: Stage 1 需要先确认两种语言，再初始化 workspace。
- `review-master-stage-3-canonical-atomization-instructions`: Stage 3 需要明确原文保留文本语言、atomic 摘要转为工作语言。
- `review-master-stage-5-strategy-card-instructions`: Stage 5 drafts 需要固定为工作语言草案。
- `review-master-stage-6-manuscript-copy-variants`: Stage 6 manuscript variants 需要固定为文本语言最终落稿。
- `review-master-stage-6-response-row-assembly`: final response rows 需要以文本语言输出。
- `review-master-template-driven-rendering`: render 机制需要支持 workspace 本地化消息覆盖与可选模板覆盖。
- `review-master-validator-instruction-payload`: instruction payload 的自然语言字段需要依据 working language 生成。
- `review-master-skill-instructions`: SKILL 执行流需要显式描述双语言上下文与语言确认门。

## Impact

- 影响 runtime schema、workspace 初始化、gate-and-render、Markdown 渲染、Stage 6 导出脚本与模板消息目录。
- 影响 `SKILL.md`、runtime digest、Stage 1/3/5/6 指南、SQL recipes、workflow state machine 与 glossary。
- 影响所有已提交的 playbook examples，因为它们需要写入 `runtime_language_context`、补充 localization overlay，并重渲染 workspace/gate 输出。
