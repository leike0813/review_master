# review-master-helper-script-cli-contracts Delta

## MODIFIED Requirements

### Requirement: Helper scripts use a uniform runtime contract

Stage 6 revision capture helpers MUST keep the standard JSON stdout contract while accepting Agent-authored semantic log payloads.

#### Scenario: commit revision round writes Agent-authored semantic logs

- **WHEN** `commit_revision_round.py` is called with `--artifact-root` and `--payload`
- **THEN** it MUST pass the payload to `capture_revision_action.py`
- **AND** `capture_revision_action.py` MUST write `revision_action_logs`, revision log links, `revision_action_log_entries`, and any requested plan action status updates
- **AND** neither script MUST scan `working_manuscript`, compare `source_snapshot`, or generate file diffs
- **AND** `commit_revision_round.py` MUST run `gate-and-render` after the semantic log write succeeds
