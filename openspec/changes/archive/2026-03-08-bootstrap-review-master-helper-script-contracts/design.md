## Context

当前 `review-master` 已经完成以下建设：

- `SKILL.md` 已固定输入/输出契约和六阶段流程
- 六类 Markdown 中间工件模板已建立
- 中间工件填写总规范已建立
- 辅助脚本 change 已建立入口辅助与一致性检查的初步契约

但现有辅助脚本契约有两个问题：

- 它把“原子化骨架生成”也纳入了脚本范围，这与 LLM 主导语义判断的定位冲突
- 现有验证脚本只做浅层检查，无法承担统一工件验证流程

因此这次不是新增能力，而是修订边界：让 `SKILL.md` 承担原子化规则，让一个统一验证程序承担工件包验证。

## Goals / Non-Goals

**Goals:**

- 把原子化职责从脚本契约迁回 `SKILL.md`
- 为统一验证程序建立完整的工件包输入模型
- 让验证器同时处理存在性、单工件格式、依赖关系和整体一致性
- 让 `SKILL.md` 明确验证器可用但非必需，并给出人工回退路径

**Non-Goals:**

- 不引入稿件写回脚本
- 不引入最终导出脚本
- 不让脚本替代原子化、策略制定或学术判断
- 不引入 YAML/JSON schema 或 runner 配置

## Decisions

### 1. 原子化规则由 `SKILL.md` 主导

- Decision: 审稿意见原子化不再由脚本承担，改为在 `SKILL.md` 中明确原子意见定义、拆分原则、不可过拆规则和自检要求
- Rationale: “一个评论应拆成几条”是语义决策，不是可稳定下放给确定性脚本的工作
- Alternatives considered:
  - 保留 `atomize_review_comments.py` 作为正式能力
  - 让脚本先候选切分，再由 LLM 复核
- Why not: 两种做法都会把本应属于主指令的核心判断继续外包给脚本，边界仍然不稳

### 2. 统一验证程序按“工件包”工作，而不是按单文件零散调用

- Decision: `validate_artifact_consistency.py` 接受 `--artifact-root PATH`，从一个约定目录中发现所有工件
- Rationale: 用户要的是统一验证流程，而不是一个个零散文件检查器；工件包输入模型更接近 OpenSpec 的工作方式
- Alternatives considered:
  - 保持当前逐个文件参数模式
  - 再拆多个单独验证脚本
- Why not: 逐文件模式调用成本高且难以表达依赖关系；多脚本方案会让验证边界分散

### 3. 验证程序统一输出完整问题清单

- Decision: 验证器遇到规范问题时仍返回退出码 `0`，并在 JSON 中完整列出问题；只有程序运行失败时才非零退出
- Rationale: 工件验证的目标是提供全面反馈，而不是第一个问题就中止
- Alternatives considered:
  - fail-fast
  - 只给总状态不给细节
- Why not: 前者不利于修订多个问题；后者不利于 Agent 和用户定位问题

### 4. 工件验证分四层，而不是只做一致性比对

- Decision: 验证器固定处理四类问题：存在性、单工件格式、依赖关系、全局一致性
- Rationale: 用户明确要求统一程序覆盖单件与整体，不再满足于浅层 consistency check
- Alternatives considered:
  - 只做单工件格式校验
  - 只做跨工件 `comment_id` 检查
- Why not: 这两种方案都不足以支撑阶段化工件体系

### 5. 工件目录结构使用固定命名

- Decision: 验证器约定工件工作目录下使用固定文件名，并使用 `response-strategy-cards/` 子目录保存单条策略卡，文件名固定为 `{comment_id}.md`
- Rationale: 没有固定命名，验证器无法稳定发现依赖关系与覆盖率
- Alternatives considered:
  - 继续自由命名并依赖显式参数
  - 将所有策略卡合并成一个文件
- Why not: 前者不利于统一验证；后者违背“单卡单 comment”约束

### 6. 入口辅助脚本继续保留

- Decision: `detect_main_tex.py` 继续保留为阶段一辅助工具
- Rationale: 主入口识别仍然属于低歧义、确定性较高的工作
- Alternatives considered:
  - 把所有脚本都收掉
- Why not: 会放弃一个已经合理收敛的脚本边界

## Risks / Trade-offs

- [Risk] 统一验证程序在阶段早期会把后续工件报告为缺失或不完整
- Mitigation: 在 `SKILL.md` 和 `helper-scripts.md` 中明确这是设计行为，Agent 需要结合当前阶段解释哪些问题应立即修复

- [Risk] 现有模板示例行可能在未经填充时触发大量格式问题
- Mitigation: 验证器明确面向运行时工件包，不面向模板原件；验证结果中会区分存在性、格式和依赖问题

- [Risk] 主入口识别无法在多候选工程目录中自动替用户做决定
- Mitigation: 这是有意为之；脚本只返回候选，不替用户拍板

## Migration Plan

1. 修订 `bootstrap-review-master-helper-script-contracts` 的 proposal、design、specs、tasks。
2. 更新 `review-master/SKILL.md`，把原子化方法写回主指令，并删除阶段三的脚本原子化依赖。
3. 更新 `review-master/references/helper-scripts.md`，改为“入口辅助 + 统一验证程序”。
4. 删除 `review-master/scripts/atomize_review_comments.py`。
5. 扩展 `review-master/scripts/validate_artifact_consistency.py` 为工件包验证器。
6. 使用 `openspec validate bootstrap-review-master-helper-script-contracts --type change --strict` 校验 change。
7. 用最小样例工件包验证验证器的存在性、格式、依赖和一致性报告。

## Open Questions

- 后续是否需要把验证报告进一步映射成用户可读的修复建议模板。
- 若后续引入 sidecar JSON，是否应作为验证器的可选输出而不是主输入。
