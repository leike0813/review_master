# Design: refine-review-master-stage-5-strategy-and-execution

## Overview

Stage 5 converts atomic planning into item-by-item execution. The design goal is to remove ambiguity around three transition points:

1. when an item becomes the active item
2. when the strategy is mature enough for user confirmation
3. when the item can be marked complete

This design keeps the runtime model unchanged and only refines instructions.

## Key Decisions

### 1. Per-item confirmation is the default path

Every `active_comment_id` must pass one explicit strategy confirmation before the Agent turns the strategy into manuscript-change and response-paragraph drafts.

Rationale:

- Stage 4 confirms the overall workboard.
- Stage 5 confirmation asks a narrower question: "Do we execute this exact stance and these exact actions for this item?"
- Without this second gate, the Agent could turn a valid workboard into an unapproved local execution plan.

### 2. Completion requires landed drafts

The completion bar for a Stage 5 item is:

- strategy card complete
- evidence judgment complete
- manuscript-change draft exists
- response-paragraph draft exists
- one-to-one linkage checked

Rationale:

- A strategy alone is still a plan.
- Stage 5 is the execution stage, so completion must mean the item has crossed from planning into drafted execution.

### 3. Blockers are explicit and sticky

If `evidence_gap = yes` and required material is not yet available, the Agent must write a blocker and stop completion for the active item.

Rationale:

- Otherwise the Agent would blur "we know what to do" and "we have enough evidence to draft it".
- The blocker model keeps this visible to the user and to future sessions through resume data.

### 4. Active item switching is controlled

`workflow_state.active_comment_id` may only change when one of the following is true:

- the current item is complete
- the current item is blocked and the Agent is explicitly pausing it
- the user has explicitly requested a different processing order

Rationale:

- Silent switching makes Stage 5 non-auditable.
- It weakens the resume protocol because the current focal item becomes unclear.

## Document Strategy

The implementation is doc-first:

- `SKILL.md` holds a compact Stage 5 summary
- `stage-5-strategy-and-execution.md` becomes the main execution handbook
- supporting docs carry exact recipe, gate, and script-boundary wording
- the complex playbook shows one concrete blocked/unblocked Stage 5 loop

## Non-Goals

This change does not:

- define manuscript patch formats
- add draft storage tables
- automate draft generation
- change validator logic
