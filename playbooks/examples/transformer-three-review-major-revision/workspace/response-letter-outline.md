# Response Letter Outline

这是从 `review-master.db` 渲染出的 Stage 6 预组装视图。数据库真源是 `raw_review_threads`、`response_thread_resolution_links`、`selected_action_copy_variants`、`response_thread_rows`、`atomic_comments`、`strategy_card_actions` 和 `strategy_action_target_locations`。最终 response letter 必须按原始 `thread_id` 顺序组织，而不是按 canonical atomic item 直接展开。这里的 thread-level row 来自 Stage 5 已确认的策略/草案、Stage 6 在各个 target location 上已选中的 manuscript 最终落稿文本，以及 thread-level 聚合；它不是从 response-side variants 中选出来的。

## reviewer_1

### reviewer_1_thread_001

- Original thread: The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.
- Normalized summary: Clarify why attention-only is a viable replacement beyond parallelism.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_001 | Explain why attention-only can replace recurrence and convolution in this translation setting. | L1 sections/introduction.tex::Introduction::paragraph 3 / v2=Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks., L2 sections/results.tex::Machine Translation::paragraph 2 / v2=Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism. | sections/introduction.tex::paragraph 3 | Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. | We revised the introduction to explain why attention-only modeling helps beyond improved parallelism. |

### reviewer_1_thread_002

- Original thread: The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.
- Normalized summary: Clarify novelty positioning against efficient sequence models.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_002 | Clarify novelty positioning against ByteNet, ConvS2S, and related prior work. | L1 sections/background.tex::Background::paragraph 3 / v2=The specific claim here is that a strong encoder-decoder translation system can be built from self-attention and feed-forward blocks alone, without sequence-aligned recurrence or convolution in the main transduction backbone. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work. | sections/background.tex::paragraph 3 | The specific claim here is that a strong encoder-decoder translation system can be built from self-attention and feed-forward blocks alone, without sequence-aligned recurrence or convolution in the main transduction backbone. | We clarified the novelty boundary against prior efficient sequence models and narrowed the claim accordingly. |

### reviewer_1_thread_003

- Original thread: The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.
- Normalized summary: Request component-level sensitivity analysis.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | L1 sections/architecture.tex::Model Configuration::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design., L2 sections/results.tex::Model Variations::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale. | sections/architecture.tex::Model Configuration::paragraph 1 | The accompanying variation study shows that the conclusions are not reducible to a single arbitrary hyperparameter choice: single-head attention underperforms, removing dropout hurts generalization, and larger models help without erasing the importance of the attention design itself. | We added a concise architecture-sensitivity explanation tied to the key configuration choices. |

### reviewer_1_thread_004

- Original thread: The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.
- Normalized summary: Request justification of architectural hyperparameters.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | L1 sections/architecture.tex::Model Configuration::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design., L2 sections/results.tex::Model Variations::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them. | sections/architecture.tex::Model Configuration::paragraph 1 | The default setting uses six layers, eight heads, and a 512-dimensional model state for the base model because this regime balanced accuracy and efficiency well in our development runs. | We now justify the reported head count, depth, and width using the restored variation evidence. |

### reviewer_1_thread_005

- Original thread: The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.
- Normalized summary: Request causal explanation for baseline gains.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_004 | Explain the mechanism behind the baseline gain in the main results. | L1 sections/results.tex::Machine Translation::paragraph 2 / v2=The attention-only encoder-decoder appears to benefit from short cross-token path lengths, which helps preserve long-range dependencies without recurrent state propagation. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage. | sections/results.tex::Machine Translation::paragraph 3 | The attention-only encoder-decoder appears to benefit from short cross-token path lengths, which helps preserve long-range dependencies without recurrent state propagation. | We strengthened the main-results discussion with a mechanism-based explanation of the baseline gain. |

## reviewer_2

### reviewer_2_thread_001

- Original thread: The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.
- Normalized summary: Clarify data usage and evaluation protocol.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_005 | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | L1 sections/training.tex::Data::paragraph 1 / v2=English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary., L2 sections/training.tex::Implementation Notes::paragraph 1 / v2=English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French. | sections/training.tex::Data::paragraph 1 | English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. | We restored the data, preprocessing, and evaluation protocol details needed for replication. |

### reviewer_2_thread_002

- Original thread: Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.
- Normalized summary: Clarify checkpoint averaging and decoding settings.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_005 | Restore reproducibility-critical data, preprocessing, checkpoint averaging, and decoding details. | L1 sections/training.tex::Data::paragraph 1 / v2=English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary., L2 sections/training.tex::Implementation Notes::paragraph 1 / v2=English-German uses approximately 4.5M sentence pairs after standard cleaning and shared byte-pair encoding with a vocabulary of roughly 37k tokens. English-French uses approximately 36M sentence pairs with a 32k word-piece vocabulary. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly. | sections/training.tex::Implementation Notes::paragraph 1 | The base model is reported after averaging the final 5 checkpoints written at 10-minute intervals, while the big model averages the final 20 checkpoints. During inference we use beam size 4, length penalty 0.6, and a maximum output length of input length plus 50 with early stopping when possible. | We made checkpoint averaging and decoding settings explicit in the training section. |

### reviewer_2_thread_003

