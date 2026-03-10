## 1. OpenSpec Artifacts

- [x] 1.1 Add `proposal.md` for supplement intake and landing capability.
- [x] 1.2 Add `design.md` with schema, gate, and rendering decisions.
- [x] 1.3 Add delta spec `specs/review-master-supplement-intake-and-landing/spec.md`.
- [x] 1.4 Add delta spec `specs/review-master-stage-5-confirmation-blocker-completion-instructions/spec.md`.
- [x] 1.5 Add delta spec `specs/review-master-sqlite-runtime/spec.md`.
- [x] 1.6 Add delta spec `specs/review-master-markdown-artifact-contract/spec.md`.

## 2. Runtime Data Model and Rendering

- [x] 2.1 Add supplement intake and landing tables to runtime schema and required table set.
- [x] 2.2 Extend workspace rendering context for supplement intake and landing data.
- [x] 2.3 Add a new workspace template `supplement-intake-plan.md.j2` and register it in render manifest.
- [x] 2.4 Update Stage 5 docs (`SKILL.md`, SQL recipes, supporting guidance) to include supplement intake flow.
- [x] 2.5 Sync `review-master/assets/runtime/skill-runtime-digest.md` with the updated `SKILL.md`.

## 3. Stage 5 Gate and Resume Contract

- [x] 3.1 Add gate checks for missing intake decisions in supplement rounds.
- [x] 3.2 Add gate checks for accepted supplements lacking landing mappings.
- [x] 3.3 Update recommended-next-action hints for blocked/ready-to-resume transitions.

## 4. Validation and Examples

- [x] 4.1 Add/extend tests for schema presence, gate behavior, and supplement view rendering.
- [x] 4.2 Update at least one complex example workspace to include supplement intake and landing view data.
- [x] 4.3 Run `openspec validate add-supplement-intake-and-landing-plan --type change --strict`.
