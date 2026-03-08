# Round 1 Supplement: Method Positioning and Mechanism Note

This note restores the argument that was intentionally compressed in the draft.

## Why attention can replace recurrence in this setting

The key point is not only parallelism. Self-attention shortens the path length between any two positions to a constant number of learned operations, which makes it easier to move information across long input sequences than strictly sequential recurrence. The model also avoids the optimization bottleneck imposed by time-step-wise hidden-state updates.

## How this differs from prior efficient sequence models

- ByteNet and ConvS2S reduce sequential dependence through convolution, but still rely on locality or stacked receptive fields.
- Memory-network style models use attention, but not as the sole sequence transduction backbone.
- The intended novelty claim is therefore narrower than “attention exists”: it is that a strong encoder-decoder translation model can be built from self-attention and feed-forward blocks alone, while remaining competitive on large benchmarks.

## Author-side instruction

Use this note to strengthen the abstract, introduction, and background positioning without overstating the novelty boundary.
