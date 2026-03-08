## Context

`review-master` 当前存在两个层次的约束：

- 项目级约束：`AGENTS.md` 已明确该 skill 必须交互式、阶段化、方案先行，且不能替用户做未经授权的决策
- 规格级约束：`define-review-master-staged-workflow` 已经把首期的输入输出、六阶段流程、逐条确认和证据缺口规则写成了 OpenSpec

但运行时主入口 `review-master/SKILL.md` 仍然停留在“理解与拆解 / 映射与评估 / 规划与建议 / 受控执行”的泛化骨架，没有把这些规格真正转成 Agent 可执行的主文档。当前最需要的不是继续加脚本或 schema，而是先让主文档与规格一致。

## Goals / Non-Goals

**Goals:**
- 将首期输入槽、输出槽与交互门禁正式写入 `review-master/SKILL.md`
- 用六阶段执行流程替换当前过于抽象的四阶段概述
- 将首期中间工件统一约束为 Markdown 优先，并说明何时生成、何时给用户确认
- 把可选输入 `editor_letter_source` 与 `user_notes` 融入主流程而不阻断仅有必需输入的主路径

**Non-Goals:**
- 不在本 change 中新增脚本、模板文件、schema 或 runner 配置
- 不在本 change 中定义中间工件的结构化 YAML/JSON 版本
- 不引入新的输入类型；首期仍只围绕 LaTeX 原稿和 Markdown/txt 审稿意见

## Decisions

### 1. 先更新 `SKILL.md`，暂不引入脚本

- Decision: 本 change 先把规格下沉到 `review-master/SKILL.md`，而不是同时引入辅助脚本
- Rationale: 当前缺的不是自动化能力，而是主契约缺位。若先上脚本，会在主文档尚未稳定的情况下提前固化接口与职责
- Alternatives considered:
  - 先定义并接入入口检查或意见原子化脚本
  - 同时推进主文档和脚本职责
- Why not: 两者都会把实现边界前置，增加后续返工成本

### 2. 首期中间工件统一采用 Markdown 优先

- Decision: 原稿结构摘要、原子清单、映射表、工作板、策略卡和最终汇编清单，都先按 Markdown 优先处理
- Rationale: 这些工件的首要用途是给用户阅读、确认和纠偏。Markdown 最符合交互式审稿工作流的可读性需求，也最适合先行固定
- Alternatives considered:
  - 统一采用 YAML/JSON
  - 同时维护 Markdown 和结构化双轨版本
- Why not: 前者会削弱可读性；后者会在首期引入双重维护成本

### 3. `editor_letter_source` 是可选文件槽，`user_notes` 是可选自由文本

- Decision: 编辑决定信采用可选文件路径输入；用户意见采用可选自由文本输入
- Rationale: 编辑决定信通常是独立文档，适合文件路径；用户意见则更像对策略、顾虑和补充说明的即时输入，文本更自然
- Alternatives considered:
  - 两者都做文件路径
  - 两者都兼容文件或文本
- Why not: 前者会让用户补充意见变得笨重；后者会让主契约和后续校验规则过于复杂

### 4. 可选输入只增强主流程，不改变主路径

- Decision: 六阶段流程的启动条件仍然只有两个必需输入；可选输入仅用于补充编辑层要求和用户偏好，不得成为启动前提
- Rationale: 这样既能保留首期最小输入路径，又能让额外上下文在工作板和策略卡阶段发挥作用
- Alternatives considered:
  - 有可选输入就强制提前吸收，无可选输入则阻断
  - 把编辑决定信升格为必需输入
- Why not: 两者都会破坏已经确认的首期最小必需输入集合

## Risks / Trade-offs

- [Risk] 不引入脚本会让某些步骤仍然依赖人工或 Agent 文本处理
- Mitigation: 当前 change 只负责把主契约固定下来；脚本能力在主契约稳定后再补

- [Risk] Markdown 工件不如结构化数据利于自动状态跟踪
- Mitigation: 首期优先解决“人可读、可确认”；结构化 schema 留给后续 change

- [Risk] 可选输入槽增加主文档长度和分支
- Mitigation: 明确要求可选输入只增强主路径，不改变主路径启动条件

## Migration Plan

1. 新建 `implement-review-master-skill-contract` change，并补齐 proposal、design、specs、tasks。
2. 更新 `review-master/SKILL.md`，使其与 staged-workflow change 中的规格一致。
3. 用 `openspec validate implement-review-master-skill-contract --type change --strict` 验证新 change。
4. 保持 `review-master/references/`、`review-master/scripts/`、`review-master/assets/` 不变，后续能力再增量补充。

本 change 不引入额外文件模板，也不迁移旧资产。若回退，只需恢复 `SKILL.md` 并删除该 change。

## Open Questions

- 后续如果要把 Markdown 工件进一步结构化，优先从工作板、策略卡还是映射表开始。
- 未来是否需要把 `editor_letter_source` 升级为期刊级必需输入，取决于实际使用频率。
