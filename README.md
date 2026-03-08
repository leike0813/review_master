# review_master

`review_master` 是一个面向学术论文修回场景的 Agent Skill 开发仓库。它的目标不是“自动改稿”，而是把论文修回过程拆成可交互、可确认、可追踪的阶段化工作流，帮助用户逐步完成原稿理解、审稿意见拆解、策略制定、证据补充、回复信组装与最终导出。

仓库中的最终发布 Skill 包位于 `review-master/`；其余目录主要是开发资料、样例资产、OpenSpec 规格和测试，不属于发布包本体。

## 项目定位

- 这是一个 Skill 包开发项目，不是常规 Web 服务或 CLI 产品仓库。
- 核心交付物是 [`review-master/SKILL.md`](/home/joshua/Workspace/Code/Skill/review_master/review-master/SKILL.md)，以及支撑它运行的 `references/`、`assets/`、`scripts/`。
- Skill 以“分阶段推进”替代“一步到位改稿”，强调用户确认、学术判断和证据驱动。
- 运行时以 `review-master.db` 作为唯一真源，渲染出的 Markdown 视图仅用于阅读与确认，不可当作真源直接编辑。

## 仓库结构

- [`review-master/`](/home/joshua/Workspace/Code/Skill/review_master/review-master)
  - 最终发布的 Skill 包。
  - 包含 `SKILL.md`、运行时脚本、模板、schema、补充参考文档。
- [`references/`](/home/joshua/Workspace/Code/Skill/review_master/references)
  - 仓库级背景研究资料。
  - 当前主要包含理工科审稿回复方法研究，不直接等同于 Skill 运行时文档。
- [`playbooks/`](/home/joshua/Workspace/Code/Skill/review_master/playbooks)
  - 仓库级演练与回放资料。
  - 用于说明 happy path、evidence supplement、failure recovery、major revision 等典型流程。
- [`examples/`](/home/joshua/Workspace/Code/Skill/review_master/examples)
  - 示例论文素材源。
  - 当前 `example_orig.md` 也被复杂 playbook 用作“终稿快照”基底。
- [`openspec/`](/home/joshua/Workspace/Code/Skill/review_master/openspec)
  - 项目的规格、变更和归档记录。
  - 用于追踪 Skill 结构、状态机、导出契约等设计演进。
- [`tests/`](/home/joshua/Workspace/Code/Skill/review_master/tests)
  - 回归测试。
  - 覆盖 workspace 初始化、gate-and-render 契约、导出逻辑、示例资产完整性等。
- [`AGENTS.md`](/home/joshua/Workspace/Code/Skill/review_master/AGENTS.md)
  - 本仓库的高优先级协作约束与项目背景说明。

## Skill 包内部结构

`review-master/` 目录内的关键部分如下：

- [`review-master/SKILL.md`](/home/joshua/Workspace/Code/Skill/review_master/review-master/SKILL.md)
  - Skill 的顶层运行契约与阶段化指令入口。
- [`review-master/references/`](/home/joshua/Workspace/Code/Skill/review_master/review-master/references)
  - 按阶段拆分的详细执行说明和辅助规则。
- [`review-master/scripts/`](/home/joshua/Workspace/Code/Skill/review_master/review-master/scripts)
  - 只承担确定性、重复性高的辅助工作。
  - 当前核心脚本包括 `detect_main_tex.py`、`init_artifact_workspace.py`、`gate_and_render_workspace.py`、`export_manuscript_variants.py`。
- [`review-master/assets/`](/home/joshua/Workspace/Code/Skill/review_master/review-master/assets)
  - 模板、schema 和运行时摘要。

## 核心工作流概览

`review-master` 当前采用六阶段主流程：

1. 入口解析与 artifact workspace 初始化。
2. 原稿结构分析。
3. 原始审稿意见块抽取、去重与 canonical atomic item 建模。
4. atomic workboard 规划与用户确认。
5. 逐条策略制定、补材闭环与执行推进。
6. 风格画像、最终文案版本选择、thread-level row 组装与双阶段导出。

其中有两个运行时原则需要始终保持一致：

- 数据库真源优先：正式写入发生在 `review-master.db`，不是 Markdown 视图。
- gate-and-render 闭环：每次正式写库后都要重新运行 `gate_and_render_workspace.py`，由它负责状态门禁、只读视图重渲染和下一步指令输出。

## 推荐阅读顺序

如果你要继续维护这个项目，建议按下面顺序进入上下文：

1. 阅读 [`AGENTS.md`](/home/joshua/Workspace/Code/Skill/review_master/AGENTS.md)，先理解项目定位、非目标和协作约束。
2. 阅读 [`review-master/SKILL.md`](/home/joshua/Workspace/Code/Skill/review_master/review-master/SKILL.md)，确认 Skill 的输入输出、状态机和脚本边界。
3. 阅读 [`playbooks/README.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/README.md)，了解仓库内有哪些演练路线。
4. 选择一个 playbook 或 example 进入细看，复杂案例推荐 [`playbooks/examples/transformer-three-review-major-revision/README.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/examples/transformer-three-review-major-revision/README.md)。
5. 若要追溯设计来由，再查看 `openspec/specs/` 或 `openspec/changes/archive/`。

## 开发与验证

项目约定优先使用 `DataProcessing` conda 环境运行 Python。

常用验证命令：

```bash
conda run --no-capture-output -n DataProcessing pytest
```

如需单独运行某个运行时脚本，也应优先使用同一环境，例如：

```bash
conda run --no-capture-output -n DataProcessing python -u \
  review-master/scripts/gate_and_render_workspace.py \
  --artifact-root <ARTIFACT_ROOT>
```

## 维护约束

- 修改 [`review-master/SKILL.md`](/home/joshua/Workspace/Code/Skill/review_master/review-master/SKILL.md) 时，必须同步检查并更新 [`review-master/assets/runtime/skill-runtime-digest.md`](/home/joshua/Workspace/Code/Skill/review_master/review-master/assets/runtime/skill-runtime-digest.md)。
- 不要把语义判断工作外包给临时脚本。脚本只负责确定性辅助，不负责审稿意见语义理解、策略制定或学术决策。
- 不要把 `playbooks/` 和 `examples/` 误认为发布包内容；它们是仓库级开发资产。

## 典型入口

- 想看最小闭环样例：[`playbooks/review-master-happy-path.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/review-master-happy-path.md)
- 想看补材驱动的多 reviewer 样例：[`playbooks/review-master-evidence-supplement-playbook.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/review-master-evidence-supplement-playbook.md)
- 想看 failure recovery：[`playbooks/review-master-evidence-supplement-failure-recovery.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/review-master-evidence-supplement-failure-recovery.md)
- 想看更接近真实 major revision 的复杂案例：[`playbooks/review-master-transformer-three-review-major-revision.md`](/home/joshua/Workspace/Code/Skill/review_master/playbooks/review-master-transformer-three-review-major-revision.md)
