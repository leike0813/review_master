# Tasks

- [x] Add the new OpenSpec change artifacts for Stage 3 instruction refinement.
- [x] Expand `review-master/SKILL.md` so Stage 3 is described at handbook-summary level and points to the detailed stage doc.
- [x] Rewrite `review-master/references/stage-3-comment-atomization.md` as an operations-manual style document.
- [x] Update `review-master/references/sql-write-recipes.md` so `recipe_stage3_replace_threaded_atomic_model` is detailed enough to support the Stage 3 doc.
- [x] Update `review-master/references/workflow-state-machine.md` so Stage 3 allowed actions, block conditions, and recommended transitions align with the refined instructions.
- [x] Update `review-master/references/helper-scripts.md` so Stage 3 explicitly states there is no semantic helper script and `gate-and-render` remains post-write only.
- [x] Lightly update the happy-path playbook so Stage 3 clearly shows what the Agent reads, how the split is decided, and why the workflow can advance.
- [x] Run `openspec validate refine-review-master-stage-3-threaded-atomization --type change --strict`.
