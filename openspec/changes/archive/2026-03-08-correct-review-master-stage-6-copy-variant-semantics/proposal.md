# Change Proposal: correct-review-master-stage-6-copy-variant-semantics

## Why

The current Stage 6 still treats copy variants as if both manuscript text and response-side explanation should each have three action-level alternatives. That is not the intended workflow.

The intended contract is:

- Stage 5 already fixes strategy, stance, evidence judgment, and draft direction.
- Stage 6 should only turn those confirmed directions into final wording.
- The three variants in Stage 6 are three alternative **final manuscript copy options** for each strategy-action target location.
- The final Response Letter must not depend on separate response-side action variants. It should be assembled in a single path from:
  - the Stage 5 confirmed strategy and draft boundary
  - the Stage 6 selected manuscript wording
  - the thread-level aggregation model

Without this correction, Stage 6 mixes “scheme variants” with “copy variants”, making the workflow more confusing than intended and adding unnecessary data/model complexity.

## What Changes

- Create a new OpenSpec change for correcting Stage 6 copy-variant semantics.
- Update `review-master/SKILL.md` so Stage 6 explicitly says the three variants are manuscript-final-copy variants only, and that they are generated per target location.
- Update `review-master/references/stage-5-strategy-and-execution.md` so the Stage 5 / Stage 6 boundary is explicit.
- Rewrite `review-master/references/stage-6-final-review-and-export.md` so:
  - Stage 6 variants are manuscript-only
  - response letter is generated through a single thread-level assembly path
- Update `review-master/references/sql-write-recipes.md`, `workflow-state-machine.md`, and `helper-scripts.md` to remove response-side variant semantics.
- Shrink the Stage 6 runtime schema:
  - `action_copy_variants` becomes manuscript-only and location-scoped
  - `selected_action_copy_variants` becomes manuscript-only and location-scoped
- Update templates and runtime rendering so:
  - `action-copy-variants.md` only shows manuscript-side final copy variants
  - `response-letter-outline.md` explains that response rows are assembled from selected manuscript copy plus Stage 5 strategy/draft truth
- Update `workspace_db.py` and `gate_and_render_workspace.py` so Stage 6 validation no longer requires response-side variants.
- Refresh playbooks and sample workspaces so Stage 6 consistently shows:
  - Stage 5 decides the plan
  - Stage 6 decides the final manuscript wording
  - response rows are assembled after manuscript copy selection

## Scope

This change updates:

- Stage 6 documentation
- Stage 6 runtime schema contract
- Stage 6 rendered view semantics
- gate-and-render Stage 6 dependency checks
- playbooks and sample fixtures

It does not:

- add a new semantic script
- replace `gate_and_render_workspace.py`
- change the six-stage workflow into a different workflow

## Default Decisions

- Stage 6 variants are generated per `strategy_card_action` target location.
- The three variants are only for the final manuscript-side wording that can be directly inserted into the revised manuscript.
- Response Letter does not use action-level three-way variant selection.
- `response_thread_rows` remains the thread-level final row truth.
- Final Response Letter still exports in Markdown and LaTeX.
