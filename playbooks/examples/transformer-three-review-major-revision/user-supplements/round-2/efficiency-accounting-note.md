# Round 2 Supplement: Efficiency Accounting Note

The draft kept the headline “lower training cost” claim but removed the accounting details. The intended restoration is:

- Training cost should be described as an estimate based on training time, GPU count, and sustained single-precision floating-point capacity per GPU.
- Comparisons are strongest when interpreted as benchmark-level efficiency signals, not perfectly standardized hardware-normalized measurements across every published baseline.
- The English-German big model trains for about 3.5 days on 8 P100 GPUs.
- The base model trains in about 12 hours on the same hardware family.

When revising the paper, the claim should be softened to “substantially lower reported training cost under the stated accounting convention,” rather than “universally cheaper in every implementation setting.”
