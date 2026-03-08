# Action Copy Variants

这是从 `review-master.db` 渲染出的 Stage 6 文案版本视图。数据库真源是 `action_copy_variants` 与 `selected_action_copy_variants`。这里的 3 个版本，指的是最终稿里真正要落下去的 manuscript 局部落稿文本版本，而不是策略版本，也不是 response-side 方案版本。若一个 action 覆盖多个位置，则每个位置都必须各自提供一组 `v1/v2/v3`。

## atomic_001 / action 1

- Manuscript change: Revise the introduction and main-results explanation to state why short attention paths help long-range dependency modeling.
- Expected response effect: Provide a direct point-to-point response for atomic_001.

### location 1

- Target location: sections/introduction.tex::Introduction::paragraph 3

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Self-attention reduces the number of sequential operations and therefore improves throughput. | Focus on efficiency. |
| v2 | yes | Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. | Best balances mechanism and caution. |
| v3 | no | Attention can replace recurrence because every position can directly consult the full sequence context. | More assertive but less nuanced. |

### location 2

- Target location: sections/results.tex::Machine Translation::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Self-attention reduces the number of sequential operations and therefore improves throughput. | Focus on efficiency. |
| v2 | yes | Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. | Best balances mechanism and caution. |
| v3 | no | Attention can replace recurrence because every position can directly consult the full sequence context. | More assertive but less nuanced. |

## atomic_002 / action 1

- Manuscript change: Rewrite the background positioning paragraph to distinguish the paper from ByteNet, ConvS2S, and memory-style attention.
- Expected response effect: Provide a direct point-to-point response for atomic_002.

### location 1

- Target location: sections/background.tex::Background::paragraph 3

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The work differs from prior efficient models by emphasizing attention rather than convolution. | Minimal distinction. |
| v2 | yes | The specific claim here is that a strong encoder-decoder translation system can be built from self-attention and feed-forward blocks alone, without sequence-aligned recurrence or convolution in the main transduction backbone. | Explicit novelty boundary. |
| v3 | no | Unlike prior efficient architectures, this model removes the need for both recurrence and convolution in the main backbone. | Sharper wording. |

## atomic_003 / action 1

- Manuscript change: Add a concise architecture-sensitivity paragraph summarizing head-count, dropout, and scale variations.
- Expected response effect: Provide a direct point-to-point response for atomic_003.

### location 1

- Target location: sections/architecture.tex::Model Configuration::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The reported architecture worked well in our experiments. | Too generic. |
| v2 | yes | Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. | Uses restored sensitivity evidence. |
| v3 | no | The ablation results show that the default architecture strikes the strongest accuracy-efficiency trade-off. | Slightly stronger claim. |

### location 2

- Target location: sections/results.tex::Model Variations::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The reported architecture worked well in our experiments. | Too generic. |
| v2 | yes | Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. | Uses restored sensitivity evidence. |
| v3 | no | The ablation results show that the default architecture strikes the strongest accuracy-efficiency trade-off. | Slightly stronger claim. |

## atomic_004 / action 1

- Manuscript change: Revise the main-results discussion to explain why short attention paths plausibly improve the baseline comparison.
- Expected response effect: Provide a direct point-to-point response for atomic_004.

### location 1

- Target location: sections/results.tex::Machine Translation::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The model may benefit from improved contextual modeling. | Vague. |
| v2 | yes | The attention-only encoder-decoder appears to benefit from short cross-token path lengths, which helps preserve long-range dependencies without recurrent state propagation. | Mechanism explanation tied to results. |
| v3 | no | The baseline gain comes from more efficient global context aggregation. | Too compressed. |

## atomic_005 / action 1

- Manuscript change: Restore WMT data, preprocessing, checkpoint averaging, and beam-search details in the training section.
- Expected response effect: Provide a direct point-to-point response for atomic_005.

### location 1

- Target location: sections/training.tex::Data::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | We used standard WMT data and common decoding settings. | Too vague. |
| v2 | yes | English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. | Protocol details for data. |
| v3 | no | We follow standard WMT preprocessing and evaluation conventions for both translation tasks. | Not enough detail. |

