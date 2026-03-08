# Manuscript Structure Summary

这是从 `review-master.db` 渲染出的全文级只读视图。数据库真源是 `manuscript_summary`、`manuscript_sections` 和 `manuscript_claims`。用户应通过这份视图确认结构理解是否准确；Agent 可以读取它获取辅助信息，但不得直接编辑。

## Project Summary

| Field | Value |
| --- | --- |
| `main_entry` | main.tex |
| `project_shape` | single_tex |

## Sections

| Section ID | Section Title | Purpose in Manuscript | Key Files or Locations |
| --- | --- | --- | --- |
| sec_intro | Introduction | State the problem and contribution | main.tex::Introduction::paragraph 1 |
| sec_results | Results | Present the main empirical findings | main.tex::Results::paragraph 2 |

## Core Claims

| Claim ID | Core Claim | Main Evidence | Supporting Section IDs | Risk Level |
| --- | --- | --- | --- | --- |
| claim_001 | The proposed method outperforms the baseline. | Main result paragraph and discussion sentence | sec_results | high |

## High Risk Areas

这些区域通常需要更谨慎地改稿或补证据。

| Zone ID | Description |
| --- | --- |
| Z1 | Abstract; Results |
