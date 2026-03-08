## 1. OpenSpec Artifacts

- [x] 1.1 Revise `openspec/changes/bootstrap-review-master-helper-script-contracts/proposal.md`.
- [x] 1.2 Revise `openspec/changes/bootstrap-review-master-helper-script-contracts/design.md`.
- [x] 1.3 Revise `openspec/changes/bootstrap-review-master-helper-script-contracts/specs/review-master-readonly-helper-scripts/spec.md`.
- [x] 1.4 Revise `openspec/changes/bootstrap-review-master-helper-script-contracts/specs/review-master-helper-script-cli-contracts/spec.md`.
- [x] 1.5 Revise `openspec/changes/bootstrap-review-master-helper-script-contracts/specs/review-master-skill-script-usage-boundaries/spec.md`.

## 2. References and Scripts

- [x] 2.1 Revise `review-master/references/helper-scripts.md`.
- [x] 2.2 Add `review-master/scripts/detect_main_tex.py`.
- [x] 2.3 Remove `review-master/scripts/atomize_review_comments.py` from the published helper-script surface.
- [x] 2.4 Expand `review-master/scripts/validate_artifact_consistency.py` into a unified artifact-package validator.

## 3. SKILL.md Sync

- [x] 3.1 Update `review-master/SKILL.md` to move comment atomization rules into the stage-three instructions.
- [x] 3.2 Update `review-master/SKILL.md` to map helper scripts only to stage 1 and unified validation checkpoints.
- [x] 3.3 Update `review-master/SKILL.md` to require manual fallback when a helper script is missing or fails.

## 4. Validation

- [x] 4.1 Validate the revised change with `openspec validate bootstrap-review-master-helper-script-contracts --type change --strict`.
- [x] 4.2 Verify the remaining helper scripts expose `--help`.
- [x] 4.3 Verify the unified validator can report artifact presence, format errors, dependency errors, and consistency errors from `--artifact-root`.
