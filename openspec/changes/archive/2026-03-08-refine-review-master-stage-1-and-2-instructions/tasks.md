# Tasks

- [x] Add the new OpenSpec change artifacts for Stage 1 and Stage 2 instruction refinement.
- [x] Expand `review-master/SKILL.md` so Stage 1 and Stage 2 are described at handbook-summary level and point to the detailed stage docs.
- [x] Rewrite `review-master/references/stage-1-entry-and-bootstrap.md` as an operations-manual style document.
- [x] Rewrite `review-master/references/stage-2-manuscript-analysis.md` as an operations-manual style document.
- [x] Update `review-master/references/sql-write-recipes.md` so `recipe_stage1_set_entry_state` and `recipe_stage2_upsert_manuscript_summary` are detailed enough to support the stage docs.
- [x] Update `review-master/references/workflow-state-machine.md` so Stage 1 and Stage 2 allowed actions, block conditions, and recommended transitions align with the refined instructions.
- [x] Update `review-master/references/helper-scripts.md` so Stage 1 and Stage 2 script invocation timing and fallback rules are explicit.
- [x] Lightly update the happy-path playbook so Stage 1 and Stage 2 clearly show what the Agent reads, writes, asks, and why the workflow can advance.
- [x] Run `openspec validate refine-review-master-stage-1-and-2-instructions --type change --strict`.
