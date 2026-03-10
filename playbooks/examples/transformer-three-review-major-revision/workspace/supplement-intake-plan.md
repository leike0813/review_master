# Supplement Intake And Landing Plan

这是从 `review-master.db` 渲染出的 Stage 5 补材接收与落地方案视图。数据库真源是 `supplement_intake_items` 与 `supplement_landing_links`。该视图用于向用户展示每轮补材的接收判定，以及被接收补材将如何落到 canonical atomic action 的具体位置。

## Round: `round-1`

| File | Concern Summary | Decision | Decision Rationale | Landing Targets |
| --- | --- | --- | --- | --- |
| `user-supplements/round-1/method-positioning-note.md` | method positioning and attention-only mechanism clarification | `accepted` | Provides direct wording support for novelty boundary and mechanism explanation. | `atomic_001` / action 1 / location 1: Use to expand attention-only mechanism explanation in Introduction.<br>`atomic_002` / action 1 / location 1: Use to sharpen novelty boundary in Background positioning paragraph. |
| `user-supplements/round-1/reproducibility-note.md` | dataset usage and reproducibility protocol details | `accepted` | Provides reproducibility-critical protocol details for data and decoding setup. | `atomic_005` / action 1 / location 1: Use to restore WMT data usage and preprocessing details. |
| `user-supplements/round-1/round-1-cover-note.md` | round logistics note | `rejected` | Administrative cover note; no standalone evidence to land in manuscript text. | N/A |
| `user-supplements/round-1/wmt-decode-settings.tex` | checkpoint averaging and decoding setup details | `accepted` | Contains compile-ready decoding and checkpoint settings for the training section. | `atomic_005` / action 1 / location 2: Use to restore checkpoint averaging and decode settings in training notes. |

## Round: `round-2`

| File | Concern Summary | Decision | Decision Rationale | Landing Targets |
| --- | --- | --- | --- | --- |
| `user-supplements/round-2/ablation-interpretation-note.md` | ablation interpretation and reporting wording | `accepted` | Explains how to translate ablation values into bounded manuscript claims. | `atomic_003` / action 1 / location 1: Use interpretation note to justify configuration sensitivity statement. |
| `user-supplements/round-2/component-ablation.csv` | component contribution and sensitivity evidence | `accepted` | Provides quantitative ablation values for component contribution claims. | `atomic_003` / action 1 / location 2: Use quantitative ablation values in Model Variations paragraph. |
| `user-supplements/round-2/efficiency-accounting-note.md` | FLOPs and fairness caveat wording | `accepted` | Defines the accounting assumptions and caveats for efficiency claims. | `atomic_006` / action 1 / location 2: Use accounting caveat wording in Conclusion boundary paragraph. |
| `user-supplements/round-2/efficiency-cost-comparison.csv` | efficiency and cost accounting evidence | `accepted` | Provides comparable cost and throughput values for fairness caveats. | `atomic_006` / action 1 / location 1: Use efficiency table values in Machine Translation cost paragraph.<br>`atomic_007` / action 1 / location 1: Use run-to-run spread summary for Stability Statement paragraph. |
| `user-supplements/round-2/round-2-cover-note.md` | round logistics note | `rejected` | Administrative cover note; no direct manuscript landing content. | N/A |

## Round: `round-3`

| File | Concern Summary | Decision | Decision Rationale | Landing Targets |
| --- | --- | --- | --- | --- |
| `user-supplements/round-3/attention-case-study.md` | qualitative interpretability case study | `accepted` | Provides case-level qualitative evidence for the interpretability response. | `atomic_009` / action 1 / location 1: Use narrative case evidence in Interpretability paragraph. |
| `user-supplements/round-3/attention-pattern-example.svg` | attention qualitative figure evidence | `accepted` | Supplies figure-level qualitative pattern evidence for interpretability. | `atomic_009` / action 1 / location 1: Embed qualitative pattern figure to support interpretability claim. |
| `user-supplements/round-3/failure-bucket-summary.csv` | failure buckets and scope boundary evidence | `accepted` | Provides failure-bucket counts to support bounded discussion claims. | `atomic_008` / action 1 / location 1: Use failure-bucket summary in Discussion limitations paragraph. |
| `user-supplements/round-3/limitations-and-boundaries.md` | limitations and scope caveat wording | `accepted` | Provides concise caveat text for limitations and conclusion scope. | `atomic_008` / action 1 / location 2: Use caveat wording in Conclusion scope-boundary paragraph. |
| `user-supplements/round-3/round-3-cover-note.md` | round logistics note | `rejected` | Administrative cover note; no direct manuscript landing content. | N/A |

