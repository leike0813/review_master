## Context

现有 Stage 5 已能记录策略卡、证据缺口与 blocker，但“补材文件 -> 接收结论 -> 预期落地位置”的链路没有独立数据模型。结果是：

- 同一轮补材里哪些文件被接收、哪些被拒收不够清晰；
- 被接收补材如何对应 `comment_id/action_order/location_order` 不可结构化校验；
- `blocked -> ready_to_resume` 触发条件偏主观，难以在 gate 中做确定性门禁。

## Goals / Non-Goals

**Goals:**
- 为每个补材文件建立文件级 intake 记录（accepted/rejected + rationale）。
- 为被接收补材建立落地映射，指向 canonical atomic action 及目标位置。
- 将 intake/landing 信息渲染为单一 workspace 只读视图，便于用户确认。
- 在 Stage 5 gate 中加入确定性校验，阻止“未完成补材闭环”就继续推进。

**Non-Goals:**
- 不改变 Stage 6 导出补丁机制与 marked/clean manuscript 输出契约。
- 不引入自动语义评估模型；接收判定仍由 Agent 语义判断后写入数据库。
- 不把补材原文拷贝进数据库，仅记录路径与判定信息。

## Decisions

### Decision 1: 新增专用表，而不是复用 strategy_card_evidence_items

- 方案：新增两张表
  - `supplement_intake_items`：记录每轮每个补材文件的接收判定与理由。
  - `supplement_landing_links`：记录被接收补材落地到哪个 `comment_id/action_order/location_order`。
- 理由：`strategy_card_evidence_items` 的粒度是 comment 视角，不是文件视角；无法完整表达“同轮多文件有接收/拒收分流”的事实。
- 备选：
  - 复用 `strategy_card_evidence_items` 增加约定字段：会造成语义混杂，且无法强约束每个文件都有判定。

### Decision 2: Stage 5 gate 引入补材闭环硬门禁

- 方案：
  - 若当前轮次存在补材 intake 记录，但任一记录缺失判定信息，则 `stage_gate=blocked`。
  - 若任一 `accepted` 补材不存在 landing link，则 `stage_gate=blocked`。
  - 只有 intake 记录完整且 accepted 文件均完成落地映射后，才允许进入 `ready_to_resume`。
- 理由：把“补材已读”与“补材可执行落地”区分开，避免过早解除 blocker。
- 备选：
  - 仅提醒不阻断：无法满足强制全量记录的要求。

### Decision 3: 新增单一只读视图承载用户可确认信息

- 方案：新增 `workspace/supplement-intake-plan.md`，按 round 展示：
  - file path
  - decision
  - rationale
  - mapped comment/action/location（若 accepted）
- 理由：避免信息分散在策略卡与 workboard，多轮补材时更可读。
- 备选：
  - 把内容嵌入 strategy card：会导致跨 comment 的同轮补材难以整体审阅。

## Risks / Trade-offs

- [Risk] 新增表与 gate 规则会提高 Stage 5 写库复杂度  
  → Mitigation: 在 SQL recipe 中提供固定写入顺序和最小字段模板。

- [Risk] 历史案例没有补材 intake 数据，可能触发新门禁失败  
  → Mitigation: 仅在“当前轮次有补材流程”时启用新门禁；并补一份迁移指导用于样例回放重建。

- [Risk] 一个补材文件可能服务多个 action/location，映射维护负担增加  
  → Mitigation: 允许一对多 landing link，并在视图中聚合显示。

## Migration Plan

1. 更新 schema 与 bootstrap，加入两张新表。  
2. 更新 workspace 渲染上下文和模板，新增 `supplement-intake-plan.md`。  
3. 更新 gate 校验逻辑与推荐 action 规则。  
4. 更新 Stage 5 参考文档、SQL recipes、`SKILL.md`、runtime digest。  
5. 回放并补齐至少一个复杂 playbook 示例中的补材 intake/landing 数据，验证 `blocked -> ready_to_resume`。  

## Open Questions

- intake 记录中的 `round_id` 是否采用固定命名（如 `round-1`）还是自由文本；默认先采用自由文本并在 playbook 中固定示例命名。
