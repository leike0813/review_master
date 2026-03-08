# review-master-thread-coverage-gating Specification

## Purpose
TBD - created by archiving change restructure-review-master-comment-mapping-model. Update Purpose after archive.
## Requirements
### Requirement: gate-and-render MUST enforce both atomic coverage and thread coverage

The core script MUST reject stage progression when canonical atomic items or original review threads are not fully covered by the required relation tables.

#### Scenario: stage four blocked by missing thread-to-atomic links

- **WHEN** `raw_review_threads` exist
- **AND** one thread has no `raw_thread_atomic_links`
- **THEN** `gate-and-render` reports a dependency error
- **AND** stage four progression remains blocked

#### Scenario: stage six blocked by incomplete response-thread coverage

- **WHEN** a raw review thread exists
- **AND** one of its linked canonical atomic items is missing from `response_thread_resolution_links`
- **THEN** `gate-and-render` reports a dependency or consistency error
- **AND** final export remains blocked

### Requirement: rendered views MUST expose the new mapping structure

The runtime render set MUST make the new threaded mapping visible to both users and agents.

#### Scenario: mapping views are rendered

- **WHEN** `gate-and-render` completes successfully
- **THEN** it renders:
  - `raw-review-thread-list.md`
  - `thread-to-atomic-mapping.md`
  - `atomic-comment-workboard.md`
  - `response-letter-outline.md`
- **AND** those views are derived from the database rather than edited directly

