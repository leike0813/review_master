## Why

`review-master/SKILL.md` 已经定义了六类中间工件，但它们目前仍然只是概念名称，没有固定模板、统一字段和明确的跨工件追踪约束。若不把这些工件具体化，后续人工填写、Agent 生成和脚本化演进都会缺少稳定锚点。

## What Changes

- 新增 change `add-review-master-markdown-artifact-templates`
- 在 `review-master/references/` 下增加六个 Markdown 模板文件，覆盖六类中间工件
- 固定六类模板采用表格/清单驱动风格，并采用“空模板 + 字段说明”形式
- 为跨工件追踪引入统一字段集：`comment_id`、`reviewer_id`、`status`、`priority`、`evidence_gap`、`target_location`
- 更新 `review-master/SKILL.md`，让六阶段流程明确指向这些模板文件及其使用时机

## Capabilities

### New Capabilities

- `review-master-markdown-artifact-templates`: 规定六类中间工件必须具备独立 Markdown 模板文件
- `review-master-cross-artifact-tracking`: 规定跨工件统一追踪字段与 `comment_id` 主关联键
- `review-master-skill-template-usage`: 规定 `review-master/SKILL.md` 必须说明各模板的生成时机和确认作用

### Modified Capabilities

<!-- None -->

## Impact

- 直接影响 `review-master/SKILL.md`
- 直接影响 `review-master/references/`
- 不引入脚本、schema、runner 配置或最终导出格式变更
