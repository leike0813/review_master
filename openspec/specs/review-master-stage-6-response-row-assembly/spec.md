# review-master-stage-6-response-row-assembly Specification

## Purpose
TBD - created by archiving change correct-review-master-stage-6-copy-variant-semantics. Update Purpose after archive.
## Requirements
### Requirement: Response rows are assembled from Stage 5 truth plus revision audit logs

Final response rows MUST be assembled from Stage 5 confirmed strategy truth together with completed revision audit logs and thread-level aggregation, and the outward-facing row text MUST use the confirmed document language.

#### Scenario: response rows are backed by revision logs

- **GIVEN** a `thread_id` linked to one or more canonical atomic comments
- **WHEN** Stage 6 assembles `response_thread_rows`
- **THEN** the row must be derivable from confirmed Stage 5 strategy data plus completed revision logs or explicit `response_only_resolution`
- **AND** the runtime must not require selected manuscript copy variants or export patches

