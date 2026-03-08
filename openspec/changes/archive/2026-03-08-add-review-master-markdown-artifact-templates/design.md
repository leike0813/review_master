## Context

当前 `review-master` 已经具备首期运行时主契约：输入槽、六阶段流程、逐条确认与最终导出门禁都已写入 `SKILL.md`。但六类中间工件仍然停留在抽象层，用户和 Agent 只能知道“应该有这些工件”，却不知道每个工件具体应该长什么样、共享哪些字段、如何跨阶段关联。

下一步最合适的推进方式不是继续扩展流程，也不是马上引入脚本，而是先把这些工件做成稳定的 Markdown 模板。这样既能服务当前纯文本交互式工作流，也能为后续脚本或 schema 演进提供稳定接口。

## Goals / Non-Goals

**Goals:**
- 在 `review-master/references/` 中提供六类中间工件的 Markdown 模板
- 让六类工件共享最小统一字段集，尤其是 `comment_id`
- 更新 `review-master/SKILL.md`，让六阶段流程明确引用这些模板
- 保持模板人可读、可复制、可直接填写

**Non-Goals:**
- 不引入 YAML/JSON 结构化版本
- 不为这些模板新增示例文件
- 不新增脚本去解析或生成这些模板
- 不改动最终稿件和 Response letter 的导出契约

## Decisions

### 1. 模板文件落在 `review-master/references/`

- Decision: 六类工件都以独立 Markdown 模板文件形式放在 `review-master/references/`
- Rationale: 模板属于按需加载的运行时参考资料，而不是 `SKILL.md` 本体，也不是最终输出资产
- Alternatives considered:
  - 只把模板结构写进 `SKILL.md`
  - 把模板放到 `assets/`
- Why not: 前者会让 `SKILL.md` 变臃肿；后者更适合最终复制使用的资产，不适合按需阅读参考

### 2. 模板采用表格/清单驱动，而不是叙述型

- Decision: 每个模板都以字段清单、状态栏、表格骨架为主
- Rationale: 这类工件的核心职责是核对、关联、追踪，而不是自由抒情分析
- Alternatives considered:
  - 叙述型模板
  - 混合大量叙述与少量表格
- Why not: 二者都会削弱跨工件的一致性和可复用性

### 3. 统一追踪字段直接写进模板

- Decision: 在多工件模板中固定共享字段：`comment_id`、`reviewer_id`、`status`、`priority`、`evidence_gap`、`target_location`
- Rationale: 若不在模板阶段就锁定字段名，后续人工和 Agent 会生成不同命名，导致跨工件难以对齐
- Alternatives considered:
  - 每个模板自由定义字段
  - 只统一 `comment_id`
- Why not: 前者会造成漂移；后者不足以支撑工作板与策略卡之间的稳定关联

### 4. 模板首期保持“空模板 + 字段说明”

- Decision: 模板只给骨架和字段说明，不附示例数据
- Rationale: 审稿场景高度依赖具体上下文，伪造示例容易被误当成推荐写法或硬编码样本
- Alternatives considered:
  - 每个模板附带一小段示例
  - 模板和示例双份文件同时提供
- Why not: 都会增加维护成本，也会制造“示例即规范”的误解

## Risks / Trade-offs

- [Risk] 没有示例时，首次使用者理解模板速度稍慢
- Mitigation: 在模板顶部写清用途、字段说明和填写规则，并在 `SKILL.md` 中写明使用时机

- [Risk] Markdown 表格在复杂场景下不如结构化文件易于程序消费
- Mitigation: 当前 change 的目标是人可读和流程可执行；结构化 schema 留待后续 change

- [Risk] 统一字段集可能无法覆盖未来所有扩展需求
- Mitigation: 当前只固定最小共享字段集，后续若有必要可在保持兼容的前提下增加字段

## Migration Plan

1. 新建 `add-review-master-markdown-artifact-templates` change，并补齐 proposal、design、specs、tasks。
2. 在 `review-master/references/` 中新增六个模板文件。
3. 更新 `review-master/SKILL.md`，让每个阶段引用相应模板并说明确认节点。
4. 删除 `review-master/references/.gitkeep`，避免模板目录与占位文件并存。
5. 运行 `openspec validate add-review-master-markdown-artifact-templates --type change --strict` 验证。

## Open Questions

- 后续若引入脚本，优先消费哪些模板：原子清单、工作板还是策略卡。
- 后续是否要把 `target_location` 进一步标准化为更细粒度的 LaTeX 定位语法。
