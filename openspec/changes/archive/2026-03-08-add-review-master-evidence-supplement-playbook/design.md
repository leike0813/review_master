## Context

当前仓库已经有：

- 一份最小 happy-path playbook
- 一套最小样例输入、最终态 workspace 和 validator 输出
- 完整的六阶段流程、状态机和统一验证器

但最小样例无法覆盖两个重要现实点：

- 多 reviewer、多 comment 下的工作板排序和阶段五推进
- 阶段五因证据缺口被阻塞，用户补材后再解除阻塞的闭环

因此这次 change 的目标不是扩功能，而是提供第二套、复杂度更高的演练资料。

## Goals / Non-Goals

**Goals:**

- 提供一份更长、更真实的仓库级 playbook
- 展示 2 位 reviewers、5 条原子意见的六阶段推进
- 展示一次显式的 `stage_5 blocked -> 用户补材 -> 解除 blocked` 闭环
- 提供多文件 LaTeX 工程、补材包、最终态 workspace、最终输出和 8 份代表性 validator JSON
- 为 `playbooks/` 提供索引文档

**Non-Goals:**

- 不替换最小 happy-path playbook
- 不修改 `review-master/SKILL.md`
- 不修改 validator 逻辑或状态机规则
- 不覆盖第二次 blocked、失败回修或冲突意见分支

## Decisions

### 1. 复杂样例与最小样例并存

- Decision: 保留现有 `review-master-happy-path.md`，新增第二份复杂样例 playbook
- Rationale: 最小样例适合快速理解主流程，复杂样例适合演练更真实的阶段五闭环

### 2. 新样例采用多文件 LaTeX 工程

- Decision: `inputs/manuscript/` 和 `outputs/revised-manuscript/` 都使用 `main.tex + sections/*.tex`
- Rationale: 更真实地覆盖入口解析、跨文件定位和补充图表落地

### 3. 复杂度固定为 2 reviewers / 5 comments

- Decision: 固定 5 条原子意见，不再让实现者设计 comment 数量
- Rationale: 足以覆盖多 reviewer、优先级排序、依赖、补证据和最终汇编，同时仍然可控

### 4. 只有 `reviewer_2_001` 触发 evidence gap

- Decision: 把多随机种子稳定性实验固定为唯一显式证据缺口
- Rationale: 这样可以清晰演示一次 blocked/unblocked 闭环，而不会让文档被多个阻塞分支拖长

### 5. 补材包固定为 Markdown + CSV + SVG

- Decision: 用户补材固定包含：
  - `supplement-note.md`
  - `stability-results.csv`
  - `seed-stability-figure.svg`
- Rationale: 足够体现“说明 + 原始结果 + 图表资产”的组合，也便于文本化管理

### 6. Validator 样例保存 8 份代表性 JSON

- Decision: 复杂样例比最小样例多保存 2 份 JSON，专门覆盖：
  - `stage-4-board-confirmation-needed`
  - `stage-5-evidence-gap-blocked`
  - `stage-5-after-supplement-ready`
- Rationale: 这 3 份是复杂样例的核心差异点

## Playbook Model

主文档固定为：

- `playbooks/review-master-evidence-supplement-playbook.md`

文档按六阶段组织，但阶段五拆成两个子段：

- Stage 5A：`reviewer_2_001` 进入 blocked，等待补材
- Stage 5B：用户提供补材后，agent 更新策略卡和 manuscript 计划，再恢复到 ready

每个阶段必须显式记录：

- 用户输入或确认
- agent 读取和调用的内容
- 工件变化
- validator 输出与推荐动作
- agent 回复
- 用户回复

## Example Asset Model

`playbooks/examples/evidence-supplement-multi-review/` 固定包含：

- `inputs/`
  - 多文件 LaTeX 工程
  - 审稿意见文件
- `user-supplements/`
  - `supplement-note.md`
  - `stability-results.csv`
  - `seed-stability-figure.svg`
- `workspace/`
  - `workflow-state.yaml`
  - 6 类 Markdown runtime 工件
  - 5 张策略卡
- `outputs/`
  - 多文件修订稿
  - `response-letter.md`
- `validator-output/`
  - 8 份代表性 JSON

## Migration Plan

1. 创建新 change 的 proposal、design、specs 和 tasks。
2. 新增 `playbooks/README.md`。
3. 新增复杂样例 playbook 主文档。
4. 新增复杂样例输入、补材、workspace、输出和 validator JSON。
5. 运行 OpenSpec 校验与 validator 样例验收。
