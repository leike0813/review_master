## Why

`review-master` now exposes a larger set of read-only runtime artifacts, but their filenames do not encode the canonical workflow order. Users must infer sequence from documentation or stage context, which becomes harder as new views are added. Numbering the non-strategy-card artifacts by creation order makes the workspace easier to scan and reduces ambiguity when the gate, docs, and user refer to artifacts by name.

## What Changes

- **BREAKING** Rename every non-strategy-card runtime artifact to use a stable numeric prefix that reflects canonical creation order.
- Keep `response-strategy-cards/{comment_id}.md` unchanged so comment-scoped card paths remain stable.
- Require render outputs, workspace layout, `SKILL.md`, and gate-facing artifact references to use the numbered filenames as the canonical contract.
- Define migration expectations for existing playbooks and legacy workspaces so old unnumbered files do not remain the normative reference after rerender.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `review-master-artifact-workspace-layout`: The fixed runtime workspace layout changes from unnumbered filenames to numbered canonical artifact filenames.
- `review-master-template-driven-rendering`: Runtime rendering must emit numbered artifact paths and treat them as the only canonical rendered filenames, except for strategy cards.
- `review-master-markdown-artifact-contract`: `SKILL.md` must describe the Markdown artifact set using the numbered filenames and preserve the strategy-card exception.
- `review-master-skill-instructions`: Stage instructions in `SKILL.md` must reference the numbered artifacts consistently when describing workflow outputs and user review steps.

## Impact

- Affected code: `review-master/scripts/workspace_db.py`, `review-master/scripts/gate_and_render_workspace.py`, render manifest/template wiring, and any path constants.
- Affected docs: `review-master/SKILL.md`, runtime digest, workflow references, helper-script guidance, and any artifact lists.
- Affected fixtures: playbook example workspaces, gate snapshots, and regression tests that assert artifact names.
- Breaking surface: artifact filenames in runtime workspaces and any human-facing instructions or tests that mention them.
