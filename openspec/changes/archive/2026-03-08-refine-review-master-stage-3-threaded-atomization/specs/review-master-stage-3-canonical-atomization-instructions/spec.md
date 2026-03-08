## ADDED Requirements

### Requirement: stage 3 guidance MUST define canonical atomic modeling and conservative merging

`review-master` MUST describe how canonical atomic items are formed, including when repeated reviewer concerns may be conservatively merged and when they must remain separate.

#### Scenario: similar comments still remain separate

- **WHEN** two reviewer comments are on a similar topic but request different kinds of work
- **THEN** Stage 3 guidance tells the Agent not to merge them into one canonical atomic item
- **AND** to preserve separate `comment_id` rows

#### Scenario: merged atomic item records its source evidence

- **WHEN** repeated reviewer concerns are merged into one canonical atomic item
- **THEN** Stage 3 guidance tells the Agent to preserve the merge rationale through `atomic_comment_source_spans`
- **AND** to ensure the merged item is still independently answerable and completable
