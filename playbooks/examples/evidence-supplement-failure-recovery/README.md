# Evidence Supplement Failure Recovery

This example is derived from `playbooks/examples/evidence-supplement-multi-review/`.

It demonstrates a Stage 5 failure-and-recovery arc:

- the first supplement round provides files that look relevant but do not actually answer the reviewer concern
- the workflow remains blocked because the evidence gap is still semantic, not structural
- a second supplement round introduces the correct repeated-run stability evidence
- the case then recovers and reaches `stage_6_completed`

This directory contains complete runtime replay assets:

- `inputs/`
- `user-supplements/round-1-bad/`
- `user-supplements/round-2-good/`
- `workspace/`
- `outputs/`
- `gate-and-render-output/`
