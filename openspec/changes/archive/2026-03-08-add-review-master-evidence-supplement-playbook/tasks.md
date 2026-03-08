## 1. OpenSpec Artifacts

- [x] 1.1 Add `openspec/changes/add-review-master-evidence-supplement-playbook/proposal.md`.
- [x] 1.2 Add `openspec/changes/add-review-master-evidence-supplement-playbook/design.md`.
- [x] 1.3 Add `openspec/changes/add-review-master-evidence-supplement-playbook/specs/review-master-playbook-index/spec.md`.
- [x] 1.4 Add `openspec/changes/add-review-master-evidence-supplement-playbook/specs/review-master-playbook-multi-review-flow/spec.md`.
- [x] 1.5 Add `openspec/changes/add-review-master-evidence-supplement-playbook/specs/review-master-playbook-evidence-supplement-assets/spec.md`.

## 2. Playbooks and Example Assets

- [x] 2.1 Add `playbooks/README.md`.
- [x] 2.2 Add `playbooks/review-master-evidence-supplement-playbook.md`.
- [x] 2.3 Add multi-file manuscript inputs and review comments under `playbooks/examples/evidence-supplement-multi-review/inputs/`.
- [x] 2.4 Add user supplement assets under `playbooks/examples/evidence-supplement-multi-review/user-supplements/`.
- [x] 2.5 Add a final-state runtime workspace with five strategy cards under `playbooks/examples/evidence-supplement-multi-review/workspace/`.
- [x] 2.6 Add revised manuscript outputs and `response-letter.md` under `playbooks/examples/evidence-supplement-multi-review/outputs/`.
- [x] 2.7 Add eight representative validator JSON files under `playbooks/examples/evidence-supplement-multi-review/validator-output/`.

## 3. Validation

- [x] 3.1 Run `openspec validate add-review-master-evidence-supplement-playbook --type change --strict`.
- [x] 3.2 Run `review-master/scripts/validate_artifact_consistency.py` against the new final-state workspace.
- [x] 3.3 Verify the new playbook uses the existing six-stage flow, state machine, and validator output shape.
