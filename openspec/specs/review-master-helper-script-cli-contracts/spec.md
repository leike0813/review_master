# review-master-helper-script-cli-contracts Specification

## Purpose
TBD - created by archiving change bootstrap-review-master-helper-script-contracts. Update Purpose after archive.
## Requirements
### Requirement: Helper scripts use a uniform runtime contract

Stage 6 revision capture helpers MUST keep the standard JSON stdout contract while accepting Agent-authored semantic log payloads.

#### Scenario: commit revision round writes Agent-authored semantic logs

- **WHEN** `commit_revision_round.py` is called with `--artifact-root` and `--payload`
- **THEN** it MUST pass the payload to `capture_revision_action.py`
- **AND** `capture_revision_action.py` MUST write `revision_action_logs`, revision log links, `revision_action_log_entries`, and any requested plan action status updates
- **AND** neither script MUST scan `working_manuscript`, compare `source_snapshot`, or generate file diffs
- **AND** `commit_revision_round.py` MUST run `gate-and-render` after the semantic log write succeeds

### Requirement: detect_main_tex.py exposes entry-detection fields
`review-master/scripts/detect_main_tex.py` MUST accept `--manuscript-source PATH` and return at least these top-level fields:

- `status`
- `input_kind`
- `main_entry`
- `candidates`
- `warnings`

`input_kind` MUST distinguish `single_tex` from `latex_project`.

#### Scenario: Multi-candidate LaTeX project
- **WHEN** the manuscript source is a LaTeX project directory with multiple plausible main `.tex` candidates
- **THEN** the script returns those candidates
- **AND** does not silently choose one on behalf of the user

### Requirement: validate_artifact_consistency.py validates one artifact package
`review-master/scripts/validate_artifact_consistency.py` MUST accept:

- required `--artifact-root PATH`

It MUST return at least:

- `status`
- `summary`
- `artifact_presence`
- `format_errors`
- `dependency_errors`
- `consistency_errors`

The validator MUST discover artifacts from a single artifact-root layout with these fixed paths:

- `manuscript-structure-summary.md`
- `atomic-review-comment-list.md`
- `comment-manuscript-mapping-table.md`
- `revision-board.md`
- `final-assembly-checklist.md`
- `response-strategy-cards/`

Each response strategy card file under `response-strategy-cards/` MUST be named `{comment_id}.md`.

#### Scenario: Missing artifacts are reported from the artifact root
- **WHEN** one or more expected artifact files are missing under the artifact root
- **THEN** the validator reports them in `artifact_presence`
- **AND** still emits one complete JSON report

#### Scenario: Single-artifact format problems are reported
- **WHEN** a present artifact has missing required fields, unsupported enum values, malformed `target_location`, or a strategy card that violates the single-comment rule
- **THEN** the validator reports those problems in `format_errors`

#### Scenario: Dependency and coverage problems are reported
- **WHEN** later-stage artifacts reference missing `comment_id` values or fail to cover the expected comment set
- **THEN** the validator reports those problems in `dependency_errors`

#### Scenario: Cross-artifact inconsistencies are reported
- **WHEN** the same `comment_id` has conflicting `reviewer_id`, `priority`, `target_location`, or strategy-card filename alignment across artifacts
- **THEN** the validator reports those problems in `consistency_errors`

