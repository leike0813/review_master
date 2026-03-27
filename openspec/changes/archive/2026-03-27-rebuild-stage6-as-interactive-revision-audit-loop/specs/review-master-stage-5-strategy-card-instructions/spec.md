## MODIFIED Requirements

### Requirement: Stage 5 strategy-card instructions are operations-manual grade

Stage 5 MUST end by deriving a revision backlog for Stage 6, including a manuscript revision guide and an execution graph, after strategy confirmation, supplement suggestion review, and supplement intake closure are complete.

#### Scenario: Stage 5 produces revision backlog artifacts

- **GIVEN** all Stage 5 strategy cards have reached executable state
- **WHEN** Stage 5 closes
- **THEN** the runtime must expose `11-manuscript-revision-guide.md` and `12-manuscript-execution-graph.md`
- **AND** `10-supplement-intake-plan.md` must already be complete rather than deferred to Stage 6
