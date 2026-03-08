# Round 3 Supplement: Limitations and Boundaries

The draft's discussion section was intentionally too confident. A more realistic revised discussion should acknowledge:

- The reported results are for machine translation on WMT 2014 and do not automatically justify broad claims about every sequence task.
- Self-attention offers short path lengths, but its quadratic cost in sequence length can become problematic for very long inputs.
- Rare-word handling and some long-sentence reordering cases remain failure points even when aggregate BLEU improves.
- Training-cost comparisons depend on a specific accounting convention and hardware setting.
- Interpretability claims should be framed as illustrative rather than definitive.

These points are suitable both for manuscript revision and for the response letter when reviewer concerns shift from correctness to scope discipline.
