# review-master Happy Path Playbook

## Purpose

这份 playbook 展示当前合同下的最小 happy path：

- 单文件稿件
- 单 reviewer、少量 atomic items
- 无 supplement blocker
- Stage 5 完成策略闭环后直接进入新的 Stage 6

## Example Assets

- 输入：
  - `playbooks/examples/happy-path-minimal/inputs/manuscript/main.tex`
  - `playbooks/examples/happy-path-minimal/inputs/review-comments.md`
- workspace：
  - `playbooks/examples/happy-path-minimal/workspace/`
- 最终产物：
  - `playbooks/examples/happy-path-minimal/outputs/response-letter.md`
  - `playbooks/examples/happy-path-minimal/outputs/response-letter.tex`
- gate 快照：
  - `playbooks/examples/happy-path-minimal/gate-and-render-output/`

## Current Workspace Contract

示例 workspace 采用当前固定工件顺序：

1. `01-agent-resume.md`
2. `02-manuscript-structure-summary.md`
3. `03-style-profile.md`
4. `04-raw-review-thread-list.md`
5. `05-atomic-review-comment-list.md`
6. `06-thread-to-atomic-mapping.md`
7. `07-review-comment-coverage.md`
8. `08-atomic-comment-workboard.md`
9. `09-supplement-suggestion-plan.md`
10. `10-supplement-intake-plan.md`
11. `11-manuscript-revision-guide.md`
12. `12-manuscript-execution-graph.md`
13. `13-revision-action-log.md`
14. `14-response-coverage-matrix.md`
15. `15-response-letter-preview.md`
16. `16-response-letter-preview.tex`
17. `17-final-assembly-checklist.md`

## Stage 6 Notes

当前 Stage 6 的主线是：

1. 读取 `11-manuscript-revision-guide.md`
2. 读取 `12-manuscript-execution-graph.md`
3. 参考 `03-style-profile.md`
4. 在 `workspace/manuscript-copies/working-manuscript/` 上交互式改稿
5. 通过 `review-master/scripts/commit_revision_round.py` 提交每一轮修改
6. 由 `13-17` 工件审计修改记录、thread 覆盖和最终回复信预览

最终正式输出是：

- `working_manuscript`
- `response_markdown`
- `response_latex`
- 可选 `latexdiff_manuscript`