### location 2

- Target location: sections/training.tex::Implementation Notes::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | We used standard WMT data and common decoding settings. | Too vague. |
| v2 | yes | English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. | Protocol details for data. |
| v3 | no | We follow standard WMT preprocessing and evaluation conventions for both translation tasks. | Not enough detail. |

## atomic_006 / action 1

- Manuscript change: Add a cost-accounting paragraph clarifying hardware, FLOPs, and fairness caveats.
- Expected response effect: Provide a direct point-to-point response for atomic_006.

### location 1

- Target location: sections/results.tex::Machine Translation::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The cost comparison remains favorable for the Transformer. | Too broad. |
| v2 | yes | The larger model achieves a new state of the art on English-to-German and remains highly competitive on English-to-French while requiring substantially less reported training cost than earlier recurrent or convolutional systems under the stated accounting convention. | Cost accounting caveat included. |
| v3 | no | The model is more efficient than prior baselines on the reported hardware budget. | Less precise. |

### location 2

- Target location: sections/conclusion.tex::Conclusion::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The cost comparison remains favorable for the Transformer. | Too broad. |
| v2 | yes | The larger model achieves a new state of the art on English-to-German and remains highly competitive on English-to-French while requiring substantially less reported training cost than earlier recurrent or convolutional systems under the stated accounting convention. | Cost accounting caveat included. |
| v3 | no | The model is more efficient than prior baselines on the reported hardware budget. | Less precise. |

## atomic_007 / action 1

- Manuscript change: Add a stability paragraph calibrated by the supplemental multi-run evidence.
- Expected response effect: Provide a direct point-to-point response for atomic_007.

### location 1

- Target location: sections/results.tex::Stability Statement::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The results seem stable. | Too weak. |
| v2 | yes | The supplemental five-run evidence shows a narrow spread around the main result. | Conservative stability wording. |
| v3 | no | The results are robust across repeated runs. | Too strong. |

## atomic_008 / action 1

- Manuscript change: Expand the discussion to name failure buckets, scope boundaries, and long-sequence cost caveats.
- Expected response effect: Provide a direct point-to-point response for atomic_008.

### location 1

- Target location: sections/discussion.tex::Discussion::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The model still has limitations. | Too vague. |
| v2 | yes | Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. | Concrete failure buckets. |
| v3 | no | The method is promising but not universally optimal, especially for difficult long-sequence settings. | Broader caveat. |

### location 2

- Target location: sections/conclusion.tex::Conclusion::paragraph 2

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | The model still has limitations. | Too vague. |
| v2 | yes | Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. | Concrete failure buckets. |
| v3 | no | The method is promising but not universally optimal, especially for difficult long-sequence settings. | Broader caveat. |

## atomic_009 / action 1

- Manuscript change: Add a qualitative attention case-study paragraph tied to a long sentence example.
- Expected response effect: Provide a direct point-to-point response for atomic_009.

### location 1

- Target location: sections/results.tex::Interpretability::paragraph 1

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Some attention heads seem interpretable. | Too vague. |
| v2 | yes | In one long English-German sentence, an upper-layer head links a subordinate-clause introducer to the postponed main verb, while another head tracks a named entity span across punctuation boundaries. | Concrete case study. |
| v3 | no | The attention patterns align with syntactic and semantic structure in some examples. | More general. |

### location 2

- Target location: sections/discussion.tex::Discussion::paragraph 4

#### manuscript final copy

| Variant | Selected | Variant Text | Rationale |
| --- | --- | --- | --- |
| v1 | no | Some attention heads seem interpretable. | Too vague. |
| v2 | yes | In one long English-German sentence, an upper-layer head links a subordinate-clause introducer to the postponed main verb, while another head tracks a named entity span across punctuation boundaries. | Concrete case study. |
| v3 | no | The attention patterns align with syntactic and semantic structure in some examples. | More general. |

