## MODIFIED Requirements

### Requirement: Validator must emit an instruction payload

Stage 3 instruction payload MUST include structured character-coverage metrics.

#### Scenario: Stage 3 payload includes coverage metrics and threshold status

- **WHEN** `gate-and-render` emits `instruction_payload`
- **THEN** it MUST include `coverage_review_metrics` with:
  - `metric_type`
  - `scope`
  - `thresholds`
  - `global`
  - `per_document`
  - `gate_status`
- **AND** `global` metrics MUST include duplicate-aware and non-duplicate character coverage values
