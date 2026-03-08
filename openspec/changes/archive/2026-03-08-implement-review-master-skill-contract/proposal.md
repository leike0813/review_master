## Why

`define-review-master-staged-workflow` 已经把首期输入输出、六阶段流程和强制交互门禁写进了 OpenSpec，但这些规则还没有真正落到 `review-master/SKILL.md`。如果不继续把规格下沉到主文档，skill 仍然只有泛化骨架，无法作为首期可执行的交互式主契约使用。

## What Changes

- 新增一个实现型 change：`implement-review-master-skill-contract`
- 更新 `review-master/SKILL.md`，把当前四阶段概述替换为首期六阶段执行流程
- 将 skill 主契约中的输入槽正式固定为：
  - 必需：`manuscript_source`、`review_comments_source`
  - 可选：`editor_letter_source`、`user_notes`
- 将中间工件正式固定为 Markdown 优先的文本工件，并说明其生成时机与确认作用
- 明确证据缺口、逐条确认、最终导出门禁都属于 `SKILL.md` 的强约束

## Capabilities

### New Capabilities

- `review-master-skill-runtime-contract`: 规定 `review-master/SKILL.md` 中的首期输入槽、输出槽和可选输入边界
- `review-master-skill-instructions`: 规定 `review-master/SKILL.md` 必须包含的六阶段执行流程、逐条闭环循环与导出门禁
- `review-master-markdown-artifact-contract`: 规定首期中间工件采用 Markdown 优先，并明确各工件的角色、生成时机与确认作用

### Modified Capabilities

<!-- None -->

## Impact

- 直接影响 `review-master/SKILL.md`，使其从骨架升级为首期可执行主文档
- 影响后续实现约束：未来若引入脚本、模板或 schema，必须遵守本次写入主文档的输入槽、工件和交互规则
- 不引入新的 runtime schema、runner 配置、脚本或参考模板文件
