## Why

`review-master` 目前只有骨架级 `SKILL.md`，明确了“应当阶段化”，但还没有把首期工作流真正定义清楚：输入是什么、输出是什么、从输入到输出要经过哪些阶段、在哪些节点必须与用户交互。若这些核心流程继续悬空，后续实现很容易退化成“一次性分析 + 一次性改稿”，违背项目的交互式、方案先行原则。

## What Changes

- 为 `review-master` 定义首期输入/输出契约，固定必需输入为 LaTeX 原稿与 Markdown/txt 审稿意见文件。
- 为 `review-master` 定义首期六阶段工作流，覆盖入口解析、原稿理解、意见拆解、映射与排序、逐条闭环处理、最终组装导出。
- 为 `review-master` 定义强制交互检查点，明确哪些阶段必须等待用户确认，哪些情况下必须要求用户补充材料。
- 明确“证据不足不得生成最终回复”的流程门禁，避免用占位内容冒充完成。

## Capabilities

### New Capabilities

- `review-master-io-contract`: 规定首期输入槽、输出槽，以及单文件/工程目录两种 LaTeX 输入形态对应的产物形态。
- `review-master-staged-workflow`: 规定首期端到端六阶段流程、中间工件与阶段推进门槛。
- `review-master-user-checkpoints`: 规定哪些交互节点是强制门禁，以及用户在各节点需要提交或确认什么。

### Modified Capabilities

<!-- None -->

## Impact

- 影响 skill 主契约：后续 `review-master/SKILL.md` 需要从泛化骨架升级为首期可执行流程。
- 影响后续脚本与中间工件设计：输入解析、工作副本管理、意见拆解和逐条状态跟踪都要围绕这次定义的阶段流程展开。
- 影响用户交互方式：首期采用强交互、逐条确认，不是后台非交互式执行。
