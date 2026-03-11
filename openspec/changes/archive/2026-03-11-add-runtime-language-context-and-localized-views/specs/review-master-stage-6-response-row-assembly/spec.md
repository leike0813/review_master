## MODIFIED Requirements

### Requirement: Response rows are assembled from Stage 5 truth plus selected manuscript copy

Final response rows MUST be assembled from the Stage 5 confirmed strategy/draft truth together with the selected manuscript copy and thread-level aggregation, and the outward-facing row text MUST use the confirmed document language.

#### Scenario: response rows do not depend on response-side action variants

- **GIVEN** a `thread_id` linked to one or more canonical atomic comments
- **AND** each linked strategy action target location has a selected manuscript-final-copy variant
- **WHEN** Stage 6 assembles `response_thread_rows`
- **THEN** the row MUST be derivable without any response-side action variants
- **AND** the final response explanation MUST follow a single assembly path

#### Scenario: thread-level response remains outward-facing truth

- **GIVEN** internal execution is indexed by `comment_id`
- **WHEN** the final Response Letter is prepared
- **THEN** it MUST still be organized by original `thread_id`
- **AND** each `thread_id` MUST map to exactly one final outward-facing row

#### Scenario: final rows use document language

- **GIVEN** Stage 5 drafts may be stored in the working language
- **WHEN** Stage 6 writes `response_thread_rows` and exports the final response letter
- **THEN** the final row text MUST use the confirmed document language
- **AND** the original reviewer comment column MUST preserve the source-language excerpt rather than translating it
