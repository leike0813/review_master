# Round 3 Supplement: Attention Case Study

This qualitative note supports the interpretability claim that was left underdeveloped in the draft.

## Case

For a long English-German sentence with a subordinate clause, one head in the upper encoder layers concentrates on the dependency between the clause introducer and the postponed main verb, while another head tracks a named entity span across punctuation boundaries.

## Why it matters

- It gives a concrete example of long-range information flow instead of relying only on intuition.
- It supports the weaker, defensible version of the interpretability claim: attention patterns can provide analyzable signals, even if they are not a complete explanation of model behavior.
- It offers a manuscript-ready bridge between the theory section and the discussion of sequence length advantages.

## Suggested manuscript use

Add a short paragraph in Results or Discussion and refer to the accompanying illustrative figure.
