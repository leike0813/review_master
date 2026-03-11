# Manuscript Structure Summary

这是从 `review-master.db` 渲染出的全文级只读视图。数据库真源是 `manuscript_summary`、`manuscript_sections` 和 `manuscript_claims`。用户应通过这份视图确认结构理解是否准确；Agent 可以读取它获取辅助信息，但不得直接编辑。

## 项目摘要

| 字段 | 值 |
| --- | --- |
| `main_entry` | main.tex |
| `project_shape` | latex_project |

## 章节列表

| Section ID | 章节标题 | 在稿件中的作用 | 关键文件或位置 |
| --- | --- | --- | --- |
| sec_discussion | Discussion | Interpret strengths and limitations. | sections/discussion.tex::Discussion::paragraph 1 |
| sec_intro | Introduction | Define the problem and motivate the method. | sections/introduction.tex::Introduction::paragraph 1 |
| sec_method | Method | Describe the training pipeline and implementation details. | sections/method.tex::Method::paragraph 2 |
| sec_results | Results | Report the main robustness comparisons. | sections/results.tex::Results::table 1 |

## 核心主张

| Claim ID | 核心主张 | 主要证据 | 支撑章节 ID | 风险等级 |
| --- | --- | --- | --- | --- |
| claim_001 | The proposed training pipeline improves robustness under limited labels. | Main result table and discussion paragraph | sec_method,sec_results,sec_discussion | high |

## 高风险区域

这些区域通常需要更谨慎地改稿或补证据。

| 区域 ID | 说明 |
| --- | --- |
| Z1 | Methods; Results; Discussion |
