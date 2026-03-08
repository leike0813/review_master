# Change Proposal: refine-review-master-stage-6-final-review-and-export

## Why

The current Stage 6 still reflects an older, simplified model:

- it jumps too quickly from thread-level mapping to final export
- it only treats Response Letter as a Markdown output
- it does not model style analysis, anti-AI polishing, or copy selection
- it does not separate marked manuscript export from final clean export

Stage 6 needs to become a real drafting-and-export stage rather than a thin closing step.

## What Changes

- Add a new OpenSpec change for handbook-grade Stage 6 guidance.
- Expand `review-master/SKILL.md` with a stronger Stage 6 summary.
- Rewrite `review-master/references/stage-6-final-review-and-export.md` as the Stage 6 execution handbook.
- Extend the runtime schema and rendered views so Stage 6 can persist:
  - global style profiles
  - per-action copy variants
  - selected variants
  - final thread-level response rows
  - export artifact states
- Refine Stage 6 sections in:
  - `review-master/references/sql-write-recipes.md`
  - `review-master/references/workflow-state-machine.md`
  - `review-master/references/helper-scripts.md`
- Update templates, runtime digest, and the evidence-supplement playbook so Stage 6 clearly shows:
  - style profile generation
  - three variants per action
  - user selection of final wording
  - thread-level point-to-point response rows
  - marked manuscript export before final clean export

## Scope

This change updates:

- documentation
- schema contract
- rendered-view contract
- Stage 6 gate-and-render guidance
- playbook assets

It does not:

- add a new semantic script
- replace `gate_and_render_workspace.py`
- change the six-stage workflow into a different workflow

## Default Decisions

- Stage 6 is split into five substeps: style profile, copy variants, row assembly, marked export, final export.
- Style analysis uses a **global style profile** instead of section-level profiles.
- Copy variants are generated at **strategy action** granularity.
- Final Response Letter output must exist in **Markdown and LaTeX**.
- Final Response Letter uses a fixed **4-column point-to-point table**.
- `changes` is the only standard path for the marked manuscript export.
- Final exports must be written to a separate output location and must not overwrite the original input files.
