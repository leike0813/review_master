## Context

`review-master` 当前已经完成三层建设：

- 发布骨架已建立
- 首期六阶段流程已写入 `SKILL.md`
- 六类 Markdown 中间工件模板已落到 `review-master/references/`

但模板现在还停留在“字段名 + 空表格”层。最大缺口不在流程，也不在模板存在性，而在模板填写规则：哪些字段必须填、哪些字段可以留空、`target_location` 到底怎么写、什么才算工件已完成。这些规则如果不先固定，后续同一类工件会被用出多种变体。

## Goals / Non-Goals

**Goals:**
- 为六类工件建立统一填写规则
- 为每类工件定义最小必填集，而不是要求全部字段填满
- 固定 `target_location` 的统一半结构化格式
- 引入一份总规范文档作为模板填写规则的单一真源

**Non-Goals:**
- 不引入脚本或自动填写器
- 不引入 YAML/JSON schema
- 不修改六阶段流程本身
- 不改变最终稿件与 Response letter 的导出契约

## Decisions

### 1. 采用“单独总规范 + 模板简述”

- Decision: 在 `review-master/references/` 下新增 `artifact-authoring-rules.md` 作为单一真源；各模板只保留简要提醒与字段说明
- Rationale: 如果完整规则散落在六个模板里，后续调整会反复同步，容易产生不一致
- Alternatives considered:
  - 把完整规则写进每个模板
  - 只写进 `SKILL.md`
- Why not: 前者重复度高；后者会让主文档继续膨胀且不利于按需读取

### 2. 首期采用“最小必填集”而不是“强完整填写”

- Decision: 每类工件只固定最小必填字段，允许非关键栏位留空
- Rationale: 首期流程强调逐步推进和边做边补，不适合在早期阶段强迫填写全部字段
- Alternatives considered:
  - 模板中的所有字段都必须填写
  - 各阶段自由决定是否填写
- Why not: 前者会降低实际可用性；后者会让工件完成标准再次漂移

### 3. `target_location` 现在就固定语法

- Decision: 统一 `target_location` 为 `path::section::anchor`
- Rationale: 这是当前最小可读、可复用、可渐进脚本化的折中格式
- Alternatives considered:
  - 只给原则，不定格式
  - 一开始就上严格机器可解析协议
- Why not: 不定格式会导致不同模板和不同执行者各写各的；过于严格的协议超出首期需要

### 4. 总规范只给格式说明，不给伪造业务样例

- Decision: 总规范解释语法、最小必填集、状态语义，但不附完整伪造样例
- Rationale: 这些工件强依赖真实审稿上下文，伪造样例容易被误当作推荐写法
- Alternatives considered:
  - 在总规范中附示例
  - 额外新增 example 文件
- Why not: 会增加维护成本，也不利于保持“规范”和“样例”的边界

## Risks / Trade-offs

- [Risk] 没有完整样例可能让首次填写者需要更多理解成本
- Mitigation: 在总规范中用字段解释和最小必填集降低歧义，并在模板顶部加明确引用

- [Risk] `path::section::anchor` 仍然不是严格机器协议
- Mitigation: 这是有意选择的半结构化格式；后续若需要脚本消费，可在兼容前提下进一步收紧

- [Risk] 最小必填集可能导致部分工件信息稀疏
- Mitigation: 先保障工件有效和可推进，再由后续阶段逐步补全非关键字段

## Migration Plan

1. 新建 `define-review-master-artifact-authoring-rules` change，并补齐 proposal、design、specs、tasks。
2. 新增 `review-master/references/artifact-authoring-rules.md`。
3. 更新六个模板文件顶部说明、最小字段定义与 `target_location` 描述。
4. 更新 `review-master/SKILL.md`，要求阶段内生成工件时遵循总规范和统一定位格式。
5. 使用 `openspec validate define-review-master-artifact-authoring-rules --type change --strict` 进行校验。

## Open Questions

- 后续若开始脚本化，应优先消费哪一类工件：原子清单、工作板还是策略卡。
- `anchor` 是否在未来需要再细分为 `paragraph/table/figure/equation/list-item` 等固定子类。
