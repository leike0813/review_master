# Change Proposal: refine-review-master-stage-5-strategy-and-execution

## Why

Stage 5 is where the skill stops doing global planning and starts executing one canonical atomic item at a time. The current docs still describe this stage too loosely, which creates drift around:

- when `active_comment_id` is allowed to change
- when a strategy is ready for user confirmation
- when an evidence gap becomes a blocker
- when an item is truly complete

This change turns Stage 5 into an operations-manual stage so the Agent can execute it consistently.

## What Changes

- Add a new OpenSpec change for Stage 5 handbook-grade guidance.
- Expand `review-master/SKILL.md` with a stronger Stage 5 summary.
- Rewrite `review-master/references/stage-5-strategy-and-execution.md` as the Stage 5 execution handbook.
- Refine Stage 5 sections in:
  - `review-master/references/sql-write-recipes.md`
  - `review-master/references/workflow-state-machine.md`
  - `review-master/references/helper-scripts.md`
- Update the evidence-supplement playbook so Stage 5 clearly shows:
  - per-item strategy confirmation
  - evidence gap to blocker
  - supplement arrival and blocker release
  - completion only after drafts and one-to-one linkage exist

## Scope

This change only updates documentation and supporting guidance.

It does not:

- change database schema
- add new scripts
- change `gate_and_render_workspace.py`
- change the six-stage workflow

## Default Decisions

- Stage 5 uses **per-item confirmation by default**.
- Stage 4 overall confirmation does not replace Stage 5 local execution confirmation.
- A Stage 5 item is **not complete** when strategy is merely agreed; it is complete only after manuscript-change draft, response-paragraph draft, evidence judgment, and one-to-one linkage are all in place.
- `evidence_gap = yes` without enough material must create a blocker.
