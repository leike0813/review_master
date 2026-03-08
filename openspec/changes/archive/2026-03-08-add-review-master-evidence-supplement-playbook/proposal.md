## Why

现有 `review-master-happy-path` playbook 证明了最小 happy path 可行，但它只覆盖：

- 单文件 `main.tex`
- 1 位 reviewer
- 1 条原子意见
- 无补证据闭环

这不足以演示当前 skill 在较真实场景中的关键价值：多 reviewer、多 comment、工作板确认、阶段五中途因证据缺口阻塞，以及用户补材后继续推进。

因此需要新增一份更长、更接近真实修回流程的仓库级 playbook，并附带一套更复杂的样例资产，作为开发与演练参考。

## What Changes

- 新增一个复杂样例 playbook change
- 在 `playbooks/` 下新增第二份 playbook：多 reviewer、多 comment、含补证据闭环
- 新增 `playbooks/README.md`，索引最小样例和复杂样例
- 新增一套多文件 LaTeX manuscript、review comments、补材包、最终态 workspace、最终输出和代表性 validator JSON
- 不修改 skill 契约、不修改 validator 逻辑、不新增发布组件

## Capabilities

### New Capabilities

- `review-master-playbook-index`: 规定仓库级 playbook 索引必须列出最小样例与复杂样例
- `review-master-playbook-multi-review-flow`: 规定复杂 playbook 必须覆盖 2 位 reviewers、5 条原子意见和一次显式 blocked/unblocked 闭环
- `review-master-playbook-evidence-supplement-assets`: 规定复杂样例必须附带多文件 manuscript、补材包、最终态 workspace、最终输出和 8 份代表性 validator JSON

### Modified Capabilities

<!-- None -->

## Impact

- 新增 `openspec/changes/add-review-master-evidence-supplement-playbook/`
- 新增 `playbooks/README.md`
- 新增 `playbooks/review-master-evidence-supplement-playbook.md`
- 新增 `playbooks/examples/evidence-supplement-multi-review/`
- 保留 `playbooks/review-master-happy-path.md`
- 不更新 `review-master/SKILL.md`
