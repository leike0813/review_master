# Round 2 Supplement: Component Interpretation Note

The draft deliberately removed the model-variation evidence. The recovered interpretation is:

- Multi-head attention matters materially; collapsing to a single head reduces quality enough that the main gain cannot be explained by capacity alone.
- Positional treatment is not arbitrary; learned and sinusoidal variants are close, which supports the claim that explicit order information is required but the exact parameterization is not the only driver.
- Regularization choices affect outcomes noticeably, so the headline results should not be framed as architecture-only wins.
- Larger models help, but the gain from scaling does not erase the importance of the attention design itself.

This note should support responses to both architecture-sensitivity and “is it just a bigger model?” reviewer questions.
