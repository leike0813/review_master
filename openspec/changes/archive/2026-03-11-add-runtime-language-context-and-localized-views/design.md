## Context

当前 runtime 把模板、推荐动作文本和中间视图都硬编码在 skill 包内，且默认使用单一语言。与此同时：

- 原稿 excerpt、reviewer 原文、canonical atomic 摘要、中间 strategy card、最终 response row 被混在同一语言层里；
- `init_artifact_workspace.py` 无法接收语言参数；
- `workspace_db.py` 只会从 `review-master/assets/templates` 加载模板，没有 workspace 级本地化覆盖入口；
- `gate_and_render_workspace.py` 的推荐动作、blocked actions 与 repair guidance 都是固定语言字符串。

这次变更是跨 schema、渲染、文档和样例的横切改造，必须先把语言边界与运行时加载机制定死，否则后续实现会在“模板翻译”“原文保护”“最终导出语言”之间互相打架。

## Goals / Non-Goals

**Goals**

- 让文本语言和工作语言成为 runtime 的正式状态，而不是仅靠 Agent 记忆。
- 让 Stage 1 在首次初始化前显式确认两种语言。
- 让 workspace 中所有用户可读的中间视图和推荐动作文本使用工作语言。
- 让原文摘录保持文本语言，最终 manuscript/response 导出固定使用文本语言。
- 提供 workspace-local localization overlay，而不是复制整套 skill 脚本。
- 让现有样例和 tests 能在新语言模型下继续回归。

**Non-Goals**

- 不在运行时复制或分叉 skill 包脚本。
- 不引入脚本级自动机器翻译依赖；语言检测和翻译判断仍由 Agent/LLM 承担。
- 不改变 `action_id`、`recipe_id`、DB 表名、字段名等机器侧标识。
- 不新增“按任意语言自动翻译 manuscript 正文”的脚本能力；Stage 6 仍由 Agent 生成最终文本语言 copy。

## Decisions

### Decision 1: 使用单份模板 + workspace-local 消息覆盖，而不是复制脚本副本

- 方案：
  - skill 包内保留单份模板和默认消息目录；
  - runtime 在渲染时优先读取 `artifact_root/runtime-localization/` 中的消息与可选模板覆盖；
  - 只有模板结构真的需要变化时，才使用 `runtime-localization/templates/`。
- 理由：
  - 满足“运行时不改 skill 包文件”；
  - 不会把脚本逻辑复制到 workspace 导致长期漂移；
  - 语言定制主要落在消息层，而非逻辑层。
- 备选：
  - 复制整套脚本与资产到 workspace：维护成本高，且运行时版本容易失控。

### Decision 2: Stage 1 采用 pre-bootstrap 语言确认

- 方案：
  - 首次进入、且 workspace 尚未存在时，先由 Agent 判断 `working_language` 和 `document_language` 并向用户确认；
  - 只有确认后才允许调用 `init_artifact_workspace.py`。
- 理由：
  - 初次渲染就应使用正确工作语言；
  - 避免“先渲染一套错误语言视图，再整体重渲染”的噪音。
- 备选：
  - 先初始化再确认语言：会让 bootstrap 阶段出现一次错误语言的只读视图。

### Decision 3: Stage 5 drafts 固定为工作语言，Stage 6 final copy 固定为文本语言

- 方案：
  - `strategy_action_manuscript_drafts` 和 `comment_response_drafts` 继续保存 Stage 5 真源，但内容为工作语言草案；
  - `action_copy_variants`、`response_thread_rows` 和最终导出内容全部切换到文本语言。
- 理由：
  - Stage 5 是协作与策略收敛阶段，工作语言最适合用户确认与调整；
  - Stage 6 才是最终成文阶段，必须严格回到文档语言。
- 备选：
  - Stage 5 直接写文本语言草案：会削弱工作语言在协作过程中的作用。

### Decision 4: schema 只记录语言上下文，不负责自动翻译

- 方案：
  - 新增 `runtime_language_context` 保存检测结果、确认结果和来源；
  - 运行时渲染与导出只读取这些已确认值；
  - 消息目录翻译由 Agent 在初始化或样例构造阶段提供。
- 理由：
  - 语言判断本来就是语义任务，应该继续由 Agent 承担；
  - 脚本只做确定性的读取、渲染与回退。
- 备选：
  - 引入自动检测/翻译库：增加依赖和不稳定性，不符合项目脚本边界。

## Risks / Trade-offs

- [Risk] 需要把大量模板静态文案与 gate 指令文本抽成消息 key  
  Mitigation: 先统一一份默认消息目录，再让模板和 gate 共享同一套 `msg()` 解析器。

- [Risk] 任意第三语言没有内置翻译时，会回退到默认消息目录  
  Mitigation: workspace overlay 始终优先；tests 只要求第三语言标签可通过 schema 与渲染链，不要求仓库内置所有语言包。

- [Risk] Stage 1 “首次先确认语言，再初始化 workspace” 与现有 resume-first 叙述冲突  
  Mitigation: 把它明确定义为“workspace 尚不存在时的唯一例外”；已有 workspace 的恢复仍保持 resume-first。

- [Risk] 示例 workspace 与 gate 快照需要整体重渲染  
  Mitigation: 统一更新四个 examples 的 DB、overlay、workspace 视图和 gate 输出，并用回归测试锁住。

## Migration Plan

1. 新开 change 并补齐 proposal/design/specs/tasks。
2. 修改 schema、init script、workspace render、gate 和 export 链。
3. 新增默认消息目录与 workspace-local localization overlay 创建逻辑。
4. 把模板与 gate 的自然语言文本改为消息 key。
5. 更新 `SKILL.md`、runtime digest、Stage 1/3/5/6 指南、SQL recipes 与 glossary。
6. 升级 examples：
   - 写入 `runtime_language_context`
   - 增加 `runtime-localization/`
   - 重渲染 workspace 和 gate snapshots
7. 运行 pytest 与 openspec validate。

## Open Questions

- 无。当前方案已锁定为 overlay 模式、双语言确认、任意语言标签、Stage 5 工作语言草案与 Stage 6 文本语言最终文案。
