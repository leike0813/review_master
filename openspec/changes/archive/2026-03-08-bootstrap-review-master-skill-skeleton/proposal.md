## Why

当前仓库只有项目级宏观约束，尚未建立可发布的 `review-master` skill 包骨架。若不先固定发布目录、最小 `SKILL.md` 入口和后续扩展位，后续能力实现很容易继续散落在仓库根目录，导致发布边界和实现边界混淆。

## What Changes

- 新增一个聚焦“建立项目骨架”的 OpenSpec change：`bootstrap-review-master-skill-skeleton`
- 为 `review-master` skill 包定义最小发布目录布局：包根 `SKILL.md`，以及预留 `references/`、`scripts/`、`assets/`
- 为 `SKILL.md` 定义骨架级契约：frontmatter、阶段化流程、非目标与强约束
- 明确开发期资产如仓库根 `openspec/`、仓库根 `references/` 不属于发布包

## Capabilities

### New Capabilities

- `review-master-skill-package-layout`: 规定 `review-master/` 发布目录的最小结构与边界
- `review-master-skill-bootstrap-contract`: 规定骨架级 `SKILL.md` 必须具备的元数据与章节

### Modified Capabilities

<!-- None -->

## Impact

- 影响发布包结构：新增 `review-master/` 作为后续唯一发布目录
- 影响后续实现方式：后续 `SKILL.md` 细化、参考文档迁移、脚本补充都必须落在该骨架内继续演进
- 本次不引入运行时 schema、runner 配置、业务脚本或 UI 元数据
