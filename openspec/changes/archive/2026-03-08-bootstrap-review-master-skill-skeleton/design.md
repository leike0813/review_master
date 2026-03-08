## Context

本仓库当前只有两类与 `review-master` 相关的资产：

- 仓库根的项目约束文档 `AGENTS.md`
- 仓库根的参考资料 `references/review_reply_guide_STEM.md`

在这次 change 之前，仓库内没有形成一个可发布的 skill 包入口，也没有把“哪些内容属于发布包、哪些内容只是开发期资产”明确固定下来。对于一个 Agent Skill 项目，这是一个结构性问题：后续如果直接开始补充 `SKILL.md` 细节、脚本或参考资料，很容易把运行时资产继续散落在仓库根目录，导致发布边界、开发边界和后续 OpenSpec 规格边界混淆。

本 change 的目标不是实现审稿意见分析逻辑，而是先用最小骨架把承载位固定下来。根据本仓库已有约束与本地 OpenSpec CLI 的 `spec-driven` 工作流，这一 change 需要完整包含 `proposal`、`design`、`specs`、`tasks` 四类 artifact。

## Goals / Non-Goals

**Goals:**
- 为 `review-master` 建立唯一的发布目录入口，并把该入口固定为 `review-master/`
- 为包根 `SKILL.md` 建立最小但可发布的骨架，使其能承载后续迭代
- 预留 `references/`、`scripts/`、`assets/` 目录，避免后续能力继续堆积在仓库根目录
- 在不引入业务实现的前提下，把关键安全边界写进 `SKILL.md`
- 让当前 change 满足 OpenSpec 的完整工件要求，并可通过 CLI 校验

**Non-Goals:**
- 不定义审稿意见拆解、映射、优先级计算或回复生成的具体算法
- 不引入运行时 input/output schema、runner 配置或业务脚本
- 不迁移仓库根 `references/review_reply_guide_STEM.md` 到发布包
- 不生成 `agents/openai.yaml` 或其它 UI 元数据

## Decisions

1. 发布入口固定为 `review-master/`
- Decision: 把 `review-master/` 作为唯一发布目录，并要求包根存在 `SKILL.md`
- Rationale: 这样可以把“发布给 Agent 的内容”与仓库级开发资料分离，后续新增资产也有明确落点
- Alternative considered: 继续使用仓库根作为 skill 根目录
- Why not: 会让 `openspec/`、开发参考资料、编辑器配置与发布包混在一起，无法形成清晰边界

2. `SKILL.md` 先做骨架，不做完整实现
- Decision: 当前 `SKILL.md` 只写 frontmatter、阶段化流程、非目标、强约束和资源加载边界
- Rationale: 项目目标本身强调交互式、阶段化和方案先行；在没有后续 OpenSpec change 的情况下写完整实现，会把未决策内容提前固化
- Alternative considered: 一次性写出完整执行版 `SKILL.md`
- Why not: 会在缺少输入契约、输出契约和中间工件设计的情况下过度承诺实现细节

3. 用预留目录而不是空想未来结构
- Decision: 在发布包中立即建立 `references/`、`scripts/`、`assets/`，并以占位文件追踪它们
- Rationale: 这样后续 change 可以直接把新增运行时资产放入稳定位置，也能把“仓库根资料默认不发布”表达清楚
- Alternative considered: 等真正需要时再创建目录
- Why not: 会让后续能力实现重新面对目录归属决策，增加结构漂移风险

4. 开发期资产留在仓库根，发布期资产只进入 `review-master/`
- Decision: 继续保留根目录 `openspec/` 和根目录 `references/` 作为开发资料来源，但不把它们默认视为发布包内容
- Rationale: 当前根目录资料主要服务于项目开发和规范沉淀，不等同于运行时必需资产
- Alternative considered: 立即把根目录参考资料迁入发布包
- Why not: 现阶段还没有裁剪、索引和调用时机设计，直接迁移会让发布包携带未经整理的开发资料

5. 暂不生成 UI 元数据
- Decision: 本次不创建 `agents/openai.yaml`
- Rationale: 该文件依赖更稳定的 skill 定位和 prompt 元数据；在 `SKILL.md` 还只是骨架时生成它，后续会产生重复同步成本
- Alternative considered: 在骨架阶段同时创建 UI 元数据占位
- Why not: 这不会提升当前骨架的可用性，反而会引入一个需要持续同步的半成品接口

## Risks / Trade-offs

- [Risk] 当前骨架只定义边界，不定义业务行为，后续 change 数量会增加
- Mitigation: 这是有意为之；将复杂领域拆成连续的小 change，避免把未决策内容一次性硬编码进 `SKILL.md`

- [Risk] 仓库根仍然保留参考资料，后来者可能误以为这些文件会随 skill 一起发布
- Mitigation: 在 package layout spec 和 `SKILL.md` 中明确“根目录资料默认不属于发布包”，后续若迁移则单独通过 change 记录

- [Risk] 只靠 `.gitkeep` 预留目录，无法表达每类资产的详细用途
- Mitigation: 在 `SKILL.md` 明确写出 `references/`、`scripts/`、`assets/` 的职责边界；具体文件契约留待后续 change

- [Risk] 没有 UI 元数据会让 skill 在某些消费端缺少展示信息
- Mitigation: 把它推迟到 `SKILL.md` 和接口语义稳定之后，再单开 change 补齐

## Migration Plan

1. 保留现有仓库根开发资料不动，不做迁移或删除。
2. 在 `review-master/` 下建立最小发布骨架，并把 `SKILL.md` 作为后续唯一入口。
3. 在 OpenSpec change 中补齐 `design.md`，使当前 change 成为完整的四工件集合。
4. 运行 `openspec validate bootstrap-review-master-skill-skeleton --type change --strict` 校验当前 change。
5. 后续功能性工作一律通过新的 change 追加到该骨架之上，而不是回到仓库根直接扩展。

本 change 不涉及数据迁移、回滚脚本或运行时兼容转换；若需回退，只需删除新建的发布骨架与对应 change。

## Open Questions

- 后续第一个功能性 change 应优先定义哪一部分：输入材料契约、中间工件格式，还是审稿意见拆解流程。
- 仓库根 `references/review_reply_guide_STEM.md` 未来是整体迁入发布包，还是拆分为多个按需加载的参考文件。
- `review-master` 最终是否需要运行时 schema 与 `runner.json`，以及它们应在第几个 change 中引入。
