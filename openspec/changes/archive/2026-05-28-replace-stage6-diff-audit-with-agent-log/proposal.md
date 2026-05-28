# Change: replace-stage6-diff-audit-with-agent-log

## Why

Stage 6 currently treats revision logging as a script-owned diff capture problem. Real paper revision often changes argument structure, evidence framing, response strategy, and multiple manuscript locations at once, so file diffs produce noisy and misleading logs. The snapshot/hash gate also makes completion depend on fragile file-state tracking instead of the actual review-response workflow.

## What Changes

- Replace diff-based Stage 6 audit capture with Agent-authored semantic revision logs.
- Keep `working_manuscript` as the collaborative manuscript, but stop using file diff/hash state as a Stage 6 completion gate.
- Add `revision_action_log_entries` as the main per-log detail table.
- Keep `revision_action_log_file_diffs` and `working_copy_file_state` only as legacy compatibility tables.
- Retain `capture_revision_action.py` and `commit_revision_round.py` as stable CLI entrypoints, but make them accept structured Agent log payloads rather than scanning manuscript files.

## Impact

- Runtime schema, helper scripts, gate-and-render, rendered templates, localization, Stage 6 docs, runtime digest, and tests.
- No automatic migration is provided for old Stage 6 workspaces beyond schema compatibility and legacy-table tolerance.
