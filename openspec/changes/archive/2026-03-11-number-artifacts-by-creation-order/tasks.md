## 1. Runtime Naming Contract

- [x] 1.1 Rename all non-strategy-card runtime artifact path constants to the numbered filenames.
- [x] 1.2 Update the render manifest and any helper-script output references so numbered filenames are the canonical rendered outputs.
- [x] 1.3 Keep `response-strategy-cards/{comment_id}.md` unchanged while verifying no other artifact family remains unnumbered.

## 2. Gate, Docs, and Workspace Migration

- [x] 2.1 Update gate-and-render presence reports, action payloads, repair hints, and artifact references to use numbered filenames.
- [x] 2.2 Update `SKILL.md`, runtime digest, and workflow/reference docs so they cite the numbered artifacts consistently.
- [x] 2.3 Ensure rerendered workspaces converge on the numbered artifact set and do not keep stale unnumbered views as the normative outputs.

## 3. Fixtures and Validation

- [x] 3.1 Regenerate playbook workspaces and snapshots to the numbered filenames.
- [x] 3.2 Update regression tests to assert the numbered artifact names and preserve the strategy-card exception.
- [x] 3.3 Run targeted validation: `pytest`, `mypy`, and `openspec validate number-artifacts-by-creation-order --type change --strict`.
