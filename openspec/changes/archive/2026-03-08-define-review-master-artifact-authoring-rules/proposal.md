## Why

`review-master` 已经有六类 Markdown 中间工件模板，但它们目前只定义了字段和骨架，没有统一的填写规则、最小必填集和 `target_location` 语法。若不把“怎么填”固定下来，后续人工填写、Agent 生成和脚本演进都容易出现漂移。

## What Changes

- 新增 change `define-review-master-artifact-authoring-rules`
- 为六类工件定义统一填写规则、最小必填集和允许留空的字段
- 固定 `target_location` 的半结构化格式为 `path::section::anchor`
- 在 `review-master/references/` 下新增总规范文档 `artifact-authoring-rules.md`
- 更新六个模板文件，使其引用总规范并统一 `target_location` 描述
- 更新 `review-master/SKILL.md`，要求阶段内生成工件时遵循总规范

## Capabilities

### New Capabilities

- `review-master-artifact-authoring-rules`: 规定六类工件的填写规则、最小必填集和可留空边界
- `review-master-target-location-format`: 规定 `target_location` 的统一半结构化语法
- `review-master-artifact-rule-reference`: 规定总规范文档作为模板填写规则的单一真源

### Modified Capabilities

<!-- None -->

## Impact

- 直接影响 `review-master/SKILL.md`
- 直接影响 `review-master/references/*.md`
- 新增 `review-master/references/artifact-authoring-rules.md`
- 不引入脚本、schema、runner 配置或导出格式改动
