## MODIFIED Requirements

### Requirement: Validator instruction payload must point operators to the canonical runtime views

The validator instruction payload MUST reference the reordered numbered artifacts and the renamed Stage 5 manuscript execution-item contracts whenever it presents resume guidance, allowed actions, or repair instructions.

#### Scenario: payload and repair text use current artifact numbering and Stage 5 terminology

- **WHEN** the validator emits allowed actions, repair hints, or resume guidance
- **THEN** it must reference the reordered numbered artifacts
- **AND** Stage 5 manuscript-side guidance must mention `strategy_action_manuscript_execution_items`
- **AND** completion guidance must use `manuscript_execution_items_done`
