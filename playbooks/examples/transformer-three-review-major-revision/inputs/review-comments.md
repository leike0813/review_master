# Reviewer 1

1. The paper claims that attention alone can replace recurrent and convolutional structure, but the abstract and introduction do not clearly explain why this should work beyond improved parallelism.
2. The positioning against ByteNet, ConvS2S, and memory-network style models is too compressed. Please clarify what is genuinely new here and what is inherited from prior attention-based work.
3. The architecture section would benefit from a controlled component analysis. At present it is hard to tell how much of the gain comes from multi-head attention, positional encoding, or simply model scale.
4. The choice of six layers, eight heads, and the reported hidden dimensions appears ad hoc. Please justify these design choices or provide evidence that the conclusions are not overly sensitive to them.
5. The main-results discussion implies a mechanism-based advantage over baselines, but the current manuscript does not provide a convincing causal explanation for that advantage.

# Reviewer 2

1. The training-data description is too brief for replication. Please clarify the exact WMT data usage, preprocessing assumptions, and the evaluation protocol for English-German and English-French.
2. Important reproducibility details are missing, including checkpoint averaging, decoding configuration, and other model-selection choices. These should be stated explicitly.
3. The training-cost claim is interesting but currently underspecified. Please report a clearer accounting of hardware, FLOPs, and what makes the comparison fair across baselines.
4. The manuscript lacks a convincing analysis of which architectural components matter most. This overlaps with the need for a stronger ablation or sensitivity study.
5. Only headline BLEU numbers are shown. Please add some indication of stability, variance, or at least a more careful statement of what can and cannot be concluded from single reported runs.

# Reviewer 3

1. The discussion of limitations is too brief. The manuscript should be more explicit about failure modes, scope boundaries, and settings in which self-attention may not be the best choice.
2. The claim that attention may yield interpretability is not supported by concrete qualitative evidence. A short case study or visualization would help.
3. Please provide more analysis of where the model still struggles, for example on long sentences, rare tokens, or specific translation phenomena.
4. The intuition for why long-range dependencies are easier to capture remains somewhat rhetorical. Please add a more concrete analysis or example to support this claim.
5. The conclusion over-generalizes the impact of the method beyond the tasks studied here. Please temper the claims or add clearer caveats.
