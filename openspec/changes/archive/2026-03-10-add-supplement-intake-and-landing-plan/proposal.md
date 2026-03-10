## Why

当前 Stage 5 已有 evidence gap 与 blocker 机制，但缺少“补材接收与落地方案”的结构化真源。补材被读取后是否被接收、为何接收/拒收、以及将落到哪些 comment/action/location，仍然容易停留在口头或分散记录里，导致可追溯性不足。

## What Changes

- 新增 Stage 5 的“补材接收与落地方案”能力，要求每轮补材按文件级记录接收判定。
- 新增 runtime 数据表，用于存储补材文件清单、接收/拒收结论、拒收理由、以及被接收补材的落地映射。
- 新增 workspace 只读视图，集中展示每轮补材的接收状态与目标落地位置。
- 更新 Stage 5 门禁：当补材轮次未完成接收判定或接收补材无落地映射时，不得解除 blocker。

## Capabilities

### New Capabilities
- `review-master-supplement-intake-and-landing`: 定义补材文件级接收判定与落地映射的 Stage 5 运行时契约。

### Modified Capabilities
- `review-master-stage-5-confirmation-blocker-completion-instructions`: Stage 5 completion gate 增加补材接收闭环要求。
- `review-master-sqlite-runtime`: runtime schema 增加补材接收与落地映射专用表。
- `review-master-markdown-artifact-contract`: 增加补材接收与落地方案的只读 Markdown 视图契约。

## Impact

- 新增 `openspec/changes/add-supplement-intake-and-landing-plan/` 变更 artifacts。
- 后续实现将影响：
  - `review-master/assets/schema/review-master-schema.yaml`
  - `review-master/scripts/gate_and_render_workspace.py`
  - `review-master/scripts/workspace_db.py`
  - `review-master/assets/templates/`（新增补材接收与落地方案视图模板并更新 render manifest）
  - `review-master/SKILL.md` 与 `review-master/assets/runtime/skill-runtime-digest.md`
- 不改变 `export_manuscript_variants.py` 的导出契约。
