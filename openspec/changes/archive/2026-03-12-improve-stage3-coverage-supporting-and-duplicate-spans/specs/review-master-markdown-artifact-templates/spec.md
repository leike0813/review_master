## MODIFIED Requirements

### Requirement: Template format style

The Stage 3 coverage template MUST expose span roles in both body and appendix.

#### Scenario: appendix mapping includes span role

- **WHEN** `06-review-comment-coverage.md` is generated
- **THEN** the appendix table MUST include `span_role` per covered span row
- **AND** body highlight color MUST be consistent with appendix role mapping
