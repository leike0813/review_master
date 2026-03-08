## Why

`review-master` 现在已经有流程、模板、填写规则和首批脚本契约，但其中有一个关键边界不够稳：审稿意见原子化被部分下放给了脚本。这和 skill 的核心定位不一致，因为“原子化”本质上是语义判断，而不是纯格式拆分。

同时，当前验证脚本还停留在浅层一致性检查，尚未形成一个统一的工件验证流程，无法像 OpenSpec 一样同时处理格式、依赖关系和整体一致性。

## What Changes

- 修订现有 `bootstrap-review-master-helper-script-contracts`
- 把“原子化”职责收回到 `review-master/SKILL.md`
- 删除 `atomize_review_comments.py` 的正式发布契约
- 把 `validate_artifact_consistency.py` 升级为统一工件验证程序
- 更新 `review-master/references/helper-scripts.md`，把脚本能力收口为“入口辅助 + 工件验证”
- 更新 `review-master/SKILL.md`，明确原子化方法、验证时机和验证器输入模型

## Capabilities

### New Capabilities

- `review-master-readonly-helper-scripts`: 规定首批辅助脚本只允许做入口辅助和统一工件验证
- `review-master-helper-script-cli-contracts`: 规定入口辅助脚本和统一验证程序的 CLI、输入模型和输出字段
- `review-master-skill-script-usage-boundaries`: 规定 `SKILL.md` 如何承担原子化规则，并如何声明验证器的使用时机和边界

### Modified Capabilities

<!-- None -->

## Impact

- 直接影响 `review-master/SKILL.md`
- 新增 `review-master/references/helper-scripts.md`
- 新增 `review-master/scripts/detect_main_tex.py`
- 修订 `review-master/scripts/validate_artifact_consistency.py`
- 移除 `review-master/scripts/atomize_review_comments.py`
- 不引入写回脚本、runner 配置、runtime schema 或最终导出自动化