- Original thread: The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.
- Normalized summary: Clarify training-cost accounting and fairness caveat.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_006 | Clarify training-cost accounting and fairness caveats in the efficiency claim. | L1 sections/results.tex::Machine Translation::paragraph 1 / v2=The larger model achieves a new state of the art on English-to-German and remains highly competitive on English-to-French while requiring substantially less reported training cost than earlier recurrent or convolutional systems under the stated accounting convention., L2 sections/conclusion.tex::Conclusion::paragraph 2 / v2=The larger model achieves a new state of the art on English-to-German and remains highly competitive on English-to-French while requiring substantially less reported training cost than earlier recurrent or convolutional systems under the stated accounting convention. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines. | sections/results.tex::Machine Translation::paragraph 1 | The larger model achieves a new state of the art on English-to-German and remains highly competitive on English-to-French while requiring substantially less reported training cost than earlier recurrent or convolutional systems under the stated accounting convention. | We qualified the efficiency claim and tied it to a stated hardware and FLOPs accounting convention. |

### reviewer_2_thread_004

- Original thread: The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.
- Normalized summary: Repeat the request for architecture sensitivity evidence.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_003 | Justify architecture sensitivity, including heads, dimensions, and model-scale effects. | L1 sections/architecture.tex::Model Configuration::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design., L2 sections/results.tex::Model Variations::paragraph 1 / v2=Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study. | sections/results.tex::Model Variations::paragraph 1 | Single-head attention underperformed the default multi-head setting, removing dropout reduced generalization quality, and scaling the model improved BLEU without eliminating the contribution of the attention design. | We added the requested sensitivity analysis and used it to separate architecture effects from pure model scale. |

### reviewer_2_thread_005

- Original thread: Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.
- Normalized summary: Request stability or variance support beyond headline BLEU.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_007 | Add stability or variance evidence beyond headline BLEU. | L1 sections/results.tex::Stability Statement::paragraph 1 / v2=The supplemental five-run evidence shows a narrow spread around the main result. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs. | sections/results.tex::Stability Statement::paragraph 1 | The supplemental five-run evidence shows a narrow spread around the main result. | We added a conservative stability statement rather than overclaiming a full robustness study. |

## reviewer_3

### reviewer_3_thread_001

- Original thread: The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.
- Normalized summary: Expand limitations and failure-mode discussion.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | L1 sections/discussion.tex::Discussion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems., L2 sections/conclusion.tex::Conclusion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice. | sections/discussion.tex::paragraph 2-4 | The current results are tied to WMT 2014 machine translation and do not by themselves establish that self-attention is universally preferable for every sequence task. | We expanded the limitations section to make the scope boundaries and deployment caveats explicit. |

### reviewer_3_thread_002

- Original thread: The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.
- Normalized summary: Request a concrete attention case study.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_009 | Add an interpretability case study with qualitative attention evidence. | L1 sections/results.tex::Interpretability::paragraph 1 / v2=In one long English-German sentence, an upper-layer head links a subordinate-clause introducer to the postponed main verb, while another head tracks a named entity span across punctuation boundaries., L2 sections/discussion.tex::Discussion::paragraph 4 / v2=In one long English-German sentence, an upper-layer head links a subordinate-clause introducer to the postponed main verb, while another head tracks a named entity span across punctuation boundaries. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help. | sections/results.tex::Interpretability::paragraph 1 | In one long English-German sentence, an upper-layer head links a subordinate-clause introducer to the postponed main verb, while another head tracks a named entity span across punctuation boundaries. | We added a concrete qualitative attention case study to support the interpretability claim. |

### reviewer_3_thread_003

- Original thread: Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.
- Normalized summary: Request explicit failure buckets.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | L1 sections/discussion.tex::Discussion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems., L2 sections/conclusion.tex::Conclusion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena. | sections/discussion.tex::paragraph 3 | Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. | We now name representative failure buckets instead of leaving the discussion purely positive. |

### reviewer_3_thread_004

- Original thread: The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.
- Normalized summary: Request a concrete long-range dependency example.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | merged_duplicate | atomic_001 | Explain why attention-only can replace recurrence and convolution in this translation setting. | L1 sections/introduction.tex::Introduction::paragraph 3 / v2=Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks., L2 sections/results.tex::Machine Translation::paragraph 2 / v2=Self-attention gives every token a short path to every other token, so long-range dependencies can be modeled without recurrent state propagation or deep convolutional stacks. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim. | sections/introduction.tex::paragraph 3; sections/results.tex::Interpretability::paragraph 1 | Self-attention gives every token a short path to every other token, and the qualitative case study shows how an upper-layer head preserves a long-distance clause relation in practice. | We paired the high-level intuition with a concrete long-range dependency example. |

### reviewer_3_thread_005

- Original thread: The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.
- Normalized summary: Temper the conclusion and scope claims.
- Final row ready: yes

| Response Order | Role | `comment_id` | Canonical Summary | Selected Manuscript Copy Summary |
| --- | --- | --- | --- | --- |
| 1 | primary | atomic_008 | Expand limitations, failure buckets, and scope boundaries. | L1 sections/discussion.tex::Discussion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems., L2 sections/conclusion.tex::Conclusion::paragraph 2 / v2=Rare words, long subordinate-clause constructions, and some coverage-sensitive cases still account for a meaningful share of residual errors, even though aggregate BLEU improves over prior systems. |

#### Final Row Preview

| 原始意见 | 修改位置/范围 | 关键修改片段 | 回复说明 |
| --- | --- | --- | --- |
| The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats. | sections/conclusion.tex::paragraph 2 | Claims beyond that scope should be made cautiously: the present evidence is strongest for the benchmark tasks studied here, and broader modality or sequence-length generalization remains future work. | We tempered the conclusion so it stays within the evidence presented here. |

