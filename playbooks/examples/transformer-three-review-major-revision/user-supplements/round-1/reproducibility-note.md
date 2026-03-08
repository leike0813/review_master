# Round 1 Supplement: Reproducibility Note

The draft intentionally omitted several replication details that reviewers are likely to request. The following settings can be added back during revision:

- WMT 2014 English-German uses approximately 4.5M sentence pairs after standard cleaning.
- WMT 2014 English-French uses approximately 36M sentence pairs.
- English-German uses shared byte-pair encoding with a vocabulary of about 37k tokens.
- English-French uses a 32k word-piece vocabulary.
- The base model is reported with checkpoint averaging across the final 5 checkpoints saved at 10-minute intervals.
- The big model is reported with checkpoint averaging across the final 20 checkpoints.
- Beam size is 4 and the length penalty is 0.6.
- Maximum output length is set to input length plus 50 with early termination.

These additions are enough to answer protocol-oriented reviewer concerns without pretending the original draft already contained them.
