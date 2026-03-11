## Why

Stage 5 currently lets the runtime move from “strategy card exists” straight toward completion-oriented actions, even when the user has not explicitly confirmed that strategy yet. The docs say confirmation must happen before execution, but the gate logic still treats a freshly authored strategy card as close enough to proceed.

Stage 5 also has only one supplement-facing artifact today: `supplement-intake-plan.md`. That view is useful after the user uploads materials and the Agent has already accepted or rejected them, but it does not give the user an upfront backlog of evidence-gap-driven material requests when Stage 5 begins.

## What Changes

- Make Stage 5 confirmation-first in both docs and runtime:
  - strategy card first
  - explicit confirmation gate second
  - Stage 5 drafts only after confirmation
- Add a new global Stage 5 read-only artifact:
  - `supplement-suggestion-plan.md`
- Add supplement suggestion truth tables:
  - `supplement_suggestion_items`
  - `supplement_suggestion_intake_links`
- Add Stage 5 recipes for:
  - strategy confirmation clearing
  - combined Stage 5 draft writing
- Update gate/render, templates, localization, docs, and tests so the new Stage 5 loop is enforced end to end

## Capabilities

### Modified Capabilities

- `review-master-sqlite-runtime`
- `review-master-template-driven-rendering`
- `review-master-stage-5-strategy-card-instructions`
- `review-master-stage-5-confirmation-blocker-completion-instructions`
- `review-master-supplement-intake-and-landing`
- `review-master-user-checkpoints`
- `review-master-workflow-state-machine-rules`
- `review-master-validator-instruction-payload`
- `review-master-markdown-artifact-contract`
- `review-master-staged-workflow`
- `review-master-skill-instructions`

## Impact

- Affects runtime schema, render manifest, Stage 5 gate ordering, action payloads, strategy-card rendering, and localization messages
- Affects `SKILL.md`, runtime digest, Stage 5 guide, SQL recipes, and workflow-state-machine docs
- Adds new OpenSpec artifacts and Stage 5 regression tests for confirmation-first gating and supplement suggestion traceability
