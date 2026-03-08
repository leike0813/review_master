# Capability: runtime-digest-sync

## ADDED Requirements

### Requirement: Runtime digest must track SKILL summary

The repository MUST treat `review-master/assets/runtime/skill-runtime-digest.md` as a compressed summary of `review-master/SKILL.md`, and maintenance guidance for keeping them aligned MUST live in the repository root `AGENTS.md`.

#### Scenario: Updating SKILL requires digest review

- **WHEN** `review-master/SKILL.md` is changed
- **THEN** maintainers are instructed by `AGENTS.md` to review and update `review-master/assets/runtime/skill-runtime-digest.md`
- **AND** the digest remains a compressed execution summary rather than an independent rule source
