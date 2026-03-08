# review-master-skill-package-layout

## Purpose

Define the published package boundary for the `review-master` skill so runtime assets live under the release directory instead of the repository root.

## Requirements

### Requirement: Published skill package layout
The project SHALL publish the skill from the `review-master/` directory. That directory MUST contain `SKILL.md` at its root and MAY contain `references/`, `scripts/`, and `assets/` as reserved extension points for later capabilities.

#### Scenario: Minimal publishable skeleton exists
- **WHEN** the initial skeleton is created
- **THEN** `review-master/SKILL.md` exists
- **AND** `review-master/references/`, `review-master/scripts/`, and `review-master/assets/` exist as reserved directories or tracked placeholders

### Requirement: Development assets remain outside the published package
Repository-level development assets MUST remain outside `review-master/` unless they are intentionally prepared for runtime use by the published skill package.

#### Scenario: Repository root docs are not treated as shipped assets
- **WHEN** the repository contains development assets such as `openspec/` or root-level reference materials
- **THEN** those assets are not considered part of the published `review-master` package by default
- **AND** later runtime references or scripts must be added under `review-master/` instead of extending the repository root
