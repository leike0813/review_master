# Manuscript Structure Summary

这是从 `review-master.db` 渲染出的全文级只读视图。数据库真源是 `manuscript_summary`、`manuscript_sections` 和 `manuscript_claims`。用户应通过这份视图确认结构理解是否准确；Agent 可以读取它获取辅助信息，但不得直接编辑。

## Project Summary

| Field | Value |
| --- | --- |
| `main_entry` | main.tex |
| `project_shape` | latex_project |

## Sections

| Section ID | Section Title | Purpose in Manuscript | Key Files or Locations |
| --- | --- | --- | --- |
| sec_discussion | Discussion | Interpret strengths and limitations. | sections/discussion.tex::Discussion::paragraph 1 |
| sec_intro | Introduction | Define the problem and motivate the method. | sections/introduction.tex::Introduction::paragraph 1 |
| sec_method | Method | Describe the training pipeline and implementation details. | sections/method.tex::Method::paragraph 2 |
| sec_results | Results | Report the main robustness comparisons. | sections/results.tex::Results::table 1 |

## Core Claims

| Claim ID | Core Claim | Main Evidence | Supporting Section IDs | Risk Level |
| --- | --- | --- | --- | --- |
| claim_001 | The proposed training pipeline improves robustness under limited labels. | Main result table and discussion paragraph | sec_method,sec_results,sec_discussion | high |

## High Risk Areas

这些区域通常需要更谨慎地改稿或补证据。

| Zone ID | Description |
| --- | --- |
| Z1 | Methods; Results; Discussion |
