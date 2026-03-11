## MODIFIED Requirements

### Requirement: stage 3 guidance MUST define canonical atomic modeling and conservative merging

`review-master` MUST describe how canonical atomic items are formed, including when repeated reviewer concerns may be conservatively merged, how original-language excerpts are preserved, and how canonical summaries are translated into the working language.

#### Scenario: similar comments still remain separate

- **WHEN** two reviewer comments are on a similar topic but request different kinds of work
- **THEN** Stage 3 guidance tells the Agent not to merge them into one canonical atomic item
- **AND** to preserve separate `comment_id` rows

#### Scenario: merged atomic item records its source evidence

- **WHEN** repeated reviewer concerns are merged into one canonical atomic item
- **THEN** Stage 3 guidance tells the Agent to preserve the merge rationale through `atomic_comment_source_spans`
- **AND** to ensure the merged item is still independently answerable and completable

#### Scenario: original text and canonical summary use different language roles

- **WHEN** Stage 3 writes `raw_review_threads` and `atomic_comments`
- **THEN** `raw_review_threads.original_text` and source spans MUST stay in the original text language
- **AND** `raw_review_threads.normalized_summary`, `atomic_comments.canonical_summary`, and `atomic_comments.required_action` MUST use the confirmed working language
