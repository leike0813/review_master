## 1. OpenSpec Artifacts

- [x] 1.1 Add `openspec/changes/define-review-master-state-machine-instruction-loop/proposal.md`.
- [x] 1.2 Add `openspec/changes/define-review-master-state-machine-instruction-loop/design.md`.
- [x] 1.3 Add `openspec/changes/define-review-master-state-machine-instruction-loop/specs/review-master-workflow-state-machine-rules/spec.md`.
- [x] 1.4 Add `openspec/changes/define-review-master-state-machine-instruction-loop/specs/review-master-validator-instruction-payload/spec.md`.
- [x] 1.5 Add `openspec/changes/define-review-master-state-machine-instruction-loop/specs/review-master-upstream-first-repair-order/spec.md`.
- [x] 1.6 Add `openspec/changes/define-review-master-state-machine-instruction-loop/specs/review-master-skill-validation-loop/spec.md`.

## 2. References and Instructions

- [x] 2.1 Add `review-master/references/workflow-state-machine.md`.
- [x] 2.2 Update `review-master/references/workflow-state.md` to cross-reference the state-machine rules.
- [x] 2.3 Update `review-master/references/helper-scripts.md` to document `instruction_payload`.
- [x] 2.4 Update `review-master/SKILL.md` to require the validator-driven execution loop.

## 3. Validator

- [x] 3.1 Extend `review-master/scripts/validate_artifact_consistency.py` to emit `instruction_payload`.
- [x] 3.2 Add upstream-first repair sequencing.
- [x] 3.3 Add stage-aware allowed, recommended, and blocked actions.

## 4. Validation

- [x] 4.1 Run `openspec validate define-review-master-state-machine-instruction-loop --type change --strict`.
- [x] 4.2 Run `mypy` on `review-master/scripts/validate_artifact_consistency.py`.
- [x] 4.3 Verify `stage_1 + ready + no issues` recommends entering stage two.
- [x] 4.4 Verify `stage_3 + atomic list format error` recommends repairing the atomic list first.
- [x] 4.5 Verify `stage_4 + pending_user_confirmations` blocks phase-five execution.
- [x] 4.6 Verify `stage_5 + active_comment_id + missing strategy card` prioritizes the matching strategy card in `repair_sequence`.
- [x] 4.7 Verify `stage_6 + export gates unmet` explicitly blocks final export.
