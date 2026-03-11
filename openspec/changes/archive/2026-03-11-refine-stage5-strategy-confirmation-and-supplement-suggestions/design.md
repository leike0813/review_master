## Context

The current Stage 5 runtime already stores:

- strategy stance and actions
- evidence items
- per-comment pending confirmations
- manuscript and response drafts
- supplement intake decisions and landing mappings

What it does not yet do is treat “user strategy confirmed” as a real hard gate between the strategy card and the draft layer. It also lacks a separate truth model for supplement requests that exist before any supplement files are submitted.

## Decisions

### Decision 1: Stage 5 becomes a strict two-step loop

- Step 1: author or revise the strategy card
- Step 2: request and receive explicit user confirmation
- Step 3: only then author Stage 5 drafts

The runtime keeps using the generic `workflow_pending_user_confirmations` gate. We do not add a new Stage 5-specific action id for confirmation.

### Decision 2: Strategy edits invalidate downstream draft truth

Any write that changes strategy semantics must:

- reset `user_strategy_confirmed` to `no`
- clear Stage 5 draft truth for that comment
- rebuild pending confirmations

This prevents stale drafts from surviving after the user changes the plan.

### Decision 3: Supplement suggestions are a separate Stage 5 artifact and truth model

`supplement-intake-plan.md` remains file-intake oriented.

A new artifact, `supplement-suggestion-plan.md`, is added for the pre-intake backlog. It is backed by:

- `supplement_suggestion_items`
- `supplement_suggestion_intake_links`

The first Stage 5 pass must create at least one suggestion item for each Stage 4-confirmed evidence-gap comment. Later supplement rounds may link uploaded files back to those suggestion items.

### Decision 4: The strategy card becomes phase-aware

Before confirmation, the strategy card must emphasize:

- what the proposed strategy is
- what the user may correct
- that drafts are not yet authored

After confirmation, the same card may render the manuscript and response draft truth.

## Risks / Trade-offs

- More Stage 5 state transitions and validation rules
  - Accepted, because silent strategy execution is riskier than extra explicit state
- New supplement suggestion truth overlaps conceptually with evidence items
  - Accepted, because Stage 4 evidence-gap backlog and Stage 5 file-intake rounds are not the same concern
- Existing sample workspaces may already contain strategy drafts before confirmation
  - Mitigation: refresh example workspaces and regression tests to reflect the confirmation-first contract

## Migration Notes

- `enter_stage_5` still selects an active comment, but the next meaningful work becomes strategy authoring plus supplement suggestion seeding
- `request_pending_confirmation` now blocks Stage 5 whenever the active strategy is still unconfirmed
- `author_comment_drafts` becomes the post-confirmation authoring step
- supplement intake continues to use `supplement_intake_items` and `supplement_landing_links`, but those records can now be traced back to suggestion rows
