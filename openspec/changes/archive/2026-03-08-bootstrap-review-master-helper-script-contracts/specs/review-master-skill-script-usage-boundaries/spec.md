## ADDED Requirements

### Requirement: SKILL.md documents helper-script boundaries
`review-master/SKILL.md` MUST explicitly state that helper scripts are optional deterministic aids rather than mandatory dependencies.

#### Scenario: Helper script remains optional
- **WHEN** `SKILL.md` introduces helper scripts
- **THEN** it still allows the workflow to proceed manually if those scripts are unavailable

### Requirement: SKILL.md maps scripts to stage usage
`review-master/SKILL.md` MUST identify where the first helper scripts may be used:

- `detect_main_tex.py` for stage 1 entry analysis
- `validate_artifact_consistency.py` for stage 4 artifact-package validation

It MAY also allow `validate_artifact_consistency.py` to be rerun before final export as a read-only preflight check.

#### Scenario: Stage-level script guidance is explicit
- **WHEN** a user or agent reads the stage instructions in `SKILL.md`
- **THEN** the document makes clear which helper script belongs to which stage and why

### Requirement: SKILL.md defines atomization rules directly
`review-master/SKILL.md` MUST define how to decompose free-form review comments into atomic items without delegating that decision to a helper script.

At minimum, the stage-three instructions MUST explain:

- what counts as an atomic review comment
- when one compound review block must be split
- when supporting explanation should stay attached to the same atomic item
- how editor comments and reviewer comments are represented
- how `Original Comment Excerpt` and `Required Action` are written
- how the agent self-checks the atomization result

#### Scenario: Atomization remains an LLM task
- **WHEN** the workflow reaches stage 3
- **THEN** `SKILL.md` instructs the agent to perform atomization as a semantic judgment task
- **AND** does not require a helper script to produce atomic items

### Requirement: Script outputs cannot bypass user confirmation
`review-master/SKILL.md` MUST state that helper-script outputs cannot replace user confirmation, strategy approval, or final academic judgment.

#### Scenario: Script result stays subordinate to workflow gates
- **WHEN** a helper script returns a candidate list or validation report
- **THEN** the workflow still enforces the existing stage gates and user confirmations before progressing
