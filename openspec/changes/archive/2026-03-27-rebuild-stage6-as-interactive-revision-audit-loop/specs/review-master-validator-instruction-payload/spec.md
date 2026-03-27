## MODIFIED Requirements

### Requirement: Validator must emit an instruction payload

The instruction payload MUST point operators to the revision-loop artifacts, the formal Stage 6 submission entrypoint, and any unaudited working-manuscript changes that block progress.

#### Scenario: payload exposes revision-loop guidance

- **WHEN** `gate-and-render` emits Stage 6 instructions
- **THEN** it must reference the reordered artifact filenames and revision-loop action ids
- **AND** it must identify when the operator must run the formal revision-round submission flow instead of continuing directly
