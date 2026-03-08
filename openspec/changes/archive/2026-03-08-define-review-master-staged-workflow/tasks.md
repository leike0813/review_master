## 1. OpenSpec Artifacts

- [ ] 1.1 Update `review-master/SKILL.md` to replace the current generic four-stage outline with the first-release six-stage workflow.
- [ ] 1.2 Add explicit input and output sections to `review-master/SKILL.md` for `manuscript_source`, `review_comments_source`, `revised_manuscript`, and `response_letter_path`.
- [ ] 1.3 Add mandatory user checkpoint rules to `review-master/SKILL.md`, including entry confirmation, revision-board confirmation, per-comment confirmation, evidence supplementation, and final review.

## 2. Workflow Documentation and Intermediate Artifacts

- [ ] 2.1 Define how the manuscript structure summary, atomic comment list, mapping table, revision board, per-comment strategy cards, and final assembly checklist are represented in the skill documentation or bundled references.
- [ ] 2.2 Document the stage transition gates so the workflow cannot skip directly from early analysis to final export.
- [ ] 2.3 Document the per-comment closed-loop cycle and the blocked state for evidence gaps.

## 3. Supporting Assets and Safety Boundaries

- [ ] 3.1 Decide whether stage-1 and stage-3 helper scripts are needed for entry inspection and comment atomization, and document their responsibilities if introduced.
- [ ] 3.2 Define the working-copy policy for LaTeX project directories so the original manuscript source is never modified in place.
- [ ] 3.3 Ensure the response letter remains Markdown-first in the first release and document any future export formats as out of scope.

## 4. Validation

- [ ] 4.1 Verify the new change remains complete and valid with `openspec validate define-review-master-staged-workflow --type change --strict`.
- [ ] 4.2 Review the specs against the project constraints in `AGENTS.md` to confirm they preserve staged execution, user-owned decisions, and the prohibition on one-shot manuscript rewriting.
