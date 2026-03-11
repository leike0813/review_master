## Context

The runtime workspace currently contains a growing set of read-only artifacts whose filenames are plain semantic labels such as `agent-resume.md` and `atomic-comment-workboard.md`. That was workable when the set was smaller, but it now hides the intended read order and makes it harder for users to connect file lists with workflow stages. The requested change is to number every non-strategy-card artifact by creation order while keeping per-comment strategy card paths unchanged.

This is a cross-cutting rename. It touches fixed workspace layout, render outputs, gate payloads, docs, playbook snapshots, and tests. Because runtime views are regenerated from SQLite truth, the design can prefer a single canonical filename set instead of maintaining indefinite dual naming.

## Goals / Non-Goals

**Goals:**

- Define one stable numbered filename scheme for all non-strategy-card runtime artifacts.
- Preserve `response-strategy-cards/{comment_id}.md` as the only unnumbered runtime artifact family.
- Make numbered filenames the canonical names across render outputs, gate references, docs, and tests.
- Ensure implementation can migrate legacy workspaces cleanly by rerendering the numbered files from DB truth.

**Non-Goals:**

- Renumber strategy cards or replace `comment_id`-based card addressing.
- Introduce dynamic numbering that changes based on optional branches or per-run conditions.
- Change the semantic content of the artifacts themselves beyond filename/path references.
- Preserve unnumbered filenames as a long-term parallel contract.

## Decisions

### 1. Use fixed two-digit prefixes for the canonical runtime order

The change will define one explicit filename mapping:

- `01-agent-resume.md`
- `02-manuscript-structure-summary.md`
- `03-raw-review-thread-list.md`
- `04-atomic-review-comment-list.md`
- `05-thread-to-atomic-mapping.md`
- `06-review-comment-coverage.md`
- `07-atomic-comment-workboard.md`
- `08-style-profile.md`
- `09-action-copy-variants.md`
- `10-response-letter-outline.md`
- `11-export-patch-plan.md`
- `12-response-letter-table-preview.md`
- `13-response-letter-table-preview.tex`
- `14-supplement-suggestion-plan.md`
- `15-supplement-intake-plan.md`
- `16-final-assembly-checklist.md`

Rationale:

- Two digits keep lexical sort aligned with workflow order.
- Stable prefixes are easier to cite in instructions than stage-relative labels.
- The mapping mirrors the canonical workflow introduction order rather than ad hoc UI preference.

Alternative considered:

- Only number artifact titles, not filenames. Rejected because the user explicitly asked to number the artifacts, and title-only numbering would leave workspace scanning and gate references inconsistent.

### 2. Numbering follows canonical creation order, not incidental render timing

Although `gate-and-render` may rerender all views on every pass, the numbering will represent the workflow order in which each artifact becomes meaningful to the operator. This keeps filenames stable even when implementation renders empty placeholders earlier.

Alternative considered:

- Derive numbering from the current render manifest execution order alone. Rejected because implementation order can drift for technical reasons, while the user-facing sequence should remain a workflow contract.

### 3. Strategy cards remain the single explicit exception

`response-strategy-cards/{comment_id}.md` stays unchanged. The card family is indexed by `comment_id`, already supports direct addressing, and would become less usable if prefixed with a shared ordinal that does not help the per-comment navigation problem.

Alternative considered:

- Prefix the strategy-card directory or filenames with a shared ordinal. Rejected because it adds noise without improving comment lookup.

### 4. The implementation should converge on numbered outputs as the sole canonical filenames

The runtime already treats SQLite as truth and Markdown files as derived views. The implementation should therefore emit numbered files as the canonical outputs and update all path constants and gate references accordingly. Legacy unnumbered files may be cleaned up during rerender or fixture refresh, but the contract will not require long-term dual-write behavior.

Alternative considered:

- Keep both numbered and unnumbered files forever. Rejected because it doubles the view surface and makes every path reference ambiguous.

## Risks / Trade-offs

- [Breaking workspace paths] → Update specs first, then implementation constants, then regenerate playbooks and snapshots in the same change.
- [Legacy workspaces may temporarily contain stale unnumbered files] → Require rerender-based migration and clean up obsolete filenames during workspace refresh.
- [Future artifact additions may disturb numbering expectations] → Treat numbering as an explicit contract and append new files at the end rather than renumbering old ones casually.
- [Docs may drift from the new filenames] → Centralize the mapping in runtime constants and update regression tests that assert path names.

## Migration Plan

1. Update the OpenSpec contract so numbered filenames become normative.
2. Rename runtime constants and render-manifest outputs to the numbered filenames.
3. Update gate payloads, docs, helper-script references, and `SKILL.md` to cite only the numbered names.
4. Regenerate playbook workspaces and snapshots so the checked-in artifacts match the new contract.
5. Remove or ignore stale unnumbered runtime views during rerender so workspace listings are not duplicated.

Rollback strategy:

- Revert the change before archive if downstream references prove too broad; there is no reason to keep a half-numbered contract.

## Open Questions

- None. The user already confirmed that filenames, not only titles, should be numbered and that strategy cards are excluded.
