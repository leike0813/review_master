# Tasks

- [x] Add the new OpenSpec change artifacts for Stage 4 instruction refinement.
- [x] Expand `review-master/SKILL.md` so Stage 4 is described at handbook-summary level and points to the detailed stage doc.
- [x] Rewrite `review-master/references/stage-4-workboard-planning.md` as an operations-manual style document.
- [x] Update `review-master/references/sql-write-recipes.md` so `recipe_stage4_upsert_atomic_workboard` and `recipe_stage4_set_pending_confirmations` are detailed enough to support the Stage 4 doc.
- [x] Update `review-master/references/workflow-state-machine.md` so Stage 4 allowed actions, block conditions, default confirmation gating, and transition rules align with the refined instructions.
- [x] Update `review-master/references/helper-scripts.md` so Stage 4 explicitly states there is no semantic helper script and `gate-and-render` remains post-write only.
- [x] Lightly update the happy-path playbook so Stage 4 clearly shows provisional planning, default confirmation, and why the workflow can advance only after confirmation.
- [x] Run `openspec validate refine-review-master-stage-4-atomic-workboard-planning --type change --strict`.
