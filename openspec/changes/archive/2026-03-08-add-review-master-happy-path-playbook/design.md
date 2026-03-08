## Context

当前仓库已经具备：

- `review-master/SKILL.md` 中的六阶段流程
- `review-master/assets/artifact-workspace/` 提供的 runtime scaffold
- `review-master/references/workflow-state-machine.md` 定义的状态机规则
- `review-master/scripts/validate_artifact_consistency.py` 输出的 `instruction_payload`

但这些能力仍然分散在多个文件中。对于一个新开发者或新 agent 而言，仅靠规范文档还不足以快速理解一次完整执行中：

- 何时创建 workspace
- 每阶段该写哪些工件
- 何时运行 validator
- validator 输出如何影响 agent 的下一步回复
- 用户在哪些节点需要确认

因此这次 change 的目标不是扩展功能，而是把现有能力组织成一条可阅读、可演练、可对照的完整 happy path。

## Goals / Non-Goals

**Goals:**

- 提供一份仓库级 happy-path playbook，完整模拟一次 skill 从调用到结束的过程
- 让 playbook 精确复用现有六阶段、workspace、状态机和 validator 规则
- 为 playbook 提供一套最小样例输入、最终态 workspace、最终输出和代表性 validator JSON
- 让开发者可以直接用 playbook 对照当前 skill 的运行机制

**Non-Goals:**

- 不改变 skill 发布目录内容
- 不新增发布时必须读取的文档
- 不修改状态机、validator 或六阶段流程的行为
- 不覆盖异常分支、失败回修分支或多 reviewer 复杂场景
- 不为每个阶段保存完整 workspace 快照

## Decisions

### 1. Playbook 放在仓库根部 `playbooks/`

- Decision: 使用 `playbooks/` 作为仓库级演练资料目录
- Rationale: 这是开发/演练材料，不属于 skill 发布包；单独目录比 `docs/` 更明确
- Alternatives considered:
  - 放入 `docs/`
  - 放入 `review-master/`
  - 放入 `openspec/`
- Why not: `docs/` 容易与普通说明文档混杂；`review-master/` 会污染发布包；`openspec/` 更适合规范工件，不适合长期演练资料

### 2. 首期只做一条 happy path

- Decision: 只覆盖最小单论文、单 reviewer、单 comment 的成功路径
- Rationale: 当前目标是把主流程串通，而不是穷举分支
- Alternatives considered:
  - 同时包含失败回修分支
  - 同时包含多 reviewer 分支
- Why not: 会显著扩大文档规模，且削弱首期 playbook 的教学作用

### 3. 样例资产采用“文档 + 最小样例文件”

- Decision: 附带最小输入、最终态 workspace、最终输出和代表性 validator JSON
- Rationale: 这样既能支撑阅读，也能支撑实际复现；比“纯文档”更可操作，比“全阶段快照”更轻
- Alternatives considered:
  - 只写文档，不放样例文件
  - 为每个阶段都保存完整快照
- Why not: 纯文档不利于复现；全阶段快照文件量过大，超出首期需要

### 4. Validator 样例按“代表性阶段输出”保存

- Decision: 在 `validator-output/` 中保存 6 个代表性 JSON 文件，对应六阶段的关键校验点
- Rationale: playbook 需要展示 validator 如何驱动流程推进；每阶段一份最清晰
- Alternatives considered:
  - 只保存最终导出前的 JSON
  - 为每一步用户回复都保存一份 JSON
- Why not: 前者无法体现状态机闭环；后者信息冗余

### 5. 样例 workspace 保存最终态

- Decision: `workspace/` 只保存最终 happy-path 态，而不是每阶段都存一份 workspace
- Rationale: 最终态最有复用价值，同时不显著增加文件数量
- Alternatives considered:
  - 保存初始态
  - 保存所有阶段态
- Why not: 初始态信息密度低；全阶段态超出首期范围

## Playbook Model

主文档固定为：

- `playbooks/review-master-happy-path.md`

主文档按六阶段组织，每阶段至少包含：

- 用户输入
- agent 读取/调用内容
- 生成或更新的工件
- validator 输出要点
- agent 回复
- 用户回复

主文档中应显式引用：

- `playbooks/examples/happy-path-minimal/inputs/`
- `playbooks/examples/happy-path-minimal/workspace/`
- `playbooks/examples/happy-path-minimal/outputs/`
- `playbooks/examples/happy-path-minimal/validator-output/`

## Example Asset Model

`playbooks/examples/happy-path-minimal/` 至少包含：

- `inputs/`
  - 最小 LaTeX 原稿
  - 最小 Markdown 审稿意见
- `workspace/`
  - `workflow-state.yaml`
  - 6 类 Markdown 工件
  - `response-strategy-cards/reviewer_1_001.md`
- `outputs/`
  - 修订后的 `.tex`
  - `response-letter.md`
- `validator-output/`
  - `stage-1-entry-ready.json`
  - `stage-2-structure-ready.json`
  - `stage-3-atomic-ready.json`
  - `stage-4-board-ready.json`
  - `stage-5-comment-ready.json`
  - `stage-6-export-ready.json`

## Acceptance Model

一份合格的首期 playbook 应满足：

- 人类读者能从头到尾理解一次完整 happy path
- 文档里所有工件名、字段名、状态名、脚本名都与当前 skill 保持一致
- 样例 workspace 能被当前统一验证器接受为合法最终态
- validator JSON 样例与当前 `instruction_payload` 结构一致

## Migration Plan

1. 创建新 change 的 proposal、design、specs 和 tasks。
2. 新增 `playbooks/review-master-happy-path.md`。
3. 新增 `playbooks/examples/happy-path-minimal/inputs/`、`workspace/`、`outputs/` 和 `validator-output/`。
4. 运行 OpenSpec 校验。
5. 运行统一验证器检查样例 workspace。
