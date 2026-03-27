## MODIFIED Requirements

### Requirement: DB-first runtime workspace

The SQLite runtime MUST model Stage 6 around workspace manuscript copies, revision plan actions, revision action logs, file-level diff traces, and working-copy audit state instead of patch-driven export truth.

#### Scenario: revision audit truth is first-class runtime state

- **WHEN** the runtime schema initializes or upgrades
- **THEN** it must include tables for manuscript copies, revision plan actions, revision action logs, revision-action links, file diff excerpts, and working-copy file state
- **AND** these tables must be sufficient for Stage 6 closure without `action_copy_variants`, `selected_action_copy_variants`, `export_patch_sets`, or `export_patches`
